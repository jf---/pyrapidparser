#!/bin/bash
cd ..

env python python rapid2py.py -i Pallettizer/schema.mod -s -f schema.py
env python rapid2py.py -e MAIN -i Pallettizer/settings.mod -i Pallettizer/gloadschema.mod -i Pallettizer/schema.mod -i Pallettizer/maintask.mod -f pallettizer.py -r
