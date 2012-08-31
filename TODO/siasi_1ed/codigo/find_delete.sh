#!/bin/bash

find "${1}" -delete -type f -a -size 2G -a -atime -10 2> /dev/null

