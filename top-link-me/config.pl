######################### Configurações Principais
$userdir="/path/para/users/";      
## Diretório onde serão gravadas as informações de cadastro e log
## Utilizar path, com / no final

$pagedir="/path/para/pages/";                    
## Dietório onde ficarão as páginas HTML
## Utilizar path, com / no final

$layout="/path/para/pages/layout.htm";           
## Layout do topsites, utillize o readme para maiores informações
## Utilizar path

$categorias="/path/para/pages/categorias.txt";   ## categorias do topsites
## Arquivo de categorias
## Utilizar path

$script="http://www.seusite.com/cgi-bin/top.cgi";
## URL para o arquivo principal do top site
## URL Completa 

$httptop="http://www.seusite.com/cgi-bin/top";    
## URL para o diretório onde ficará o topsites
## Não utilize barra, utilize url completa 

######################### Administração
$admpassword="senha123";
## Senha Administrativa

$admfile="admfile.inf";
## Arquivo usado para login, atenção, esse arquivo nao acompanha o topsites, 
## sendo riado quando você acessar a administração 
## utilizar path
##### entre na administraçãop pelo admin.cgi

######################### Selos
$dirselos="http://www.seusite.com/cgi-bin/selos";
## Endereço http para o diretório onde ficarão os selos
## Não utilizar barra no final
$selodef="selo.gif";  
## Selo principal do topsites
## deve ficar no diretório de selos, não se deve usar url completa para o mesmo     

####################### Extensões referentes aos arquivos de cadastro, não e necessário alterar
$extcadastro="cad";
$extlog="log";
$extvoto="votos";
$extprot="extprot";

####################### Configuração da fonte default
$fonte="verdana, arial";
$size="1";

####################### Configurações de Email
$mail_prog="/usr/sbin/sendmail";
## Programa de email

$mailadmin="seu\@email.com";
# Email administrativo, utilizar sempre um \ antes do @

########################### Configuração dos rankings
### Célula 1 - Título
$pfonte="Verdana, arial";    ## fonte da celula referente ao título
$ptamanho=1;                 ##tamanho da fonte referente ao título
$pfontecolor="#FFFFFF";      ## cor referente a fonte do título
$pfcolor="#000080";          ## cor de fundo referente a célula do título

### Célula 2 - Dados
$bfonte="Verdana, arial";    ## fonte da celula referente a célula de dados tipo1
$btamanho=1;                 ## tamanho da fonte referente a célula tipo 1
$bfontecolor="#FFFFFF";      ## cor referente a fonte referente a célula tipo 1
$bfcolor="#0000FF";           ## cor de fundo referente a célula tipo1

### Célula 3 - Dados
$cfonte="Verdana, arial";    ## fonte da celula referente a célula de dados tipo1
$ctamanho=1;                 ## tamanho da fonte referente a célula tipo 1
$cfontecolor="#FFFFFF";      ## cor referente a fonte referente a célula tipo 1
$cfcolor="#9B9BFF";           ## cor de fundo referente a célula tipo1

#################################################################################################
##################################### Não mexa depois daqui #####################################
#################################################################################################


################### Imprime Página
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

################### Formulário

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