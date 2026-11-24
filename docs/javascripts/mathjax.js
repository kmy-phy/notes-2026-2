window.MathJax = {
  loader: { load: ["[tex]/unicode"] },
  tex: {
    packages: { "[+]": ["unicode"] },
    // 닫힌곡면 적분 기호 ∯
    macros: { oiint: "\\mathop{\\unicode{x222F}}\\nolimits" },
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true,
    tags: "ams"
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

// 페이지를 옮길 때마다 수식을 다시 렌더링
document$.subscribe(() => {
  // 첫 로드 때는 MathJax가 아직 안 올라와 있다: 그때는 MathJax가 스스로 렌더링한다
  if (!MathJax.startup || !MathJax.startup.output) return;
  MathJax.startup.output.clearCache();
  MathJax.typesetClear();
  MathJax.texReset();
  MathJax.typesetPromise();
});
