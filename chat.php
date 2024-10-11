<?php
// Faz alguma coisa (requisições com cURL por exemplo) para conseguir o JSON que deve aparecer no HTML
$resultado = array(); // coloquei um array vazio, mas vamos pensar que ele contêm os dados que devem ser direcionados para o HTML
header('Content-Type: application/json');
echo json_encode($resultado);
$(function(){
  $.ajax({
    url: 'https://https://needgol.github.io/chat.php',
    dataType: 'json',
    success: function(data) {
curl -X GET "https://v2.sparktraffic.com/balance" \
 -H 'accept: application/json'\
 -H 'api_key: f3eff12541ace4adf69b47b58b03a6a1'
      $('#resultado').html(data.test);
    }, error: function(err) {
      $('#resultado').html('Deu erro, porque não temos o backend neste exemplo');
    }
  });
});
