#!/usr/bin/env python3
"""온유 리모트 사이트 만들기 — python3 _build.py
버전이 바뀌면 아래 RELEASE 값만 고치고 다시 실행한다(페이지는 GitHub에서 최신 값을 읽어 덮어쓰지만,
읽지 못할 때 보여 줄 기본값이 이것이다). 디자인 규칙은 DESIGN.md, 값은 style.css."""
import html, pathlib

RELEASE = {
    "version": "1.1.3",
    "date": "2026년 11월 11일",
    "size": "3.0MB",
    "sha256": "b527454795861f3ce4e2d5cf91e1bc01efb6a2aebfd507d40b4aed766b30b911",
}
REPO = "sanghyun97/onyu-remote"
DMG = f"https://github.com/{REPO}/releases/latest/download/OnyuRemote.dmg"
APPSTORE = "https://apps.apple.com/kr/app/id6830655052"
TAILSCALE = "https://tailscale.com/download"
ISSUES = f"https://github.com/{REPO}/issues/new"
SITE = "https://sanghyun97.github.io/onyu-remote/"
DESC = "아이폰·아이패드·맥에서 내 맥을 렉 없이 제어하는 원격 앱. 같은 Wi-Fi에서는 맥 앞에 앉은 것처럼, 밖에서는 Tailscale로 어디서든."


def page(name, title, body, desc=DESC, sub_title="온유 리모트"):
    out = f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE}{'' if name == 'index.html' else name}">
<meta property="og:image" content="{SITE}img/remote.jpg">
<meta name="theme-color" content="#000000">
<link rel="icon" href="icon.png">
<link rel="apple-touch-icon" href="icon.png">
<link rel="stylesheet" href="style.css">
</head>
<body>
<nav class="global-nav" aria-label="사이트">
  <div class="inner">
    <a class="brand" href="./"><img src="icon.png" alt="" width="20" height="20">온유 리모트</a>
    <a href="./#features" class="optional">기능</a>
    <a href="install.html">설치 안내</a>
    <a href="support.html">지원</a>
    <a href="changelog.html" class="optional">변경 기록</a>
  </div>
</nav>
<div class="sub-nav">
  <div class="inner">
    <span class="title">{html.escape(sub_title)}</span>
    <div class="links">
      <a href="./#security" class="optional">보안</a>
      <a href="{APPSTORE}">App Store</a>
      <a class="btn small" href="./#download">맥 앱 받기</a>
    </div>
  </div>
</div>
<main>
{body}
</main>
<footer class="footer">
  <div class="inner">
    <div class="cols">
      <div><h4>온유 리모트</h4><a href="./">소개</a><a href="./#features">기능</a><a href="./#download">맥 앱 내려받기</a><a href="{APPSTORE}">아이폰·아이패드 (App Store)</a></div>
      <div><h4>도움말</h4><a href="install.html">설치 안내</a><a href="support.html">자주 묻는 것</a><a href="changelog.html">변경 기록</a><a href="{ISSUES}">문의 남기기</a></div>
      <div><h4>정책</h4><a href="privacy.html">개인정보 처리방침</a><a href="https://github.com/{REPO}/releases">모든 버전</a></div>
    </div>
    <p class="legal">© 2026 SANGHYUN LEE. 온유 리모트는 개인 개발자가 만든 독립 앱으로 Apple Inc.와 관계가 없으며, Apple의 후원이나 승인을 받지 않았습니다. Apple, Mac, macOS, iPhone, iPad, App Store는 미국 및 그 밖의 나라에 등록된 Apple Inc.의 상표입니다. Tailscale은 Tailscale Inc.의 상표입니다.</p>
  </div>
