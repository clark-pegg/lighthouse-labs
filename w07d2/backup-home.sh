#!/bin/bash

rm -rf /home/backup/*
rsync -av --exclude=".*" /home/clark /home/backup
