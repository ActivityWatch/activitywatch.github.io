document.addEventListener("DOMContentLoaded", function () {
  let timelineItems = document.querySelectorAll(".timeline-item");
  const filterBtns = document.querySelectorAll(".filter-btn");

  // Sort by date in-place
  timelineItems = Array.from(timelineItems).sort((a, b) => {
    const aDateStr = a.querySelector("time")?.getAttribute("datetime");
    const bDateStr = b.querySelector("time")?.getAttribute("datetime");

    const aDate = aDateStr ? new Date(aDateStr) : new Date("1970-01-01");
    const bDate = bDateStr ? new Date(bDateStr) : new Date("1970-01-01");

    return bDate - aDate;
  });

  // For some reason, this doesn't quite work
  const timeline = document.querySelector(".timeline");
  timeline.innerHTML = "";

  timelineItems.forEach((item) => timeline.appendChild(item)); // cloneNode to force re-attachment

  filterBtns.forEach((btn) => {
    btn.addEventListener("click", function () {
      const type = this.getAttribute("data-type");
      filterBtns.forEach((b) =>
        b.classList.remove("bg-blue-500", "text-white")
      );
      this.classList.add("bg-blue-500", "text-white");
      timelineItems.forEach((item) => {
        if (type === "all" || item.getAttribute("data-type") === type) {
          item.classList.remove("hidden");
        } else {
          item.classList.add("hidden");
        }
      });
    });
  });

  // Find <a> tags with empty hrefs
  // Change them to span tags
  const emptyLinks = document.querySelectorAll("a[href='']");
  emptyLinks.forEach((link) => {
    const span = document.createElement("span");
    span.innerHTML = link.innerHTML;
    link.parentNode.replaceChild(span, link);
  });
});
