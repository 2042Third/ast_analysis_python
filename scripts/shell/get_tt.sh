ls -R | grep --exclude=*.{pyc,cpython-38.pyc} "\.py" | wc -l

ls -R | grep -v "\.pyc" | grep "\.py"| wc -l