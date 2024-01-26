# Summary

api end points for automation

## Pre-requisites

1. python 3.11.6

## Starting The Service

1. Clone repo

    `git clone https://github.com/smetroid/python-tools.git`

1. Change into tools directory

    `cd python-tools`

1. Create the virtual environment

    `python -m venv .venv`

1. Source the virtual env

    `source .venv/bin/activate`

1. Install python packages

    `pip install -r requirements.txt`

1. Start the flask app

    `waitress-serve 'tools:tools'`

## Usage

## Running Development Environment

1. Export the apps

    `export FLASK_APP=tools.py`

1. Start development server

    `flask run`

1. Running tests

    `pytest`

## VSCode Debug HowTo

I've included my `.vscode/settings`  which includes a `launch.json` file which you can use to run the VSCode debugger.  It may need to be updated based on your Operating System.

