// const dropdowns= document.querySelectorAll'.dropdown');
//
// dropdowns.forEach(dropdown =>{
//
//     const select = dropdown.querySelector('.select');
//     const caret = dropdown.querySelector('.caret');
//     const menu = dropdown.querySelector('.menu');
//     const options = dropdown.querySelectorAll('.menu li');
//     const selected = dropdown.querySelector('.selected');
//
//
// select.addEventListener('click',() =>{
//     select.classList.toggle('select-clicked');
//
//     caret.classList.toggle('caret-rotate');
//
//     menu.classList.toggle('menu-open');
// });
//
// options.forEach(option =>{
//
//     option.addEventListener('click', ()=>{
//
//         selected.innerText = option.innerText;
//
//         select.classList.remove('select-clicked');
//
//         caret.classList.remove('click-rotate');
//
//         menu.classList.remove('menu-open');
//
//         options.forEach(option =>{
//             option.claalist.remove('active');
//         });
//         option.classList.add('active');
//         });
//     });
// });


function auth_code() {
    var code = document.getElementById("code").value;

    if(!(code != " " && code > 999)) {
        alert("請輸入正確格式");
        return;
    }
}

function auth_time() {
    var day = document.getElementById("time").value;

    if(day != " " && (day > 0 && day < 6) && Number.isInteger(parseInt(day)) == true) {
    }
    else if(parseInt(day) <= 0 || parseInt(day) >= 6) {
        alert("請輸入一到五!!!");
    }
}

function auth_name() {
    var coursename = document.getElementById("coursename").value;

    if(coursename != " " && coursename.charCodeAt() > 255) {
    }
    else {
        alert("請輸入中文!!!");
        return;
    }
}

function auth_teachername() {
    var instructorname = document.getElementById("instructorname").value;

    if(instructorname != " " && instructorname.charCodeAt() > 255) {
    }
    else {
        alert("請輸入中文!!!");
        return;
    }
}
