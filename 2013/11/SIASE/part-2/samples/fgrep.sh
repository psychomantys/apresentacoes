#!/bin/bash
echo "Digite o nome de um usuario:"
read nome

fgrep "${nome}" /etc/{passwd,group}