</footer>
<script src="site.js" defer></script>
</body>
</html>
"""
    pathlib.Path(name).write_text(out, encoding="utf-8")


def icon(d):
    return f'<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>'


def card(ic, title, text):
    return f'<div class="card">{icon(ic)}<h3>{title}</h3><p>{text}</p></div>'


R = RELEASE
FEATURES = "".join([
    card('<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>', "기기에 딱 맞는 화면", "연결하는 동안만 맥 화면을 아이폰·아이패드 크기에 맞춥니다. 검은 띠 없이 꽉 차고, 끊으면 원래대로 돌아옵니다."),
    card('<path d="M9 11V5a2 2 0 0 1 4 0v6"/><path d="M13 9a2 2 0 0 1 4 0v3a6 6 0 0 1-6 6h-1a5 5 0 0 1-4-2l-2-3a1.6 1.6 0 0 1 2.6-1.8L9 12"/>', "손에 익은 조작", "트랙패드처럼 밀고 탭하고, 두 손가락으로 스크롤. 애플 펜슬, 매직 키보드, 트랙패드도 그대로 씁니다."),
    card('<rect x="2" y="6" width="20" height="12" rx="2"/><path d="M6 10h.01M10 10h.01M14 10h.01M18 10h.01M7 14h10"/>', "키보드 그대로", "한/영 전환과 Command·Option·Control·Shift를 맥에 그대로 보냅니다. 맥에서 맥을 제어할 때는 ⌘Tab까지."),
    card('<path d="M12 3l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.4 6.8 19.1l1-5.8L3.5 9.2l5.9-.9z"/>', "내 버튼", "자주 쓰는 단축키를 버튼으로 만들어 패널에서 바로 누릅니다. 아이폰이 작업용 리모컨이 됩니다."),
    card('<path d="M6 9a6 6 0 0 1 12 0c0 6 2 7 2 7H4s2-1 2-7"/><path d="M10 20a2 2 0 0 0 4 0"/>', "맥 알림 받기", "연결하지 않아도 맥에서 보낸 알림이 아이폰으로 옵니다. 새 기기가 연결하려 할 때도 바로 압니다."),
    card('<path d="M3 3l18 18"/><path d="M10.6 5.1A10.5 10.5 0 0 1 12 5c6 0 9.5 7 9.5 7a15 15 0 0 1-3 3.7M6.5 6.6A15 15 0 0 0 2.5 12S6 19 12 19a9.6 9.6 0 0 0 4-.9"/>', "화면 가리기", "원격으로 쓰는 동안 맥의 모니터를 검게 가립니다. 화면은 제어하는 기기에서만 보입니다."),
    card('<path d="M12 3v12M8 11l4 4 4-4"/><path d="M4 17v2a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-2"/>', "맥끼리 파일·클립보드", "맥에서 맥으로 파일을 끌어다 놓고, 한쪽에서 복사한 글자를 다른 쪽에서 붙여넣습니다."),
    card('<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>', "항상 켜 두기", "로그인하면 켜지고, 꺼져도 스스로 다시 켜집니다. 연결이 끊기면 알아서 다시 붙습니다."),
])

page("index.html", "온유 리모트 — 내 맥을 어디서든 렉 없이", f"""
<section class="tile">
  <div class="wrap">
    <h1 class="hero-display">내 맥을, 어디서든.</h1>
    <p class="lead">아이폰·아이패드·맥에서 내 맥을 렉 없이 제어합니다.</p>
    <div class="cta">
      <a class="btn" href="#download">맥 앱 받기</a>
      <a class="btn ghost" href="{APPSTORE}">App Store에서 받기</a>
    </div>
    <p class="caption" style="margin-top:17px">무료 · 맥 앱 <span data-version>{R['version']}</span> · macOS 15 이상 · iOS 18 이상</p>
    <div class="shot wide-shot"><img src="img/remote.jpg" alt="아이폰에서 맥의 사진 셀렉 화면을 원격으로 보고 있는 모습" width="1600" height="736"></div>
  </div>
</section>

