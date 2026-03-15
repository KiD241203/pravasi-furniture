const readBtn = document.getElementById("readMore");
const desc = document.getElementById("desc");

readBtn.addEventListener("click", function(){

desc.classList.toggle("expand");

if(desc.classList.contains("expand")){
readBtn.innerText="Read less";
}else{
readBtn.innerText="Read more";
}

});

/* quantity buttons */

// let minus = document.querySelector('.minus')
// let plus = document.querySelector('.plus')
// let input = document.querySelector('.qty-input')

// minus.addEventListener('click',()=>{
//     if(input.value >1){
//         input.value --;
//     }
// })

// plus.addEventListener('click',()=>{
//     input.value ++
// })