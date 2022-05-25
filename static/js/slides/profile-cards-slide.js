var swiper = new Swiper(".profile-card__slide", {
    slidesPerView: 1,
    spaceBetween: 20,
    speed: 500,
    loop: true,
    pagination: {
        el: ".swiper-pagination",
        clickable: true
    },
});