<section class="tile dark">
  <div class="wrap">
    <p class="eyebrow">빠르기</p>
    <h2 class="display-lg">기다리지 않는 화면.</h2>
    <p class="copy">받은 화면을 쌓아 두지 않고 바로 보여 줍니다. 늦게 도착한 화면은 다시 받지 않고 버려서, 손이 움직인 만큼 화면이 따라옵니다. 화면이 멈추면 한 장을 더 선명하게 다시 보내, 사진의 초점까지 확인할 수 있습니다.</p>
    <div class="grid three stats" style="margin-top:48px">
      <div><p class="tagline">버퍼 0</p><p class="caption">화면을 쌓아 두지 않고 받는 즉시 표시</p></div>
      <div><p class="tagline">초당 60장</p><p class="caption">하드웨어 HEVC로 부드럽게</p></div>
      <div><p class="tagline">멈추면 선명하게</p><p class="caption">정지 화면은 고화질로 한 번 더</p></div>
    </div>
  </div>
</section>

<section class="tile parchment">
  <div class="wrap">
    <p class="eyebrow">조작</p>
    <h2 class="display-lg">손가락 하나로, 맥 전체를.</h2>
    <p class="copy">구석의 버튼을 누르면 조작 패널이 열립니다. 수정 키를 고정해 두고, 한/영을 바꾸고, 직접 만든 단축키 버튼을 누릅니다.</p>
    <div class="shots-row">
      <div class="shot phone"><img src="img/home.jpg" alt="연결할 맥 목록 화면" width="644" height="1400" loading="lazy"></div>
      <div class="shot phone"><img src="img/custom.jpg" alt="직접 만든 단축키 버튼이 있는 조작 패널" width="644" height="1400" loading="lazy"></div>
      <div class="shot phone"><img src="img/onboarding.jpg" alt="처음 시작 안내 화면" width="644" height="1400" loading="lazy"></div>
    </div>
  </div>
</section>

<section class="tile" id="features">
  <div class="wide">
    <p class="eyebrow">기능</p>
    <h2 class="display-lg">작업에 필요한 것만, 빠짐없이.</h2>
    <div class="grid">{FEATURES}</div>
  </div>
</section>

<section class="tile dark-2" id="security">
  <div class="wrap">
    <p class="eyebrow">보안</p>
    <h2 class="display-lg">내 기기끼리만, 직접.</h2>
    <p class="copy">화면·조작·파일은 연결마다 새로 만든 키로 모두 암호화되고, 중간 서버 없이 기기끼리 직접 오갑니다. 처음 한 번 맥 화면에 뜨는 6자리 숫자를 넣은 기기만 연결할 수 있습니다. 계정도, 가입도, 수집하는 정보도 없습니다.</p>
    <div class="cta"><a class="btn ghost" href="privacy.html">개인정보 처리방침</a></div>
  </div>
</section>

<section class="tile parchment">
  <div class="wrap">
    <p class="eyebrow">시작하기</p>
    <h2 class="display-lg">세 단계면 됩니다.</h2>
    <div class="grid three">
      <div class="card"><span class="num">1</span><h3>맥에 설치</h3><p>제어받을 맥에 온유 리모트를 설치하고, 처음 뜨는 창에서 화면 기록과 손쉬운 사용 권한을 허용합니다.</p></div>
      <div class="card"><span class="num">2</span><h3>같은 Wi-Fi에서 연결</h3><p>아이폰·아이패드의 목록에 맥이 나타나면 [연결]을 누르고, 맥에 뜬 6자리 숫자를 한 번 입력합니다.</p></div>
      <div class="card"><span class="num">3</span><h3>밖에서도</h3><p>맥과 기기에 Tailscale을 같은 계정으로 켜 두면, 밖에서도 같은 항목으로 연결됩니다.</p></div>
    </div>
    <div class="cta"><a class="btn ghost" href="install.html">설치 안내 자세히 보기</a></div>
  </div>
</section>

