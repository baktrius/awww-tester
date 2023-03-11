#!/bin/bash

# setting default value of expected environmental variables
export PROJECT_PATH="${PROJECT_PATH:-../grader/project}"
export REPORT="${REPORT:-0}"

# seting cwd to itself
cd "${0%/*}"

# activating python virtualenv
source .venv/bin/activate

echo "Running pytest tests suite"
pytest pytests --capture=sys
