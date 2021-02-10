#!/bin/sh -l

echo "EXECUTING PYTHON SCRIPT..."
python3 /main.py ${INPUT_FIRSTPARAM} ${INPUT_SECONDPARAM}

echo "ls -lah"
ls -lah

echo "pwd"
pwd

echo "ls -lah /github/workspace"
ls -lah /github/workspace
