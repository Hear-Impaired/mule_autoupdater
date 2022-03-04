#!/bin/bash

FILENAME=temp_file

cd /root/github_repository/mule_autoupdater;

if [ -f ${FILENAME} ]; then
    /bin/python3 /root/github_repository/mule_autoupdater/main.py polarisr gusxjf85!@
    rm /root/github_repository/mule_autoupdater/${FILENAME}
else
    /bin/python3 /root/github_repository/mule_autoupdater/main.py polarisr1 gusxjf85!@
    touch /root/github_repository/mule_autoupdater/${FILENAME}
fi