<section class="tile" id="download">
  <div class="wrap">
    <p class="eyebrow">내려받기</p>
    <h2 class="display-lg">맥용 온유 리모트</h2>
    <p class="copy">제어받는 맥과, 다른 맥을 제어하는 맥 모두 이 앱 하나면 됩니다. Apple의 공증을 받은 설치 파일이라 경고 없이 열립니다.</p>
    <div class="cta">
      <a class="btn hero" href="{DMG}" data-dmg>내려받기 (DMG)</a>
    </div>
    <div class="card download-card">
      <div class="row"><span>버전</span><span><span data-version>{R['version']}</span> · <span data-date>{R['date']}</span></span></div>
      <div class="row"><span>크기</span><span data-size>{R['size']}</span></div>
      <div class="row"><span>요구 사항</span><span>macOS 15 이상 · Apple 실리콘·Intel</span></div>
      <div class="row"><span>서명</span><span>Developer ID · Apple 공증</span></div>
      <details class="more">
        <summary>자세히</summary>
        <div class="row"><span>SHA-256</span><code data-sha>{R['sha256']}</code></div>
        <p class="fine">받은 파일이 원본과 같은지 확인하는 값입니다. 터미널에서 <code>shasum -a 256 OnyuRemote.dmg</code>를 실행해 같은 값이 나오면 변조되지 않은 파일입니다. 확인하지 않아도 맥이 설치할 때 Apple 공증으로 따로 검증합니다.</p>
      </details>
    </div>
    <p class="caption" style="margin-top:17px">아이폰·아이패드 앱은 <a href="{APPSTORE}">App Store</a>에서 받으세요. · <a href="changelog.html">변경 기록</a> · <a href="https://github.com/{REPO}/releases">이전 버전</a></p>
  </div>
