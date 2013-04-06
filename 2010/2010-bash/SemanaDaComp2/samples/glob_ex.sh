#!/bin/bash

for file in {{0..4},{6..9}}{0..9}{0..9} ; do
	echo > "${file}".txt
done
for file in 4{3..6}{0..9} 42{3..9} 47{0..4} ; do
	rm "${file}".txt
done
