const ul = document.querySelector('ul');
let new_li = document.createElement('li')
new_li.classList.add('item');
new_li.textContent = 'Nam';
ul.append(new_li);

const button_number = document.querySelectorAll('li');

function showDialog(){
    let dia = document.createElement('div');
    dia.className = 'dia';

    const con = document.querySelector('.container');
    con.append(dia);
}

button_number.forEach((item) => {
    item.addEventListener('click', ()=>{
        console.log(item.innerText + " is clicked");
        if(item.matches('li')){
            item.style.backgroundColor = 'lightgrey';
        }

    }, true)
});

setInterval(()=>{
    let but_5 = document.getElementsByClassName('item')[4];
    // console.log(but_5);
    let d = new Date();
    
    but_5.innerHTML = d.getHours() + ":" + d.getMinutes() + ":" + d.getSeconds();
}, 1000);



// console.log(button_number);
