#!/bin/bash

SYSTEMD_NAME=$1
SYSTEMD_PATH=/etc/systemd/system

SERVICE=$SYSTEMD_NAME-webhook.service
SERVICE_FILE_FULL=$SYSTEMD_PATH/$SERVICE

REPOSITORY_PATH=/etc/$SYSTEMD_NAME_webook

if [[ ! -d $REPOSITORY_PATH ]]
then
    mkdir -p $REPOSITORY_PATH
fi

cp -rf call_to_hook perpetrator scripts utilities main.py $REPOSITORY_PATH/

if [[ ! -f $SERVICE_FILE_FULL ]]
then
    cp bitbucket-webhook.service $SERVICE_FILE_FULL
    systemctl daemon-reload
    systemctl enable $SERVICE
    systemctl restart $SERVICE
    echo "Installation/Update Complete"
else
    echo "File exists"
fi
