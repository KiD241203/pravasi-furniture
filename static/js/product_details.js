

let minus = document.getElementsByClassName('minus')[0]
let plus = document.getElementsByClassName('plus')[0]
let input = document.getElementsByClassName('input')[0]

minus.addEventListener('click', ()=>{
    if (input.value > 1){
        input.value--;
    }
})

plus.addEventListener('click', ()=>{
    input.value++
})


let btn = document.getElementById("readMore")
let desc = document.getElementById("desc")

btn.addEventListener("click", function(e){

e.preventDefault()

desc.classList.toggle("expand")

if(desc.classList.contains("expand")){
btn.innerText = "Read less"
}else{
btn.innerText = "Read more"
}

})