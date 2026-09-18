# -*- coding: utf-8 -*-
"""꽃 12종을 절차적으로 모델링해 glTF(GLB)로 내보낸다.

실행:  /Applications/Blender.app/Contents/MacOS/Blender -b --factory-startup --python blender/make_flowers.py

handoff.md "3D 꽃다발 프리뷰" 규칙을 따른다.
- 원점 = 줄기 밑 끝, 위 = Blender +Z (glTF 내보내기에서 +Y), 1 unit = 1m, 줄기 약 0.35m
- 송이당 3,000 tri 이하, 텍스처 없음. 색 변형은 'petal' 머티리얼 색만 바꾼다.
- UV는 텍스처용이 아니라 음영 신호다: u = 겹 밝기(안쪽 0 → 바깥 1), v = 밑(0) → 끝(1).
  웹에서 이 값으로 꽃잎 그러데이션을 만든다.
산출물: landing/models/*.glb, landing/models.js(base64 묶음), blender/flowers.blend
"""
import bpy, bmesh, math, os, base64, json, random
from mathutils import Vector, Matrix

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "landing", "models")
os.makedirs(OUT, exist_ok=True)

MATS = {}
def mat(name, rgb):
    key = (name, tuple(round(c, 4) for c in rgb))      # 이름이 같아도 색이 다르면 다른 머티리얼(Blender가 'center.001'처럼 번호를 붙인다 → 웹에서는 점 앞부분만 본다)
    if key in MATS: return MATS[key]
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    m.use_backface_culling = False
    b = m.node_tree.nodes.get("Principled BSDF")
    b.inputs["Base Color"].default_value = (*rgb, 1.0)
    b.inputs["Roughness"].default_value = 0.72
    MATS[key] = m
    return m

def srgb(hexstr):
    h = hexstr.lstrip("#")
    c = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    return tuple(((x + 0.055) / 1.055) ** 2.4 if x > 0.04045 else x / 12.92 for x in c)


class Builder:
    """머티리얼 슬롯별로 면을 모아 하나의 메시 오브젝트를 만든다."""
    def __init__(self, name):
        self.name = name
        self.bm = bmesh.new()
        self.uv = self.bm.loops.layers.uv.new("UVMap")
        self.slots = []

    def slot(self, m):
        if m not in self.slots: self.slots.append(m)
        return self.slots.index(m)

    def grid(self, pts, uvs, m, close_u=False):
        """pts[j][i] 격자 → 사각 면. uvs는 같은 모양의 (u, v)."""
        si = self.slot(m)
        vs = [[self.bm.verts.new(p) for p in row] for row in pts]
        nu = len(pts[0])
        for j in range(len(pts) - 1):
            for i in range(nu if close_u else nu - 1):
                i2 = (i + 1) % nu
                quad = [(j, i), (j, i2), (j + 1, i2), (j + 1, i)]
                try:
                    f = self.bm.faces.new([vs[a][b] for a, b in quad])
                except ValueError:
                    continue
                f.material_index = si
                f.smooth = True
                for loop, (a, b) in zip(f.loops, quad):
                    loop[self.uv].uv = uvs[a][b]

    def fan(self, center, ring, m, shade, v_center=0.2, v_rim=1.0):
        si = self.slot(m)
        c = self.bm.verts.new(center)
        rs = [self.bm.verts.new(p) for p in ring]
        for i in range(len(rs)):
            f = self.bm.faces.new([c, rs[i], rs[(i + 1) % len(rs)]])
            f.material_index = si
            f.smooth = True
            for loop, vv in zip(f.loops, (v_center, v_rim, v_rim)):
                loop[self.uv].uv = (shade, vv)

    def finish(self):
        me = bpy.data.meshes.new(self.name)
        bmesh.ops.remove_doubles(self.bm, verts=self.bm.verts, dist=1e-6)
        self.bm.normal_update()
        self.bm.to_mesh(me)
        tris = sum(len(f.verts) - 2 for f in self.bm.faces)
        self.bm.free()
        for m in self.slots: me.materials.append(m)
        ob = bpy.data.objects.new(self.name, me)
        bpy.context.scene.collection.objects.link(ob)
        return ob, tris


