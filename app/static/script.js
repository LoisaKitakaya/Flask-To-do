const addHighlight = () => {
  const aboutBtn = document.getElementById("about");
  aboutBtn.classList.add("active");
};

const removeHighlight = () => {
  const aboutBtn = document.getElementById("about");
  aboutBtn.classList.remove("active");
};

const hoverState = () => {
  const pageBanner = document.getElementById("page-banner");
  pageBanner.style.transform = "scale(1.025)";
};

const hoverStateReverse = () => {
  const pageBanner = document.getElementById("page-banner");
  pageBanner.style.transform = "scale(1)";
};
