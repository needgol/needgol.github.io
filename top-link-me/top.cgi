#!d:/home/perl/bin/perl.exe
##!/usr/bin/perl

################################################################################################

print"Content-type: text/html\n\n";
require"config.pl";

###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################
############################### Gera Dados para a tabela $$####################################
###############################################################################################
###############################################################################################
###############################################################################################
if($in{'action'} eq "selos"){
    &print('selos.htm');
}elsif($in{'action'} eq "premios"){
    &print('premios.htm');
}elsif($in{'action'} eq "regras"){
    &print('regras.htm');
}elsif($in{'action'} eq "vencedores"){
    &print('vencedores.htm');
}


opendir(L,$userdir)||do{&html('Erro ao abrir diretório de usuários');exit;};
   @files=readdir(L);
closedir(L);

$t=0;
$r=0;

if(!$in{'categoria'} or $in{'categoria'} eq "Geral" ){
  @fill=@files;
  $pst="Ranking Geral";
}else{
  $pst="Ranking - ".$in{'categoria'};
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
   $categoria=$in{'categoria'};
   $s=0; $g=0;

   foreach $idf(@idf){
   #print"$cat{$idf}-";
        if($in{'categoria'} eq $cat{$idf}){
          @fill[$s]=$idf.'.'.$extvoto;
          $s++;
        }
   }
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


if($t==0){
&html('<p align="center">&nbsp;</p><p align="center">&nbsp;</p><p align="center">
       <font face="verdana, arial" size="1"><b>Ainda não obtivemos nenhum cadastro</b>
       </font></p>');

exit;
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
###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################
###############################$$$$$$$$$$$$$$$$$$$$$$$$$$$$####################################
###############################################################################################
###############################################################################################
###############################################################################################
$h=0;
foreach $g(@id){
   $tt="";
   $rrt=$userdir.$g.'.'.$extcadastro;
   open(A,$rrt)||do{&html('Erro ao gerar ranking');exit;};
      @re=<A>;
   close(A);
   foreach $re(@re){
     $tt=$tt.$re;   
   }
   @dsd=split(/\|+&+\|/,$tt);
   @website[$h]=@dsd[2];
   @url[$h]=@dsd[3];
   $h++;
}

$r=0;
$q=$in{'p'}*10;
$u=$q+10;

$tdy=0;
foreach $id(@id){
$tdy++;
}
$outro=$tdy;
$pages=0;
while ($outro>10){
 $outro-=10;
 $pages++;
} 
$h=0;

@conteudo[$h]= qq~
<div align="center">
  <center>
<table border="0" width="95%" cellspacing="1" cellpadding="0" height="28">
  <tr>
    <td width="100%" colspan="4" align="center" bgcolor="#000080" height="4"><font face="Verdana" size="1" color="#FFFFFF"><b>$pst</b></font></td>
  </tr>
~;
$h++;
$tk=0;
while($q<$u and $q<$tdy){
   $y=$q+1;

   #if($tdy>$q){
   #@conteudo[$h]="$yº-@website[$q]-@url[$q]-@clique[$q]-@id[$q]----$q<bR>";
 $website=@website[$q];
 $votos=@clique[$q];
if($tk==0){
@conteudo[$h]= qq~
  <tr>
    <td width="5%" bgcolor="$bfcolor" height="1">
      <p align="center"><font color="$bfontecolor" face="$bfonte" size="$btamanho">$yº</font></td>
    <td width="71%" bgcolor="$bfcolor" " height="1"><a href="@url[$q]" target="_blank"><font color="$bfontecolor" face="$bfonte" size="$btamanho">$website</font></a></td>
    <td width="13%" bgcolor="$bfcolor" " height="1" align="center"><font color="$bfontecolor" face="$bfonte" size="$btamanho">$votos
      votos</font></td>
    <td width="11%" bgcolor="$bfcolor" " height="1">
      <form method="GET" action="votar.cgi">
      <input type="hidden" name="id" value="@id[$q]">
      <p align="center"><input type="submit" value="Votar" style="font-family: verdana; font-size: 8 pt"></p>     
    </td></form>
  </tr>
~;
}if($tk==1){
@conteudo[$h]= qq~
  <tr>
    <td width="5%" bgcolor="$cfcolor" height="1">
      <p align="center"><font color="$cfontecolor" face="$cfonte" size="$ctamanho">$yº</font></td>
    <td width="71%" bgcolor="$cfcolor" " height="1"><a href="@url[$q]" target="_blank"><font color="$cfontecolor" face="$cfonte" size="$ctamanho">$website</font></a></td>
    <td width="13%" bgcolor="$cfcolor" " height="1" align="center"><font color="$cfontecolor" face="$cfonte" size="$ctamanho">$votos
      votos</font></td>
    <td width="11%" bgcolor="$cfcolor" " height="1">
      <form method="GET" action="votar.cgi">
      <input type="hidden" name="id" value="@id[$q]">
      <p align="center"><input type="submit" value="Votar" style="font-family: verdana; font-size: 8 pt"></p>     
    </td></form>
  </tr>
~;

}
    $h++;
    $q++;
    $tk++;
if($tk==2){$tk=0;}

}

@conteudo[$h]="</table></center></div><center>";

$g=0;
$ol=0;
$p2=$in{'p'}-1;

if($in{'p'}>0){
   @pr[$ol]="<font face=\"Verdana\" size=\"1\" color=\"#800080\"><b>[<a href=\"top.cgi?p=$p2&categoria=$in{'categoria'}\">anterior</a>]&nbsp;&nbsp;&nbsp;</b></font>";
$ol++;
}
if($pages==0){$pages--;}

while($g<=$pages){
$t=$g+1;

   @pr[$ol]="<font face=\"Verdana, arial\" size=\"1\" color=\"#800080\"><b><a href=\"top.cgi?p=$g&categoria=$in{'categoria'}\">&nbsp;&nbsp;$t&nbsp;&nbsp;</a></b></font>";

$ol++;
$g++;
}
if($in{'p'}<$pages){
     $kp=$in{'p'}+1;
     @pr[$ol]="<font face=\"Verdana\" size=\"1\" color=\"#800080\"><b>&nbsp;&nbsp;&nbsp;[<a href=\"top.cgi?p=$kp&categoria=$in{'categoria'}\">próximo</a>]</b></font>";
}


### imprime resultados
&html(@conteudo,@pr,'</center>');




sub print{
    local($open) = @_;
    open(L,$pagedir.$open);
         @linhas=<L>;
    close(L);
    &html(@linhas);
    exit;
}