def petal_pts(L, W, a=0.5, b=4.0, tip=0.5, cup=0.4, bend0=0.0, bend1=0.0, bend_pow=1.5,
              ruffle=0.0, ruffle_f=3.0, phase=0.0, serr=0.0, nu=4, nv=5, twist=0.0):
    """꽃잎 로컬 좌표. 밑=원점, 길이 +Z, 폭 X, 바깥쪽 +Y(오목한 면이 축을 향한다)."""
    rows, y, z = [], 0.0, 0.0
    for j in range(nv + 1):
        v = j / nv
        if j:
            vm = (j - 0.5) / nv
            ang = math.radians(bend0 + bend1 * vm ** bend_pow)
            y += L / nv * math.sin(ang)
            z += L / nv * math.cos(ang)
        w = W * (max(v, 0.04) ** a) * max(1 - v ** b, 0.0) ** tip
        row = []
        for i in range(nu + 1):
            u = i / nu - 0.5
            x = u * w
            yy = y - cup * (2 * u) ** 2 * w * 0.5
            yy += ruffle * math.sin(ruffle_f * 2 * math.pi * u + phase) * v * v
            zz = z + (serr * (1 if i % 2 else -1) if j == nv else 0.0)
            if twist:
                ca, sa = math.cos(twist * v), math.sin(twist * v)
                x, yy = x * ca - yy * sa, x * sa + yy * ca
            row.append(Vector((x, yy, zz)))
        rows.append(row)
    return rows


def place(rows, r0, z0, tilt, az, base=Vector((0, 0, 0)), axis=None):
    """꽃잎을 축 둘레에 놓는다: X축으로 바깥쪽 기울임 → 반경 이동 → Z축 회전."""
    M = Matrix.Rotation(az, 4, 'Z') @ Matrix.Translation((0, r0, z0)) @ Matrix.Rotation(-tilt, 4, 'X')
    if axis is not None: M = axis @ M
    T = Matrix.Translation(base)
    return [[(T @ M @ p) for p in row] for row in rows]


def layer(B, m, n, shade, r0, z0, tilt, az0=0.0, base=Vector((0, 0, 0)), axis=None, jitter=0.06, rng=None, **kw):
    nu, nv = kw.get("nu", 4), kw.get("nv", 5)
    for k in range(n):
        j = (rng.uniform(-jitter, jitter) if rng else 0.0)
        kk = dict(kw)
        kk["phase"] = kw.get("phase", 0.0) + k * 1.7
        kk["L"] = kw["L"] * (1 + j)
        rows = petal_pts(**kk)
        az = az0 + 2 * math.pi * k / n + j * 0.8
        pts = place(rows, r0, z0, math.radians(tilt) * (1 + j), az, base, axis)
        uvs = [[(shade, jj / nv) for _ in range(nu + 1)] for jj in range(nv + 1)]
        B.grid(pts, uvs, m)


def stem(B, m, H, r_base, r_top, bend=0.006, seg=6, rings=6, base=Vector((0, 0, 0)), axis=None, bend_az=0.0):
    pts, uvs = [], []
    for j in range(rings + 1):
        t = j / rings
        off = bend * math.sin(math.pi * t)
        r = r_base + (r_top - r_base) * t
        c = Vector((off * math.cos(bend_az), off * math.sin(bend_az), H * t))
        row = []
        for i in range(seg):
            a = 2 * math.pi * i / seg
            p = c + Vector((r * math.cos(a), r * math.sin(a), 0))
            if axis is not None: p = axis @ p
            row.append(p + base)
        pts.append(row)
        uvs.append([(0.5, 0.35 + 0.65 * t)] * seg)
    B.grid(pts, uvs, m, close_u=True)


def blob(B, m, center, rx, rz, shade, seg=7, rings=4, v0=0.3, v1=0.9):
    """꽃받침·수술용 작은 타원체."""
    pts, uvs = [], []
    for j in range(rings + 1):
        t = j / rings
        ph = math.pi * t
        r = max(rx * math.sin(ph), 1e-5 if 0 < j < rings else 0.0)
        row = [Vector(center) + Vector((r * math.cos(2 * math.pi * i / seg), r * math.sin(2 * math.pi * i / seg), -rz * math.cos(ph))) for i in range(seg)]
        pts.append(row)
        uvs.append([(shade, v0 + (v1 - v0) * t)] * seg)
    B.grid(pts, uvs, m, close_u=True)


