const options = {
    method: 'GET',
    headers: {

        'X-RapidAPI-Key': '4b00a3f18amshe5bdc0c197938dbp1b559ejsn8f78bb838ed3',

        'X-RapidAPI-Host': 'free-nba.p.rapidapi.com'

    }

};

let data = []

function load_data(response_data){

    data = response_data

    let dropdown = document.getElementById("teams")

    console.log(response_data)
    response_data.forEach(team => {
        let option_element = document.createElement("option")
        option_element.innerHTML = team.full_name
        option_element.value = team.id
        dropdown.append(option_element)
    });

   

}

let players = []

function load_players(response_players, id){
    players = response_players
    response_players.forEach(player => {
        if(id == player.team.id){
            console.log(player)

        }

 

    });

   

}

fetch('https://free-nba.p.rapidapi.com/teams?page=0&per_page=100', options)
    .then(response => response.json())
    .then(response => load_data (response.data))
    .catch(err => console.error(err));

function select_team(){
    select = document.getElementById("teams")
    i = select.selectedIndex
    console.log(data[i])
    name_element = document.getElementById("name")
    team_element = document.getElementById("team")
    name_element.innerHTML = data[i].id

    fetch('https://free-nba.p.rapidapi.com/players?page=0&per_page=100', options)
        .then(response => response.json())
        .then(response => load_players(response.data, data[i].id))
        .catch(err => console.error(err));

}