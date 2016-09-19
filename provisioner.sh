#!/bin/bash

# vagrant ssh
sudo su root
sudo apt-key update
sudo apt-get update

sudo apt-get install build-essential libssl-dev libcurl4-gnutls-dev libexpat1-dev gettext unzip
echo Y | sudo apt-get install git

# install python tools
echo Y | sudo apt-get install python-pip python-dev
yes | sudo pip install --upgrade pip 
yes | sudo pip install --upgrade virtualenv

# install python libraries
yes | sudo pip install numpy

sudo pip install pandas

sudo apt-get install libatlas-base-dev gfortran
wget https://pypi.python.org/packages/13/cb/8e74d28e1519b34636e4d985d49d01c23778064e01eb102914f844cd6051/scipy-0.18.1-cp27-cp27mu-manylinux1_x86_64.whl#md5=8819378eceb1d7a51042031a7846f394
pip install scipy-0.18.1-cp27-cp27mu-manylinux1_x86_64.whl

yes | sudo pip install scikit-learn

# install xgboost
sudo git clone --recursive https://github.com/dmlc/xgboost
cd xgboost; make; cd python-package; python setup.py install

pip install psutil

cd /home/vagrant
sudo git clone --recursive https://github.com/jhabib/loadrunner
cd loadrunner
