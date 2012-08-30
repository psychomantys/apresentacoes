#!/bin/bash

find "${1}" -xdev -perm +4000 2> /dev/null

