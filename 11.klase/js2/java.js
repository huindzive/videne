// const luksofors = document.getElementById('luksofors');

// const colors = ['red','yellow','green'];
// let selected = 0;

// function changeColor(){
//     if(selected === 2){
//         selected = 0;
//     }
//     else{
//         selected +=1;
//     }
//     luksofors.style.backgroundColor = colors[selected];
// }

function setState(selected){

    for(let i = 0;i<3;i++){
        console.log('a'+ (i+1), colorSet[selected][i]);
        const luks = document.getElementById('a'+(i+1))
        luks.style.backgroundColor = colorSet[selected][i]
    }
}
function changeColor(){
    if(selected === 3){
        selected = 0;
    }
    else{
        selected +=1;
    }
    setState(selected);
}

const colorSet = [['red','black','black'],['red','orange','black'],['black','black','green'],['black','orange','black']];
let selected = 0;
setState(selected);