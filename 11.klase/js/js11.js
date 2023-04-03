// let x;
// x = 8;
// const y = 23;
// console.log(x);

// if(x>5){
//     console.log('ok')
// }
// else{
//     console.log('no')
// }

// for(let i = 0 ; i < 5 ; i++){
//     console.log(i)
// }

// const a=[1,4,2,7,2]
// console.log(a.length)
// console.log('numbers: ')

// for(const item of a){
//     console.log(item)
// }

// for(let i = 0 ; i< a.length;i++){
//     console.log(a[i])
// }

// let obj = {
//     name:'Arturs',
//     age: 17
// }

// console.log(obj.age)

// function funkcias_nosauk(a,b){
//     return a+b
// }
// console.log(funkcias_nosauk(2,3))

const page = document.createElement('p')
page.innerHTML = '<h1>Hey</h1>'
page.classList.add('red')
document.body.appendChild(page)

const list = document.createElement('ul')

array = ['Mārcis','Tomass','Edgars']
for(const boy of array){
    list.innerHTML += '<li>' + boy + '</li>'
}
document.body.appendChild(list)

const people = [
    {
        name:'Artūrs',
        surname:'Balnass',
        age: 17,
    },
    {
        name: 'Elizabete',
        surname: 'Balnasa',
        age: 22,
    }
]
const table = document.createElement('table')
for(const person of people){
    const row = document.createElement('tr');
    for (const atribute in person){
        row.innerHTML += '<td>' +  person[atribute] + '</td>'
    }
    // row.innerHTML = '<td>' + person.name + '</td><td>' + person.surname + '</td>';
    table.appendChild(row);
}

document.body.appendChild(table)