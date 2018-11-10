function change_coin(){

    var coin_exchange_rate = document.getElementById('selected_coin_exchange_rate');
    var selector = document.getElementById('coin_selector');
    var selected_value = selector.options[selector.selectedIndex].value;

    console.log(selector);
    console.log(selected_value);
    var url = 'https://min-api.cryptocompare.com/data/price?fsym='+selected_value+'&tsyms=EUR';
    console.log(url);

    fetch(url)
        .then((resp) => resp.json())
            .then(function(response){
                coin_exchange_rate.innerHTML = +response["EUR"];
    });
}
