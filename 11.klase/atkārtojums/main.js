//piekļūšana pie elementiem
// kā nomainām elementu tekstuālo saturu vai stilojumu
const title = document.getElementById('virsraksts')

title.innerHTML = 'Čau';
title.style.color = 'pink'
title.style.backgroundColor = 'black'

//kā izveidojam elementus

const p_elements = document.createElement('p')

p_elements.innerHTML = 'kokaīns'

document.body.append(p_elements)

const saraksts = document.createElement('ul')
const elem1 = document.createElement('li')
elem1.innerHTML = 'Mārcis'
const elem2 = document.createElement('li')
elem2.innerHTML = 'Arturs'

//pievienošana sarakstam
saraksts.append(elem1)
saraksts.append(elem2)

//saraksta pievienošana bodijam
document.body.append(saraksts)

//pogas un funkciju palaišana
//nospiežot pogu

let skaits = 0
const count = document.getElementById('count')
count.innerHTML = skaits

function plusOne(){
    skaits += 1;
    count.innerHTML = skaits;
}
