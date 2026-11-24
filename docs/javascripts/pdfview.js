// PDF 링크를 누르면 바로 내려받지 않고 사이트 안의 PDF 보기 화면(viewer.html)으로 연다.
// 보기 화면 위쪽의 버튼으로 내려받는다. (Ctrl/⌘ 클릭 등은 브라우저 기본 동작 그대로)
(function () {
  var src = document.currentScript && document.currentScript.src;
  if (!src) return;
  var base = src.replace(/javascripts\/pdfview\.js.*$/, "");   // 사이트 루트 URL

  document.addEventListener("click", function (e) {
    if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    var a = e.target.closest && e.target.closest("a.pdf-link, .pdf-links a");
    if (!a || !/\.pdf(\?|#|$)/.test(a.href) || a.href.indexOf(base) !== 0) return;
    e.preventDefault();
    e.stopPropagation();
    var q = "file=" + encodeURIComponent(a.href.slice(base.length)) +
            "&name=" + encodeURIComponent(a.getAttribute("download") || a.href.split("/").pop()) +
            "&lang=" + (/-ko\//.test(location.pathname) ? "ko" : "en");
    location.href = base + "viewer.html?" + q;
  }, true);
})();
