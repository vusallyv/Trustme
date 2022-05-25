const tabBtn1 = document.getElementById("brief-tab__btn-1")
const tabBtn2 = document.getElementById("brief-tab__btn-2")
const tabBtn3 = document.getElementById("brief-tab__btn-3")

function OpenTab(evt, index) {
    var i, tabcontent, tablinks, decor;
    tabcontent = document.getElementsByClassName("tabcontent");

    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    tablinks = document.getElementsByClassName("brief-tab__btn");
    decor = document.getElementsByClassName("brief__decor");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
        decor[i].className = decor[i].className.replace(" active", "");
    }

    document.getElementById(index).style.display = "block";
    document.getElementById(`${index}-decor`).classList.add("active");
    evt.currentTarget.className += " active";

    if (tabBtn3.classList.contains("active")) {
        tabBtn1.classList.add("active")
        tabBtn2.classList.add("active")
    } else if (tabBtn2.classList.contains("active")) {
        tabBtn1.classList.add("active")
    }
}

tabBtn1.click()
document.getElementById("move-brief-2").onclick = () => tabBtn2.click()
document.getElementById("move-brief-3").onclick = () => tabBtn3.click()

document.querySelector(".brief__back-btn").onclick = () =>{
     if (tabBtn2.classList.contains("active") && !tabBtn3.classList.contains("active")) {
        tabBtn1.click()
     }else if(tabBtn3.classList.contains("active") && tabBtn2.classList.contains("active")){
        tabBtn2.click()
     }
}