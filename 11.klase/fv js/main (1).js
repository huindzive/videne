function changeBodyColor() {
    document.body.style.backgroundColor = "purple";
}

function changeBtnText() {
    document.querySelector("#btn").innerHTML = "clicked";

    // vai arī

    document.getElementById("btn").innerHTML = "clicked";
}

function displayName() {
    const p = document.createElement("p");
    p.innerHTML = "Atis Ozols";
    document.body.append(p);
}
