#!/bin/bash
if [ -z "$1" ]
then 
  echo "Directory to be mined?"
  read searchdir
else
  searchdir=$1
fi
echo "Start mining on ${searchdir}"
python3 src/ast_analysis.py ${searchdir} -wv