#!d:/home/perl/bin/perl.exe
##!/usr/bin/perl

################################################################################################

print"Content-type: text/html\n\n";
require"config.pl";

if(!$in{'action'}){
   &htmlcad;
   &html(@linhas);
}elsif($in{'action'} eq 'login'){
   &login;
}elsif($in{'action'} eq 'altdados'){
   &altdados;
}

sub login{
  $id=$in{'id'};
  $tmp=$userdir.$in{'id'}.'.'.$extcadastro;
  open(L,$tmp)||&erro1;
    @cod=<L>;
  close(L);
  foreach $c(@cod){
     $cod=$cod.$c;
  }
  $senha=crypt($in{'senha'},HJ);
  @dados=split(/\|+&+\|/,$cod);

  if(@dados[6] eq $senha){
     $local=$userdir.$id.'.'.$extprot;
     $log=crypt($id.$ENV{REMOTE_HOST},HJ);
     open(L,">$local");
        print L"$log";
     close(L);
     &exibe;
  }else{ 
       &erro2;
  }
}

sub htmlcad{
@linhas= qq~
   <form method="POST" action="usuarios.cgi">
   <p>&nbsp;</p><input type="hidden" name="action" value="login"><div align="center"> <center><table border="0" width="24%" cellspacing="0" cellpadding="0">
   <tr><td width="100%" colspan="2"><p align="center"><font face="Verdana" size="1"><b>Administração</b></font></td>
   </tr><tr><td width="100%" colspan="2">&nbsp;</td></tr><tr><td width="7%" align="right"><font face="Verdana" size="1">ID:</font></td>
   <td width="93%"><font face="Verdana" size="1"><input type="text" name="id" value="$id" size="20"></font></td></tr><tr><td width="7%" align="right"><font face="Verdana" size="1">Senha:</font></td><td width="93%"><font face="Verdana" size="1"><input type="password" name="senha" size="20"></font></td>
   </tr><tr><td width="100%" colspan="2"><font face="Verdana" size="1">&nbsp;</font></td></tr><tr><td width="100%" colspan="2"><p align="center"><font face="Verdana" size="1"><input type="submit" value="Entrar" style="font-family: verdana; font-size: 8 pt"></font></p>
   </td></tr></table> </center></div></form>
~;

}
sub erro1{
     @lines= qq~
       <center><font face=\"$fonte\" size=\"$size\">ID Inválida</font></center><hr>
     ~;
     &htmlcad;
     $r=0;
     foreach $line(@lines){
        @li[$r]=$line;
        $r++;
     }
     foreach $line(@linhas){
        @li[$r]=$line;
        $r++;
     }
     &html(@li);
}
sub erro2{
     @lines= qq~
       <center><font face=\"$fonte\" size=\"$size\">Senha Inválida</font></center><hr>
     ~;
     &htmlcad;
     $r=0;
     foreach $line(@lines){
        @li[$r]=$line;
        $r++;
     }
     foreach $line(@linhas){
        @li[$r]=$line;
        $r++;
     }
     &html(@li);
}
###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################
################################## verifica usuário e mostra pagina ###########################
###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################

sub exibe{
   $verifica=crypt($in{'id'}.$ENV{'REMOTE_ADDR'},HJ);
   $loc=$userdir.$in{'id'}.'.'.$extprot;
   open(L,$loc);
      $ig=<L>;
   close(L);
   if($verifica ne $ig){
       &erro2;
   }

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

  &htmldados;

}

