function auth_code() {
    var code = document.getElementById("code").value;

    if(code != " " && code > 999) {
        window.location.assign("search.html");
        alert("successfully found!!!");
    }
        else {
        alert("請輸入正確格式");
        return;
    }
}

function auth_time() {
    var day = document.getElementById("time").value;

    if(day != " " && (day > 0 && day < 6) && Number.isInteger(parseInt(day)) == true) {
        window.location.assign("search.html");
        alert("successfully found!!!");
    }
    else if(parseInt(day) <= 0 || parseInt(day) >= 6) {
        alert("請輸入一到五!!!");
    }
}

function auth_name() {
    var coursename = document.getElementById("coursename").value;

    if(coursename != " " && coursename.charCodeAt() > 255)
    {
        window.location.assign("search.html");
        alert("successfully found!!!");
    }
    else {
        alert("請輸入中文!!!");
        return;
    }
}

function auth_teachername() {
    var instructorname = document.getElementById("instructorname").value;

    if(instructorname != " " && instructorname.charCodeAt() > 255) {
        window.location.assign("search.html");
        alert("successfully found!!!");
    }
    else {
        alert("請輸入中文!!!");
        return;
    }
}