let n = 0;
const container = document.querySelector(".container");
const buttons = document.querySelectorAll(".btn");

buttons.forEach(btn => {
    btn.addEventListener("click", (e) => {
        if(btn.classList.contains("left-btn"))
        {
            n++;
            if(n>7)
                n=1;
        }
        else
        {
            n--;
            if(n<1)
                n=7;
        }
        container.style.background=`url("image/${n}.jpg") center/cover fixed no-repeat`;
    })
});