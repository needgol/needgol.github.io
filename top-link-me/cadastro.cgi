#!d:/home/perl/bin/perl.exe
##!/usr/bin/perl

################################################################################################

print"Content-type: text/html\n\n";
require"config.pl";

if(!$in{'action'}){
    &printpage;
}
if($in{'action'} eq 'cadastrar'){
  $nome=$in{'webmaster'};
  $email=$in{'email'};
  $site=$in{'website'};
  $url=$in{'url'};
  $descricao=$in{'descricao'};
  $categoria=$in{'categoria'};
  $regras=$in{'regras'};
  $senha=$in{'senha'};
  $conf=$in{'conf'};
  $todos=$nome.$email.$site.$url.$descricao.$categoria.$senha.$conf.$regras;

  $senha2=crypt($senha,HJ);

$e=0;


$u=$userdir.'last.last';
open(L,$u);
  @var=<L>;
close(L);

foreach $v(@var){
 $var=$var.$v;
}

if($var eq "$nome|&|$email|&|$site|&|$url|&|$descricao|&|$categoria|&|$senha2"){
  &html('<center><font face=\"$fonte\" size=\"$size\">Este cadastro já foi completado</font></center>');
}


opendir(L,$userdir)||do{&html('Erro ao abrir diretório de membros');};
  @files=readdir(L);
closedir(L);
  $z=0;
foreach $files(@files){
  ($f,$i)=split(/\./,$files);

  if($i eq $extcadastro){
     $loc=$userdir.$f.'.'.$i;
     open(L,$loc);
         @val[$z]=<L>;
     close(L);
     $z++;
  }
}
foreach $val(@val){
  @yw=split(/\|+&+\|/,$val);
  if ($url =~ /@yw[3]/i and @yw[3] =~ /$url/i){
    @erro[$e]="<center><font face=\"$fonte\" size=\"$size\">Este website já está cadastrado em nosso sistema</font></center>";
    $e++;
  }

}


if($in{'id'} =~ /[abcdefghijklmnopqrstuvxz]/){
  &html('Erro ao gerar id, contate o administrador');
  exit;
}
if($in{'id'} =~ /[!\@#\$%^&*();+=:\/]/){
  &html('Erro ao gerar id, contate o administrador');
  exit;
}
if($in{'id'} =~ /[\[\];:'"<>?,.|]/){
  &html('Erro ao gerar id, contate o administrador');
  exit;
}

if(!$nome or !$email or !$site or !$url or !$descricao or !$categoria){
   @erro[$e]="<center><font face=\"$fonte\" size=\"$size\">Preencha todos os campos</font></center>";
   $e++;
} 

if($todos =~ /\|&\|/){
   @erro[$e]="<center><font face=\"$fonte\" size=\"$size\"> Sequência de caracteres inválidos, |&|</font></center>";
   $e++;
}

if($nome =~ /[!@#\$%^&*();+=:\/]/){
   @erro[$e]="<center><font face=\"$fonte\" size=\"$size\">O nome contém caracteres inválidos</font></center>";
   $e++;
}
if($email !~ /@/){
   @erro[$e]="<center><font face=\"$fonte\" size=\"$size\">Email Inválido</font></center>";
   $e++;
}

if($url !~ "http://"){
   @erro[$e]="<center><font face=\"$fonte\" size=\"$size\">A url de seu site precisa começar com http://</font></center>";
   $e++;
}
if($url eq "http://"){
   @erro[$e]="<center><font face=\"$fonte\" size=\"$size\">A url está incompleta</font></center>";
   $e++;
}

if($regras ne "on" ){
   @erro[$e]="<center><font face=\"$fonte\" size=\"$size\">Marque a caixa que confima sua concordância com as regras</font></center>";
   $e++;
}
if($senha ne $conf){
   @erro[$e]="<center><font face=\"$fonte\" size=\"$size\">A senha e sua confirmação estão diferentes</font></center>";
   $e++;
}if(length($senha)<6){
   @erro[$e]="<center><font face=\"$fonte\" size=\"$size\">A senha deverá ter no mínimo 6 caracteres</font></center>";
   $e++;
}

if($e>0){
  $erro[$e]="<hr>";
  &printpage;
}else{
############################# Faz cadastro ##########################################

  $descricao =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
  $cry=crypt($senha,HJ);


$idfile=$userdir."ids.txt";

open(L,$idfile);
   flock(L,2);
   $id=<L>;
close(L);

$id++;

$tmp=$userdir.$id.'.'.$extcadastro;
$tmp2=$userdir.$id.'.'.$extvoto;
$tmp3=$userdir.'last.last';

open(L,">$tmp");
   print L"$nome|&|$email|&|$site|&|$url|&|$descricao|&|$categoria|&|$cry";
close(L);

open(L,">$tmp3");
   print L"$nome|&|$email|&|$site|&|$url|&|$descricao|&|$categoria|&|$cry";
close(L);

open(L,">$idfile");
   flock(L,2);
   print L"$id";
close(L);

open(L,">$tmp2");
   print L"0";
close(L);


@tpr = qq~
<table border="0" width="100%" height="139" cellspacing="0" cellpadding="0"><tr><td width="100%" height="10"><p align="center"><b><font size="2" face="Verdana">Cadastro Realizado com
Sucesso</font></b></td></tr><tr><td width="100%" height="9">
      <p align="center"><b><font size="2" face="Verdana">ID: $id</font></b></td></tr><tr><td width="100%" height="19"><p align="center"><font face="Verdana" size="1" color="#008000">Código HTML</font></td>
</tr><tr><td width="100%" height="58" style="font-family: $font; font-size: $size"><p align="center"><font face="Verdana" size="1"><textarea rows="7" name="htmlcode" cols="47" style="font-family: $fonte; font-size: 8 pt"><form method="post" action="$httptop/votar.cgi">
<input type="hidden" name="id" value="$id"><input type="image" src="$dirselos/$selodef" border=0>
</form></textarea></font></p></td></tr><tr><td width="100%" height="19"><p align="center"><font face="Verdana" size="1">Copie o código a seguir em
qualquer lugar em seu website</font><tr><td width="100%" height="19">
      <p align="center"><a href="top.cgi?action=selos"><font face="Verdana" size="1" color="#008000">**
      Para trocar o selo, entre em selos e siga as intruções</font></a>  </table>
~;
&html(@tpr);

}

} 



sub printpage{
   $n=0;
   foreach $erro(@erro){
     @printline[$n]=$erro;
     $n++;
   }
   &htmlcadastro;
   foreach $linhas(@linhas){
    if($linhas =~ "<categorias>"){
           ($g,$h)=split(/<+c+a+t+e+g+o+r+i+a+s+>/,$linhas);
           @printline[$n]=$g;

           open(L,$categorias)||do{&html('<center><font face=\"$fonte\" size=\"$size\">Erro ao abrir arquivo de categorias</font></center>'); exit;};
              @categorias=<L>;
           close(L);
           foreach $cat(@categorias){
              ($cat,$r) = split(/\n/,$cat); 
              if($in{'categoria'} eq $cat){
                  @printline[$n]=@printline[$n]."<option selected value=\"$cat\">$cat</option>\n";
              }else{
                  @printline[$n]=@printline[$n]."<option value=\"$cat\">$cat</option>\n";
              }
           }
           
           @printline[$n]=@printline[$n].$h; 
     }else{
        @printline[$n]=$linhas;
     }

    $n++;
   }
&html(@printline);
}


#&html('nada');


sub htmlcadastro{


if(!$url){
 $url="http://";
}

###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################
#### Código HTML do cadastro                                                               ####
#### Edite como quiser o código html abaixo, mas faça alteração no nome nem no conteúdo de ####
#### nenhum dos campos do formulário                                                       ####
###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################


@linhas = qq~

<p align="center"><b><font face="Verdana" size="2">Cadastre seu Website</font></b></p>
<form method="POST" action="cadastro.cgi">
<input type="hidden" name="action" value="cadastrar">
 
  <div align="center">
    <center>
  <table border="0" width="328" height="115" cellspacing="0" cellpadding="0">
    <tr>
      <td height="13" align="center" colspan="2" bgcolor="#FFFFFF">
        <font face="Verdana" size="1"><b>Seus Dados</b></font> </td>
    </tr>
    <tr>
      <td width="133" height="11" align="right" bgcolor="#FFFFFF">
        <p align="right"><font face="Verdana" size="1">Seu Nome:&nbsp;</font> </td>
      <td width="195" height="11" bgcolor="#FFFFFF">
      <input type="text" name="webmaster" size="30" style="font-family: verdana; font-size: 8 pt" 
      value="$nome"></td>
    
    </tr>
    <tr>
      <td width="133" height="5" align="right" bgcolor="#FFFFFF"><font face="Verdana" size="1">E-Mail:&nbsp;</font> </td>
      <td width="195" height="5" bgcolor="#FFFFFF"><font face="Verdana" size="1"><input type="text" name="email" size="30" style="font-family: verdana; font-size: 8 pt" value="$email"></font></td>
    </tr>
    <tr>
      <td width="300" height="5" align="right" bgcolor="#FFFFFF" colspan="2"><font face="Verdana" size="1">&nbsp;</font> </td>
    </tr>
    <tr>
      <td height="13" align="right" colspan="2" bordercolor="#E2E2E2" bgcolor="#FFFFFF">
        <p align="center"><font face="Verdana" size="1"><b>Dados do Website</b></font></td>
    </tr>
    <tr>
      <td width="133" height="19" align="right" bordercolor="#E2E2E2" bgcolor="#FFFFFF"><font face="Verdana" size="1">Nome do Site:&nbsp;</font> </td>
      <td width="195" height="19" bordercolor="#E2E2E2" bgcolor="#FFFFFF"><font face="Verdana" size="1"><input type="text" name="website" size="30" style="font-family: verdana; font-size: 8 pt" value="$site"></font></td>
    </tr>
    <tr>
      <td width="133" height="19" align="right" bordercolor="#E2E2E2" bgcolor="#FFFFFF"><font face="Verdana" size="1">URL:&nbsp;</font> </td>
      <td width="195" height="19" bordercolor="#E2E2E2" bgcolor="#FFFFFF"><font face="Verdana" size="1"><input type="text" name="url" size="30" style="font-family: verdana; font-size: 8 pt" value="$url"></font></td>
    </tr>
    <tr>
      <td width="133" height="19" align="right" bordercolor="#E2E2E2" bgcolor="#FFFFFF"><font face="Verdana" size="1">Descrição:&nbsp;</font> </td>
      <td width="195" height="19" bordercolor="#E2E2E2" bgcolor="#FFFFFF"><font face="Verdana" size="1"><textarea rows="7" name="descricao" cols="29" style="font-family: verdana; font-size: 8 pt">$descricao
</textarea></font></td>
    </tr>
    <tr>
      <td width="133" height="19" align="right" bordercolor="#E2E2E2" bgcolor="#FFFFFF"><font face="Verdana" size="1">Categorias:&nbsp;</font> </td>
      <td width="195" height="19" bordercolor="#E2E2E2" bgcolor="#FFFFFF"><font face="Verdana" size="1">
      
<select size="1" name="categoria" style="font-family: verdana; font-size: 8 pt">
<categorias>          
</select>
        
        </font></td>
    </tr>
    <tr>
      <td width="328" height="2" align="left" bordercolor="#E2E2E2" bgcolor="#FFFFFF" colspan="2"><font face="Verdana" size="1">&nbsp;</font> </td>
    </tr>
    <tr>
      <td width="328" height="2" align="left" bordercolor="#E2E2E2" bgcolor="#FFFFFF" colspan="2">
        <p align="center"><font face="Verdana" size="1"><b>Dados Administrativos</b></font> </td>
    </tr>
    <tr>
      <td width="133" height="5" align="left" bordercolor="#E2E2E2" bgcolor="#FFFFFF">
        <p align="right"><font face="Verdana" size="1">Senha:</font> </td>
      <td width="195" height="5" bordercolor="#E2E2E2" bgcolor="#FFFFFF"><font face="Verdana" size="1"><input type="password" name="senha" size="19" style="font-family: verdana; font-size: 8 pt"></font></td>
    </tr>
    </center>
    <tr>
      <td width="133" height="5" align="left" bordercolor="#E2E2E2" bgcolor="#FFFFFF">
        <p align="right"><font face="Verdana" size="1">Confirme sua senha:</font> </td>
    <center>
      <td width="195" height="5" bordercolor="#E2E2E2" bgcolor="#FFFFFF"><font face="Verdana" size="1"><input type="password" name="conf" size="19" style="font-family: verdana; font-size: 8 pt"></font></td>
    </tr>
    <tr>
      <td width="133" height="4" align="left" bordercolor="#E2E2E2" bgcolor="#FFFFFF">&nbsp; </td>
      <td width="195" height="4" bordercolor="#E2E2E2" bgcolor="#FFFFFF"><font face="Verdana" size="1"><input type="checkbox" name="regras" value="on" style="font-family: verdana; font-size: 10 px"><a href="$script?regras">Li
        e concordo com as regras</a></font></td>
    </tr>
    <tr>
      <td width="298" height="35" align="right" colspan="2" bordercolor="#E2E2E2" bgcolor="#FFFFFF">
        <p align="center"><input type="submit" value="Enviar" style="font-family: verdana; font-size: 8 pt">
        <input type="reset" value="Apagar Campos" style="font-family: verdana; font-size: 8 pt"> </td>
    </tr>
  </table>
    </center>
  </div>
</form>


~;
}