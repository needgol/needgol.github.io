                                Iron Scripts Top Sites - Versão 1.0

Todos os direitos reservados a Iron Scripts, www.zmasters.com.br/ironscripts
Para obter qualquer tipo de ajuda sobre esse script, vá em www.zmasters.com.br/ironscripts/forum

Siga abaixo as principais dicas para instalação do topsites:

1 - Construa seu próprio layout
         Qualquer pessoa sem nenhum conhecimento em cgi, poderá altera o layout. Para isso, basta
    incluir uma tag chamada <topsites> no código html do layout (layout.htm), no lugar em que 
    você deseja que apareça o conteúdo do topsites. Veja um exemplo abaixo:

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

    o conteúdo da célula aparecerá no lugar onde foi colocado o topsites. Para as categorias, o processo e bem
    semelhante, mas usando a tag <categorias>, porém essa tag deerá vir dentro da caixa de diálogos do tipo 
    SELECT, veja um exemplo:

              <select size="1" name="categoria">
                <option>Geral</option>
<categorias>
              </select> 

    Recomendamos manter as mesmas linhas do exemplo, antes e depois da tag <categorias>, 
OBS: Repare que tanto a tag <categorias> e <topsites>, estão em uma linha destinadas a ela, e no inicio,
     essa atitude, pode evitar alguns erros futuros.

2 - Editando as categorias:
         Por default, o arquivo de categorias está na pasta pages/categorias.txt, caso você
    troque o nome no config.pl, você deverá renomear esse arquivo. Para adicionar ou remover 
    categoria, basta editar este arquivo, mantendo uma categoria por linha, e sem espaços no 
    início e no fim do nome.

3 - Editando páginas de selos, premios, regras e vencedores:
         Basta editar os arquivos HTML no diretorio pages, ou no que você escolheu para esta
    categoria no config.pl. Estes arquivos serão adicionados automaticamente no topsites


Qualquer dúvida, use nosso forum, www.zmasters.com.br/ironscripts/forum

Iron Scripts Top Sites - Versão 1.0 - www.zmasters.com.br/ironscripts
Uma parceria entre Allmasters e Zmaters