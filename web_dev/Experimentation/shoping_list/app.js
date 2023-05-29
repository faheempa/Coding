
const form = document.querySelector(".itemform");
const input = document.querySelector(".item");
const itemlist = document.querySelector(".itemlist");
const curitem = document.querySelector(".curitem");

form.addEventListener("submit", function (e) {
    e.preventDefault();
    const text = input.value;
    if (text === "") return;
    const newli = document.createElement("li");
    newli.append(text);
    itemlist.append(newli);
    input.value = "";
    curitem.innerText = input.value;
})

itemlist.addEventListener("click", function (e) {
    console.log(e)
    if (e.target.nodeName === "LI") e.target.remove();
})

input.addEventListener("input", function(e)
{
    curitem.innerText = input.value;
})