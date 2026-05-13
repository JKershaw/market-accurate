(function () {
  var nav = document.getElementById("analysis-toc-nav");
  if (!nav) return;
  var body = document.querySelector(".analysis-body");
  if (!body) return;

  var headings = body.querySelectorAll("h2, h3");
  if (headings.length < 3) {
    // Not enough headings to warrant a TOC — hide the widget.
    var toc = document.querySelector(".analysis-toc");
    if (toc) toc.style.display = "none";
    return;
  }

  var list = document.createElement("ul");
  list.className = "toc-list";

  headings.forEach(function (h) {
    if (!h.id) {
      // Generate slug from text if Jekyll/kramdown didn't auto-assign.
      var slug = h.textContent
        .toLowerCase()
        .trim()
        .replace(/[^\w\s-]/g, "")
        .replace(/\s+/g, "-");
      h.id = slug || "section";
    }
    var li = document.createElement("li");
    li.className = "toc-" + h.tagName.toLowerCase();
    var a = document.createElement("a");
    a.href = "#" + h.id;
    a.textContent = h.textContent;
    li.appendChild(a);
    list.appendChild(li);
  });

  nav.appendChild(list);
})();
