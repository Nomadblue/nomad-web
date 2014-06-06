=========
Nomad-web
=========

The website for Nomadblue.com - Yout CTO on-demand.

Requirements
============

In order to work with LESS, we will need to add the new generated CSS files
each time we want to commit changes to our repository. To compile LESS files,
we use the command line tool provided as a Node.js NPM.

Installation instructions for OS X under Homebrew::

    brew install npm
    npm install -g less

We use Twitter Bootstrap. We will be joining its ``.less`` files together with
our own ones to produce a single ``styles.css``. This way we can override the
bootstrap variables. Clone the twitter bootstrap repo to a place outside
the repository::

    git clone https://github.com/twbs/bootstrap.git

Installation
============

Check out the source::

    git clone git@github.com:Nomadblue/nomad-web.git

Create virtual environment::

    mkvirtualenv nomadweb

Jump into project folder and install requirements::

    pip install -r requirements.txt
    pip install -r requirements_dev.txt

Copy the following files and follow their instructions inside to
edit them (the copied files, not the "_sample" ones!!!!)::

    cp conf/env_sample .env
    cp conf/localsettings_sample.py ahorramos/localsettings.py
    cp conf/imports.less website/static/less/
    vim .env
    vim nomadweb/localsettings.py
    vim website/static/less/imports.less

Run the reset script corresponding to your db (sqlite or postgres)::

    ./scripts/reset_sqlite_db.sh

Start devel webserver and visit ``http://localhost:8000/``::

    python manage.py runserver

Development
===========

Translations
------------

To update the translations, run ``makemessages`` and edit the new ``.po`` files with an editor like Poedit_::

    ./manage.py makemessages -l es
    open locale/es/LC_MESSAGES/django.po 

.. _Poedit:: http://poedit.net/

Remember to change the symlink names to clean up after yourself
and avoid clashing with the library imports::

    mv nomadblog nomadblog_symlink
    mv base_accounts base_accounts_symlink

LESS to CSS
===========

Project is deployed with CSS already compiled from LESS files. So do not
forget to run ``lessc`` before commiting changes to the repository,
otherwise deployments will miss them::

    lessc website/static/less/imports.less > website/static/css/styles.css
