#!d:/home/perl/bin/perl.exe
##!/usr/bin/perl

################################################################################################

print"Content-type: text/html\n\n";
require"config.pl";

  ($sec,$min,$hour,$day,$mon,$year,$wday) = (localtime(time))[0,1,2,3,4,5,6];

$senha=$admpassword;
$verifica=crypt($senha.$ENV{REMOTE_ADDR}.$day,BC);

open(L,$admfile);
   $ct=<L>;
close(L);

if($in{'action'} eq "entrar"){

    $hg=crypt($in{'senha'}.$ENV{REMOTE_ADDR}.$day,BC);
    $hj=crypt($admpassword.$ENV{REMOTE_ADDR}.$day,BC);

    if($hg ne $hj ){
          print"<font face=\"Verdana\" size=\"2\">Senha Inválida</font><hr>";
          &senha;
          exit;
    }

    open(L,">$admfile");
       print L"$hg";
    close(L);   
    &frames;
    exit;
}

if($ct ne $verifica){
  &senha;
  exit;
}

###############################################################################################
###############################################################################################
###############################################################################################
################################## Define Ações ###############################################
###############################################################################################
###############################################################################################
###############################################################################################
if($ct ne $verifica){
    &senha;
    exit;
}elsif($in{'action'} eq 'menu'){
   &menu;
}elsif($in{'action'} eq 'page'){
   &page;
}elsif($in{'action'} eq 'logout'){
   &logout;
}elsif($in{'action'} eq 'maillist'){
   &maillist;
}elsif($in{'action'} eq 'buscamembros'){
   &buscamembros;
}elsif($in{'action'} eq 'verdados'){
   &verdados;
}elsif($in{'action'} eq 'altdados'){
   &altdados;
}elsif($in{'action'} eq 'exwebsite'){
   &exwebsite;
}elsif($in{'action'} eq 'log'){
   &log;
}elsif($in{'action'} eq 'verlog'){
   &verlog;
}elsif($in{'action'} eq 'final'){
   &final;
}elsif($in{'action'} eq 'finalizar'){
   &finalizar;
}

&frames;

sub logout{
  unlink($admfile);
  &senha;
  exit;
}

sub frames{
print<<"HTML";
<frameset cols="25%,*">
  <frame name="esquerdo" src="admin.cgi?action=menu">
  <frame name="direito" src="admin.cgi?action=page">
</frameset>
HTML
exit;
}

sub menu{
print<<"HTML";
<body bgcolor="#E9E9E9"><table border="0" width="100%" height="219" cellspacing="0" cellpadding="0"><tr><td width="100%" align="center" height="40"><b><font face="Verdana" size="1">Irons Script - Top Sites</font></b></td></tr><tr><td width="100%" align="center" height="19"><font face="verdana, arial" size="1"><b>Busca Membros</b></font></td></tr><tr><td width="100%" height="19"><form method="POST" action="admin.cgi" target="direito"><input type="hidden" name="action" value="buscamembros">   
        <p align="center"><input type="text" name="pal" size="17" style="font-family: verdana; font-size: 8 pt"><input type="submit" value="Ir" style="font-family: verdana; font-size: 8 pt"></p></form></td></tr><tr><td width="100%" height="19"> <p align="center">
<center><b><font face="verdana, arial" size="1">Exibir dados por ID</font></b></center></td></tr><tr><td width="100%" height="19">

<form method="POST" action="admin.cgi" target="direito"><p align="center">
<input type="hidden" name="action" value="verdados">
 <select size="1" name="id" style="font-family: verdana; font-size: 8 pt">
HTML

open(L,$userdir."ids.txt");
  $qtda=<L>;
close(L);
$n=1;

while($n<$qtda+1){
   print"<option value=\"$n\">$n</option>";
   $n++;
}

print<<"HTML";
</select>
<input type="submit" value="Ir" style="font-family: verdana, arial; font-size: 8 pt"></p></form>
  <tr><td width="100%" height="23"><p align="center"><b><a href="admin.cgi?action=log" target="direito"><font face="verdana, arial" size="1" color="#000080">Logs</font></a></b></td></tr><tr><td width="100%" height="23"><p align="center"><b><a href="admin.cgi?action=maillist" target="direito"><font face="verdana, arial" size="1" color="#000080">Maillist</font></a></b></td></tr><tr><td width="100%" height="23">
      <p align="center"><b><a href="admin.cgi?action=final" target="direito"><font face="verdana, arial" size="1" color="#000080">Finalizar  Concurso</font></a></b></td></tr><tr><td width="100%" height="24"><p align="center"><b><a href="admin.cgi?action=logout" target="_top"><font face="verdana, arial" size="1" color="#000080">Sair</font></a></b></td></tr><tr><td width="100%" height="24"></td></tr>
  <td height="15"><p align="center"><font size="1" face="verdana, arial">OBS: <b>NUNCA</b> saia da administração sem antes clicar em <a href="admin.cgi?action=logout" target="_top"><b>sair</b></a> na barra acima</font></p>
HTML
exit;
}

