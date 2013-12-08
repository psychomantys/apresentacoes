#!/bin/bash

echo "Digite o primeiro nome:"
read nome1

echo "Digite o segundo nome:"
read nome2

if test "${nome1}" = "${nome2}" ; then
	echo "iguais"
else
	echo "diferentes"
fi
