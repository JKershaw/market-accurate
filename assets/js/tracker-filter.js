(function () {
  var filter = document.getElementById("tracker-filter");
  if (!filter) return;

  var qInput = document.getElementById("tracker-q");
  var statusSel = document.getElementById("tracker-status");
  var analysisSel = document.getElementById("tracker-analysis");
  var yearSel = document.getElementById("tracker-year");
  var resetBtn = document.getElementById("tracker-reset");
  var countEl = document.getElementById("tracker-count");

  var sections = Array.prototype.slice.call(document.querySelectorAll(".tracker-section"));
  var rows = Array.prototype.slice.call(document.querySelectorAll(".tracker-table tbody tr"));

  // Populate analysis and year dropdowns from row data
  var analyses = {};
  var years = {};
  rows.forEach(function (r) {
    var a = r.getAttribute("data-analysis");
    var y = r.getAttribute("data-year");
    if (a) analyses[a] = true;
    if (y) years[y] = true;
  });

  Object.keys(analyses).sort().forEach(function (a) {
    var opt = document.createElement("option");
    opt.value = a;
    opt.textContent = a;
    analysisSel.appendChild(opt);
  });

  Object.keys(years).sort().forEach(function (y) {
    var opt = document.createElement("option");
    opt.value = y;
    opt.textContent = y;
    yearSel.appendChild(opt);
  });

  function apply() {
    var q = (qInput.value || "").trim().toLowerCase();
    var status = statusSel.value;
    var analysis = analysisSel.value;
    var year = yearSel.value;

    var visibleCount = 0;
    rows.forEach(function (r) {
      var matches = true;
      if (status && r.getAttribute("data-status") !== status) matches = false;
      if (matches && analysis && r.getAttribute("data-analysis") !== analysis) matches = false;
      if (matches && year && r.getAttribute("data-year") !== year) matches = false;
      if (matches && q) {
        var hay = r.textContent.toLowerCase();
        if (hay.indexOf(q) === -1) matches = false;
      }
      r.style.display = matches ? "" : "none";
      if (matches) visibleCount++;
    });

    // Hide sections whose visible row count is zero
    sections.forEach(function (sec) {
      var trs = sec.querySelectorAll(".tracker-table tbody tr");
      var any = false;
      for (var i = 0; i < trs.length; i++) {
        if (trs[i].style.display !== "none") { any = true; break; }
      }
      sec.style.display = any ? "" : "none";
    });

    if (countEl) {
      countEl.textContent =
        visibleCount === rows.length
          ? rows.length + " predictions"
          : "Showing " + visibleCount + " of " + rows.length + " predictions";
    }
  }

  [qInput, statusSel, analysisSel, yearSel].forEach(function (el) {
    el.addEventListener("input", apply);
    el.addEventListener("change", apply);
  });

  resetBtn.addEventListener("click", function () {
    qInput.value = "";
    statusSel.value = "";
    analysisSel.value = "";
    yearSel.value = "";
    apply();
  });

  apply();
})();
