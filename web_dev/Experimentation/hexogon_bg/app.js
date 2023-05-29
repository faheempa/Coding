// grid 
const light = document.querySelector(".hex-grid .light");

document.addEventListener("mousemove", e => {
    light.style.left = `${e.clientX}px`;
    light.style.top = `${e.clientY}px`;
    light.style.display = "block";
})
light.style.display = "none";


document.addEventListener("mouseout", e => {
    light.style.display = "none";
})

// letters
const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

let interval = null;

const myname = document.querySelector(".name");
myname.onmouseover = async function(e) {
    random_effect();
}
function random_effect(n=3)
{  
    let iteration = -1;
    
    clearInterval(interval);
    
    interval = setInterval(() => {
      myname.innerText = myname.innerText
        .split("")
        .map((letter, index) => {
          if(index < iteration) {
            return myname.dataset.value[index];
          }
        
          return letters[Math.floor(Math.random() * 26)]
        })
        .join("");
      
      if(iteration >= myname.dataset.value.length){ 
        clearInterval(interval);
      }
      
      iteration += 1 / n;
    }, 30);
}
random_effect(5);