#!/bin/bash

find "${1}" -type f -a ! -atime +10 2> /dev/null