def leaf(B, m, z, az, L, W, tilt=55, bend1=35, cup=0.35, nu=4, nv=5, r0=0.002, b=2.2, a=0.6, shade=0.6):
    rows = petal_pts(L, W, a=a, b=b, tip=0.9, cup=cup, bend0=0, bend1=bend1, nu=nu, nv=nv)
    pts = place(rows, r0, z, math.radians(tilt), az)
    uvs = [[(shade, 0.35 + 0.65 * jj / nv) for _ in range(nu + 1)] for jj in range(nv + 1)]
    B.grid(pts, uvs, m)


# ------------------------------------------------------------------ 품목
def rose():
    B, rng = Builder("rose"), random.Random(11)
    P, S, Lf = mat("petal", srgb("#B23A3A")), mat("stem", srgb("#5E7A4E")), mat("leaf", srgb("#4F7245"))
    H = 0.318
    stem(B, S, H, 0.0030, 0.0024, bend=0.007)
    blob(B, S, (0, 0, H + 0.002), 0.0085, 0.008, 0.5)
    layer(B, S, 5, 0.5, 0.006, H - 0.002, 118, L=0.020, W=0.007, a=0.4, b=1.6, tip=1.0, cup=0.3, bend1=25, nu=2, nv=3)
    z = H + 0.004
    common = dict(a=0.55, b=5.0, tip=0.5, nu=4, nv=5, rng=rng)
    layer(B, P, 3, 0.00, 0.0015, z + 0.004, 3,  az0=0.3, L=0.032, W=0.026, cup=1.30, bend0=6, bend1=-16, **common)
    layer(B, P, 4, 0.20, 0.0040, z + 0.003, 8,  az0=0.9, L=0.035, W=0.032, cup=1.00, bend0=6, bend1=-8, **common)
    layer(B, P, 5, 0.45, 0.0065, z + 0.002, 15, az0=0.2, L=0.037, W=0.037, cup=0.75, bend0=6, bend1=22, bend_pow=3, **common)
    layer(B, P, 5, 0.70, 0.0085, z + 0.001, 25, az0=0.8, L=0.039, W=0.041, cup=0.55, bend0=6, bend1=60, bend_pow=3, **common)
    layer(B, P, 5, 0.90, 0.0100, z,         38, az0=0.1, L=0.039, W=0.044, cup=0.42, bend0=4, bend1=95, bend_pow=3, **common)
    layer(B, P, 4, 1.00, 0.0110, z - 0.001, 54, az0=0.6, L=0.036, W=0.044, cup=0.34, bend0=2, bend1=110, bend_pow=3, **common)
    for zz, az in ((0.215, 0.4), (0.250, 2.6), (0.280, 4.6)):     # 꽃다발용: 아래 잎은 훑어낸 상태
        leaf(B, Lf, zz, az, 0.050, 0.030, tilt=42, bend1=35)
    return B.finish()


def mum():
    B, rng = Builder("mum"), random.Random(5)
    P, C = mat("petal", srgb("#F6F2E8")), mat("center", srgb("#D9DB9A"))
    S, Lf = mat("stem", srgb("#5E7A4E")), mat("leaf", srgb("#4F7245"))
    H = 0.322
    stem(B, S, H, 0.0032, 0.0028, bend=0.005)
    blob(B, S, (0, 0, H), 0.011, 0.007, 0.5)
    z = H + 0.002
    common = dict(a=0.30, b=5.0, tip=0.6, cup=0.9, nu=2, nv=4, rng=rng, jitter=0.10)
    layer(B, P, 24, 1.00, 0.0085, z,          84, L=0.036, W=0.0110, bend0=0,  bend1=-44, **common)
    layer(B, P, 22, 0.85, 0.0080, z + 0.003,  66, az0=0.13, L=0.034, W=0.0110, bend0=0, bend1=-52, **common)
    layer(B, P, 20, 0.70, 0.0072, z + 0.006,  49, az0=0.05, L=0.031, W=0.0105, bend0=0, bend1=-60, **common)
    layer(B, P, 16, 0.55, 0.0060, z + 0.009,  33, az0=0.21, L=0.027, W=0.0100, bend0=0, bend1=-68, **common)
    layer(B, P, 12, 0.35, 0.0045, z + 0.011,  19, az0=0.09, L=0.022, W=0.0090, bend0=0, bend1=-76, **common)
    layer(B, C, 8,  0.30, 0.0025, z + 0.012,  8,  az0=0.30, L=0.016, W=0.0075, bend0=0, bend1=-84, **common)
    for zz, az in ((0.225, 1.0), (0.255, 3.4), (0.285, 5.3)):
        leaf(B, Lf, zz, az, 0.046, 0.026, tilt=44, bend1=30, b=1.8)
    return B.finish()