sub page{
print<<"HTML";
<p align="center">&nbsp;</p><p align="center"><font face="verdana, arial" size="3"><b>Iron Scripts Top Sites - Versão 1.0</b></font></p>
<p align="center"><font face="Verdana" color="#000080" size="2"><a href="http://www.zmasters.com.br/ironscripts" target="_blank">Website</a></font></p><p align="center"><font face="verdana, arial" size="2"><a href="http://www.allmasters.com.br/forum/ikonboard.cgi" target="_blank">Fórum</a></font></p><p align="center">&nbsp;</p>
HTML
exit;
}

sub senha{
print<<"HTML";
<form method="POST" action="admin.cgi">
<p align="center"><font face="verdana, arial" size="4"><a href="http://www.zmasters.com.br/ironscripts" target="_blank"><font color="#000000">Iron Scripts - Topsites</font></a></font></p>
<input type="hidden" name="action" value="entrar">
  <table border="0" width="100%" height="81" cellspacing="0" cellpadding="0">
    <tr>
      <td width="100%" height="16">
        <p align="center"><b><font face="verdana, arial" size="2">Administração</font></b></td>
    </tr>
    <tr>
      <td width="100%" align="center" height="22"></td>
    </tr>
    <tr>
      <td width="100%" align="center" height="25"></td>
    </tr>
    <tr>
      <td width="100%" align="center" height="25"><font face="verdana, arial" size="2">Senha:
        </font><font face="verdana, arial"><input type="password" name="senha" size="20" style="font-family: verdana, arial; font-size: 8 pt">
        <input type="submit" value="Entrar" style="font-family: verdana, arial; font-size: 8 pt"></font></td>
    </tr>
  </table>
</form>
HTML
}
###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################
######################## Fim da parte de login e inicio da administração ######################
###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################
########## Maillist #######
###########################
sub maillist{
   opendir(L,$userdir)||do{print"Erro ao abrir diretório de membros";exit;};
      @files=readdir(L);
   closedir(L);
$s=0;
   foreach $files(@files){
      ($a,$b)=split(/\./,$files);
      $info="";
      if($b eq $extcadastro){
         $tploc=$userdir.$a.'.'.$b;
         open(L,$tploc);
             @info=<L>;
         close(L);
         foreach $i(@info){
            $info=$info.$i;
         } 
            @ddf=split(/\|+&+\|/,$info);
            @listmail[$s]=@ddf[1];
            $s++;
      }

   }

if(!$in{'a2'}){
     $n=$s;
     print<<"HTML";
     <form method="POST" name="admin.cgi"><input type="hidden" name="action" value="maillist"><input type="hidden" name="a2" value="sendmail"><p align="center"><font face="verdana, arial" size="3"><b>Maillist - $n emails</b></font></p><div align="center"><center><table border="0" width="417" height="291" cellspacing="0" cellpadding="0"><tr><td width="94" rowspan="3" height="260" valign="top"><font face="vedana, arial" size="1">
     <select size="14" name="emails" style="font-family: verdana, arial; font-size: 8 pt">
HTML
     print"<option value=\"todos\">todos</option>";

     foreach $listmail(@listmail){
         print"<option value=\"$listmail\">$listmail</option>";
     }

     print<<"HTML";
     </select>
     </font></td><td width="309" height="26"><font face="vedana, arial" size="1">&nbsp;Assunto: <input type="text" name="assunto" size="20" style="font-family: verdana, arial; font-size: 8 pt"></font></td>
     </tr><tr><td width="309" height="17"><font face="vedana, arial" size="1">&nbsp;Mensagem:</font></td></tr><tr><td width="309" height="205" valign="top"><p align="center"><font face="vedana, arial" size="1">&nbsp;<textarea rows="9" name="mensagem" cols="47" style="font-family: verdana; font-size: 8 pt"></textarea></font><font face="vedana, arial" size="1"><input type="submit" value="Enviar Mensagens" style="font-family: verdana, arial; font-size: 8 pt">
     <input type="reset" value="Apagar" style="font-family: verdana; font-size: 8 pt"></font></p></td></tr><tr><td width="388" height="19" colspan="2"><p align="center"><font face="vedana, arial" size="1">&nbsp;Para enviar email para todos os participantes, selecione todos na caixa de  emails</font></td>
     </tr></table></center></div></form>
HTML
}elsif($in{'a2'} eq "sendmail"){
    if($in{'emails'} eq "todos"){
           foreach $listmail(@listmail){
                open(MAIL, "|$mail_prog -t")||do{print"Falha ao enviar o email"; exit; };
                   print MAIL"To: $listmail\n";
                   print MAIL"From: $mailadmin\n";
                   print MAIL"Subject: $in{'assunto'}\n\n";
                   print MAIL"$in{'mensagem'}";
                close(MAIL);
   
           }
     }else{
                open(MAIL, "|$mail_prog -t")||do{print"Falha ao enviar o email"; exit; };
                   print MAIL"To: $in{'emails'}\n";
                   print MAIL"From: $mailadmin\n";
                   print MAIL"Subject: $in{'assunto'}\n\n";
                   print MAIL"$in{'mensagem'}";
                close(MAIL);
     }

print qq~
<p align="center"><font face="verdana, arial" size="3"><b>Email(s) Enviado(s) com sucesso</b></font></p><p align="center">&nbsp;</p><p align="center"><b><font face="verdana, arial" size="1" color="#000080"><a href="javascript: history.back();">Clique aqui para voltar</a></font></b></p>
~;
}
}
##########################################################
########## Busca Membros #################################
##########################################################
sub buscamembros{
   opendir(L,$userdir)||do{print"Erro ao abrir diretório de membros";exit;};
      @files=readdir(L);
   closedir(L);
$s=0;
   foreach $files(@files){
      ($a,$b)=split(/\./,$files);
      $info="";
      if($b eq $extcadastro){
             $tploc=$userdir.$a.'.'.$b;
             open(L,$tploc);
                @info=<L>;
             close(L);
             foreach $i(@info){
                $info=$info.$i;
             } 

             @dadost=split(/\|&\|/,$info);
             @nome[$s]=@dadost[2];
             @url[$s]=@dadost[3];
             @descricao[$s]=@dadost[4];
             @list[$s]=$info;  
             @listid[$s]=$a;

             $s++;
      }

   }

   $u=0;
   foreach $list(@list){
     @list[$u] =~ s/\|+&+\|/ /g;
     $u++;
   }

   $z=0; $r=0;
   foreach $list(@list){
      if($list =~ /$in{'pal'}/i){
         $x=$r+1;
         @linhas[$r]= qq~
              <p align="left"><font face="Verdana" size="2"><b><font color="#008000">$x</font> -
              <a href="admin.cgi?action=verdados&amp;id=@listid[$z]"> @nome[$z]</a>: @descricao[$z].&nbsp; <font color="#000080">ID: @listid[$z]&nbsp; 
              </font></b></font></p>
         ~; 
         $r++;
      }
      $z++;
   }

print qq~
<p align="center"><font face="Verdana" size="2"><b>Foram encontrados $r resultados com &quot;$in{'pal'}&quot;</b></font></p>

~;

print @linhas;

}
##########################################################
##########################################################
########## Ver Dados #####################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################

