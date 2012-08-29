#!/bin/bash

echo 'Digite o nome do usuario:'

read nome

if fgrep -qs "${nome}:" /etc/passwd ; then
	echo "Usuario existe!!"
	echo "Seus grupos sao:"
	fgrep "${nome}" /etc/group | cut -f1 -d':'
else
	echo "usuario nao existe!"
fi