def lisianthus():
    B, rng = Builder("lisianthus"), random.Random(23)
    P, C = mat("petal", srgb("#F4EFE4")), mat("center", srgb("#D8C36A"))
    S, Lf = mat("stem", srgb("#6E8A63")), mat("leaf", srgb("#6A8A62"))
    H = 0.325
    stem(B, S, H, 0.0026, 0.0020, bend=0.008)
    blob(B, S, (0, 0, H + 0.001), 0.0055, 0.006, 0.5)
    layer(B, S, 5, 0.5, 0.004, H, 35, L=0.020, W=0.004, a=0.3, b=1.5, tip=1.0, cup=0.2, bend1=10, nu=2, nv=3)
    z = H + 0.003
    common = dict(a=0.70, b=6.0, tip=0.5, nu=6, nv=6, rng=rng, ruffle_f=2.5)
    layer(B, P, 3, 0.15, 0.0020, z + 0.002, 6,  az0=0.5, L=0.034, W=0.030, cup=1.10, bend0=4,  bend1=4,  ruffle=0.0015, **common)
    layer(B, P, 5, 0.60, 0.0040, z + 0.001, 16, az0=0.0, L=0.041, W=0.040, cup=0.60, bend0=8,  bend1=34, bend_pow=2.5, ruffle=0.0035, **common)
    layer(B, P, 5, 1.00, 0.0055, z,         27, az0=0.63, L=0.042, W=0.044, cup=0.42, bend0=10, bend1=58, bend_pow=2.5, ruffle=0.0045, **common)
    blob(B, C, (0, 0, z + 0.016), 0.0035, 0.007, 0.8, seg=6, rings=3)
    # 곁가지 + 봉오리
    ax = Matrix.Rotation(math.radians(28), 4, 'Y')
    base = Vector((0.0045, 0, 0.225))
    stem(B, S, 0.085, 0.0016, 0.0013, bend=0.004, seg=5, rings=4, base=base, axis=ax)
    tipp = base + ax @ Vector((0, 0, 0.085))
    layer(B, S, 5, 0.5, 0.0025, 0, 22, base=tipp, axis=ax, L=0.016, W=0.003, a=0.3, b=1.5, tip=1.0, cup=0.2, nu=2, nv=2)
    layer(B, P, 4, 0.10, 0.0012, 0.002, 4, base=tipp, axis=ax, L=0.034, W=0.017, a=0.6, b=2.2, tip=0.8, cup=1.3, bend0=5, bend1=-12, nu=4, nv=5, twist=0.9)
    for zz, az in ((0.20, 0.0), (0.20, math.pi), (0.26, math.pi / 2), (0.26, -math.pi / 2)):
        leaf(B, Lf, zz, az, 0.040, 0.020, tilt=40, bend1=20, b=2.0, cup=0.25)
    return B.finish()


def carnation():
    B, rng = Builder("carnation"), random.Random(31)
    P = mat("petal", srgb("#EBA9AD"))
    S, Lf = mat("stem", srgb("#7A9478")), mat("leaf", srgb("#7A9478"))
    H = 0.305
    stem(B, S, H, 0.0026, 0.0024, bend=0.004)
    # 긴 꽃받침통
    pts, uvs = [], []
    for j, (zz, r) in enumerate(((0, 0.0028), (0.006, 0.0062), (0.020, 0.0078), (0.027, 0.0086))):
        pts.append([Vector((r * math.cos(2 * math.pi * i / 8), r * math.sin(2 * math.pi * i / 8), H + zz)) for i in range(8)])
        uvs.append([(0.5, 0.4 + 0.2 * j)] * 8)
    B.grid(pts, uvs, S, close_u=True)
    z = H + 0.024
    common = dict(a=1.1, b=9.0, tip=0.35, nu=8, nv=3, rng=rng, jitter=0.12, ruffle_f=3.0, serr=0.0016)
    layer(B, P, 9, 1.00, 0.0060, z,         84, L=0.024, W=0.026, cup=0.10, bend0=-40, bend1=55, ruffle=0.0040, **common)
    layer(B, P, 8, 0.85, 0.0055, z + 0.002, 64, az0=0.35, L=0.025, W=0.026, cup=0.12, bend0=-30, bend1=40, ruffle=0.0045, **common)
    layer(B, P, 8, 0.65, 0.0048, z + 0.003, 45, az0=0.10, L=0.025, W=0.025, cup=0.15, bend0=-20, bend1=30, ruffle=0.0050, **common)
    layer(B, P, 6, 0.45, 0.0038, z + 0.004, 27, az0=0.50, L=0.024, W=0.023, cup=0.18, bend0=-10, bend1=20, ruffle=0.0050, **common)
    layer(B, P, 5, 0.25, 0.0022, z + 0.004, 11, az0=0.20, L=0.022, W=0.020, cup=0.25, bend0=0,   bend1=10, ruffle=0.0045, **common)
    for zz in (0.19, 0.235, 0.275):
        for az in (zz * 40, zz * 40 + math.pi):
            leaf(B, Lf, zz, az, 0.050, 0.007, tilt=30, bend1=50, b=1.4, a=0.2, cup=0.5, nu=2, nv=5)
    return B.finish()


