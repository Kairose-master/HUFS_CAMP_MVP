/* 3D 꽃다발 프리뷰 — handoff.md "3D 꽃다발 프리뷰" 규칙 구현.
 * 의존: window.THREE(r147 UMD) + THREE.GLTFLoader, window.FLOWER_GLB(models.js).
 * 사용: var bq = Bouquet3D.mount(hostEl, {fallback: fn(host, lines)}); bq.update(lines)
 *       lines = [{key, model, color, qty, green}]  (color는 'petal' 머티리얼 색)
 * 슬롯은 동심원 링(1, 6, 12, 18 …). 슬롯 순서와 슬롯별 흔들림은 고정 시드라 다시 그려도 자리가 바뀌지 않는다.
 */
(function () {
  'use strict';
  var RINGS = [1, 6, 12, 18, 24, 30];
  var TILT = [0, 12.5, 22, 30, 37, 43];
  var TIE = 0.04;                       // 줄기가 모이는 높이(m). 손으로 쥐는 자리
  var STEM = 0.31;                      // TIE 에서 꽃 머리까지
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  function webglOk() {
    try { var c = document.createElement('canvas'); return !!(window.WebGLRenderingContext && (c.getContext('webgl2') || c.getContext('webgl'))); }
    catch (e) { return false; }
  }
  function rand(seed) { var x = Math.sin(seed * 127.1 + 311.7) * 43758.5453; return x - Math.floor(x); }

  // 링 안에서 채우는 순서: 이미 채운 자리에서 가장 먼 자리부터(적게 담아도 한쪽으로 쏠리지 않는다)
  var orderCache = {};
  function ringOrder(n) {
    if (orderCache[n]) return orderCache[n];
    var out = [0], i, j;
    while (out.length < n) {
      var best = -1, bestD = -1;
      for (i = 0; i < n; i++) {
        if (out.indexOf(i) > -1) continue;
        var d = n;
        for (j = 0; j < out.length; j++) { var a = Math.abs(i - out[j]); d = Math.min(d, a, n - a); }
        if (d > bestD) { bestD = d; best = i; }
      }
      out.push(best);
    }
    return (orderCache[n] = out);
  }

  // ---------- 모델 ----------
  var modelCache = {};
  function b64buf(s) { var bin = atob(s), n = bin.length, u = new Uint8Array(n); for (var i = 0; i < n; i++) u[i] = bin.charCodeAt(i); return u.buffer; }
  function bakeShade(geo) {            // uv(u=겹 밝기, v=밑→끝) → 정점 색
    var uv = geo.getAttribute('uv'), n = geo.getAttribute('position').count, col = new Float32Array(n * 3);
    for (var i = 0; i < n; i++) {
      var u = uv ? uv.getX(i) : 1, v = uv ? 1 - uv.getY(i) : 1;
      var f = (0.50 + 0.50 * Math.pow(Math.max(v, 0), 0.8)) * (0.74 + 0.26 * u);
      col[i * 3] = col[i * 3 + 1] = col[i * 3 + 2] = f;
    }
    geo.setAttribute('color', new THREE.BufferAttribute(col, 3));
  }
  function loadModel(name) {
    if (modelCache[name]) return modelCache[name];
    return (modelCache[name] = new Promise(function (res, rej) {
      var data = window.FLOWER_GLB && window.FLOWER_GLB[name];
      if (!data) return rej(new Error('no model ' + name));
      new THREE.GLTFLoader().parse(b64buf(data), '', function (g) {
        var parts = [];
        g.scene.updateMatrixWorld(true);
        g.scene.traverse(function (o) {
          if (!o.isMesh) return;
          var geo = o.geometry.clone(); geo.applyMatrix4(o.matrixWorld); bakeShade(geo);
          parts.push({ geo: geo, name: String(o.material.name || '').split('.')[0], color: o.material.color.clone() });   // 'center.001' → 'center'
        });
        res(parts);
      }, rej);
    }));
  }

  // ---------- 배치 ----------
  function layout(lines) {
    var flowers = [], greens = [], i, k;
    lines.forEach(function (l) { if (l.qty > 0) (l.green ? greens : flowers).push({ l: l, left: l.qty }); });
    // 품목을 비율대로 섞는다(같은 입력이면 항상 같은 순서)
    var seq = [], total = flowers.reduce(function (a, f) { return a + f.l.qty; }, 0);
    for (k = 0; k < total; k++) {
      var pick = null, bestScore = -1;
      for (i = 0; i < flowers.length; i++) {
        var f = flowers[i]; if (!f.left) continue;
        var score = f.left / f.l.qty;
        if (score > bestScore + 1e-9) { bestScore = score; pick = f; }
      }
      pick.left--; seq.push(pick.l);
    }
    var inst = [], ring = 0, used = 0;
    seq.forEach(function (l, n) {
      while (ring < RINGS.length - 1 && used >= RINGS[ring]) { used = 0; ring++; }
      var N = RINGS[ring], slot = ringOrder(N)[used % N]; used++;
      var seed = ring * 100 + slot;
      inst.push({
        key: ring + ':' + slot + ':' + l.key, line: l, ring: ring,
        az: (slot / N) * Math.PI * 2 + ring * 0.37 + (rand(seed) - 0.5) * 0.16,
        tilt: (TILT[ring] + (rand(seed + 7) - 0.5) * 7) * Math.PI / 180,
        spin: rand(seed + 3) * Math.PI * 2,
        scale: 0.95 + rand(seed + 5) * 0.12,
        drop: ring * 0.012 + rand(seed + 9) * 0.010
      });
    });
    var lastRing = inst.length ? inst[inst.length - 1].ring : 0;
    var maxTilt = inst.reduce(function (a, n) { return Math.max(a, n.tilt); }, 0.16);
    var gTotal = greens.reduce(function (a, g) { return a + g.l.qty; }, 0), gi = 0;
    greens.forEach(function (g) {
      for (var q = 0; q < g.l.qty; q++, gi++) {
        var seed = 900 + gi;
        inst.push({
          key: 'g:' + gi + ':' + g.l.key, line: g.l, ring: lastRing + 1,
          az: (gi / gTotal) * Math.PI * 2 + 0.9 + (rand(seed) - 0.5) * 0.3,
          tilt: (TILT[Math.min(lastRing, TILT.length - 1)] + 5 + rand(seed + 7) * 4) * Math.PI / 180,
          spin: rand(seed + 3) * Math.PI * 2, scale: 0.98 + rand(seed + 5) * 0.1, drop: 0.02
        });
      }
    });
    return { inst: inst, radius: Math.max(0.06, STEM * Math.sin(maxTilt)) };
  }

  var _m = null, _q, _s, _p, _e;
  function matrixFor(n, grow) {
    if (!_m) { _m = new THREE.Matrix4(); _q = new THREE.Quaternion(); _s = new THREE.Vector3(); _p = new THREE.Vector3(); _e = new THREE.Euler(); }
    // 자기 축 회전 → 묶음 지점을 중심으로 바깥 기울임 → 방위각
    var s = n.scale * grow;
    var M = new THREE.Matrix4().makeRotationY(n.az);
    M.multiply(_m.makeTranslation(0, TIE, 0));
    M.multiply(_m.makeRotationZ(-n.tilt));
    M.multiply(_m.makeTranslation(0, -TIE - n.drop, 0));
    M.multiply(_m.makeRotationY(n.spin));
    M.multiply(_m.makeScale(s, s, s));
    return M;
  }

  // 포장지: 밑이 좁은 원뿔. 뒤쪽이 높고 가장자리가 물결친다.
  var PAPER_Y0 = 0.028, PAPER_H = 0.205;   // 포장지 아래로 줄기 끝이 보인다(핸드타이드)
  function paperR(t, rTop) { return 0.027 + (rTop - 0.027) * Math.pow(t, 1.15); }
  function paperGeo(R, innerLayer) {
    var seg = 56, rows = 7, pos = [], idx = [], uv = [], i, j;
    var rTop = R + (innerLayer ? 0.012 : 0.030), h = PAPER_H - (innerLayer ? 0.025 : 0);
    for (j = 0; j <= rows; j++) {
      var t = j / rows;
      for (i = 0; i <= seg; i++) {
        var a = (i / seg) * Math.PI * 2;
        var wave = 0.014 * Math.sin(5 * a + (innerLayer ? 1.3 : 0)) + 0.008 * Math.sin(11 * a + 0.7);
        var back = 0.028 * (0.5 - 0.5 * Math.cos(a - Math.PI * 0.5 + (innerLayer ? 0.5 : 0)));
        var r = paperR(t, rTop) * (1 + 0.05 * Math.sin(7 * a + 2) * t * t);
        var y = PAPER_Y0 + t * h + (wave + back) * Math.pow(t, 2.2);
        pos.push(r * Math.cos(a), y, r * Math.sin(a)); uv.push(i / seg, t);
      }
    }
    for (j = 0; j < rows; j++) for (i = 0; i < seg; i++) {
      var p = j * (seg + 1) + i, q = p + seg + 1;
      idx.push(p, q, p + 1, p + 1, q, q + 1);
    }
    var g = new THREE.BufferGeometry();
    g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
    g.setAttribute('uv', new THREE.Float32BufferAttribute(uv, 2));
    g.setIndex(idx); g.computeVertexNormals();
    return g;
  }

  function hex(c) { return new THREE.Color(c).convertSRGBToLinear(); }

  // ---------- 무대: 장면 + 꽃다발(마운트와 썸네일이 같이 쓴다) ----------
  function createStage() {
    var scene = new THREE.Scene();
    var cam = new THREE.PerspectiveCamera(28, 1, 0.05, 10);
    scene.add(new THREE.HemisphereLight(0xffffff, 0xcbbfa8, 0.95));
    var key = new THREE.DirectionalLight(0xfff1dc, 0.95); key.position.set(0.7, 1.2, 0.9); scene.add(key);
    var fill = new THREE.DirectionalLight(0xdfe8ff, 0.30); fill.position.set(-0.8, 0.4, -0.6); scene.add(fill);
    var pivot = new THREE.Group(); scene.add(pivot);
    var wrap = new THREE.Group(); pivot.add(wrap);
    var paper = new THREE.Mesh(new THREE.BufferGeometry(), new THREE.MeshStandardMaterial({ color: hex('#C9A878'), roughness: 0.95, metalness: 0, side: THREE.DoubleSide }));
    var tissue = new THREE.Mesh(new THREE.BufferGeometry(), new THREE.MeshStandardMaterial({ color: hex('#F3EBDD'), roughness: 0.95, metalness: 0, side: THREE.DoubleSide }));
    var ribbon = new THREE.Mesh(new THREE.TorusGeometry(0.0315, 0.0045, 8, 40), new THREE.MeshStandardMaterial({ color: hex('#1F5A3C'), roughness: 0.55, metalness: 0 }));
    var RIB_T = 0.14; ribbon.rotation.x = Math.PI / 2; ribbon.position.y = PAPER_Y0 + RIB_T * PAPER_H;
    wrap.add(paper, tissue, ribbon);
    var st = { scene: scene, cam: cam, pivot: pivot, meshes: [], born: {}, radius: 0.1, token: 0 }, matCache = {};

    function material(part, line) {
      var c = part.name === 'petal' && line.color ? line.color : null;
      var k = part.name + '|' + (c || '#' + part.color.getHexString());
      if (!matCache[k]) matCache[k] = new THREE.MeshStandardMaterial({
        color: c ? hex(c) : part.color.clone(), vertexColors: true, roughness: part.name === 'petal' ? 0.62 : 0.8, metalness: 0, side: THREE.DoubleSide
      });
      return matCache[k];
    }
    st.setLines = function (lines, animate) {
      var lay = layout(lines), names = {}, token = ++st.token;
      lines.forEach(function (l) { if (l.qty > 0) names[l.model] = 1; });
      return Promise.all(Object.keys(names).map(function (n) { return loadModel(n).then(function (p) { return [n, p]; }); })).then(function (loaded) {
        if (token !== st.token) return false;               // 더 새로운 요청이 있다
        var parts = {}; loaded.forEach(function (x) { parts[x[0]] = x[1]; });
        st.meshes.forEach(function (m) { pivot.remove(m); m.dispose && m.dispose(); });
        st.meshes = [];
        var now = performance.now(), nextBorn = {}, first = !Object.keys(st.born).length;
        lay.inst.forEach(function (n) { nextBorn[n.key] = st.born[n.key] || (first || !animate ? now - 1000 : now); });
        st.born = nextBorn;
        var groups = {};
        lay.inst.forEach(function (n) { var k = n.line.model + '|' + (n.line.color || ''); (groups[k] = groups[k] || []).push(n); });
        Object.keys(groups).forEach(function (k) {
          var list = groups[k];
          parts[list[0].line.model].forEach(function (part) {
            var im = new THREE.InstancedMesh(part.geo, material(part, list[0].line), list.length);
            im.userData.list = list; im.frustumCulled = false;
            pivot.add(im); st.meshes.push(im);
          });
        });
        wrap.visible = lay.inst.length > 0;
        st.radius = lay.radius;
        paper.geometry.dispose(); paper.geometry = paperGeo(st.radius, false);
        tissue.geometry.dispose(); tissue.geometry = paperGeo(st.radius, true);
        var rr = (paperR(RIB_T, st.radius + 0.030) + 0.002) / 0.0315; ribbon.scale.set(rr, rr, 2.4);
        st.writeMatrices(now);
        return true;
      });
    };
    st.writeMatrices = function (now) {
      st.meshes.forEach(function (im) {
        im.userData.list.forEach(function (n, i) {
          var t = Math.max(0, Math.min(1, (now - st.born[n.key]) / 380));
          var grow = t >= 1 ? 1 : 1 - Math.pow(1 - t, 3);
          im.setMatrixAt(i, matrixFor(n, Math.max(grow, 0.001)));
        });
        im.instanceMatrix.needsUpdate = true;
      });
    };
    st.frame = function (w, h) {
      var aspect = w / h, d = (0.62 + st.radius * 2.1) / Math.min(1, aspect * 0.9);
      cam.aspect = aspect; cam.position.set(0, 0.50 + st.radius * 0.6, d); cam.lookAt(0, 0.175, 0); cam.updateProjectionMatrix();
    };
    return st;
  }

  // ---------- 마운트 ----------
  function mount(host, opts) {
    opts = opts || {};
    var api = { update: function (lines) { pending = lines; if (ready) apply(); else if (opts.fallback) opts.fallback(host, lines); }, ok: false };
    var pending = null, ready = false;
    if (!window.THREE || !THREE.GLTFLoader || !webglOk()) return api;

    var renderer;
    try { renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: 'low-power' }); }
    catch (e) { return api; }
    api.ok = true;
    renderer.outputEncoding = THREE.sRGBEncoding;
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    var canvas = renderer.domElement;
    canvas.className = 'bq-canvas';
    canvas.tabIndex = 0;
    canvas.setAttribute('role', 'img');
    canvas.setAttribute('aria-label', opts.label || '꽃다발 3D 미리보기. 좌우로 끌거나 화살표 키로 돌려 보세요.');

    var st = createStage();
    var rot = 0.5, vel = 0, auto = !reduce, dirty = true, visible = true, animUntil = 0, growing = false;

    function apply() {
      var lines = pending || [];
      st.setLines(lines, !reduce).then(function (ok) {
        if (!ok) return;
        animUntil = performance.now() + 420; growing = true; dirty = true;
        if (!host.contains(canvas)) { host.innerHTML = ''; host.appendChild(canvas); }
        resize();
      }).catch(function () { if (opts.fallback) opts.fallback(host, lines); });
    }
    function resize() { var w = host.clientWidth, h = host.clientHeight; if (!w || !h) return; renderer.setSize(w, h, false); st.frame(w, h); dirty = true; }

    var last = performance.now();
    function tick() {
      requestAnimationFrame(tick);
      // rAF 가 넘겨주는 시각은 긴 작업 뒤에 과거 값일 수 있다 → born 과 같은 시계(performance.now)만 쓴다
      var now = performance.now();
      var dt = Math.min(0.05, (now - last) / 1000); last = now;
      if (!visible) return;
      if (auto) { rot += dt * 0.22; dirty = true; }
      if (Math.abs(vel) > 0.0004) { rot += vel; vel *= 0.92; dirty = true; }
      if (growing) { st.writeMatrices(now); dirty = true; if (now >= animUntil) growing = false; }   // 마지막 한 번은 반드시 완성 상태로 쓴다
      if (!dirty) return;
      st.pivot.rotation.y = rot; dirty = false;
      renderer.render(st.scene, st.cam);
    }

    // 끌어서 회전(세로 스크롤은 그대로), 화살표 키
    var dragging = false, px = 0;
    canvas.addEventListener('pointerdown', function (e) { dragging = true; px = e.clientX; auto = false; vel = 0; try { canvas.setPointerCapture(e.pointerId); } catch (err) { } });
    canvas.addEventListener('pointermove', function (e) { if (!dragging) return; var dx = e.clientX - px; px = e.clientX; rot += dx * 0.011; vel = dx * 0.011; dirty = true; });
    ['pointerup', 'pointercancel'].forEach(function (t) { canvas.addEventListener(t, function () { dragging = false; }); });
    canvas.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') { auto = false; rot += (e.key === 'ArrowLeft' ? -1 : 1) * 0.25; dirty = true; e.preventDefault(); }
    });
    if (window.ResizeObserver) new ResizeObserver(resize).observe(host); else window.addEventListener('resize', resize);
    if (window.IntersectionObserver) new IntersectionObserver(function (en) { visible = en[0].isIntersecting; dirty = true; }).observe(host);

    ready = true;
    requestAnimationFrame(tick);
    if (pending) apply();
    return api;
  }

  // ---------- 썸네일: 꽃다발을 PNG data URL 로(완성 사진 자리, 주문서 썸네일) ----------
  var thumbStage = null, thumbRenderer = null, thumbCache = {}, thumbQueue = Promise.resolve();
  function thumb(lines, size) {
    size = size || 320;
    var live = lines.filter(function (l) { return l.qty > 0; });
    var sig = size + JSON.stringify(live.map(function (l) { return [l.key, l.qty, l.color]; }));
    if (thumbCache[sig]) return thumbCache[sig];
    if (!window.THREE || !THREE.GLTFLoader || !webglOk()) return Promise.resolve(null);
    return (thumbCache[sig] = thumbQueue = thumbQueue.then(function () {
      try {
        if (!thumbRenderer) {
          thumbRenderer = new THREE.WebGLRenderer({ antialias: true, alpha: false, preserveDrawingBuffer: true });
          thumbRenderer.outputEncoding = THREE.sRGBEncoding;
          thumbRenderer.setClearColor(hex('#ECE5D8'), 1);
          thumbStage = createStage();
        }
        thumbRenderer.setPixelRatio(1); thumbRenderer.setSize(size, size, false);
        return thumbStage.setLines(live, false).then(function () {
          thumbStage.frame(size, size);
          thumbStage.pivot.rotation.y = 0.6;
          thumbRenderer.render(thumbStage.scene, thumbStage.cam);
          return thumbRenderer.domElement.toDataURL('image/jpeg', 0.86);
        });
      } catch (e) { return null; }
    }).catch(function () { return null; }));
  }

  window.Bouquet3D = { mount: mount, thumb: thumb };
})();
