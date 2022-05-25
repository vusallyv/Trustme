var swiper = new Swiper(".seo-rank__slide", {
    slidesPerView: 1,
    spaceBetween: 20,
    speed: 500,
    loop: true,
    navigation: {
        nextEl: ".seo-rank-next-btn",
        prevEl: ".seo-rank-prev-btn",
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true
      },
    breakpoints: {
        600: {
            slidesPerView: 2,
        },
        900: {
            slidesPerView: 3,
        },
        1200: {
            slidesPerView: 2,
        },
    },
});