def tulip():
    B, rng = Builder("tulip"), random.Random(47)
    P, C = mat("petal", srgb("#E9C24F")), mat("center", srgb("#3A3526"))
    S, Lf = mat("stem", srgb("#7FA05F")), mat("leaf", srgb("#5F8A52"))
    H = 0.292
    stem(B, S, H, 0.0042, 0.0034, bend=0.010)
    z = H - 0.001
    common = dict(a=0.55, b=2.6, tip=0.75, nu=6, nv=8, rng=rng, jitter=0.03)
    layer(B, P, 3, 0.35, 0.0030, z, 0, az0=0.0,           L=0.060, W=0.044, cup=1.00, bend0=44, bend1=-62, bend_pow=0.8, **common)
    layer(B, P, 3, 1.00, 0.0042, z, 0, az0=math.pi / 3,   L=0.058, W=0.046, cup=0.85, bend0=48, bend1=-62, bend_pow=0.8, **common)
    blob(B, C, (0, 0, z + 0.014), 0.0030, 0.012, 0.5, seg=6, rings=3)
    leaf(B, Lf, 0.035, 0.6, 0.235, 0.046, tilt=9,  bend1=26, b=1.6, a=0.25, cup=0.75, nu=4, nv=9, r0=0.003)
    leaf(B, Lf, 0.070, 3.5, 0.190, 0.038, tilt=12, bend1=34, b=1.6, a=0.25, cup=0.75, nu=4, nv=9, r0=0.003)
    return B.finish()


def eucalyptus():
    B, rng = Builder("eucalyptus"), random.Random(59)
    S, Lf = mat("stem", srgb("#8C8F7A")), mat("leaf", srgb("#8FA58E"))
    H = 0.40
    stem(B, S, H, 0.0024, 0.0009, bend=0.012, seg=5, rings=8)

    def disc(center, normal_az, tiltdeg, rad, shade):
        ax = Matrix.Rotation(normal_az, 4, 'Z') @ Matrix.Rotation(-math.radians(tiltdeg), 4, 'X')
        ring = []
        for i in range(10):
            a = 2 * math.pi * i / 10
            rr = rad * (1 + 0.06 * math.sin(3 * a))
            p = Vector((rr * math.cos(a), 0.0025 + 0.10 * rr * (math.cos(a) ** 2), rad * 1.08 + rr * math.sin(a)))
            ring.append(center + ax @ p)
        B.fan(center + ax @ Vector((0, 0.0, rad * 1.08)), ring, Lf, shade, v_center=0.55, v_rim=1.0)

    def twig(base, axis, length, z_from, step, r_big, r_small):
        n = int((length - z_from) / step)
        for k in range(n + 1):
            t = k / max(n, 1)
            zz = z_from + k * step
            off = 0.012 * math.sin(math.pi * zz / H) if axis is None else 0.0
            c = Vector((off, 0, zz))
            if axis is not None: c = base + axis @ Vector((0, 0, zz))
            rad = r_big + (r_small - r_big) * t
            az = (math.pi / 2) * k + rng.uniform(-0.25, 0.25)
            for s in (0, math.pi):
                disc(c, az + s, 52 + rng.uniform(-10, 10) - 18 * t, rad * rng.uniform(0.9, 1.08), 0.55 + 0.45 * t)

    twig(None, None, H, 0.10, 0.030, 0.021, 0.009)
    for (zb, azb, tl) in ((0.15, 0.8, 0.15), (0.21, 3.6, 0.12)):
        ax = Matrix.Rotation(azb, 4, 'Z') @ Matrix.Rotation(math.radians(38), 4, 'Y')
        base = Vector((0.012 * math.sin(math.pi * zb / H), 0, zb))
        stem(B, S, tl, 0.0014, 0.0007, bend=0.004, seg=4, rings=3, base=base, axis=ax)
        twig(base, ax, tl, 0.035, 0.028, 0.016, 0.008)
    return B.finish()