sub verdados{

   $loc2=$userdir.$in{'id'}.'.'.$extcadastro;
   open(L,$loc2);
      @var=<L>;
   close(L);
   foreach $var(@var){
     $d=$d.$var;
   }
   @dados=split(/\|+&+\|/,$d);
   $nome=@dados[0];
   $email=@dados[1];
   $site=@dados[2];
   $url=@dados[3];
   $descricao=@dados[4];
   $categoria=@dados[5];

&verposicao('cat');
$p1=$posicao;
  $contvar=0;
&verposicao;
$p2=$posicao;
$pgeral=$p2;
$posicao=$p1;

$qtvotos=$voto{$in{'id'}};

print<<"HTML";
<form method="POST" action="admin.cgi">
<input type="hidden" name="action" value="altdados"><input type="hidden" name="id" value="$in{'id'}"><div align="center"><center><table border="0" width="305" cellspacing="0" cellpadding="0" height="68"><tr><td colspan="2" height="13" width="303"><p align="center"><font face="Verdana" size="1"><b>Administração: ID $in{'id'}</b></font></td></tr><tr><td height="19" align="right" width="152"><font face="Verdana" size="1">Website:</font></td><td height="19" width="153"><font face="Verdana" size="1">&nbsp; $site</font></td> 
</tr> <tr> <td height="20" align="right" width="152"><font face="Verdana" size="1">Categoria:</font></td> <td height="20" width="153"><font face="Verdana" size="1">&nbsp; $categoria</font></td> </tr> <tr> <td height="20" align="right" width="152"><font face="Verdana" size="1">Votos:</font></td> <td height="20" width="153"><font face="Verdana" size="1">&nbsp; $qtvotos</font></td> </tr><tr> <td height="20" align="right" width="152"><font face="Verdana" size="1">Posição:</font></td> <td height="20" width="153"><font face="Verdana" size="1">&nbsp; $posicao</font></td> </tr><tr> <td height="20" align="right" width="152"><font face="Verdana" size="1">Posição Geral:</font></td> <td height="20" width="153"><font face="Verdana" size="1">&nbsp;  $pgeral</font></td> </tr><tr> <td height="20" align="right" width="305" colspan="2">
<p align="center"><font face="Verdana" size="1" color="#000080"><b><a href="admin.cgi?action=exwebsite&amp;id=$in{'id'}">Excluir Website</a></b></font></td> </tr></table>



</center></div><br><div align="center"><center><table border="0" width="321" cellspacing="0" cellpadding="0" height="289"></center><center><tr><td width="319" colspan="2" height="15"><p align="center"><font face="Verdana" size="1"><b>Dados do Website</b></font></td></tr><tr><td width="111" height="25" align="right" valign="middle"><font face="Verdana" size="1">Webmaster:</font></td>
<td width="206" height="25" valign="middle"><font face="Verdana" size="1">&nbsp;<input type="text" name="nome" size="29" style="font-family: verdana, arial; font-size: 8 pt" value="$nome"></font></td></tr><tr><td width="111" height="25" align="right" valign="middle"><font face="Verdana" size="1">Email:&nbsp;</font></td><td width="206" height="25" valign="middle"><font face="Verdana" size="1">&nbsp;<input type="text" name="email" size="29" style="font-family: verdana, arial; font-size: 8 pt" value="$email"></font></td></tr><tr><td width="111" height="29" align="right" valign="middle"><font face="Verdana" size="1">Nome do Website:</font></td><td width="206" height="29" valign="middle"><font face="Verdana" size="1">&nbsp;</font><font face="Verdana" size="1"><input type="text" name="website" size="29" style="font-family: verdana, arial; font-size: 8 pt" value="$site"></font></td></tr><tr><td width="111" height="29" align="right" valign="middle"><font face="Verdana" size="1">URL:</font></td><td width="206" height="29" valign="middle"><font face="Verdana" size="1">&nbsp;</font><font face="Verdana" size="1"><input type="text" name="url" size="29" style="font-family: verdana, arial; font-size: 8 pt" value="$url"></font></td></tr><tr><td width="111" height="62" valign="top" align="right"><font face="Verdana" size="1">Descrição:</font></td><td width="206" height="62"><font face="Verdana" size="1">&nbsp;<textarea rows="5" name="descricao" cols="27" style="font-family: verdana, arial; font-size: 8 pt">$descricao</textarea></font></td></tr><tr> <td width="111" height="20" align="right" valign="middle"><font face="Verdana" size="1">
Categoria:</font> </td><td width="206" height="20" valign="middle"><font face="Verdana" size="1">&nbsp;
<select size="1" name="categoria" style="font-family: verdana, arial; font-size: 8 pt">
HTML

open(L,$categorias)||do{print"Erro ao abrir arquivo de categorias";exit;};
  @categorias=<L>;
close(L);

  foreach $cat(@categorias){
        $cat =~ s/\n//;
        if($categoria eq $cat){
           print"<option selected value=\"$cat\">$cat</option>";
         }else{
           print"<option value=\"$cat\">$cat</option>";
         }
  }

#$categoria

print<<"HTML";
</select>
</font></td></tr><tr><td width="317" height="20" align="right" valign="middle" colspan="2"><p align="center"><font face="verdana, arial" size="1">&nbsp;</font> </td></tr><tr><td width="317" height="20" align="right" valign="middle" colspan="2"><p align="center"><input type="submit" style="font-family: 'verdana ', arial; font-size: 8 pt" value="Alterar Dados"> </td></tr></table></center></div><p>&nbsp;</p></form>

HTML

}

