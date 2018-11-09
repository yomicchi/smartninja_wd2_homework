// define an array with at least 3 fruits, with their names and their sweetness (1 to 10)

// write a function which can append a row to the fruits table, with a fruit as input

// iterate over all fruits and insert them as rows in the table
var fruit = {name:"orange", sweetness: 2};
document.getElementById("fruit").innerHTML = "Fruits";


var fruits = [
    {name:"orange", sweetness: 2},
    {name:"banana", sweetness: 8},
    {name:"kiwi", sweetness: 4},
    {name:"apple", sweetness: 6}
];


function fruit_to_table_appender(fruit_object) {
    var table_body_element = document.getElementById("fruits_table_body");
    var new_table_row = table_body_element.insertRow(0);

    // Insert new cells (<td> elements) at the 1st and 2nd position of the "new" <tr> element:
    var name_cell = new_table_row.insertCell(0);
    var km_cell = new_table_row.insertCell(1);
    var sweetness_cell = new_table_row.insertCell(2);

    name_cell.innerHTML = fruit_object.name;
    sweetness_cell.innerHTML = fruit_object.sweetness;
}

fruits.forEach(function(fruit) {
    fruit_to_table_appender(fruit)
});