def gerbera():
    B, rng = Builder("gerbera"), random.Random(71)
    P, C, S = mat("petal", srgb("#F08A3C")), mat("center", srgb("#5B4A1E")), mat("stem", srgb("#7A9A5C"))
    H = 0.335
    stem(B, S, H, 0.0034, 0.0030, bend=0.009)                       # 거베라는 줄기에 잎이 없다
    blob(B, S, (0, 0, H - 0.002), 0.012, 0.006, 0.5)
    blob(B, C, (0, 0, H + 0.004), 0.0115, 0.0045, 0.9, seg=9, rings=3)
    z = H + 0.003
    common = dict(a=0.25, b=6.0, tip=0.6, cup=0.35, nu=2, nv=3, rng=rng, jitter=0.07)
    layer(B, P, 28, 1.00, 0.0100, z,         84, L=0.034, W=0.0080, bend0=0, bend1=10, **common)
    layer(B, P, 24, 0.85, 0.0095, z + 0.001, 78, az0=0.11, L=0.031, W=0.0075, bend0=0, bend1=6, **common)
    layer(B, P, 20, 0.45, 0.0085, z + 0.002, 62, az0=0.05, L=0.012, W=0.0040, bend0=0, bend1=-20, **common)
    return B.finish()


def sunflower():
    B, rng = Builder("sunflower"), random.Random(73)
    P, C = mat("petal", srgb("#F2B632")), mat("center", srgb("#4A3420"))
    S, Lf = mat("stem", srgb("#6E8E50")), mat("leaf", srgb("#5C8247"))
    H = 0.325
    stem(B, S, H, 0.0050, 0.0044, bend=0.006)
    layer(B, S, 14, 0.5, 0.020, H - 0.004, 104, L=0.022, W=0.010, a=0.4, b=1.8, tip=1.0, cup=0.3, bend1=15, nu=2, nv=3)
    blob(B, C, (0, 0, H + 0.004), 0.027, 0.008, 0.85, seg=12, rings=4, v0=0.35, v1=0.95)
    z = H + 0.002
    common = dict(a=0.35, b=2.0, tip=0.9, cup=0.45, nu=2, nv=4, rng=rng, jitter=0.08)
    layer(B, P, 22, 1.00, 0.0240, z,         86, L=0.036, W=0.0130, bend0=0, bend1=14, **common)
    layer(B, P, 20, 0.80, 0.0235, z + 0.002, 78, az0=0.14, L=0.033, W=0.0120, bend0=0, bend1=6, **common)
    for zz, az in ((0.20, 0.7), (0.26, 3.6)):
        leaf(B, Lf, zz, az, 0.065, 0.050, tilt=48, bend1=40, b=1.6, a=0.35, cup=0.3)
    return B.finish()


def lily():
    B, rng = Builder("lily"), random.Random(79)
    P, C = mat("petal", srgb("#F7F3EA")), mat("center", srgb("#9A4E1E"))
    S, Lf = mat("stem", srgb("#5E8250")), mat("leaf", srgb("#557C49"))
    H = 0.285
    stem(B, S, H, 0.0036, 0.0030, bend=0.006)
    z = H
    common = dict(a=0.5, b=2.2, tip=0.9, cup=0.55, nu=4, nv=7, rng=rng, jitter=0.04, bend_pow=2.0)
    layer(B, P, 3, 0.55, 0.0030, z, 0, az0=0.0,            L=0.088, W=0.030, bend0=26, bend1=96, **common)
    layer(B, P, 3, 1.00, 0.0036, z, 0, az0=math.pi / 3,    L=0.084, W=0.026, bend0=30, bend1=104, **common)
    for k in range(6):                                                  # 수술 6 + 꽃밥
        ax = Matrix.Rotation(2 * math.pi * k / 6 + 0.3, 4, 'Z') @ Matrix.Rotation(math.radians(17), 4, 'Y')
        base = Vector((0, 0, z + 0.004))
        stem(B, S, 0.052, 0.0007, 0.0006, bend=0.003, seg=4, rings=2, base=base, axis=ax)
        blob(B, C, base + ax @ Vector((0, 0, 0.054)), 0.0018, 0.0045, 0.9, seg=5, rings=2)
    stem(B, S, 0.060, 0.0010, 0.0012, bend=0.0, seg=4, rings=2, base=Vector((0, 0, z + 0.004)))
    # 곁가지 봉오리
    ax = Matrix.Rotation(2.4, 4, 'Z') @ Matrix.Rotation(math.radians(30), 4, 'Y')
    base = Vector((0.003, 0, 0.215))
    stem(B, S, 0.075, 0.0020, 0.0016, bend=0.004, seg=5, rings=3, base=base, axis=ax)
    tipp = base + ax @ Vector((0, 0, 0.075))
    layer(B, P, 3, 0.15, 0.0015, 0.0, 3, base=tipp, axis=ax, L=0.062, W=0.018, a=0.5, b=2.0, tip=0.9, cup=1.4, bend0=6, bend1=-14, nu=4, nv=6)
    for zz, az in ((0.14, 0.2), (0.17, 2.4), (0.20, 4.5), (0.23, 1.3), (0.255, 3.4)):
        leaf(B, Lf, zz, az, 0.070, 0.013, tilt=38, bend1=45, b=1.5, a=0.25, cup=0.4, nu=2, nv=5)
    return B.finish()


