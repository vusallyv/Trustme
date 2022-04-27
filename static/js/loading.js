setTimeout(() => {
    document.querySelectorAll(".loading-gif").forEach(element => {
        element.style.display = "none"
    });

    document.querySelectorAll(".loading-item").forEach(element => {
        element.classList.replace("d-none", "d-block")
    });
}, 1);