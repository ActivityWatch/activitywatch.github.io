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

  let lastYear;
  // Append each item to the timeline
  timelineItems.forEach((item) => {
    const dateStr = item.querySelector("time")?.getAttribute("datetime");
    const thisYear = dateStr ? new Date(dateStr).getFullYear() : null;

    // Add year separator if the year has changed
    if (thisYear && thisYear !== lastYear) {
      const yearSeparator = document.createElement("h2");
      yearSeparator.textContent = thisYear.toString();
      yearSeparator.setAttribute("data-type", thisYear.toString());
      yearSeparator.classList.add("year-separator", "text-2xl", "px-3", "pb-2", "pt-3");
      timeline.appendChild(yearSeparator);

      lastYear = thisYear;
    }

    timeline.appendChild(item) 
  });


  // Add event listeners to filter buttons
  filterBtns.forEach((btn) => {
    btn.addEventListener("click", function () {
      const type = this.getAttribute("data-type");
      const yearVisibilityCount = {};

      // Re-set active filter button
      filterBtns.forEach((b) =>
        b.classList.remove("bg-blue-500", "text-white")
      );
      this.classList.add("bg-blue-500", "text-white");

      // Show/hide timeline items
      timelineItems.forEach((item) => {
        const dateStr = item.querySelector("time")?.getAttribute("datetime");
        const thisYear = dateStr ? new Date(dateStr).getFullYear() : null;

        // Make sure year is in the count object
        yearVisibilityCount[thisYear] = yearVisibilityCount[thisYear] || 0;

        if (type === "all" || item.getAttribute("data-type") === type) {
          item.classList.remove("hidden");

          // Count visible items for each year
          if (thisYear) {
            yearVisibilityCount[thisYear] += 1;
          }
        } else {
          item.classList.add("hidden");
        }
      });

      // Show/hide year separators for each element
      for (const separator of document.querySelectorAll(".year-separator")) {
        const year = separator.getAttribute("data-type");
        if (type === "all" || yearVisibilityCount[year] > 0) {
          separator.classList.remove("hidden");
        } else {
          separator.classList.add("hidden");
        }
      }
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