def hydrangea():
    B, rng = Builder("hydrangea"), random.Random(83)
    P, C = mat("petal", srgb("#8FA8D8")), mat("center", srgb("#E8E2C8"))
    S, Lf = mat("stem", srgb("#64864F")), mat("leaf", srgb("#4E7843"))
    H = 0.295
    stem(B, S, H, 0.0042, 0.0036, bend=0.005)
    c0, R, N = Vector((0, 0, H + 0.030)), 0.046, 58
    blob(B, S, tuple(c0), R * 0.80, R * 0.72, 0.4, seg=8, rings=4)      # 속을 채우는 덩어리(틈으로 비쳐 보이지 않게)
    up = Vector((0, 0, 1))
    for k in range(N):                                                 # 피보나치 구면에 작은 꽃(4장) 배치
        t = (k + 0.5) / N
        zn = 1 - 1.55 * t                                              # 위쪽 반구 + 아래 조금
        rr = math.sqrt(max(0.0, 1 - zn * zn))
        ph = k * 2.399963
        n = Vector((rr * math.cos(ph), rr * math.sin(ph), zn))
        ax = up.rotation_difference(n).to_matrix().to_4x4() @ Matrix.Rotation(rng.uniform(0, 1.5), 4, 'Z')
        base = c0 + Vector((n.x * R, n.y * R, n.z * R * 0.9))
        layer(B, P, 4, 0.55 + 0.45 * rng.random(), 0.0012, 0.0, 78, base=base, axis=ax,
              L=0.0125, W=0.0125, a=0.45, b=3.0, tip=0.5, cup=0.25, bend0=0, bend1=8, nu=2, nv=2)
    for zz, az in ((0.20, 0.5), (0.24, 3.5)):
        leaf(B, Lf, zz, az, 0.075, 0.050, tilt=52, bend1=35, b=1.8, a=0.4, cup=0.3)
    return B.finish()


def peony():
    B, rng = Builder("peony"), random.Random(89)
    P, S, Lf = mat("petal", srgb("#F2B5C0")), mat("stem", srgb("#5E7A4E")), mat("leaf", srgb("#4F7245"))
    H = 0.312
    stem(B, S, H, 0.0034, 0.0030, bend=0.006)
    blob(B, S, (0, 0, H + 0.002), 0.010, 0.008, 0.5)
    z = H + 0.004
    common = dict(a=0.6, b=6.0, tip=0.4, nu=5, nv=5, rng=rng, jitter=0.10, ruffle_f=2.0)
    layer(B, P, 5, 0.00, 0.0020, z + 0.006, 4,  az0=0.2, L=0.030, W=0.030, cup=1.30, bend0=6, bend1=-24, ruffle=0.0010, **common)
    layer(B, P, 7, 0.20, 0.0050, z + 0.005, 12, az0=0.7, L=0.036, W=0.038, cup=1.05, bend0=8, bend1=-18, ruffle=0.0010, **common)
    layer(B, P, 8, 0.40, 0.0080, z + 0.004, 24, az0=0.1, L=0.041, W=0.044, cup=0.85, bend0=8, bend1=-6,  ruffle=0.0020, **common)
    layer(B, P, 9, 0.60, 0.0105, z + 0.002, 38, az0=0.5, L=0.044, W=0.050, cup=0.70, bend0=8, bend1=12,  ruffle=0.0045, **common)
    layer(B, P, 9, 0.85, 0.0125, z + 0.001, 54, az0=0.9, L=0.044, W=0.054, cup=0.55, bend0=6, bend1=34,  bend_pow=2.5, ruffle=0.0030, **common)
    layer(B, P, 8, 1.00, 0.0135, z,         72, az0=0.3, L=0.042, W=0.056, cup=0.45, bend0=4, bend1=50,  bend_pow=2.5, ruffle=0.0030, **common)
    for zz, az in ((0.21, 0.9), (0.25, 3.0), (0.28, 5.0)):
        leaf(B, Lf, zz, az, 0.060, 0.026, tilt=42, bend1=35, b=1.6)
    return B.finish()


