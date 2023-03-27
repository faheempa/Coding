const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add("-show");
        } else {
            entry.target.classList.remove("-show");
        }
    })
});

console.log("helo");
const hiddenelements = document.querySelectorAll(".-hide");
hiddenelements.forEach(ele=>observer.observe(ele));