######### verposicao

sub verposicao{
    local($tipo) = @_;

opendir(L,$userdir)||do{&html('Erro ao abrir diretório de usuários');exit;};
   @files=readdir(L);
closedir(L);

$t=0;
$r=0;

if($tipo eq 'cat'){
     opendir(LOC,$userdir);
         @arqs=readdir(LOC);
     closedir(LOC);
     
     foreach $arqs(@arqs){
        ($a,$b)=split(/\./,$arqs);
        $tvar="";
        if($b eq $extcadastro){
          $tpm=$userdir.$a.'.'.$b;

          @idf[$r]=$a;
          $r++;

          open(K,$tpm);
               @tvar=<K>;
          close(K);
          foreach $tv(@tvar){
             $tvar=$tvar.$tv;
          }
          @campos=split(/\|+&+\|/,$tvar);
          $cat{$a}=@campos[5];
        }
     }
   $categoria=$cat{$in{'id'}};
   $s=0; $g=0;

   foreach $idf(@idf){
        if($cat{$in{'id'}} eq $cat{$idf}){
          @fill[$s]=$idf.'.'.$extvoto;
          $s++;
        }
   }

}else{
  @fill=@files;
}



foreach $files(@fill){
     ($arq,$ext)=split(/\./,$files);
     if($ext eq $extvoto){
         $loc=$userdir.$arq.'.'.$extvoto;
         open(L,$loc);
            $voto=<L>;
         close(L);

         @ids[$t]=$arq;
         @votos[$t]=$voto;
         $voto{$arq}=$voto;
         $t++;
     }
}




###############################################################################################
@cliques2=@votos;
@id2=@ids;

foreach $cliques2(@cliques2){
  $valor=0;
  if($cliques>0-1){
    $cont2=0;
    &vermaior;
  }
}

sub vermaior{
foreach $cliques2(@cliques2){
   $not=1;
   foreach $cl(@cliques2){
        if( $cliques2<$cl ){
              $not=0;
        }
   }

  if( ($not!=0) && ($cliques2!=-1) ){
     @clique[$contvar]=$cliques2;
     @id[$contvar]=@id2[$cont2];

     $contvar++;
     @cliques2[$cont2]=-1;
  }
$cont2++;
}
}

$n=0;
foreach $id(@id){
  if($in{'id'} eq $id){
    $posicao=$n+1;
  }
#print"$id<br>";
$n++;
}

#print"<br><br><br>";

}


