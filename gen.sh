#!/bin/bash

if [ ! "$1" ] ; then
	set - .
fi

mkindex(){
# usage: auto-index [dir]

	local directory=

	if [ ! "$1" ] ; then
		directory=.
	else
		directory="$1"
	fi

	(
	cd "${directory}"
	echo "<html>
<head><title>Index of ${directory}</title></head>
<body>
<h2>Index of ${directory}</h2>
<a href=../ls_index.html>Parent Dir.</a>
<hr>
<ui>
"
	for x in * ; do
		#INDEX=`ls -1 $1 | sed "s/^.*/      <li\>\<a\ href=\"&\"\>&\<\\/a\>\<\\/li\>/"`
		if [ -d "${x}" ] ; then
			echo "<li><a href=\"${x}/ls_index.html\">[DIR] &nbsp;&nbsp;&nbsp;&nbsp; ${x}/</a></li>"
		else
			if [ "$x" != "ls_index.html" ] ; then
				echo "<li><a href=\"${x}\">[FILE] &nbsp;&nbsp;&nbsp; ${x}</a></li>"
			fi
		fi
	done
	echo "
<ui>
</body>
</html>"
	)
}

ndx=ls_index.html
find "$1" -type d | while read dir ; do
(
	mkindex "${dir}" > "${dir}/${ndx}"
	## where mkindex is a script to create index file
)
done

