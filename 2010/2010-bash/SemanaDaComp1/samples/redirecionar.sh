#!/bin/bash
#Lalalaalla, não serei executado, sou um comentário
#Fale o que você vai mostrar agora:
echo Informações sobre a memoria usada: > log.txt
free -m >> log.txt
#vamos mostrar as infos do diretório raiz
echo >> log.txt
echo Infomações sobre o tamanho da partição principal: >> log.txt
echo >> log.txt
df -h / >> log.txt
echo >> log.txt
echo O meu sistema operacional é: >> log.txt
uname -s >> log.txt
