var swiper = new Swiper(".recommend__slide", {
    slidesPerView: 1,
    spaceBetween: 35,
    speed: 500,
    loop: true,
    pagination: {
        el: ".swiper-pagination",
        clickable: true
    },
    breakpoints: {
        480: {
          slidesPerView: 2,
        },
      }
});