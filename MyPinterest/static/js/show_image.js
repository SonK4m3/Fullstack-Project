function show_set_image(set_url){
    let p= document.getElementById('image');
    for(let i = 0; i < set_url.length; i++){
        let img = document.createElement('img');
        img.src = set_url[i];
        img.width = 200;
        p.appendChild(img);
    }
}
function show_image(url){
    let p = document.getElementById('image');
    let a = document.createElement("img");
    a.src = url;
    a.alt = url;
    a.width = 300;
    p.appendChild(a);
}