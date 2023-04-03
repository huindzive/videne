// 1. ievērojot pareizu tabulas HTML struktūru, aizpildīt tabulu ar vienu rindu, kas satur
// 3 šūnas - vārdu, uzvārdu, klasi
const people =[
    {
        name: 'Arturs',
        surname: 'Balnass',
        age: 17
    }
]
const table = document.getElementById('name')
    for(const person of people){
        const row= document.createElement('tr');
        row.innerHTML = '<td>' + person.name + '</td><td>' + person.surname + '</td><td>' + person.age + '</td>'
        table.appendChild(row)
    }
// 2. klikšķinot abas pogas, attiecīgā count elementa saturam jāpalielinās par 1
// 3. summas elementā uzrādīt abu count elementu summu

let skaits1 = 0
let sum2 = 0
const count1 = document.getElementById('count1')
const sum = document.getElementById('sum')
count1.innerHTML = skaits1
sum.innerHTML = sum2

function plusOne1() {
    skaits1 += 1;
    count1.innerHTML = skaits1;
    sum2 +=1;
    sum.innerHTML = sum2
}

let skaits2 = 0
const count2 = document.getElementById('count2')
count2.innerHTML = skaits2

function plusOne2() {
    skaits2 += 1;
    count2.innerHTML = skaits2;
    sum2 +=1;
    sum.innerHTML = sum2
}
// 4. switch theme nomaina lapas motīvu, ja fons ir balts un teksts melns -
// nomaina fonu un melnu un tekstu uz baltu un otrādi.

function switchTheme(){
    if(document.body.style.backgroundColor === "white"){
        document.body.style.backgroundColor = "black"
        document.body.style.color = "white"
        console.log(0)
    }
    else{
        document.body.style.backgroundColor = "white"
        document.body.style.color = "black"
        console.log(1)
    }
}
