arr = [
    {
        name: "apple",
        color: "red",
        src: "apple.jpg"
    },
    {
        name: "pear",
        color: "green",
        src: "pear.jpg"
    },
    {
        name: "orange",
        color: "orange",
        src: "orange.jpg"
    }
]

// arr.sort(function(a, b) {
//     var keyA = a.name,
//       keyB = b.name;
//     // Compare the 2 keys
//     if (keyA[0] < keyB[0]) return -1;
//     if (keyA[0] > keyB[0]) return 1;
//     return 0;
//   });
  
// console.log(arr);

const div = document.getElementById("main")
for(const o of arr){
    const wrap = document.createElement("div")
    const title = document.createElement("h1")
    const image = document.createElement("img")

    title.style.color = o.color
    title.innerHTML = o.name

    image.src = o.src
    image.style.width = "400px"

    wrap.append(title)
    wrap.append(image)
    wrap.style.textAlign = "center"

    div.append(wrap)
}

