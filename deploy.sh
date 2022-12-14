#!/bin/bash

# commands to be run when new version of app is re-deployed

# upgrade pip
pip install --upgrade pip

# install packages
pip install -r requirements.txt