sub altdados{
   $verifica=crypt($in{'id'}.$ENV{'REMOTE_ADDR'},HJ);
   $loc=$userdir.$in{'id'}.'.'.$extprot;
   open(L,$loc);
      $ig=<L>;
   close(L);
   if($verifica ne $ig){
       &erro2;
   }

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
   $senha=@dados[6];

$todos=$in{'nome'}.$in{'email'}.$in{'descricao'}.$in{'senha'};

if(!$in{'nome'} or !$in{'email'}  or !$in{'descricao'} or !$in{'senha'}){
    &html('<center><font face=\"$fonte\" size=\"$size\">Campos em Branco</font></center>
      <hr><p><font face="$fonte" size="$size"><a href="javascript: history.back();">Voltar</a></font></p>
    ');
    exit;
} if($in{'nome'} =~ /[!@#\$%^&*();+=:\/]/){
   &html('<center><font face=\"$fonte\" size=\"$size\">O nome contém caracteres inválidos</font></center>
      <hr><p><font face="$fonte" size="$size"><a href="javascript: history.back();">Voltar</a></font></p>
   ');
   exit;
} if($in{'email'} !~ /@/){
   &html('<center><font face=\"$fonte\" size=\"$size\">Email Inválido</font></center>
      <hr><p><font face="$fonte" size="$size"><a href="javascript: history.back();">Voltar</a></font></p>
   ');
   exit;
} if(length($in{'senha'})<6){
   &html('<center><font face=\"$fonte\" size=\"$size\">A senha deverá ter no mínimo 6 caracteres</font></center>
      <hr><p><font face="$fonte" size="$size"><a href="javascript: history.back();">Voltar</a></font></p>
   ');
   exit;
} if($todos =~ /\|&\|/){
   &html('<center><font face=\"$fonte\" size=\"$size\">Sequência de caracteres inválidos detectado: |&|</font></center>
      <hr><p><font face="$fonte" size="$size"><a href="javascript: history.back();">Voltar</a></font></p>
   ');
   exit;
}

$cry=crypt($in{'senha'},HJ);

   open(L,">$loc2");
      print L"$in{'nome'}|&|$in{'email'}|&|$site|&|$url|&|$in{'descricao'}|&|$categoria|&|$cry";
   close(L);

&html('<p align="center"><font face="Verdana" size="3"><b>Dados Alterados com Sucesso</b></font></p>
        <p align="center"><font face="Verdana" size="1"><a href="javascript: history.back();">Voltar</a></font></p>
      ');

}

###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################
################################# Verifica Posição ############################################
###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################


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

###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################



sub htmldados{
@linhas = qq~
<form method="POST" action="usuarios.cgi">
<input type="hidden" name="action" value="altdados">
<input type="hidden" name="id" value="$id"><div align="center"><center><table border="0" width="305" cellspacing="0" cellpadding="0" height="68"><tr><td colspan="2" height="13" width="303"><p align="center"><font face="Verdana" size="1"><b>Administração</b></font></td></tr><tr><td height="19" align="right" width="152"><font face="Verdana" size="1">Website:</font></td><td height="19" width="153"><font face="Verdana" size="1">&nbsp; $site</font></td> 
</tr> <tr> <td height="20" align="right" width="152"><font face="Verdana" size="1">Categoria:</font></td> <td height="20" width="153"><font face="Verdana" size="1">&nbsp; $categoria</font></td> </tr> <tr> <td height="20" align="right" width="152"><font face="Verdana" size="1">Posição:</font></td> <td height="20" width="153"><font face="Verdana" size="1">&nbsp; $posicao</font></td> </tr><tr> <td height="20" align="right" width="152"><font face="Verdana" size="1">Posição Geral:</font></td> <td height="20" width="153"><font face="Verdana" size="1">&nbsp; $pgeral</font></td> </tr><tr> <td height="20" align="center" width="305" colspan="2"><font face="Verdana" size="1"><b>Código HTML</b></font></td> </tr><tr> <td height="20" align="right" width="305" colspan="2"><p align="center"><font face="Verdana" size="1"><textarea rows="7" name="htmlcode" cols="47" style="font-family: $fonte; font-size: 8 pt"><form method="post" action="$httptop/votar.cgi">
<input type="hidden" name="id" value="$id"><input type="image" src="$dirselos/$selodef" border=0>
</form></textarea></font></td> </tr></table></center></div><br><div align="center"><center><table border="0" width="321" cellspacing="0" cellpadding="0" height="289"></center><center><tr><td width="319" colspan="2" height="15"><p align="center"><font face="Verdana" size="1"><b>Dados do Website</b></font></td></tr><tr><td width="111" height="25" align="right" valign="middle"><font face="Verdana" size="1">Webmaster:</font></td>
<td width="206" height="25" valign="middle"><font face="Verdana" size="1">&nbsp;<input type="text" name="nome" size="29" style="font-family: verdana, arial; font-size: 8 pt" value="$nome"></font></td></tr><tr><td width="111" height="25" align="right" valign="middle"><font face="Verdana" size="1">Email:&nbsp;</font></td><td width="206" height="25" valign="middle"><font face="Verdana" size="1">&nbsp;<input type="text" name="email" size="29" style="font-family: verdana, arial; font-size: 8 pt" value="$email"></font></td></tr><tr><td width="111" height="29" align="right" valign="middle"><font face="Verdana" size="1">Nome do Website:</font></td><td width="206" height="29" valign="middle"><font face="Verdana" size="1">&nbsp;$site</font></td></tr><tr><td width="111" height="29" align="right" valign="middle"><font face="Verdana" size="1">URL:</font></td><td width="206" height="29" valign="middle"><font face="Verdana" size="1">&nbsp;$url</font></td></tr><tr><td width="111" height="62" valign="top" align="right"><font face="Verdana" size="1">Descrição:</font></td><td width="206" height="62"><font face="Verdana" size="1">&nbsp;<textarea rows="5" name="descricao" cols="27" style="font-family: verdana, arial; font-size: 8 pt">$descricao</textarea></font></td></tr><tr> <td width="111" height="20" align="right" valign="middle"><font face="Verdana" size="1">Categoria:</font> </td><td width="206" height="20" valign="middle"><font face="Verdana" size="1">&nbsp;$categoria</font></td></tr><tr><td width="111" height="20" align="right" valign="middle"><font face="Verdana" size="1">Senha:</font> </td>
<td width="206" height="20" valign="middle"><font face="Verdana" size="1">&nbsp;<input type="password" name="senha" size="29" style="font-family: verdana, arial; font-size: 8 pt"></font></td></tr><tr><td width="317" height="20" align="right" valign="middle" colspan="2"><p align="center"><font face="verdana, arial" size="1">&nbsp;</font> </td></tr><tr><td width="317" height="20" align="right" valign="middle" colspan="2"><p align="center"><input type="submit" style="font-family: 'verdana ', arial; font-size: 8 pt" value="Alterar Dados"> </td></tr></table></center></div>


~;
&html(@linhas);
}