</section>
""")

page("install.html", "설치 안내 — 온유 리모트", f"""
<article class="article">
  <h1>설치 안내</h1>
  <p class="caption">처음부터 밖에서 연결하기까지, 순서대로 따라 하면 됩니다.</p>

  <h2>1. 맥에 설치하기</h2>
  <ol>
    <li><a href="./#download">맥 앱(DMG)을 내려받습니다.</a></li>
    <li>내려받은 <code>OnyuRemote.dmg</code>를 열고, 온유 리모트를 <b>응용 프로그램</b> 폴더로 끌어 놓습니다.</li>
    <li>응용 프로그램에서 온유 리모트를 엽니다. 메뉴바에 화면 모양 아이콘이 생깁니다.</li>
  </ol>

  <h2>2. 권한 허용하기</h2>
  <p>처음 열면 '시작하기' 목록이 뜹니다. 위의 두 가지는 꼭 필요합니다.</p>
  <ul>
    <li><b>화면 기록</b> — 다른 기기에 이 맥 화면을 보여 주는 데 필요합니다. 허용한 뒤 목록의 [다시 켜기]를 눌러야 적용됩니다.</li>
    <li><b>손쉬운 사용</b> — 다른 기기에서 이 맥을 조작하는 데 필요합니다.</li>
    <li><b>항상 켜 두기</b> — 켜 두면 로그인할 때 자동으로 켜지고, 꺼져도 다시 켜집니다. 시스템 설정 › 일반 › 로그인 항목에서 허용이 필요할 수 있습니다.</li>
  </ul>
  <div class="note">macOS는 화면을 공유하는 동안 메뉴바에 표시를 띄웁니다. 맥 앞에서 그 표시의 [중지]를 누르면 연결이 끝납니다.</div>

  <h2>3. 아이폰·아이패드에서 연결하기</h2>
  <ol>
    <li><a href="{APPSTORE}">App Store에서 온유 리모트</a>를 받습니다.</li>
    <li>맥과 <b>같은 Wi-Fi</b>에 연결하고 앱을 엽니다. 로컬 네트워크 접근을 허용하면 목록에 맥이 나타납니다.</li>
    <li>[연결]을 누르면 맥 화면에 <b>6자리 숫자</b>가 뜹니다. 그 숫자를 기기에 입력하면 페어링이 끝나고, 다음부터는 바로 연결됩니다.</li>
  </ol>

  <h2>4. 다른 맥에서 연결하기</h2>
  <p>제어하는 맥에도 같은 앱을 설치합니다. 메뉴바 아이콘 › <b>온유 리모트 열기</b>에서 연결할 맥을 고르면 원격 창이 열립니다. 손쉬운 사용 권한을 주면 ⌘Tab·⌘Space 같은 시스템 단축키도 원격 맥으로 가고, <b>⌃⌥를 빠르게 두 번</b> 누르면 내 맥으로 돌아옵니다.</p>

  <h2>5. 밖에서 연결하기</h2>
  <ol>
    <li>맥과 기기 모두에 <a href="{TAILSCALE}">Tailscale</a>(무료)을 설치하고 <b>같은 계정</b>으로 로그인합니다.</li>
    <li>같은 Wi-Fi에서 한 번 연결해 두면, 밖에서는 목록의 같은 맥을 눌러도 자동으로 Tailscale로 연결됩니다.</li>
    <li>목록에 없으면 [맥 추가]에 맥의 Tailscale 이름이나 <code>100.</code>으로 시작하는 주소를 넣습니다.</li>
  </ol>
  <h3>밖에서 느릴 때</h3>
  <p>Tailscale이 직접 연결하지 못하면 해외 중계 서버를 거쳐 0.1초쯤 늦어집니다. 이럴 때는 앱이 화면에 알려 줍니다. 제어받는 맥이 있는 곳의 공유기 설정에서 <b>포트포워딩</b>으로 <code>UDP 41641</code>(안내에 나온 번호)을 그 맥의 내부 주소로 열어 두면 직접 연결됩니다. 이 포트는 Tailscale의 것이라, 같은 Tailscale 계정의 기기만 통과합니다.</p>

  <h2>업데이트와 삭제</h2>
  <ul>
    <li><b>업데이트</b> — 새 DMG를 받아 응용 프로그램 폴더의 앱을 바꿔 넣습니다. 페어링과 설정은 그대로 남습니다. 아이폰·아이패드는 App Store에서 업데이트됩니다.</li>
    <li><b>삭제</b> — 메뉴바 아이콘에서 [항상 켜 두기]를 끄고 종료한 뒤, 응용 프로그램 폴더에서 앱을 휴지통으로 옮깁니다. 페어링 정보까지 지우려면 <code>~/Library/Application Support/MacRemote</code> 폴더를 지웁니다.</li>
  </ul>
  <p style="margin-top:32px"><a class="btn" href="./#download">맥 앱 받기</a> &nbsp; <a class="btn ghost" href="support.html">자주 묻는 것</a></p>
