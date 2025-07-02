#!d:/home/perl/bin/perl.exe
##!/usr/bin/perl

################################################################################################

print"Content-type: text/html\n\n";
require"config.pl";

$id=$in{'id'};

if(!$in{'action'}){
   &vconf;
}else{
   &votar;
}

sub votar{
 if($ENV{REQUEST_METHOD} ne "POST"){
  &html('<center><font face=\"$fonte\" size=\"$size\">Falha ao confirmar voto, isso pode ter ocorrido por alteração do código de votação.</font></center>');
  exit; 
 }

 $id=$in{'id'};
 $num=$in{'numero'};

 $i=$num.$ENV{'REMOTE_ADDR'};
 $v=crypt($i,YL);

if(!$id){
  &html('<center><font face=\"$fonte\" size=\"$size\">Este website não está cadastrado em nosso sistema</font></center>');
  exit;
}

if($v ne $in{'controle'}){
  &html('<center><font face=\"$fonte\" size=\"$size\">Você digitou o número de controle errado</font></center>');

  exit;
}

&verip;
###############################################################################################
############ Conta votos caso ip esteja ok
###############################################################################################
if($perm==1){

$loc=$userdir.$in{'id'}.'.'.$extcadastro;
$loc2=$userdir.$in{'id'}.'.'.$extvoto;

open(L,$loc)||do{ &html('Erro ao abrir registro do website');};
  flock(L,2);
  @var=<L>;
close(L);
foreach $var(@var){
  $cont=$cont.$var;
}
@dados=split(/\|+&+\|/,$cont);
$nome=@dados[2];
$url=@dados[3];
$categoria=@dados[5];

  $tmp=$userdir.$id.'.'.$extvoto;
  open(L,$tmp)||do{&html('<center><font face=\"$fonte\" size=\"$size\">Erro ao brir arquivo de registro</font></center>');exit;};
    flock(L,2);
    $cont=<L>;
  close(L);
  $cont++;
  open(L,">$tmp")||do{&html('<center><font face=\"$fonte\" size=\"$size\">Erro ao brir arquivo de registro</font></center>');exit;};
    flock(L,2);
    print L"$cont";
  close(L); 

@lines = qq~
<p align="center"><b><font face="verdana, arial" size="3">Voto Computado</font></b></p>
<p align="center">&nbsp;</p>
<p align="center"><font face="verdana, arial" size="2">O website <a href="$url">$nome</a>
agora está com $cont votos</font></p>
<p align="center"><font face="verdana, arial" size="2"><a href="$script?categoria=$categoria">Ver
Colocação desse website na categoria $categoria</a></font></p>
~;

&html(@lines);

}else{
       $loc=$userdir.$in{'id'}.'.'.$extcadastro;

       open(L,$loc)||do{ &html('Erro ao abrir registro do website');};
         flock(L,2);
         @var=<L>;
       close(L);
       foreach $var(@var){
         $cont=$cont.$var;
       }
       @dados=split(/\|+&+\|/,$cont);
       $nome=@dados[2];
       $url=@dados[3];
       $categoria=@dados[5];
         @lines = qq~
            <p align="center"><font face="Verdana" size="3"><b>Acesso Negado:</b></font></p><p align="center">
            <font face="Verdana" size="2">Você já votou nesse website hoje</font></p><p align="center">
            <font face="verdana, arial" size="2"><a href="$script?categoria=$categoria">Ver
            Colocação desse website na categoria $categoria</a></font></p>
         ~;
  
         &html(@lines);

       exit;
}

}
###############################################################################################
############ Verifica IP
###############################################################################################

sub verip{
  ($sec,$min,$hour,$day,$mon,$year,$wday) = (localtime(time))[0,1,2,3,4,5,6];

$log=$userdir.$day.'-'.$mon.'.'.$extlog;

open(L,"+<$log")||do{open(L,">>$log");close(L);};
   flock(L,2);
   @t=<L>;
close(L);
$jk=0;
foreach $t(@t){
   ($idd,$ipp,$resto)=split(/\|+&+\|/,$t);
   if($idd eq $in{'id'}){
       @did[$jk]=$idd;
       @dip[$jk]=$ipp;
       $jk++;
   }
}$lo=0; $tty=0;
foreach $dip(@dip){
     if($ENV{'REMOTE_ADDR'} eq $dip){
       $tty++;
     }

     $lo++;
}

   if($tty==0){
      $perm=1;
      open(L,">>$log");
         flock(L,2);
         print L"$in{'id'}|&|$ENV{'REMOTE_ADDR'}|&|$hour:$min:$sec\n";
       close(L);
   }else{
     $perm=0;
   }



}

