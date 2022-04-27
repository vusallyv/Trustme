var swiper = new Swiper("#advantages__slide", {
    slidesPerView: 3,
    spaceBetween: 10,
    speed: 500,
    loop: true,
    navigation: {
        nextEl: ".advantages-next-btn",
        prevEl: ".advantages-prev-btn",
    },
});