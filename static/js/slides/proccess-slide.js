var swiper = new Swiper(".process__slide", {
    slidesPerView: 3,
    spaceBetween: 20,
    speed: 500,
    loop: true,
    pagination: {
        el: ".swiper-pagination",
        clickable: true
    },
    breakpoints: {
        650: {
          slidesPerView: 5,
        },
        450: {
          slidesPerView: 4,
        },
      }
});