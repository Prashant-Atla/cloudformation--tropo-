SHELL := /bin/bash

Run:
	apt-get install -y python-pip
	mkdir deps/
	pip install \
		-r make_requirements.txt \
		--target dependencies/

	python template_creator.py generate --config-file template_config.yaml

