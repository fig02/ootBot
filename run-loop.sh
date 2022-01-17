#!/bin/bash

trap "echo Exited!; exit;" SIGINT

while :
do
	python3 ./ootBot.py
done
