######################### Configura��es Principais
$userdir="/path/para/users/";      
## Diret�rio onde ser�o gravadas as informa��es de cadastro e log
## Utilizar path, com / no final

$pagedir="/path/para/pages/";                    
## Diet�rio onde ficar�o as p�ginas HTML
## Utilizar path, com / no final

$layout="/path/para/pages/layout.htm";           
## Layout do topsites, utillize o readme para maiores informa��es
## Utilizar path

$categorias="/path/para/pages/categorias.txt";   ## categorias do topsites
## Arquivo de categorias
## Utilizar path

$script="http://www.seusite.com/cgi-bin/top.cgi";
## URL para o arquivo principal do top site
## URL Completa 

$httptop="http://www.seusite.com/cgi-bin/top";    
## URL para o diret�rio onde ficar� o topsites
## N�o utilize barra, utilize url completa 

######################### Administra��o
$admpassword="senha123";
## Senha Administrativa

$admfile="admfile.inf";
## Arquivo usado para login, aten��o, esse arquivo nao acompanha o topsites, 
## sendo riado quando voc� acessar a administra��o 
## utilizar path
##### entre na administra��op pelo admin.cgi

######################### Selos
$dirselos="http://www.seusite.com/cgi-bin/selos";
## Endere�o http para o diret�rio onde ficar�o os selos
## N�o utilizar barra no final
$selodef="selo.gif";  
## Selo principal do topsites
## deve ficar no diret�rio de selos, n�o se deve usar url completa para o mesmo     

####################### Extens�es referentes aos arquivos de cadastro, n�o e necess�rio alterar
$extcadastro="cad";
$extlog="log";
$extvoto="votos";
$extprot="extprot";

####################### Configura��o da fonte default
$fonte="verdana, arial";
$size="1";

####################### Configura��es de Email
$mail_prog="/usr/sbin/sendmail";
## Programa de email

$mailadmin="seu\@email.com";
# Email administrativo, utilizar sempre um \ antes do @

########################### Configura��o dos rankings
### C�lula 1 - T�tulo
$pfonte="Verdana, arial";    ## fonte da celula referente ao t�tulo
$ptamanho=1;                 ##tamanho da fonte referente ao t�tulo
$pfontecolor="#FFFFFF";      ## cor referente a fonte do t�tulo
$pfcolor="#000080";          ## cor de fundo referente a c�lula do t�tulo

### C�lula 2 - Dados
$bfonte="Verdana, arial";    ## fonte da celula referente a c�lula de dados tipo1
$btamanho=1;                 ## tamanho da fonte referente a c�lula tipo 1
$bfontecolor="#FFFFFF";      ## cor referente a fonte referente a c�lula tipo 1
$bfcolor="#0000FF";           ## cor de fundo referente a c�lula tipo1

### C�lula 3 - Dados
$cfonte="Verdana, arial";    ## fonte da celula referente a c�lula de dados tipo1
$ctamanho=1;                 ## tamanho da fonte referente a c�lula tipo 1
$cfontecolor="#FFFFFF";      ## cor referente a fonte referente a c�lula tipo 1
$cfcolor="#9B9BFF";           ## cor de fundo referente a c�lula tipo1

#################################################################################################
##################################### N�o mexa depois daqui #####################################
#################################################################################################


################### Imprime P�gina
sub html{
    local(@printpage) = @_;
    open(LOC,$layout);
        @linhas=<LOC>;
    close(LOC);

    foreach $linha(@linhas){
         if($linha =~ "<topsites>"){
               ($rt,$rz)=split(/<+t+o+p+s+i+t+e+s+>/,$linha);
                print $rt;
                print @printpage;
                print $rz;
         }elsif($linha =~ "<categorias>"){
               ($rt,$rz)=split(/<+c+a+t+e+g+o+r+i+a+s+>/,$linha);
                print $rt;
                open(L,$categorias);
                   @catv=<L>;
                close(L);
                foreach $catv(@catv){
                    $catv =~ s/\n//;
                    print"<option value=\"$catv\">$catv</option>";
                }
                print $rz;
         }else{
                print"$linha";
         }
    }

}

################### Formul�rio

   read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
   if (length($buffer) < 5) {
         $buffer = $ENV{QUERY_STRING};
    }
 
  @pairs = split(/&/, $buffer);
   foreach $pair (@pairs) {
      ($name, $value) = split(/=/, $pair);

      $value =~ tr/+/ /;
      $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

      $FORM{$name} = $value;
      $form{$name} = $value;
      $in{$name} = $value;
   }

1;