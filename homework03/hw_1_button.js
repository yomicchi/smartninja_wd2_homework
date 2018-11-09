var button = document.getElementById("btn");
var is_red = false;


function changeColor(){
    //ternary operator
    btn.style.color = is_red ? "red" : "green";
    //btn.style.BackgroundColor = is_red ? "red" : "green";
    is_red = !is_red;
}

