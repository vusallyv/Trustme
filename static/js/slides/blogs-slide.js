var swiper = new Swiper(".blogs__slide", {
    slidesPerView: 1,
    spaceBetween: 20,
    speed: 500,
    loop: true,
    navigation: {
        nextEl: ".blogs-next-btn",
        prevEl: ".blogs-prev-btn",
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