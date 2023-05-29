const input = document.querySelector(".form input");
const items = document.querySelectorAll(".item");

input.addEventListener("input", () => {
    let value = input.value.toUpperCase();
    items.forEach(item => {
        let product_name = item.children[1].children[0].textContent.toUpperCase();
        if (product_name.includes(value))
            item.classList.remove("hide")
        else
            item.classList.add("hide")
    })
})