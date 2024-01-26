# Summary

api end points for automation

## Pre-requisites

1. python 3.11.6

## Starting The Service

1. Clone repo

    `git clone https://github.com/smetroid/tools.git`

1. Change into tools directory

    `cd tools`

1. Create the virtual environment

    `python -m venv .venv`

1. Source the virtual env

    `source .venv/bin/activate`

1. Install python packages

    `pip install -r requirements.txt`

1. Start the flask app

    `waitress-serve 'tools:tools'`

## Usage

1. Shortening a url using curl

    ```
    curl --header "Content-Type: application/json" -X POST localhost:8080/encode --data '{"url": ""}'
    ```

    Result:

    ```
    {"id":"4LoFSC","return":""}
    ```

2. Retrieving original URL using the id above

    ```
    curl --header "Content-Type: application/json" -X POST localhost:5000/decode --data '{"id": "rcj3GA"}'
    ```

    Result:

    ```
    {"id":"4LoFSC","original_url":""}
    ```

## Running Development Environment

1. Export the apps

    `export FLASK_APP=tools.py`

1. Start development server

    `flask run`

1. Running tests

    `pytest`

## VSCode Debug HowTo

I've included my `.vscode/settings`  which includes a `launch.json` file which you can use to run the VSCode debugger.  It may need to be updated based on your Operating System.
