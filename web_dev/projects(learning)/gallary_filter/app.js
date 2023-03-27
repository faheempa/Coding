const btns = document.querySelectorAll(".-btn");
const pics = document.querySelectorAll(".pic");

btns.forEach((btn) => {
    btn.addEventListener("click", (e) => {
        e.preventDefault();
        let filter = e.target.dataset.filter;
        const active_btn = document.querySelector(".active");
        active_btn.classList.remove("active");
        e.target.classList.add("active");

        pics.forEach(pic => {
            if (pic.classList.contains(`${filter}`) === false)
                pic.classList.add("-hide");
            else
                pic.classList.remove("-hide");

        })
    })
})

