#!/bin/bash

# setting default value of expected environmental variables
PROJECT_PATH="${PROJECT_PATH:-../moje1}"

echo "Validating html files using html-validate"
npx html-validate $PROJECT_PATH/*.htm $PROJECT_PATH/*.html

echo "Running pytest tests suite"
pytest pytests