</article>
""", desc="온유 리모트 설치 방법 — 맥에 설치, 권한 허용, 아이폰·아이패드 연결, Tailscale로 밖에서 연결하기.", sub_title="설치 안내")


def qa(q, a):
    return f"<details><summary>{q}</summary><p>{a}</p></details>"


FAQ = "".join([
    qa("맥이 목록에 안 보여요", "맥에서 온유 리모트가 켜져 있는지, 두 기기가 같은 Wi-Fi인지 확인하세요. 아이폰·아이패드는 설정 › 개인정보 보호 및 보안 › 로컬 네트워크에서 온유 리모트를 허용해야 합니다."),
    qa("화면이 안 나오거나 연결이 바로 끊겨요", "맥의 시스템 설정 › 개인정보 보호 및 보안 › 화면 기록에서 온유 리모트를 허용한 뒤 앱을 다시 켜세요."),
    qa("화면은 보이는데 조작이 안 돼요", "맥의 시스템 설정 › 개인정보 보호 및 보안 › 손쉬운 사용에서 온유 리모트를 허용하세요."),
    qa("밖에서 연결하려면", f"두 기기 모두 <a href=\"{TAILSCALE}\">Tailscale</a>을 같은 계정으로 켜고, 같은 Wi-Fi에서 한 번 연결해 두세요. 자세한 순서는 <a href=\"install.html\">설치 안내</a>에 있습니다."),
    qa("밖에서 느려요", "앱의 연결 상태(점)를 누르면 지연이 보입니다. 중계 서버를 거치면 100ms가 넘습니다. 제어받는 맥 쪽 공유기의 포트포워딩에서 UDP 41641(연결 중 안내에 나온 번호)을 그 맥의 내부 주소로 열어 두면 직접 연결돼 빨라집니다."),
    qa("한/영이 안 바뀌어요", "패널의 [한/영] 버튼이나 연결한 키보드의 한/영(Caps Lock) 키를 누르세요. 맥에서 맥을 제어할 때는 내 맥의 한/영을 바꾸면 원격 맥도 따라 바뀝니다. 맥 앱을 최신 버전으로 업데이트해 주세요."),
    qa("맥에서 맥을 제어할 때 ⌘Tab이 내 맥에서 동작해요", "내 맥에서 온유 리모트에 손쉬운 사용 권한을 주고, 커서를 원격 화면 안에 두세요. 내 맥으로 돌아오려면 ⌃⌥를 빠르게 두 번 누릅니다."),
    qa("맥 알림이 안 와요", "아이폰 설정 › 맥 알림 받기를 켜고 알림을 허용하세요. 맥과 아이폰이 같은 iCloud 계정이어야 하고, 맥의 온유 리모트 창 › 아이폰으로 알림도 켜져 있어야 합니다. 맥 앱과 아이폰 앱 모두 1.1 이상이 필요합니다."),
    qa("페어링을 다시 하고 싶어요 / 기기를 잃어버렸어요", "맥의 온유 리모트 창 › 페어링된 기기에서 그 기기를 지우세요. 그 기기는 맥 화면의 숫자를 다시 넣어야 연결할 수 있습니다."),
    qa("맥이 꺼져 있거나 잠들어 있으면요", "맥이 켜져 있고 온유 리모트가 실행 중이어야 합니다. [항상 켜 두기]를 켜 두면 로그인할 때 켜지고 꺼져도 다시 켜집니다. 데스크톱 맥은 [잠자기 안 함]으로 본체가 잠들지 않게 할 수 있습니다."),
    qa("연결을 끊으면 맥이 멈추거나 화면이 안 켜져요", "맥 앱을 1.1.3 이상으로 업데이트하세요. 인텔 맥은 온유 리모트 창에서 '제어하는 기기 화면에 맞추기'와 '공유 중 색 프로파일을 애플 표준으로'를 꺼 주세요. 외장 모니터가 검게 남으면 모니터 전원 버튼을 누르고, '연결 중 외장 모니터 대기'를 꺼 두세요."),
    qa("다른 사람이 내 맥에 연결할 수 있나요", "아니요. 맥 화면에 뜨는 6자리 숫자를 넣어 페어링한 기기만 연결할 수 있습니다. 숫자를 5번 틀리면 10분 동안 새 기기 연결을 막고, 인터넷 쪽에서 오는 처음 페어링은 받지 않습니다."),
])

page("support.html", "지원 — 온유 리모트", f"""
<article class="article">
  <h1>지원</h1>
  <p class="caption">자주 묻는 것부터 확인해 보세요. 해결되지 않으면 문의를 남겨 주세요.</p>
  <p style="margin:24px 0 32px"><a class="btn" href="{ISSUES}">문의 남기기</a> &nbsp; <a class="btn ghost" href="install.html">설치 안내</a></p>
  <h2>자주 묻는 것</h2>
  {FAQ}
  <h2>앱 안 도움말</h2>
  <p>아이폰·아이패드는 목록 화면의 [?] 또는 설정 › 사용 설명서, 맥은 온유 리모트 창의 [?]에서 사용 설명서를 볼 수 있습니다.</p>
