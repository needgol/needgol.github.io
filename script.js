$.ajax({
  url: 'https://v2.sparktraffic.com/balance',
  crossDomain: true,
  headers: {
    'accept': 'application/json',
    'api_key': 'f3eff12541ace4adf69b47b58b03a6a1'
  }
}).done(function(response) {
  console.log(response);
});
