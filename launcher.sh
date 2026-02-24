#!/usr/bin/env bash

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"


if [ ! -d $SCRIPT_DIR/env ]; then
	echo "Installing dependencies for the first launch..."
	python3.12 -m venv $SCRIPT_DIR/env
	source $SCRIPT_DIR/env/bin/activate
	pip install -r $SCRIPT_DIR/requirements.txt
fi
source $SCRIPT_DIR/env/bin/activate
python $SCRIPT_DIR/src/main.py
