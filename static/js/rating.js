document.querySelectorAll(".rating-radio").forEach((item) =>{
    item.onchange = (e) =>{
        document.querySelector(".star-rating__score").style.display = "flex"
        const number = document.querySelector(".star-rating__number")
        const result =  document.querySelector(".star-rating__result")
        const rating =  e.target.value

        if (Number(rating)  === 1) {
            result.innerHTML = "Kafi"
        }else if(Number(rating)  === 2){
            result.innerHTML = "Pis"
        }
        else if(Number(rating) === 3){
            result.innerHTML = "Orta"
        }
        else if(Number(rating) === 4){
            result.innerHTML = "Yaxşı"
        }
        else if(Number(rating) === 5){
            result.innerHTML = "Super"
        }

        number.innerHTML = rating
    }
})