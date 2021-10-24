#!/bin/sh

source venv/bin/activate

cd src/
python main.py

cd ..
deactivate