def gypsophila():
    B, rng = Builder("gypsophila"), random.Random(97)
    P, S = mat("petal", srgb("#FAF8F2")), mat("stem", srgb("#8AA07A"))
    H = 0.30
    stem(B, S, H, 0.0018, 0.0010, bend=0.008, seg=4, rings=5)

    def spray(base, axis, length, depth):
        stem(B, S, length, 0.0010 if depth else 0.0014, 0.0006, bend=0.003, seg=4, rings=2, base=base, axis=axis)
        tip = base + axis @ Vector((0, 0, length))
        if depth >= 2:
            blob(B, P, tip, 0.0042, 0.0034, 0.7 + 0.3 * rng.random(), seg=5, rings=2, v0=0.6, v1=1.0)
            return
        n = 4 if depth == 0 else 3
        for k in range(n):
            ax = axis @ Matrix.Rotation(2 * math.pi * k / n + rng.uniform(-0.4, 0.4), 4, 'Z') @ Matrix.Rotation(math.radians(rng.uniform(28, 48)), 4, 'Y')
            spray(tip, ax, length * rng.uniform(0.50, 0.68), depth + 1)
        blob(B, P, tip + axis @ Vector((0, 0, 0.004)), 0.0040, 0.0032, 0.9, seg=5, rings=2, v0=0.6, v1=1.0)

    for k, zb in enumerate((0.15, 0.19, 0.23, 0.265, 0.30)):
        t = zb / H
        off = Vector((0.008 * math.sin(math.pi * t), 0, zb))
        ax = Matrix.Rotation(k * 2.3999, 4, 'Z') @ Matrix.Rotation(math.radians(34 - 20 * (k == 4) - 3 * k), 4, 'Y')
        spray(off, ax, 0.085 - 0.006 * k, 0)
    return B.finish()


# ------------------------------------------------------------------ 내보내기
bpy.ops.wm.read_factory_settings(use_empty=True)
report, packed = {}, {}
for idx, fn in enumerate((mum, rose, lisianthus, carnation, tulip, eucalyptus, gerbera, sunflower, lily, hydrangea, peony, gypsophila)):
    ob, tris = fn()
    ob.location.x = idx * 0.16          # .blend 에서 나란히 보이도록
    report[ob.name] = {"tris": tris, "height": round(max((ob.matrix_world @ v.co).z for v in ob.data.vertices), 3)}

for ob in list(bpy.context.scene.collection.objects):
    x = ob.location.x
    ob.location.x = 0
    bpy.ops.object.select_all(action='DESELECT')
    ob.select_set(True)
    bpy.context.view_layer.objects.active = ob
    path = os.path.join(OUT, ob.name + ".glb")
    bpy.ops.export_scene.gltf(filepath=path, export_format='GLB', use_selection=True, export_yup=True,
                              export_apply=True, export_animations=False, export_cameras=False, export_lights=False)
    ob.location.x = x
    report[ob.name]["bytes"] = os.path.getsize(path)
    with open(path, "rb") as f: packed[ob.name] = base64.b64encode(f.read()).decode("ascii")

with open(os.path.join(ROOT, "landing", "models.js"), "w", encoding="utf-8") as f:
    f.write("// blender/make_flowers.py 가 만든 파일 — 직접 고치지 않는다. landing/models/*.glb 의 base64 묶음.\n")
    f.write("window.FLOWER_GLB=" + json.dumps(packed, separators=(",", ":")) + ";\n")

bpy.ops.wm.save_as_mainfile(filepath=os.path.join(ROOT, "blender", "flowers.blend"))
print("REPORT " + json.dumps(report))
