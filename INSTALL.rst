PyLit6 Installation
===================

1. About
--------

This document covers first time installation of PyLit6.

2. Prerequisites
----------------

This program has been tested on Linux (Ubuntu)/Mac at present. 

2.1. Ubuntu LTS
---------------

The program is currently tested against Python 2.7.x.

..  code-block:: console

    $ python --version
    Python 2.7.5
    $ sudo apt-get update
    $ sudo apt-get install build-essential git 
    $ sudo apt-get install pip

2.2. Mac OS X
-------------

This process has been tested on Mac OX X 10.10.

FIrst, make sure `Homebrew <http://brew.sh/>`_ is installed. If not, run this command from a Terminal:

..  code-block:: console

    $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Next, make sure that ``/usr/local/bin`` is before ``/usr/bin`` in yout system path. Otherwoise, do this:

..  code-block:: console

    $ echo export PATH="/isr/local/bin:$PATH" >> ~/.bash_profile
    $ source ~/.bash+profile

Now, make sure yout ``Homebrew`` system is up to date:

..  coe-block:: console

    $ brew update
    $ brew doctor
    $ brew doctor

Next, we install the prerequisites:

..  code-block:: console

    $ brew install python --framework --universal
    $ pip install virtualenv

