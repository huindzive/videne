const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': '092d095284mshf1f625d9d5b639ep167dbbjsn288e3836d4c3',
		'X-RapidAPI-Host': 'love-calculator.p.rapidapi.com'
	}
};

function load_data(){
    dzeriens = document.getElementById('ja').value

    fetch('https://www.thecocktaildb.com/api/json/v1/1/search.php?s='+dzeriens)
    .then(response => response.json())
    .then(response => {
        console.log(response)
        // document.getElementById("kkas").innerHTML = response['drinks']
        response["drinks"].forEach(drink=> {
            console.log(drink)
            list_item=document.createElement("li")
            list_item.innerHTML = drink.strDrink
            document.getElementById("kkas2").append(list_item)
            list_image=document.createElement("img")
            list_image.src = drink.strDrinkThumb
            list_image.style = 'width:100px'
            document.getElementById("kkas2").append(list_image)
        })
    })
}