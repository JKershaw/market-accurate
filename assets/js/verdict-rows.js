(function () {
  // Tag table rows that carry verdict markers so CSS can tint them.
  // Looks for ✅ / ❌ glyphs or the literal words CORRECT / INCORRECT.
  var rows = document.querySelectorAll(".site-main tbody tr");
  rows.forEach(function (row) {
    var text = row.textContent;
    if (text.indexOf("✅") !== -1 || /\bCORRECT\b/.test(text) && !/INCORRECT/.test(text)) {
      row.classList.add("verdict-correct");
    } else if (text.indexOf("❌") !== -1 || /\bINCORRECT\b/.test(text)) {
      row.classList.add("verdict-incorrect");
    }
  });
})();