</article>
""", desc="온유 리모트 지원 — 자주 묻는 것과 문의.", sub_title="지원")

page("privacy.html", "개인정보 처리방침 — 온유 리모트", f"""
<article class="article">
  <h1>개인정보 처리방침</h1>
  <p class="caption">온유 리모트 · 시행일 2026년 11월 11일 (1.1)</p>
  <div class="note"><b>온유 리모트는 개인정보를 수집하지 않습니다.</b> 개발자나 제3자의 서버로 어떤 정보도 보내지 않으며, 광고·분석·추적 도구를 쓰지 않습니다.</div>

  <h2>앱이 다루는 정보</h2>
  <ul>
    <li><b>화면·입력·파일</b>: 사용자가 연결한 자신의 기기끼리 직접 주고받습니다. 전송 내용은 연결마다 새로 만든 키로 암호화되며, 어디에도 저장하지 않습니다.</li>
    <li><b>페어링 정보</b>: 처음 연결할 때 만든 페어링 열쇠와 기기 이름은 각 기기 안에만 저장됩니다(아이폰·아이패드는 키체인). 앱을 지우면 함께 지워집니다.</li>
    <li><b>받은 파일</b>: 맥 ↔ 맥 파일 전송으로 받은 파일은 받는 맥의 다운로드/온유 리모트 폴더에만 저장됩니다.</li>
    <li><b>로컬 네트워크</b>: 같은 Wi-Fi에 있는 맥을 찾기 위해서만 사용합니다.</li>
    <li><b>맥 알림 받기(선택)</b>: 사용자가 켜면, 맥이 보내는 알림(제목·내용·맥 이름)을 사용자 <b>본인 iCloud 계정의 개인 저장소</b>(Apple CloudKit)에 잠시 저장해 같은 계정의 아이폰·아이패드로 전달합니다. 개발자는 이 저장소에 접근할 수 없으며, 기록은 이틀 뒤 맥이 지웁니다.</li>
    <li><b>다른 앱 알림 전달(선택, 맥)</b>: 사용자가 직접 고른 앱의 알림만 맥의 알림 센터 기록에서 읽어 위 방식으로 전달합니다. 기본으로 꺼져 있고, 켜려면 사용자가 '전체 디스크 접근' 권한을 줘야 합니다. 고르지 않은 앱의 알림 내용은 읽지 않습니다.</li>
    <li><b>클립보드 공유(선택, 맥 ↔ 맥)</b>: 연결된 두 맥 사이에서 복사한 글자만 암호화해 주고받으며 저장하지 않습니다. 암호 관리자가 숨김으로 표시한 내용은 보내지 않습니다.</li>
    <li><b>진단 기록(맥)</b>: 연결 시작·끝, 오류 같은 동작 기록만 맥 안(~/Library/Application Support/MacRemote)에 남깁니다. 화면·입력·알림 내용은 남기지 않습니다.</li>
  </ul>

  <h2>외부 서비스</h2>
  <p>맥 알림 받기는 Apple의 iCloud(CloudKit)와 푸시 알림을 사용하며, Apple의 개인정보 처리방침을 따릅니다.</p>
  <p>밖에서 연결할 때 사용자가 직접 설치한 Tailscale을 쓸 수 있습니다. Tailscale은 별도 서비스이며 그 회사의 개인정보 처리방침을 따릅니다. 온유 리모트는 Tailscale에 어떤 정보도 따로 보내지 않습니다.</p>
  <p>이 웹사이트는 GitHub Pages로 제공되며, 쿠키나 분석 도구를 쓰지 않습니다. 내려받기 정보를 보여 주려고 GitHub의 공개 정보를 읽습니다.</p>

  <h2>Privacy Policy (English)</h2>
  <p>Onyu Remote does not collect any personal data. Screen, input and files are sent only between the user's own devices, end-to-end encrypted per connection, and are not stored. Pairing keys stay on each device. No analytics, ads or tracking. Optional Mac-to-iPhone alerts are stored briefly in the user's own private iCloud database (Apple CloudKit), which the developer cannot access, and are deleted after two days. Forwarding other apps' notifications is off by default and reads only the apps the user selects. Clipboard sharing between Macs is encrypted and not stored.</p>

  <h2>문의</h2>
  <p><a href="{ISSUES}">GitHub에서 문의하기</a></p>
