#!/usr/bin/env make -s -f
# Copyright © 2017 Spotify AB

#############################################################################
# Configuration
#############################################################################

HERE = $(shell pwd)
VENV = $(HERE)/.venv

APP_VERSION ?= $(shell cat version.txt)
APP_ROOT = $(HERE)/mypy_example

PYTHON = PYTHONPATH=$(APP_ROOT) python3
PIP = pip3

default: test

###########################################
# Install
###########################################
install: requirements.txt
	$(PIP) install -r requirements.txt

###########################################
# Runners
###########################################
test:
	tox

###########################################
# Cleanup
###########################################
clean:
	find . -name "*.pyc" -print0 | xargs -0 rm
