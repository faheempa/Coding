const msg_entry = document.querySelector(".text_input");
const submit_btn = document.querySelector(".submit_button");
const msg_display = document.querySelector(".message");

submit_btn.addEventListener("click", (e) => {
    e.preventDefault();
    if (msg_entry.value !== "") {
        msg_display.textContent = msg_entry.value;
        msg_entry.value = "";
        document.querySelector(".feedback").classList.add("-hide");

    }
    else {
        document.querySelector(".feedback").classList.remove("-hide");
    }
})

submit_btn.addEventListener("mouseover", () => {
    submit_btn.classList.add("-shadow");
})
submit_btn.addEventListener("mouseout", () => {
    submit_btn.classList.remove("-shadow");
})