###############################################################################################
############ Confirmação de Voto
###############################################################################################


sub vconf{

  ($sec,$min,$hour,$day,$mon,$year,$wday) = (localtime(time))[0,1,2,3,4,5,6];

if(!$in{'id'}){
 &html('Este website não está cadastrado em nosso sistema');
 exit;
}
$loc=$userdir.$in{'id'}.'.'.$extcadastro;
$loc2=$userdir.$in{'id'}.'.'.$extvoto;

open(L,$loc)||do{ &html('Erro ao abrir registro do website');};
  flock(L,2);
  @var=<L>;
close(L);
foreach $var(@var){
  $cont=$cont.$var;
}
@dados=split(/\|+&+\|/,$cont);
$site=@dados[2];
$categoria=@dados[5];

open(L,$loc2)||do{ &html('Erro ao abrir registro do website');};
  flock(L,2);
  $votos=<L>;
close(L);
}
###############################################################################################
####################### Gera Número Randômico #################################################
###############################################################################################

  @seq[0]=$sec;
  if($sec==0){$sec=1;}
  if($min==0){$min=1;}
  @seq[1]=$sec*$min*3;  
  @seq[2]=$sec*$min*7;  
 
  foreach $seq(@seq){
      while($seq>9){
          $seq=$seq-10;    
      }
  @seq[$n]=$seq;
  $rand=$rand.$seq;
  $n++;
  }
  $i=$rand.$ENV{'REMOTE_ADDR'};
  $v=crypt($i,YL);
   &html1;
   &html(@linhas);
 

###############################################################################################
############ Código html da confirmação de votos
###############################################################################################


sub html1{
@linhas=qq~
<br><div align="center"><center><table border="0" width="260" cellspacing="0" cellpadding="0" height="144"><tr><td width="256" height="11" colspan="2" align="center" bgcolor="#C0C0C0"><b><font face="verdana, arial" size="2">Votar</font></b></td>
</tr><tr><td width="78" height="10" bgcolor="#E8E8E8"><font face="verdana, arial" size="1"><b>&nbsp;Website:</b></font></td>
<td width="178" height="10" bgcolor="#E8E8E8"><font face="verdana, arial" size="1">$site</font></td></tr><tr><td width="78" height="21" bgcolor="#E8E8E8"><font face="verdana, arial" size="1"><b>&nbsp;Categoria:</b></font> </td>
<td width="178" height="21" bgcolor="#E8E8E8"><font face="verdana, arial" size="1">$categoria</font></td></tr><tr><td width="78" height="22" bgcolor="#E8E8E8"><font face="verdana, arial" size="1"><b>&nbsp;Votos:</b></font></td>
<td width="178" height="22" bgcolor="#E8E8E8"><font face="verdana, arial" size="1">$votos</font></td></tr><tr><td width="258" colspan="2" height="21" bgcolor="#E8E8E8">&nbsp;</td></tr><tr><td width="258" colspan="2" height="8" bgcolor="#E8E8E8">
<p align="center"><font face="verdana, arial" size="1">Para Confirmar seu voto, copie o número abaixo na caixa de texto e clique em votar</font></td>
</tr><tr><td width="258" colspan="2" height="7" bgcolor="#E8E8E8"><font face="verdana, arial" size="1">&nbsp;</font></td>
</tr><tr><td width="78" height="15" bgcolor="#E0E0E0"><p align="center"><font face="verdana, arial" size="1"><b>Número</b></font></p>
</td><td width="178" height="15" bgcolor="#D4D4D4" align="center"><font face="Verdana" size="1">Copie aqui o número</font></td></tr><tr><td height="29" bgcolor="#E0E0E0"><p align="center"><font face="verdana, arial" size="1">&nbsp;</font><font face="verdana, arial" size="2">$rand</font></p>
</td><td width="178" height="29" bgcolor="#D4D4D4" align="center">  <form method="POST" action="votar.cgi"><input type="hidden" name="id" value="$in{'id'}"><input type="hidden" name="action" value="votar"><input type="hidden" name="controle" value="$v"><p><font face="verdana, arial" size="1"><input type="text" name="numero" size="4" style="font-family: verdana; font-size: 8 pt">
<input type="submit" value="Votar" style="font-family: verdana; font-size: 8 pt"></font></p></form></td></tr></table></center></div>

~;


}