sub altdados{

   $loc2=$userdir.$in{'id'}.'.'.$extcadastro;
   open(L,$loc2);
      @var=<L>;
   close(L);
   foreach $var(@var){
     $d=$d.$var;
   }
   @dados=split(/\|+&+\|/,$d);
   $site=@dados[2];
   $url=@dados[3];
   $descricao=@dados[4];
   $categoria=@dados[5];
   $cry=@dados[6];

$todos=$in{'nome'}.$in{'email'}.$in{'descricao'}.$in{'senha'}.$in{'website'}.$in{'url'};

if(!$in{'nome'} or !$in{'email'}  or !$in{'descricao'}){
    print qq~ <center><font face=\"$fonte\" size=\"$size\">Campos em Branco</font></center>
      <hr><p><font face="$fonte" size="$size"><a href="javascript: history.back();">Voltar</a></font></p>
    ~;
    exit;
} if($in{'nome'} =~ /[!@#\$%^&*();+=:\/]/){
   print qq~ <center><font face=\"$fonte\" size=\"$size\">O nome contém caracteres inválidos</font></center>
      <hr><p><font face="$fonte" size="$size"><a href="javascript: history.back();">Voltar</a></font></p>
   ~;
   exit;
} if($in{'email'} !~ /@/){
      print qq~ <center><font face=\"$fonte\" size=\"$size\">Email Inválido</font></center>
      <hr><p><font face="$fonte" size="$size"><a href="javascript: history.back();">Voltar</a></font></p>
   ~;
   exit;
}if($in{'url'} !~ "http://"){ 
      print qq~ <center><font face=\"$fonte\" size=\"$size\">A url deve começar com http://</font></center>
      <hr><p><font face="$fonte" size="$size"><a href="javascript: history.back();">Voltar</a></font></p>
   ~;
   exit;
}
if($todos =~ /\|&\|/){
   print qq~ <center><font face=\"$fonte\" size=\"$size\">Sequência de caracteres inválidos detectado: |&|</font></center>
      <hr><p><font face="$fonte" size="$size"><a href="javascript: history.back();">Voltar</a></font></p>
   ');
   ~;
}

$cry=crypt($in{'senha'},HJ);
$in{'descricao'} =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

   open(L,">$loc2");
      print L"$in{'nome'}|&|$in{'email'}|&|$in{'website'}|&|$in{'url'}|&|$in{'descricao'}|&|$in{'categoria'}|&|$cry";
   close(L);

print<<"HTML";
<p align="center"><font face="Verdana" size="3"><b>Dados Alterados com Sucesso</b></font></p>
<p align="center"><font face="Verdana" size="1"><a href="javascript: history.back();">Voltar</a></font></p>
HTML
##########################################################
##########################################################
########## Excluir website ###############################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################

}sub exwebsite{
 @loc[0]=$userdir.$in{'id'}.'.'.$extprot;
 @loc[1]=$userdir.$in{'id'}.'.'.$extcadastro;
 @loc[2]=$userdir.$in{'id'}.'.'.$extvoto;

foreach $loc(@loc){
   unlink $loc;
}

print qq~
<blockquote><p align="center"><font face="verdana, arial" size="3"><b>Website removido com sucesso</b></font></p></blockquote><p align="center"><font face="verdana, arial" size="2" color="#000080"><a href="javascript: history.back();">Voltar</a></font></p>
~;

exit;
}
##########################################################
##########################################################
########## Ver log #######################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
sub log{
print qq~
  <p align="center"><font face="verdana, arial" size="3"><b>LOGS - dia/mes</b></font></p>
~;

  opendir(L,$userdir);
     @files=readdir(L);
  closedir(L);
  foreach $files(@files){
    ($a,$b)=split(/\./,$files);
    if($b eq $extlog){
      ($dia,$mes)=split(/\-/,$a);
         $mesp=$mes+1;
         print qq~
            <p align="center"><font face="Verdana" size="1">
              <a href="admin.cgi?action=verlog&amp;log=$dia-$mes">$dia/$mesp</a></font></p>
         ~;
    }

  }
exit;
}
sub verlog{
print qq~
<div align="center">
<table border="0" width="60%" cellspacing="1" cellpadding="0" height="79">
  <tr><td width="100%" colspan="3" align="center" bgcolor="#000080" height="15"><font color="#FFFFFF" size="1" face="verdana, arial"><b>Tabela
      de IDS</b></font></td></tr><tr><td width="33%" bgcolor="#C0C0C0" align="center" height="15"><font face="verdana, arial" size="1">ID</font></td>
    <td width="33%" bgcolor="#C0C0C0" align="center" height="15"><font face="verdana, arial" size="1">IP</font></td>    <td width="34%" bgcolor="#C0C0C0" align="center" height="15"><font face="verdana, arial" size="1">Hora</font></td></tr>
~;

  $loc=$userdir.$in{'log'}.'.'.$extlog;
  open(L,$loc);
     @va=<L>;
  close(L);
   foreach $va(@va){
     ($id,$ip,$hora)=split(/\|+&+\|/,$va);
    if($in{'idv'}){
      if($in{'idv'} eq $id){
          print qq~
            <tr>
              <td width="33%" align="center" bgcolor="#F3F3F3" height="20"><font size="1" face="verdana, arial">&nbsp;$id</font></td>
              <td width="33%" align="center" bgcolor="#F3F3F3" height="20"><font size="1" face="verdana, arial">$ip</font></td>
              <td width="34%" align="center" bgcolor="#F3F3F3" height="20"><font size="1" face="verdana, arial">$hora</font></td>
            </tr>
          ~;
       }
     }else{
          print qq~
            <tr>
              <td width="33%" align="center" bgcolor="#F3F3F3" height="20"><font size="1" face="verdana, arial">&nbsp;$id</font></td>
              <td width="33%" align="center" bgcolor="#F3F3F3" height="20"><font size="1" face="verdana, arial">$ip</font></td>
              <td width="34%" align="center" bgcolor="#F3F3F3" height="20"><font size="1" face="verdana, arial">$hora</font></td>
            </tr>
          ~;
    }
     
   }

print qq~
</table></div>
<form method="GET" action="admin.cgi" target="direito">
<input type="hidden" name="action" value="verlog">
<input type="hidden" name="log" value="$in{'log'}">
   <center><font face="Verdana" size="1"><b>Busca ID - Dia</b></font></center>
  <p align="center"><font face="Verdana" size="1"><b>ID: </b></font><input type="text" name="idv" size="7" style="font-family: verdana, arial; font-size: 8 pt">
  <input type="submit" value="Buscar" style="font-family: verdana, arial; font-size: 8 pt"></p>
</form>
~;

exit;
}
##########################################################
########## Finaliza Concurso #############################
##########################################################
sub final{
print <<"HTML";
<p align="center"><font face="verdana, arial" size="1"><b>Todos os votos serão apagados, você terá que ter toda a relação de colocação antes de conclui essa açao. </b></font></p><p align="center"><font face="verdana, arial" size="1"><b><font color="#000080"><a href="admin.cgi?action=finalizar">Finalizar
Concurso</a></font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="admin.cgi?action=page">Cancelar</a></b></font></p>
HTML
exit;
}sub finalizar{

   opendir(L,$userdir)||do{print"Erro ao abrir diretório de membros";exit;};
      @files=readdir(L);
   closedir(L);
   $s=0;
   foreach $files(@files){
      ($a,$b)=split(/\./,$files);
      $info="";
      if($b eq $extvoto){
         $tploc=$userdir.$a.'.'.$b;
         open(L,">$tploc");
             print L"0";
         close(L);

      }

   }

print<<"HTML";
       <p align="center">&nbsp;</p><p align="center">&nbsp;</p><p align="center">&nbsp;</p><p align="center">&nbsp;</p><p align="center"><font face="verdana, arial" size="1"><b>Operação finalizada com sucesso</b></font></p>
HTML

   exit;
}
