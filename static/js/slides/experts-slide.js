var swiper = new Swiper("#experts__slide", {
    slidesPerView: 1,
    spaceBetween: 10,
    speed: 500,
    loop: true,
    breakpoints: {
        576: {
            slidesPerView: 2,
        },
        768: {
            slidesPerView: 3,
        },
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true
    },
    navigation: {
        nextEl: ".experts-next-btn",
        prevEl: ".experts-prev-btn",
    },
});