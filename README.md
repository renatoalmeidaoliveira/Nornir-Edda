# Nornir-Edda

This repository implements the architecture proposed on [A Network Programmability Essay](https://www.linkedin.com/pulse/network-programmability-essay-renato-oliveira/). Which aims the following problems:
* Abstraction of multiple vendors syntax in a single data model;
* Decoupling of input data and configuration logic;
* Single entry point for the configuration deploy;
* Automatic vendor logic selection;

## Requirements
* Python 3.6.2 or higher
* git
* virtualenv
* pip
Additional requirements going to be installed automatically with pip
## Installing
```shell
git clone https://github.com/renatoalmeidaoliveira/Nornir-Edda.git
cd Nornir-Edda/
virtualenv .
source bin/activate
pip install -r requirements.txt  
```
## Repository Structure 
    .
    ├── controllers						# Controllers folder
    │   ├── Controller.py				# Controller Abstract Class
    │   ├── Fabric.py					# Controller Fabric
    │   ├── ios							# ios vendor Controller folder
    │    │   ├── iosController.py		# ios Controller
    │    │   ├── templates				# ios Jinja2 template
    │    │    │   ├── interfaces.j2		# ios Interfaces template
    ├── models							# Models folder
    │   ├── Model.py					# Model abstract Class
    │   ├── interface.py				# Interface concrete Class
    │   ├── interfaces.py				# Interfaces concrete Class
    ├── data							# Hosts data files
    │   ├──cisco						# Device with hostname cisco data folder
    │    │   ├── interfaces.yaml		# interfaces data model
    │   ├──mikro						# Device with hostname mikro data folder
    │    │   ├── interfaces.yaml		# interfaces data model
    ├── defaults.yaml					# Nornir defaults file
    ├── hosts.yaml						# Nornir hosts file
    ├── groups.yaml						# Nornir groups file
    ├──main.py							# Sample python scrips
    ├──requirements.txt					# Python pip requirements
    ├──NOTICE							# License Notice
    └── README.md						# Readme file

## Getting started
In this version only interfaces model for Cisco IOS, HP ComWare and MikroTik Routeos were implemented. 
For testing this repository follow the steps bellow:
* Edit hosts.yaml file to suit your scenario
* Create one folder for each host in your hosts.yml, in the data folder, where the folder name is the hostname, e.q ./data/hostname/
* For each host create an interfaces.yaml with the desired configuration
* Run main.py

## Extending the models
If you want to deploy different models, follow the steps bellow:
* Create a concrete class of the Model abstract model that will receive the data and output in some standard form
* Implement the getModel() method that MUST be the same name of the Jinja2 template
* Implement the getModelData() method that will return the data used by the Jinja2 template
* For each vendor create the appropriate Jinja2 template with the same name returned by getModel(), i.e, f”{getModel()}.j2}” 
* Edit main.py to read the data model
