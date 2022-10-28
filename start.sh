#!/bin/sh

#####################################################################
#
# script name: start.sh
# created in: 21/19/22
# modified in: 09:14:41
#
# summary: inicia o projeto de ia do machado de assis
#                                               developed by: bates
#####################################################################

#variables
DATE=$(date)

if [ $?  -eq 0 ]
then
    clear
    echo "Checking dependencies"
    sleep 1
    if source env/env.sh
    then
        pip install --upgrade pip > /dev/null
        pip3 install -r env/requeriments.txt --upgrade > /dev/null
        sleep 1
        echo "Running the scripts"
        sleep 1
        python3 script/main.py 2> /dev/null
    else
        echo "Something went wrong"
        fi
else
    echo "You ran the program wrong!"
fi



