
// change the h1 tag with id="title" to have the text "flowers"

// create a list of flowers

// write a function which adds a text to a ul element as an li element

// iterate through your flowers array and create an li for each flower

var flowers = ["daisy", "daffodil", "rose", "buttercup", "lavender", "orchid"];

document.getElementById("title").innerHTML = "Flowers";


function appender(li_text) {
    var ul = document.getElementById("list");
    var li = document.createElement("li");
    li.appendChild(document.createTextNode(li_text));
    ul.appendChild(li);
}

function start_appender(){
    flowers.forEach(function(flower) {
        appender(flower);
    });
}

