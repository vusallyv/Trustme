var swiper = new Swiper(".clients-comments__slide", {
    slidesPerView: 1,
    spaceBetween: 20,
    speed: 500,
    loop: true,
    navigation: {
        nextEl: ".clients-comments-next-btn",
        prevEl: ".clients-comments-prev-btn",
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true
    },
    breakpoints: {
        768: {
          slidesPerView: 2,
          spaceBetween: 30,
        },
      }
});