#!/bin/bash
x=
resultado=1

read x

while [ ${x} != 0 ] ; do
	resultado=$(( resultado*x ))
	x=$((x-1))
done

echo ${resultado}
