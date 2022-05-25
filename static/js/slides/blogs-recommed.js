var swiper = new Swiper(".blog-detail__slide", {
    slidesPerView: 1,
    spaceBetween: 30,
    speed: 500,
    loop: true,
    pagination: {
        el: ".swiper-pagination",
        clickable: true
    },
    breakpoints: {
        576: {
          slidesPerView: 2,
        },
      }
});