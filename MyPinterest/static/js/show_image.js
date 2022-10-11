function show_set_image(set_url) {
    let p = document.getElementsByClassName('row')[0];
    for (let i = 0; i < set_url.length; i++) {
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
        button_accept.className = 'btn-a btn-accept';
        button_accept.textContent = 'Accept';
        let button_deny = document.createElement('button');
        button_deny.className = 'btn-a btn-deny';
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

function show_single_image(url) {
    let p = document.getElementById('image');
    let a = document.createElement("img");
    a.src = url;
    a.alt = url;
    a.width = 300;
    p.appendChild(a);
}

function select_topic(list_topics) {
    let select = document.getElementById("select-topic");
    for (let i = 0; i < list_topics.length; i++) {
        let option = document.createElement('option');
        option.value = list_topics[i];
        option.textContent = list_topics[i];
        select.appendChild(option);
    }
}

function set_return_link(topic) {
    let ul = document.getElementById('actives');
    let activities = ['home', 'image', 'list', 'random-list', 'public'];
    for (let i = 0; i < activities.length; i++) {
        let li = document.createElement('li');
        li.className = 'link-return';
        let a = document.createElement('a');
        a.className = 'nav-link px-2 link-secondary';
        a.href = (activities[i] == 'home' || activities[i] == 'public') ? "/" + activities[i] : '/' + activities[i] + '/' + topic;
        a.textContent = activities[i];
        li.appendChild(a);
        ul.appendChild(li);
    }
}

function _basic(list_topics, topic) {
    select_topic(list_topics);
    set_return_link(topic);
}

function _image(url, list_topics, topic) {
    _basic(list_topics, topic);
    show_single_image(url);
}

function _set_image(set_url, list_topics, topic) {
    _basic(list_topics, topic);
    show_set_image(set_url);
}

function _list_image(list_url, list_topics, topic, index_start, number_limit) {
    //initialize static web
    _basic(list_topics, topic);  
}

