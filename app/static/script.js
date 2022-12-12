const hoverState = () => {
  const pageBanner = document.getElementById("page-banner");
  pageBanner.style.transform = "scale(1.025)";
};

const hoverStateReverse = () => {
  const pageBanner = document.getElementById("page-banner");
  pageBanner.style.transform = "scale(1)";
};
