# MyPy Example Repo
Hey, this is an example repo that will maybe help you get MyPy integrated into your own code base :)

### What is MyPy?
[MyPy](https://github.com/python/mypy) is an optional static type checker for Python.

To understand what MyPy is and why it's awesome, I recommend you [check out the README](https://github.com/python/mypy#what-is-mypy).

## How to run this
#### Quick setup
In termimnal, cd into this repo's directory and run
```
./quick_setup.sh
```
and answer the prompts.  This will install some dependencies (python3, virtualenv, autoenv), create a virtualenv, and then install pip dependencies into that virtualenv.

It will also give you the option to install [autoenv](https://github.com/kennethreitz/autoenv), which is a really handy tool for automatically activating your python virtualenv when you `cd` into a directory.

## Description of Files
#### [mypy.ini](/mypy.ini)
The mypy configuration file.  [Read about how to configure your mypy here.](http://mypy.readthedocs.io/en/stable/config_file.html)

#### [tox.ini](/tox.ini)
The tox config file.  We use [tox](https://tox.readthedocs.io/en/latest/) for testing in this repo.

To run `tox` simply run
```
tox
```
and it will run your tests in fancy isolated test environments.

#### [requirements.txt](/requirements.txt)
Our pip dependencies file.  This file includes any python packages you need in order to run this jawn.  It also specifies Mypy as a dependency.