</article>
""", desc="온유 리모트 개인정보 처리방침 — 개인정보를 수집하지 않습니다.", sub_title="개인정보 처리방침")

VERSIONS = [
    ("1.1.3", "2026년 11월 11일 · 맥", [
        "인텔 맥에서 연결을 끊을 때 맥이 멈추던 문제에 대응했습니다. 화면 구성을 바꾸는 기능을 인텔 맥에서는 기본으로 끕니다.",
        "연결을 끊은 뒤 외장 모니터가 켜지지 않을 수 있던 문제를 고쳤습니다('연결 중 외장 모니터 대기'는 원할 때만 켬).",
    ]),
    ("1.1.2", "2026년 11월 11일 · 맥", [
        "화면 캡처가 멈춰도 연결을 끊지 않고 다시 시작합니다.",
        "원격 창이 앞으로 오면 클릭하지 않아도 키보드가 원격 맥으로 갑니다. 메뉴바 메뉴에 Tailscale로 닿는 맥도 나옵니다.",
        "처음 쓸 때 '시작하기' 목록으로 권한·항상 켜 두기·Tailscale·아이폰 알림을 한눈에.",
        "밖에서 중계 서버를 거쳐 느릴 때 알려 주고, 공유기에서 열 포트를 안내합니다.",
        "페어링 정보를 더 안전하게 저장합니다.",
    ]),
    ("1.1.1", "2026년 11월 11일 · 맥", [
        "맥에서 다른 맥을 제어할 때 한/영이 잘 안 먹던 문제를 고쳤습니다. 한/영을 바꾼 직후 바로 친 글자도 바뀐 언어로 들어갑니다.",
    ]),
    ("1.1", "2026년 11월 11일 · 맥 · 아이폰·아이패드는 11월 12일 App Store 공개", [
        "한/영 전환과 ⌘·⌥·⌃·⇧ 키를 맥에 그대로 보냅니다. 맥에서 맥을 제어할 때는 ⌘Tab·⌘Space까지.",
        "아이폰·아이패드 패널: 수정 키 고정, 방향키, Tab, 복사·붙여넣기, F키, 직접 만드는 '내 버튼'.",
        "맥 알림을 아이폰으로(iCloud), 연결 중 맥 화면 가리기, 화면이 멈추면 더 선명하게.",
        "맥끼리 클립보드 공유, 항상 켜 두기, 페어링된 기기 하나씩 지우기, 앱 안 사용 설명서.",
    ]),
    ("1.0", "2026년 11월 4일 · 맥 · 아이폰·아이패드는 11월 6일 App Store 공개", ["첫 출시."]),
]
vhtml = "".join(f'<div class="version"><h2>{v}</h2><p class="caption">{d}</p><ul>{"".join(f"<li>{x}</li>" for x in items)}</ul></div>' for v, d, items in VERSIONS)

page("changelog.html", "변경 기록 — 온유 리모트", f"""
<article class="article">
  <h1>변경 기록</h1>
  <p class="caption">버전별로 달라진 점입니다. 설치 파일은 <a href="./#download">내려받기</a>, 이전 버전은 <a href="https://github.com/{REPO}/releases">모든 버전</a>에 있습니다.</p>
  {vhtml}
</article>
""", desc="온유 리모트 버전별 변경 기록.", sub_title="변경 기록")

print("만든 페이지: index install support privacy changelog")
