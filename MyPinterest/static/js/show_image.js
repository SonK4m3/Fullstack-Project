function detail_image_and_button(){
    let div = document.createElement('div');
    div.className = 'card-body';
    let detail = document.createElement('p');
    detail.className = 'card-text';
    detail.innerHTML = 'This is card';
    let options = document.createElement('div');
    options.className = 'btn-group';
    let button_accept = document.createElement('button').className = 'btn-accept';
    button_accept.textContent = 'Accept';
    let button_deny = document.createElement('button').className = 'btn-deny';
    button_deny.textContent = 'Deny';
    options.appendChild([button_accept, button_deny]);
    div.appendChild([detail, options]);

    return div;
}

function show_set_image(set_url){
    let p= document.getElementsByClassName('row')[0];
    for(let i = 0; i < set_url.length; i++){
        // card image
        let col = document.createElement('div');
        col.className = 'col';
        let card = document.createElement('div');
        card.className = 'card';
        let img = document.createElement('img');
        img.src = set_url[i];
        img.width = 400;
        //card detail
        let div = document.createElement('div');
        div.className = 'card-body';
        let detail = document.createElement('p');
        detail.className = 'card-text';
        let options = document.createElement('div');
        options.className = 'btn-group';
        let button_accept = document.createElement('button');
        button_accept.className = 'btn btn-accept';
        button_accept.textContent = 'Accept';
        let button_deny = document.createElement('button');
        button_deny.className = 'btn btn-deny';
        button_deny.textContent = 'Deny';
        options.appendChild(button_accept);
        options.appendChild(button_deny);
        div.appendChild(detail);
        div.appendChild(options);

        card.appendChild(img);
        card.appendChild(div);
        col.appendChild(card);
        p.appendChild(col);
    }
}

function show_single_image(url){
    let p = document.getElementById('image');
    let a = document.createElement("img");
    a.src = url;
    a.alt = url;
    a.width = 300;
    p.appendChild(a);
}

function select_topic(list_topics){
    let select = document.getElementById("select-topic");
    for(let i = 0; i < list_topics.length; i++){
        let option = document.createElement('option');
        option.value = list_topics[i];
        option.textContent = list_topics[i];
        select.appendChild(option);
    } 
}

function set_return_link(topic){
    let ul = document.getElementById('actives');
    let activities = ['home', 'image', 'list', 'random-list', 'public'];
    for(let i = 0; i < activities.length; i++){
        let li = document.createElement('li');
        let a = document.createElement('a');
        a.className = 'nav-link px-2 link-secondary';
        a.href = (activities[i] == 'home' || activities[i] == 'public') ? "/" + activities[i] : '/' + activities[i] + '/' + topic;
        a.textContent = activities[i];
        li.appendChild(a);
        ul.appendChild(li);
    }
}

function show_list_image(list_url, index_start, number_limit){
    let p= document.getElementsByClassName('row')[0];
    for(let i = index_start; i < index_start + number_limit; i++){
        let col = document.createElement('div');
        col.className = 'col';
        let card = document.createElement('div');
        card.className = 'card';
        let img = document.createElement('img');
        img.src = list_url[i];
        img.width = 400;
        //card detail
        let div = document.createElement('div');
        div.className = 'card-body';
        let detail = document.createElement('p');
        detail.className = 'card-text';
        let options = document.createElement('div');
        options.className = 'btn-group';
        let button_accept = document.createElement('button');
        button_accept.className = 'btn btn-accept';
        button_accept.textContent = 'Accept';
        let button_deny = document.createElement('button');
        button_deny.className = 'btn btn-deny';
        button_deny.textContent = 'Deny';
        options.appendChild(button_accept);
        options.appendChild(button_deny);
        div.appendChild(detail);
        div.appendChild(options);

        card.appendChild(img);
        card.appendChild(div);
        col.appendChild(card);
        p.appendChild(col);
    }
}

function page_controller(list_length, start, number){

    let x = document.getElementsByClassName('btn-page-controller');

    let page_controller = document.getElementsByClassName('page-controller')[0];
    //left button
    let button_left = document.createElement('button');
    button_left.className = 'btn-page-controller btn-left';
    button_left.textContent = 'left';
    //right button
    let button_right = document.createElement('button');
    button_right.className = 'btn-page-controller btn-right';
    button_right.textContent = 'right';

    let button_start = document.createElement('button');
    button_start.className = 'btn-page-controller btn-st';
    button_start.textContent = start + 1;

    let button_end = document.createElement('button');
    button_end.className = 'btn-page-controller btn-end';
    button_end.textContent = Math.ceil(list_length/number);

    page_controller.appendChild(button_left);

    page_controller.appendChild(button_start);
    page_controller.appendChild(button_end);

    page_controller.appendChild(button_right);
}

function _basic(list_topics, topic){
    select_topic(list_topics);
    set_return_link(topic);
}

function _image(url, list_topics, topic){
    _basic(list_topics, topic);
    show_single_image(url);
}

function _set_image(set_url, list_topics, topic){
    _basic(list_topics, topic);
    show_set_image(set_url);
}

function _list_image(list_url, list_topics, topic){
    let index_start = 0;
    let _number_limit = 6;

    _basic(list_topics, topic);
    page_controller(list_url.length, index_start, _number_limit);
    show_list_image(list_url, index_start, _number_limit);

    const btn_another_list = document.getElementById('btn-another-list');
    btn_another_list.addEventListener('click', ()=>{
        for(let i = 0; i < _number_limit; i++){
            let p = document.getElementsByClassName('col')[0];
            p.remove();
        }
        _number_limit = parseInt(document.querySelector('#limit-number').value);
        page_controller(list_url.length, index_start, _number_limit);
        show_list_image(list_url, index_start, _number_limit);
    }, true);

    const btn_right = document.getElementsByClassName('btn-right')[0];
    btn_right.addEventListener('click', ()=>{
        if(index_start + _number_limit <= list_url.length){
            index_start += _number_limit;
            for(let i = 0; i < _number_limit; i++){
                let p = document.getElementsByClassName('col')[0];
                p.remove();
            }
            page_controller(list_url.length, index_start, _number_limit);
            show_list_image(list_url, index_start, _number_limit);
        }
    }, true);

    const btn_left = document.getElementsByClassName('btn-left')[0];
    btn_left.addEventListener('click', ()=>{
        if(index_start - _number_limit >= 0){
            index_start -= _number_limit;
            for(let i = 0; i < _number_limit; i++){
                let p = document.getElementsByClassName('col')[0];
                p.remove();
            }
            page_controller(list_url.length, index_start, _number_limit);
            show_list_image(list_url, index_start, _number_limit);
        }
    }, true);

}

