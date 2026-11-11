// 최신 맥 앱 정보를 GitHub 공개 정보에서 읽어 페이지에 채운다. 읽지 못하면 페이지에 적힌 값 그대로 둔다.
(function () {
  var targets = document.querySelector('[data-version]');
  if (!targets || !window.fetch) return;
  fetch('https://api.github.com/repos/sanghyun97/onyu-remote/releases/latest', { headers: { Accept: 'application/vnd.github+json' } })
    .then(function (r) { return r.ok ? r.json() : null; })
    .then(function (rel) {
      if (!rel || !rel.tag_name) return;
      var version = rel.tag_name.replace(/^v/, '');
      var assets = rel.assets || [];
      var dmg = assets.filter(function (a) { return a.name === 'OnyuRemote.dmg'; })[0]
        || assets.filter(function (a) { return /\.dmg$/.test(a.name); })[0];
      if (!dmg) return;   // 설치 파일이 없는 릴리스면 건드리지 않는다
      set('[data-version]', version);
      var d = new Date(rel.published_at);
      if (!isNaN(d)) set('[data-date]', d.getFullYear() + '년 ' + (d.getMonth() + 1) + '월 ' + d.getDate() + '일');
      set('[data-size]', (dmg.size / 1048576).toFixed(1) + 'MB');
      if (dmg.digest && dmg.digest.indexOf('sha256:') === 0) set('[data-sha]', dmg.digest.slice(7));
      document.querySelectorAll('[data-dmg]').forEach(function (a) { a.href = dmg.browser_download_url; });
    })
    .catch(function () {});

  function set(selector, text) {
    document.querySelectorAll(selector).forEach(function (el) { el.textContent = text; });
  }
})();
