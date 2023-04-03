const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': '092d095284mshf1f625d9d5b639ep167dbbjsn288e3836d4c3',
		'X-RapidAPI-Host': 'love-calculator.p.rapidapi.com'
	}
};

function calculate(){
    male = document.getElementById("male").value
    female = document.getElementById("female").value
    
    fetch('https://love-calculator.p.rapidapi.com/getPercentage?sname='+male+'%fname'+female, options)
	.then(response => response.json())
	.then(response => {
        console.log(response);
        document.getElementById('result').innerHTML = response['percentage'] + '%';
        document.getElementById("recom").innerHTML = response['result'];
    })
	.catch(err => console.error(err));
}