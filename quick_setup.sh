#!/usr/bin/env bash
#
# setup.sh
# Written by Mark Koh
# 2/24/2017
#
# This script will install apt-get and brew dependencies as well as install autoenv
# which will automatically activate your virtual environment when you `cd` into this directory.
#
# Feel free to update this file with your own os-level dependencies :)

# See if we have either brew or apt-get installed
BREW_CMD=$(which brew)
APT_CMD=$(which apt-get)

if [[ ! -z $BREW_CMD ]]; then
    # What to install with `brew`
    echo "Installing brew dependencies...";
    brew install --upgrade python3

elif [[ ! -z $APT_CMD ]]; then
    # What to install with `apt-get`
    echo "Installing python3...";

    sudo apt-get install -y python3 python3-pip

else
    echo "Neither brew nor apt-get are installed.  Exiting..."
    exit 1;
fi

echo "Installing virtualenv...";
pip3 install virtualenv

echo "Checking for autoenv installation...";
pip3 freeze | grep -q  autoenv
autoenv_installed=$?
if [ ! ${autoenv_installed} -eq 0 ]
then
    read -r -p "Autoenv will automatically activate this virtualenv when you 'cd' into the directory.  Do you want to install autoenv? [y/n] " response
    if [[ "$response" =~ ^([yY][eE][sS]|[yY])+$ ]]
    then
        pip3 install autoenv

        read -p "Bash startup file [~/.bashrc]: " BASHRC
        BASHRC=${BASHRC:-~/.bashrc}
        BASHRC_ABS=`eval echo ${BASHRC//>}`

        # Check if their bash file has autoenv activated in it, if not, see if they want to add it
        if ! grep -q "activate.sh" $BASHRC_ABS ; then
            echo "Adding autoenv to $BASHRC...";
            echo "# Activate autoenv" >> $BASHRC_ABS
            echo "source `which activate.sh`" >> $BASHRC_ABS
            echo "cd ." >> $BASHRC_ABS
        fi
    fi
else
    echo "Autoenv already installed.";
fi

VENV=.venv

# Create the actual virtualenv
if [ ! -d $VENV ]; then
    echo "Creating virtual env..."
    virtualenv -p python3 $VENV
fi

# If we have a requirements file, install them reqs
if [ -f requirements.txt ]; then
    echo "Installing pip requirements..."
    source $VENV/bin/activate
    pip3 install -r requirements.txt
fi

if [ ! -z "${BASHRC}" ]; then
    echo "
    Please run
      source $BASHRC

    "
else
    echo "
    To activate your virtualenv, please run
        source $VENV/bin/activate

    ";
fi
