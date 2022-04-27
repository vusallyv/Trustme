// fixed navbar
window.addEventListener("scroll", () => {
    const navBar = document.querySelector("header");
    const scrollHeight = window.pageYOffset;
    const navHeight = navBar.getBoundingClientRect().height;

    if (scrollHeight > navHeight) {
        navBar.classList.add("fix-nav");
    } else {
        navBar.classList.remove("fix-nav");
    }
});

// OPEN NAVBAR 
document.querySelector(".navbar__open").onclick = () => {
    document.querySelector(".mob-navbar").classList.add("active")
    document.body.style.overflow = "hidden"
}

// CLOSE NAVBAR 
document.querySelector(".mob-navbar__close").onclick = () => {
    document.querySelector(".mob-navbar").classList.remove("active")
    document.body.style.overflow = "initial"
}

// SCROLL ACTIVE ITEM
if (document.querySelector(".categories-tab__item--active")) {
    const scrollDistance = document.querySelector(".categories-tab__item--active").offsetLeft
    document.querySelector(".categories-tab").scrollLeft = scrollDistance - 100
}
