#!/bin/bash
echo 'pull project:'$1
gitBasePath='/home/gitBase/'
cd $gitBasePath$1
git pull