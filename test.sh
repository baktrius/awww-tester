#!/bin/bash

# setting default value of expected environmental variables
PROJECT_PATH="${PROJECT_PATH:-../moje1}"
REPORT="${REPORT:-1}"

# seting cwd to itself
cd "${0%/*}"

# activating python virtualenv
source .venv/bin/activate

echo "Running pytest tests suite"
pytest pytests

echo "Validating html files using html-validate"
npx html-validate $PROJECT_PATH/**/*.htm $PROJECT_PATH/**/*.html
