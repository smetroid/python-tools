SHELL=/bin/bash
venv_dir=.venv
activate = ${venv_dir}/bin/activate



setup-venv:
	(test -d ${venv_dir} || python -m venv ${venv_dir})
	. ${activate}; pip install -r requirements.txt;

activate:
	. ${activate}

run-test: activate
	pytest

run-dev: activate
	export FLASK_APP=tools.py; flask run

run-prod: activate
	waitress-serve 'tools:tools'

