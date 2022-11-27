const MIN_PAGE_NUMBER = 6;
const FIRST_PAGE = 1;
let curr_page = 1;
let number = document.getElementById('limit-number');
let topic = document.querySelector('#select-topic').value;
let list_images = [];

//loading image and display
async function loadingImage(topic) {
    let response = await fetch(`/get-image/${topic}`)
    // waiting response convert result to json
    let l = await response.json();
    return Promise.resolve(l);
}

async function displayImage(number = MIN_PAGE_NUMBER, curr = curr_page) {
    const row = document.getElementsByClassName('row')[0];
    let start = (curr - 1) * number;
    for (let i = start; i < start + number; i++) {
        if (list_images[i]) {
            let col = document.createElement('div');
            col.className = 'col';
            col.innerHTML = `
            <div class="card">
                <img src=${list_images[i]} width=400>
                <div class="card-body">
                <p class="card-text"></p>
                <div class="btn-group">
                    <button class="btn-a btn-accept" form="change" type="submit" name="button" value="${list_images[i]}">Public</button>
                    <button class="btn-a btn-deny" form="change" type="submit" name="button" value="${list_images[i]}">Deny</button>
                </div>
                </div>
            </div>`

            row.append(col);
        }
    }
    const accept_button = document.getElementsByClassName('btn-accept');
    for(let i = 0; i < accept_button.length; i++){
        accept_button[i].addEventListener('click', async ()=>{
            fetch(`/get-public-image?topic=${topic}&url=${accept_button[i].value}`);
            // remove image out of list
            list_images.splice(start + i, 1); 
            await renew_display_image(curr);
        });
    }
    return Math.ceil(list_images.length / number);
}

// remove all image when we reload page
async function removeAllImage() {
    const col = document.querySelectorAll('.col');
    col.forEach(ele => {
        ele.remove();
    });
}

async function renew_display_image(curr = curr_page) {
    // get numer page
    number = document.getElementById('limit-number');
    number = parseInt(number.value);
    // check is number or not
    number = (!Number(number)) ? MIN_PAGE_NUMBER : number;
    await removeAllImage();
    let list_len = await displayImage(number, curr);
    pagination(list_len, curr);
}

// show pagination
async function pagination(list_len, curr, index = 0) {
    // index = 0 : show pagination in top
    // index = 1 : show pagination in bottom
    const nav = document.getElementsByClassName('pagination')[index];
    const pc = document.getElementsByClassName('pagination-container')[index];
    // renew after change topic, new page
    if (pc !== undefined) {
        pc.remove();
    }
    const pagination_container = document.createElement('div');
    pagination_container.className = 'pagination-container';

    let btn_left = document.createElement('button');
    let numbers = document.createElement('div');
    let btn_right = document.createElement('button');

    btn_left.className = 'btn-left-page';
    btn_left.textContent = '<';

    btn_right.className = 'btn-right-page';
    btn_right.textContent = '>';

    numbers.className = 'page-numbers';

    let first_page = document.createElement('button');
    first_page.className = "btn-page";
    first_page.textContent = 1;

    let last_page = document.createElement('button');
    last_page.className = "btn-page";
    last_page.textContent = list_len;

    let previous_page = document.createElement('button');
    previous_page.className = "btn-page";
    previous_page.textContent = curr - 1;

    let current_page = document.createElement('button');
    current_page.className = "btn-page current-page";
    current_page.textContent = curr;

    let next_page = document.createElement('button');
    next_page.className = "btn-page";
    next_page.textContent = curr + 1;

    let space_page_1 = document.createElement('button');
    let space_page_2 = document.createElement('button');
    space_page_1.disabled = true;
    space_page_1.textContent = "...";
    space_page_2.disabled = true;
    space_page_2.textContent = "...";

    // check current diff with start and end page to add pre + next button and ...
    if (curr > 2) numbers.append(first_page);
    if (curr > 3) numbers.append(space_page_1);
    if (curr > 1) numbers.append(previous_page);
    numbers.append(current_page);
    if (curr < list_len) numbers.append(next_page);
    if (curr < list_len - 2) numbers.append(space_page_2);
    if (curr < list_len - 1) numbers.append(last_page);
    // add button event listener
    btn_left.addEventListener('click', async () => {
        if (curr > 1) {
            curr -= 1;
            await renew_display_image(curr);
        } else {
            console.log("can't go left");
        }
    });

    btn_right.addEventListener('click', async () => {
        if (curr < list_len) {
            curr += 1;
            await renew_display_image(curr);
        } else {
            console.log("can't go right");
        }
    });

    for (let i = 0; i < numbers.childElementCount; i++) {
        numbers.children[i].addEventListener('click', async () => {
            curr = parseInt(numbers.children[i].textContent);
            await renew_display_image(curr);
        }, true);
    }

    pagination_container.append(btn_left, numbers, btn_right);
    nav.append(pagination_container);
    // display pagination in bottom
    if(index == 0) pagination(list_len, curr, 1);
}

(async () => {
    // start rending 
    // waiting for loading image from server
    list_images = await loadingImage(topic);

    let list_len = await displayImage();
    pagination(list_len, curr_page);

    const button_select_topic = document.getElementsByClassName('btn-select-topic')[0];
    button_select_topic.addEventListener('click', async () => {
        topic = document.querySelector('#select-topic').value;
        list_images = await loadingImage(topic);
        // get numer page
        await renew_display_image();
    }, true);

    const button_select_number_page = document.getElementsByClassName('btn-select-number')[0];
    button_select_number_page.addEventListener('click', async () => {
        await renew_display_image();
    }, true);
})();
