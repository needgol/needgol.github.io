                                Iron Scripts Top Sites - Vers�o 1.0

Todos os direitos reservados a Iron Scripts, www.zmasters.com.br/ironscripts
Para obter qualquer tipo de ajuda sobre esse script, v� em www.zmasters.com.br/ironscripts/forum

Siga abaixo as principais dicas para instala��o do topsites:

1 - Construa seu pr�prio layout
         Qualquer pessoa sem nenhum conhecimento em cgi, poder� altera o layout. Para isso, basta
    incluir uma tag chamada <topsites> no c�digo html do layout (layout.htm), no lugar em que 
    voc� deseja que apare�a o conte�do do topsites. Veja um exemplo abaixo:

<table border="1" width="100%">
  <tr>
    <td width="100%"></td>
  </tr>
  <tr>
    <td width="100%">

<topsites>    

    </td>
  </tr>
</table>

    o conte�do da c�lula aparecer� no lugar onde foi colocado o topsites. Para as categorias, o processo e bem
    semelhante, mas usando a tag <categorias>, por�m essa tag deer� vir dentro da caixa de di�logos do tipo 
    SELECT, veja um exemplo:

              <select size="1" name="categoria">
                <option>Geral</option>
<categorias>
              </select> 

    Recomendamos manter as mesmas linhas do exemplo, antes e depois da tag <categorias>, 
OBS: Repare que tanto a tag <categorias> e <topsites>, est�o em uma linha destinadas a ela, e no inicio,
     essa atitude, pode evitar alguns erros futuros.

2 - Editando as categorias:
         Por default, o arquivo de categorias est� na pasta pages/categorias.txt, caso voc�
    troque o nome no config.pl, voc� dever� renomear esse arquivo. Para adicionar ou remover 
    categoria, basta editar este arquivo, mantendo uma categoria por linha, e sem espa�os no 
    in�cio e no fim do nome.

3 - Editando p�ginas de selos, premios, regras e vencedores:
         Basta editar os arquivos HTML no diretorio pages, ou no que voc� escolheu para esta
    categoria no config.pl. Estes arquivos ser�o adicionados automaticamente no topsites


Qualquer d�vida, use nosso forum, www.zmasters.com.br/ironscripts/forum

Iron Scripts Top Sites - Vers�o 1.0 - www.zmasters.com.br/ironscripts
Uma parceria entre Allmasters e Zmaters