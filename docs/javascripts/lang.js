// 언어 탭을 누르면 지금 보던 절(#앵커)을 유지한 채 다른 언어 페이지로 이동
document.addEventListener("click", function (e) {
  var a = e.target.closest && e.target.closest(".lang-switch a[href]");
  if (!a || !location.hash) return;
  e.preventDefault();
  location.href = a.getAttribute("href") + location.hash;
});
