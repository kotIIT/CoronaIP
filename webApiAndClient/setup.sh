#!/usr/bin/env bash

Install_Config(){
	sudo apt install python3 npm -y
	python3.7 -m pip install -U pip pipenv
	pipenv install
  Start_Config
}

Start_Config(){
  export FLASK_APP=app.py
  python3 -m pipenv shell flask run --host=0.0.0.0

}

Menu(){
echo "1 or i to Install Requirements"
echo "2. or s  to start server"
}

arg=$1
Output()
{
  case $arg in

    1 | "i") Install_Config;;
    2 | "s" ) Start_Config;;
    *) Menu;;
  esac
}

Output