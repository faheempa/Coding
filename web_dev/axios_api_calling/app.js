const input = document.querySelector(".input");
const submit_btn = document.querySelector(".btn");


submit_btn.addEventListener("click", async (e) => {
    e.preventDefault();
    const searchTerm = input.value;

    // fetching data
    const config = { params: { q: searchTerm } };
    const result = await axios.get("https://api.tvmaze.com/search/shows", config);

    makeImages(result.data);
    input.value = "";
})

function makeImages(result)
{
    const images = document.querySelector(".images");
    images.innerHTML="";
    result.forEach(movie => {
        if(movie.show.image)
        {
            const newImage = document.createElement("img");
            newImage.src = movie.show.image.medium;
            images.append(newImage);
        }
    });
}