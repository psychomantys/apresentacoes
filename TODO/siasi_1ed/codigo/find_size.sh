#!/bin/bash

find "${1}" -xdev -size +4G -type f 2> /dev/null

