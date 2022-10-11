function createPagination(list_url, index_start, page, _number_limit) {
    let element = document.querySelector(".page-controller");
    let totalPages = Math.ceil(list_url.length/_number_limit);
    alert(index_start + " " + page + " " + _number_limit);
    let liTag = '';
    let active;
    let beforePage = page - 1;
    let afterPage = page + 1;
    if (page > 1) { //show the next button if the page value is greater than 1
        liTag += `<li class="btn-page prev" onclick="createPagination(${list_url}, ${index_start}, ${page - 1}, ${_number_limit})"><span><i class="fas fa-angle-left"></i> Prev</span></li>`;
    }
    if (page > 2) { //if page value is less than 2 then add 1 after the previous button
        liTag += `<li class="first numb" onclick="createPagination(${list_url}, ${index_start}, 1, ${_number_limit})"><span>1</span></li>`;
        if (page > 3) { //if page value is greater than 3 then add this (...) after the first li or page
            liTag += `<li class="dots"><span>...</span></li>`;
        }
    }
    // how many pages or li show before the current li
    if (page == totalPages) {
        beforePage = beforePage - 2;
    } else if (page == totalPages - 1) {
        beforePage = beforePage - 1;
    }
    // how many pages or li show after the current li
    if (page == 1) {
        afterPage = afterPage + 2;
    } else if (page == 2) {
        afterPage = afterPage + 1;
    }
    for (var plength = beforePage; plength <= afterPage; plength++) {
        if (plength > totalPages) { //if plength is greater than totalPage length then continue
            continue;
        }
        if (plength == 0) { //if plength is 0 than add +1 in plength value
            plength = plength + 1;
        }
        if (page == plength) { //if page is equal to plength than assign active string in the active variable
            active = "active";
        } else { //else leave empty to the active variable
            active = "";
        }
        liTag += `<li class="numb ${active}" onclick="createPagination(${list_url}, ${index_start}, ${plength}, ${_number_limit})"><span>${plength}</span></li>`;
    }
    if (page < totalPages - 1) { //if page value is less than totalPage value by -1 then show the last li or page
        if (page < totalPages - 2) { //if page value is less than totalPage value by -2 then add this (...) before the last li or page
            liTag += `<li class="dots"><span>...</span></li>`;
        }
        liTag += `<li class="last numb" onclick="createPagination(${list_url}, ${index_start}, ${totalPages}, ${_number_limit})"><span>${totalPages}</span></li>`;
    }
    if (page < totalPages) { //show the next button if the page value is less than totalPage(20)
        liTag += `<li class="btn-page next" onclick="createPagination(${list_url}, ${index_start + _number_limit}, ${page + 1}, ${_number_limit})"><span>Next <i class="fas fa-angle-right"></i></span></li>`;  
    }
    element.innerHTML = liTag; //add li tag inside ul tag
    // for (let i = 0; i < _number_limit; i++) {
    //     let p = document.getElementsByClassName('col')[0];
    //     p.remove();
    // }
    show_list_image(list_url, index_start, _number_limit);
}