votainteligente-portal-electoral
================================

[![Build Status](https://travis-ci.org/ciudadanointeligente/votainteligente-portal-electoral.png?branch=master)](https://travis-ci.org/ciudadanointeligente/votainteligente-portal-electoral)
[![Coverage Status](https://coveralls.io/repos/ciudadanointeligente/votainteligente-portal-electoral/badge.png?branch=master)](https://coveralls.io/r/ciudadanointeligente/votainteligente-portal-electoral?branch=master)

Votainteligente the electoral platform that Fundación Ciudadano Inteligente uses to transparent the electoral positions of different candidates to an election.

#Installation

VotaInteligente depends on 3 parts candideit.org, popit and write-it. You might choose to use all of them or just part. In the following document it is described how to install.

## Assumptions

This guide was made using an ubuntu 13.10 just installed.

## Requirements

Before the installation process is started a number of requirements is needed

- [virtualenv](https://pypi.python.org/pypi/virtualenv)
- [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)
- [Git](http://git-scm.com/)
- The requirements that [sorl-thumbnail has](http://sorl-thumbnail.readthedocs.org/en/latest/requirements.html)

Anyway, this command should install all you need:

`sudo apt-get install virtualenv virtualenvwrapper python git g++ imagemagick`

## Installation process

* Clone votainteligente somewhere in your system.

`git clone https://github.com/YoQuieroSaber/votainteligente-portal-electoral.git`

Enter the installation directory

`cd votainteligente-portal-electoral`

* Create a virtual environment

`virtualenv votainteligente`

* Activate your virtual environment

`source votainteligente/bin/activate`

* Install the requirements that votainteligente needs in the current virtualenvironment

`pip install -r requirements.txt`

It might take some time to get all installed

* Create the database and tables.

`python manage.py syncdb`

Update the tables with migrations

`python manage.py migrate`

## Theming

### Previously created themes

* [votainteligente-venezuela-theme](https://github.com/ciudadanointeligente/votainteligente-venezuela-theme) is the theme for [eligetucandidato.org](http://eligetucandidato.org/)
* [votai-theme](https://github.com/YoQuieroSaber/votai-theme) is the theme for the YoQuieroSaber.org Argentinian gamified instance.


### Creating your own custom theme

If you want to create a new theme you have to create a directory containing two different subdirectories templates and static, and copy the templates that you want to replace.

And in your project in your local_settings.py file you have to add the following

```
 STATICFILES_DIRS = (
     '/full/path/to/your/theme/static/',
 )
 TEMPLATE_DIRS = (
     '/full/path/to/your/theme/templates/',
 )
```

## Localization

If you want to help us translate votainteligente please join our project in [poeditor.com](https://poeditor.com/join/project?hash=6a3a384490bd4d69669db94c1cc22d78)

## Licensing

VotaInteligente is free and released as open source software covered by the terms of the [GNU Public License](http://www.gnu.org/licenses/gpl-3.0.html) (GPL v3)
