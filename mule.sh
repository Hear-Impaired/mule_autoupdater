#!/bin/bash

FILENAME=temp_file

cd /root/github_repository/python_study;

if [ -f ${FILENAME} ]; then    
    /bin/python3 /root/github_repository/python_study/main.py polarisr gusxjf85!
    rm /root/github_repository/python_study/${FILENAME}
else
    /bin/python3 /root/github_repository/python_study/main.py polarisr1 gusxjf85
    touch /root/github_repository/python_study/${FILENAME}
fi