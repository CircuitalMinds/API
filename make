#!/usr/bin/env bash


Opt=$1
Venv=./venv/bin/activate
Reqs=./requirements.txt


function InstallApp () {

    if ! [ -f $Venv ]; then
        virtualenv venv
    fi

    if [[ -f $Reqs ]]; then
        source $Venv && pip install -r $Reqs
    fi

}


function RunApp () {
    
    source $Venv && python3 app.py
    
}


if [[ $Opt == "install" ]]; then

    (InstallApp)

elif [[ $Opt == "app" ]]; then

    (RunApp)

fi
