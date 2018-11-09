function change_location(){

    var location = document.getElementById('selected_location');
    var wind = document.getElementById('selected_location_wind');
    var description = document.getElementById('selected_location_desc');
    var selector = document.getElementById('location_selector');
    var selected_value = selector.options[selector.selectedIndex].value;

    console.log(selector);
    console.log(selected_value);
    var app_id = "ba746c3ff8be7c058e4b75b26e1273bf";
    var url = 'http://api.openweathermap.org/data/2.5/weather?q='+selected_value+'&units=metric&appid='+app_id;
    console.log(url);

    fetch(url)
        .then((resp) => resp.json())
            .then(function(response){
                location.innerHTML = response.main.temp;
                description.innerHTML = response.weather[0].description;
                wind.innerHTML = response.wind.speed
    });
}