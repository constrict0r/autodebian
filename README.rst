
autodebian
**********

.. image:: https://readthedocs.org/projects/autodebian/badge
   :alt: readthedocs

Automated Debian-like systems setup monolith repository.

.. image:: https://gitlab.com/constrict0r/img/raw/master/autodebian/autodebian.png
   :alt: autodebian

Full documentation on `Readthedocs
<https://autodebian.readthedocs.io>`_.

Source code on:

`Github <https://github.com/constrict0r/autodebian>`_.

`Gitlab <https://gitlab.com/constrict0r/autodebian>`_.

`Part of: <https://gitlab.com/explore/projects?tag=doombots>`_

.. image:: https://gitlab.com/constrict0r/img/raw/master/autodebian/doombots.png
   :alt: doombots

**Ingredients**

.. image:: https://gitlab.com/constrict0r/img/raw/master/autodebian/ingredients.png
   :alt: ingredients


Contents
********

* `Usage <#Usage>`_
* `Components <#Components>`_
   * `aptitude <#aptitude>`_
   * `basik <#basik>`_
   * `constructor <#constructor>`_
   * `desktop <#desktop>`_
   * `develbase <#develbase>`_
   * `develmicro <#develmicro>`_
   * `develpy <#develpy>`_
   * `devels <#devels>`_
   * `groups <#groups>`_
   * `home <#home>`_
   * `iso <#iso>`_
   * `jsnode <#jsnode>`_
   * `kick <#kick>`_
   * `latveria <#latveria>`_
   * `madvillain <#madvillain>`_
   * `pyp <#pyp>`_
   * `servicez <#servicez>`_
   * `sourcez <#sourcez>`_
   * `sysconfig <#sysconfig>`_
   * `task <#task>`_
   * `unify <#unify>`_
   * `upgrade <#upgrade>`_
   * `userconfig <#userconfig>`_
   * `users <#users>`_
* `License <#License>`_
* `Links <#Links>`_
* `UML <#UML>`_
   * `Deployment <#deployment>`_
* `Author <#Author>`_

Usage
*****

Clone the repository and its submodules:

::

   git clone --recurse-submodules -j8 git://gitlab.com/constrict0r/autodebian.git


Components
**********

This repository includes the following components:


aptitude
========

Ansible role to use as a wrapper for apt to manage packages.

This role performs the following actions:

* Ensure the requirements are installed.

* Ensure the current user can obtain administrative (root)
   permissions.

* Update the apt cache.

* If the **packages_purge** variable is defined, purge the packages
   listed on it.

* If the **configuration** variable is defined, purge the
   *packages_purge* listed on it.

* If the **packages** variable is defined, install the packages
   listed on it.

* If the **configuration** variable is defined, install the packages
   listed on it.

Documentation on `aptitude readthedocs
<https://aptitude.readthedocs.io>`_.

Code on `aptitude Gitlab <https://gitlab.com/constrict0r/aptitude>`_.

Code on `aptitude Github <https://github.com/constrict0r/aptitude>`_.

.. image:: https://gitlab.com/constrict0r/img/raw/master/autodebian/aptitude.png
   :alt: aptitude


basik
=====

Ansible role to setup basic Debian-like systems.

This is capable of:

* Upgrade the system.

* Add `apt <https://wiki.debian.org/Apt>`_ repository sources.

* Update the apt cache.

* Uninstall apt packages.

* Install apt packages.

* Install `npm <http://npmjs.org/>`_ packages.

* Install `pip <https://pypi.org/project/pip/>`_ packages.

* Apply system-wide configuration using git.

* Stop services and disable them.

* Enable services and restart them.

* Create users.

* Add users to groups.

* Apply user-wide configuration using git.

* Run custom user tasks.

By default this role applies the following configuration:

* Installs the software:

..

   * apt-transport-https

   * bzip2

   * ca-certificates

   * curl

   * sudo

   * unrar-free

   * unzip

   * vim

   * wget

   * xz-utils

* Configures the following software:

..

   * vim

   ..

      * Creates a *.vimrc* configuration file on each user home
         directory.

      * Enable syntax highlight.

      * Set two spaces instead of tabs.

Documentation on `basik readthedocs <https://basik.readthedocs.io>`_.

Code on `basik Gitlab <https://gitlab.com/constrict0r/basik>`_.

Code on `basik Github <https://github.com/constrict0r/basik>`_.

.. image:: https://gitlab.com/constrict0r/img/raw/master/autodebian/basik.png
   :alt: basik


constructor
===========

Ansible role to setup Debian-like systems.

This is capable of:

* Upgrade the system.

* Add `apt <https://wiki.debian.org/Apt>`_ repository sources.

* Update the apt cache.

* Uninstall apt packages.

* Install apt packages.

* Install `npm <http://npmjs.org/>`_ packages.

* Install `pip <https://pypi.org/project/pip/>`_ packages.

* Apply system-wide configuration using git.

* Stop services and disable them.

* Enable services and restart them.

* Create users.

* Add users to groups.

* Apply user-wide configuration using git.

* Run custom user tasks.

Documentation on `constructor readthedocs
<https://constructor.readthedocs.io>`_.

Code on `constructor Gitlab
<https://gitlab.com/constrict0r/constructor>`_.

Code on `constructor Github
<https://github.com/constrict0r/constructor>`_.

.. image:: https://gitlab.com/constrict0r/img/raw/master/autodebian/basik.png
   :alt: basik


desktop
=======

Ansible role to setup Debian-like systems desktop configuration.

This is capable of:

* Upgrade the system.

* Add `apt <https://wiki.debian.org/Apt>`_ repository sources.

* Update the apt cache.

* Uninstall apt packages.

* Install apt packages.

* Install `npm <http://npmjs.org/>`_ packages.

* Install `pip <https://pypi.org/project/pip/>`_ packages.

* Apply system-wide configuration using git.

* Stop services and disable them.

* Enable services and restart them.

* Create users.

* Add users to groups.

* Apply user-wide configuration using git.

* Run custom user tasks.

By default this role applies the following configuration:

* Installs the base software:

..

   * apt-transport-https

   * bzip2

   * ca-certificates

   * curl

   * sudo

   * unrar-free

   * unzip

   * vim

   * wget

   * xz-utils

* Installs the desktop software:

..

   * audacity

   * easytag

   * ffmpeg

   * gedit

   * gimp

   * gnome

   * gparted

   * inkscape

   * kdenlive

   * keepassx

   * obs-studio

   * rhythmbox

   * vlc

* Configures the base software:

..

   * vim

   ..

      * Creates a *.vimrc* configuration file on each user home
         directory.

      * Enable syntax highlight.

      * Set two spaces instead of tabs.

* Configures the desktop software:

..

   * emacs

   ..

      * Creates a *.emacs.d* configuration folder on each user home
         directory.

      * Enable line numbers.

      * Set themes folder.

      * Set wintermute theme.

      * Use spaces instead of tabs.

Documentation on `desktop readthedocs
<https://desktop.readthedocs.io>`_.

Code on `desktop Gitlab <https://gitlab.com/constrict0r/desktop>`_.

Code on `desktop Github <https://github.com/constrict0r/desktop>`_.

.. image:: https://gitlab.com/constrict0r/img/raw/master/autodebian/desktop.png
   :alt: desktop


develbase
=========

Ansible role to apply basic developer configuration.

This is capable of:

* Upgrade the system.

* Add `apt <https://wiki.debian.org/Apt>`_ repository sources.

* Update the apt cache.

* Uninstall apt packages.

* Install apt packages.

* Install `npm <http://npmjs.org/>`_ packages.

* Install `pip <https://pypi.org/project/pip/>`_ packages.

* Apply system-wide configuration using git.

* Stop services and disable them.

* Enable services and restart them.

* Create users.

* Add users to groups.

* Apply user-wide configuration using git.

* Run custom user tasks.

By default this role applies the following configuration:

* Installs the base software:

..

   * apt-transport-https

   * bzip2

   * ca-certificates

   * curl

   * sudo

   * unrar-free

   * unzip

   * vim

   * wget

   * xz-utils

* Installs the base developer software:

..

   * bats

   * emacs

   * git

   * libtext-csv-perl

   * make

   * meld

   * retext

   * ssh-askpass

   * tree

* Configures the base software:

..

   * vim

   ..

      * Creates a *.vimrc* configuration file on each user home
         directory.

      * Enable syntax highlight.

      * Set two spaces instead of tabs.

Documentation on `develbase readthedocs
<https://develbase.readthedocs.io>`_.

Code on `develbase Gitlab
<https://gitlab.com/constrict0r/develbase>`_.

Code on `develbase Github
<https://github.com/constrict0r/develbase>`_.

.. image:: https://gitlab.com/constrict0r/img/raw/master/autodebian/develbase.png
   :alt: develbase


develmicro
==========

Ansible role to apply microcontroller developer configuration.

This is capable of:

* Upgrade the system.

* Add `apt <https://wiki.debian.org/Apt>`_ repository sources.

* Update the apt cache.

* Uninstall apt packages.

* Install apt packages.

* Install `npm <http://npmjs.org/>`_ packages.

* Install `pip <https://pypi.org/project/pip/>`_ packages.

* Apply system-wide configuration using git.

* Stop services and disable them.

* Enable services and restart them.

* Create users.

* Add users to groups.

* Apply user-wide configuration using git.

* Run custom user tasks.

By default this role applies the following configuration:

* Installs the base software:

..

   * apt-transport-https

   * bzip2

   * ca-certificates

   * curl

   * sudo

   * unrar-free

   * unzip

   * vim

   * wget

   * xz-utils

* Installs the base developer software:

..

   * bats

   * emacs

   * git

   * libtext-csv-perl

   * make

   * meld

   * retext

   * ssh-askpass

   * tree

* Installs the microcontroller developer software:

..

   * Via apt:

   ..

      * clang

      * fritzing

      * fritzing-data

      * fritzing-parts

      * python3

      * python3-pip

   * Via pip:

   ..

      * platformio

* Configures the base software:

..

   * vim

   ..

      * Creates a *.vimrc* configuration file on each user home
         directory.

      * Enable syntax highlight.

      * Set two spaces instead of tabs.

* Configures the base developer software:

..

   * emacs

   ..

      * Creates a *.emacs.d* configuration folder on each user home
         directory.

      * Enable line numbers.

      * Set themes folder.

      * Set wintermute theme.

      * Use spaces instead of tabs.

* Configures the microcontroller developer software:

..

   * emacs

   ..

      * Set `platformio plugin <https://is.gd/8HIcsb>`_ plugin.

      * Set keybindings:

      ..

         * C-c i b: Build the project without auto-uploading.

         * C-c i c: Clean compiled objects.

         * C-c i u: Build and upload.

   * groups - Adds users to the groups:

      * dialout.

   * udev - Adds the rules file
      */etc/udev/rules.d/99-platformio-udev.rules*.

* Creates the following home directory layout:

..

   ::

      home/
      ├── .emacs.d
      │   ├── config
      │   │   ├── base.el
      │   │   ├── micro.el
      |   │   └── org.el
      │   ├── init.el
      │   └── themes
      │       └── wintermute-theme.el
      └── .vimrc

* Modifies the following files:

..

   ::

      home/
      ├── .bashrc
      └── .profile

Documentation on `develmicro readthedocs
<https://develmicro.readthedocs.io>`_.

Code on `develmicro Gitlab
<https://gitlab.com/constrict0r/develmicro>`_.

Code on `develmicro Github
<https://github.com/constrict0r/develmicro>`_.

.. image:: https://gitlab.com/constrict0r/img/raw/master/autodebian/develmicro.png
   :alt: develmicro


develpy
=======

Ansible role to apply python developer configuration.

This is capable of:

* Upgrade the system.

* Add `apt <https://wiki.debian.org/Apt>`_ repository sources.

* Update the apt cache.

* Uninstall apt packages.

* Install apt packages.

* Install `npm <http://npmjs.org/>`_ packages.

* Install `pip <https://pypi.org/project/pip/>`_ packages.

* Apply system-wide configuration using git.

* Stop services and disable them.

* Enable services and restart them.

* Create users.

* Add users to groups.

* Apply user-wide configuration using git.

* Run custom user tasks.

By default this role applies the following configuration:

* Installs the base software:

..

   * apt-transport-https

   * bzip2

   * ca-certificates

   * curl

   * sudo

   * unrar-free

   * unzip

   * vim

   * wget

   * xz-utils

* Installs the base developer software:

..

   * bats

   * emacs

   * git

   * libtext-csv-perl

   * make

   * meld

   * retext

   * ssh-askpass

   * tree

* Installs the python developer software:

..

   * Via apt:

   ..

      * direnv

      * python3

      * python3-pip

      * python3-pytest

      * python3-venv

      * python3-virtualenv

      * tox

   * Via pip:

   ..

      * ansible-lint

      * autopep8

      * flake8

      * jedi

      * poetry

      * sphinx

      * sphinx_rtd_theme

      * rope

      * yapf

* Configures the base software:

..

   * vim

   ..

      * Creates a *.vimrc* configuration file on each user home
         directory.

      * Enable syntax highlight.

      * Set two spaces instead of tabs.

* Configures the base developer software:

..

   * emacs

   ..

      * Creates a *.emacs.d* configuration folder on each user home
         directory.

      * Enable line numbers.

      * Set themes folder.

      * Set wintermute theme.

      * Use spaces instead of tabs.

* Configures the python developer software:

..

   * direnv

   ..

      * Enable *direnv* command on *~/.bashrc* file.

   * emacs

   ..

      * Set `elpy <https://is.gd/tPU9gM>`_ plugin.

      * Set `tox.el <https://is.gd/hUqDMw>`_ plugin.

      * Set keybindings:

      ..

         * C-c C-c: Evaluates the current script.

         * C-RET (Enter): Evaluates the curren statement (current
            line plus the
               following nested line).

         * C-c C-z: Switches between your script and the interactive
            shell.

         * C-c C-d: Displays documentation for the thing under cursor
            (function or module). The documentation will pop in a
            different buffer, can be closed with *q*.

         * C-c C-t: Run pytest tests.

         * M-x tox-current-test: Run tox tests for current test.

         * M-x tox-current-class: Run tox tests for current class.

         * M-x pdb: Run PDB on a new window.

         * C-x: Set breakpoint on current line.

   * `poetry <https://poetry.eustace.io/>`_

   ..

      * Add poetry path to the *~/.profile* file to maintain
         dependecies aisolated.

   * `python3-virtualenv <https://virtualenv.pypa.io/en/latest/>`_

   ..

      * Enable elpy virtual enviroments on the *~/.bashrc* file.

* Creates the following home directory layout:

..

   ::

      home/
      ├── .emacs.d
      │   ├── base.el
      │   ├── init.el
      │   ├── python.el
      │   └── themes
      │       └── wintermute-theme.el
      └── .vimrc

* Modifies the following files:

..

   ::

      home/
      ├── .bashrc
      └── .profile

Documentation on `develpy readthedocs
<https://develpy.readthedocs.io>`_.

Code on `develpy Gitlab <https://gitlab.com/constrict0r/develpy>`_.

Code on `develpy Github <https://github.com/constrict0r/develpy>`_.

.. image:: https://gitlab.com/constrict0r/img/raw/master/autodebian/develpy.png
   :alt: develpy


devels
======

Ansible role to apply developer configuration.

This is capable of:

* Upgrade the system.

* Add `apt <https://wiki.debian.org/Apt>`_ repository sources.

* Update the apt cache.

* Uninstall apt packages.

* Install apt packages.

* Install `npm <http://npmjs.org/>`_ packages.

* Install `pip <https://pypi.org/project/pip/>`_ packages.

* Apply system-wide configuration using git.

* Stop services and disable them.

* Enable services and restart them.

* Create users.

* Add users to groups.

* Apply user-wide configuration using git.

* Run custom user tasks.

By default this role applies the following configuration:

* Installs the base software:

..

   * apt-transport-https

   * bzip2

   * ca-certificates

   * curl

   * sudo

   * unrar-free

   * unzip

   * vim

   * wget

   * xz-utils

* Installs the base developer software:

..

   * bats

   * emacs

   * git

   * libtext-csv-perl

   * make

   * meld

   * retext

   * ssh-askpass

   * tree

* Installs the python developer software:

..

   * Via apt:

   ..

      * direnv

      * python3

      * python3-pip

      * python3-pytest

      * python3-venv

      * python3-virtualenv

      * tox

   * Via pip:

   ..

      * ansible-lint

      * autopep8

      * flake8

      * jedi

      * poetry

      * sphinx

      * sphinx_rtd_theme

      * rope

      * yapf

* Installs the microcontroller developer software:

..

   * Via apt:

   ..

      * clang

      * fritzing

      * fritzing-data

      * fritzing-parts

      * python3

      * python3-pip

   * Via pip:

   ..

      * platformio

* Configures the base software:

..

   * vim

   ..

      * Creates a *.vimrc* configuration file on each user home
         directory.

      * Enable syntax highlight.

      * Set two spaces instead of tabs.

* Configures the base developer software:

..

   * emacs

   ..

      * Creates a *.emacs.d* configuration folder on each user home
         directory.

      * Enable line numbers.

      * Set themes folder.

      * Set wintermute theme.

      * Use spaces instead of tabs.

* Configures the python developer software:

..

   * direnv

   ..

      * Enable *direnv* command on *~/.bashrc* file.

   * emacs

   ..

      * Set `elpy <https://is.gd/tPU9gM>`_ plugin.

      * Set `tox.el <https://is.gd/hUqDMw>`_ plugin.

      * Set keybindings:

      ..

         * C-c C-c: Evaluates the current script.

         * C-RET (Enter): Evaluates the curren statement (current
            line plus the
               following nested line).

         * C-c C-z: Switches between your script and the interactive
            shell.

         * C-c C-d: Displays documentation for the thing under cursor
            (function or module). The documentation will pop in a
            different buffer, can be closed with *q*.

         * C-c C-t: Run pytest tests.

         * M-x tox-current-test: Run tox tests for current test.

         * M-x tox-current-class: Run tox tests for current class.

         * M-x pdb: Run PDB on a new window.

         * C-x: Set breakpoint on current line.

   * `poetry <https://poetry.eustace.io/>`_

   ..

      * Add poetry path to the *~/.profile* file to maintain
         dependecies aisolated.

   * `python3-virtualenv <https://virtualenv.pypa.io/en/latest/>`_

   ..

      * Enable elpy virtual enviroments on the *~/.bashrc* file.

* Configures the microcontroller developer software:

..

   * emacs

   ..

      * Set `platformio plugin <https://is.gd/8HIcsb>`_ plugin.

      * Set keybindings:

      ..

         * C-c i b: Build the project without auto-uploading.

         * C-c i c: Clean compiled objects.

         * C-c i u: Build and upload.

   * groups - Adds users to the groups:

      * dialout.

   * udev - Adds the rules file
      */etc/udev/rules.d/99-platformio-udev.rules*.

* Creates the following home directory layout:

..

   ::

      home/
      ├── little-lab
      ├── repos
      ├── .emacs.d
      │   ├── config
      │   │   ├── base.el
      │   │   ├── org.el
      │   │   └── python.el
      │   ├── init.el
      │   └── themes
      │       └── wintermute-theme.el
      └── .vimrc

* Modifies the following files:

..

   ::

      home/
      ├── .bashrc
      └── .profile

Documentation on `devels readthedocs
<https://devels.readthedocs.io>`_.

Code on `devels Gitlab <https://gitlab.com/constrict0r/devels>`_.

Code on `devels Github <https://github.com/constrict0r/devels>`_.

.. image:: https://gitlab.com/constrict0r/img/raw/master/autodebian/devels.png
   :alt: devels


groups
======

Ansible role to add users to system groups.

This role performs the following actions:

* Ensure the requirements are installed.

* Ensure the current user can obtain administrative (root)
   permissions.

* If the **users** variable is defined and the **groups** variable is
   defined, add all users to the specified groups.

* If the **configuration** variable is defined, add all users listed
   on it to the specified groups.

Documentation on `groups readthedocs
<https://groups.readthedocs.io>`_.

Code on `groups Gitlab <https://gitlab.com/constrict0r/groups>`_.

Code on `groups Github <https://github.com/constrict0r/groups>`_.

.. image:: https://gitlab.com/constrict0r/img/raw/master/autodebian/groups.png
   :alt: groups


home
====

`Skeleton repository <http://www.linfo.org/etc_skel.html>`_ for
standard user home directory layout.

This repository provides the following file tree layout:

::

   home/
   ├── .emacs.d
   │   ├── config
   │   │   ├── base.el
   │   │   └── org.el
   │   ├── init.el
   │   └── themes
   │       └── wintermute-theme.el
   └── .vimrc

Code on `home Gitlab <https://gitlab.com/constrict0r/home>`_.

Code on `home Github <https://github.com/constrict0r/home>`_.

.. image:: https://gitlab.com/constrict0r/img/raw/master/autodebian/home.png
   :alt: home


iso
===

Ansible role to generate a Linux installer **.iso** file with or
without `preseeding
<https://wiki.debian.org/DebianInstaller/Preseed>`_.

When using preseeding on the generated iso, the questions asked by the
Debian installer during the installation process will be automatically
answered and when the installation process ends, the `kick.sh
<https://gitlab.com/constrict0r/kick>`_ script will be runned to setup
the newly installed system.

Documentation on `iso readthedocs <https://iso.readthedocs.io>`_.

Code on `iso Gitlab <https://gitlab.com/constrict0r/iso>`_.

Code on `iso Github <https://github.com/constrict0r/iso>`_.

.. image:: https://gitlab.com/constrict0r/img/raw/master/autodebian/iso.png
   :alt: iso


jsnode
======

Ansible role to use as a wrapper for npm to install nodejs packages.

This role performs the following actions:

* Ensure the requirements are installed.

* Ensure the current user can obtain administrative (root)
   permissions.

* If not already added, add the nodejs repository to the apt sources.

* If not installed, install nodejs.

* If the **packages_npm** variable is defined, install the npm
   packages listed on it.

* If the **configuration** variable is defined, install the npm
   packages listed on it.

Documentation on `jsnode readthedocs
<https://jsnode.readthedocs.io>`_.

Code on `jsnode Gitlab <https://gitlab.com/constrict0r/jsnode>`_.

Code on `jsnode Github <https://github.com/constrict0r/jsnode>`_.

.. image:: https://gitlab.com/constrict0r/img/raw/master/autodebian/jsnode.png
   :alt: jsnode


kick
====

Bash script that uses a stack of Ansible roles to kick-start
Debian-like systems.

When executed this script performs the following actions:

* Installs Ansible.

* If the **-u** (username) parameter is present, the specified user
   is created and added to the *sudoers* group.

* If the **-w** (password) parameter is present, the specified
   password is assigned to the created user.

* Configures a very basic text-mode system.

* If the **-d** (desktop) parameter is present, the **gnome** desktop
   enviroment is installed.

* If the **-x** (extra role) parameter is present, the specified
   extra Ansible role is installed and included, additionally if the
   **-v** (extra variables) parameter is present, the variable keys
   and values specified are passed to the extra role.

* If the **-r** (remove) parameter is present, Ansible is uninstalled
   at the end of the kickstart process.

* For more fine-grained configuration, you can specify a
   configuration file using the **-c** (configuration) parameter, this
   parameter is used as the **configuration** variable and passed to
   the **constrict0r.constructor** role.

When a configuration file is specified, the **expand** variable for
the **constrict0r.constructor** role is setted to *true* **always** so
when writing configuration files, be sure to use the **item_path** and
**item_expand** attributes if you need to change the default behaviour
(see `expand attribute
<https://github.com/constrict0r/constructor#item_expand>`_).

For more information see: `constructor role
<https://github.com/constrict0r/constructor>`_.

Documentation on `kick readthedocs <https://kick.readthedocs.io>`_.

Code on `kick Gitlab <https://gitlab.com/constrict0r/kick>`_.

Code on `kick Github <https://github.com/constrict0r/kick>`_.

.. image:: https://gitlab.com/constrict0r/img/raw/master/autodebian/kick.png
   :alt: kick


latveria
========

`Skeleton repository <http://www.linfo.org/etc_skel.html>`_ for the
madvillain user home directory layout.

This repository provides the following file tree layout:

::

   home/
   ├── .config
   │   ├── gtk-3.0
   │   │   └── bookmarks
   │   └── monitors.xml
   ├── Documentos
   │   ├── biblioteca
   │   │   └── piscunov-cálculo-diferencial-integral-1.pdf
   │   ├── configme.sh
   │   └── madvillain.yml
   ├── Imágenes
   │   ├── animado
   │   ├── a-publicar
   │   │   └── existence.jpg
   │   └── avatar
   │       └── doom_master.jpg
   ├── Instaladores
   │   └── firmware
   │       ├── firmware-iwlwifi_20161130-4_all.deb
   │       └── firmware-realtek_20161130-4_all.deb
   ├── LICENSE
   ├── little-lab
   ├── Música
   │   └── Hip-Hop
   │       ├── A Tribe Called Quest
   │       │   └── Midnight Marauders
   │       │       └── cover.jpg
   │       ├── Aesop Rock
   │       │   ├── Float
   │       │   │   └── cover.jpg
   │       │   └── None Shall Pass
   │       │       └── cover.jpg
   │       ├── Czarface
   │       │   ├── Czarface
   │       │   │   └── cover.jpg
   │       │   ├── Czarface meets Ghostface
   │       │   │   └── cover.jpg
   │       │   ├── Czarface Meets Metal Face
   │       │   │   └── cover.jpg
   │       │   └── Every Hero Needs A Villain
   │       │       └── cover.jpg
   │       ├── Deltron 3030
   │       │   ├── Deltron 3030
   │       │   │   └── cover.jpg
   │       │   └── Event 2
   │       │       └── cover.jpg
   │       ├── Gramatik
   │       │   └── SB3
   │       │       └── cover.jpg
   │       ├── GZA
   │       │   └── Liquid Swords
   │       │       └── cover.jpg
   │       ├── Instrumentals
   │       │   ├── Aesop Rock
   │       │   │   └── None Shall Pass
   │       │   │       └── cover.jpg
   │       │   ├── Jeru the Damaja
   │       │   │   └── You Can't Stop The Prophet
   │       │   │       └── cover.jpg
   │       │   └── Viktor Vaughn
   │       │       └── Vaudeville Villain
   │       │           └── cover.jpg
   │       ├── Jeru the Damaja
   │       │   └── You Can't Stop The Prophet
   │       │       └── cover.jpg
   │       ├── JJ Doom
   │       │   └── Key To The Kuffs
   │       │       └── cover.jpg
   │       ├── Joey Bada$$
   │       │   └── 1999
   │       │       └── cover.jpg
   │       ├── MF Doom
   │       │   ├── Born Like This
   │       │   │   └── cover.jpg
   │       │   ├── Doom!
   │       │   │   └── cover.jpg
   │       │   ├── Operation Doomsday
   │       │   │   └── cover.jpg
   │       │   ├── Vaudeville Villain (Gold Edition)
   │       │   │   ├── cover.jpg
   │       │   │   ├── Disc 1
   │       │   │   └── Disc 2
   │       │   └── Venomous Villain
   │       │       └── cover.jpg
   │       ├── Quasimoto
   │       │   ├── Microphone Mathematics
   │       │   │   └── cover.jpg
   │       │   └── The Unseen
   │       │       └── cover.jpg
   │       └── The Herbaliser
   │           ├── Blow Your Headphones
   │           │   └── cover.jpg
   │           └── Take London
   │               └── cover.jpg
   ├── README.md
   ├── repos
   └── Vídeos
       ├── geeklog
       └── misc

Code on `latveria Gitlab <https://github.com/constrict0r/latveria>`_.

Code on `latveria Github <https://github.com/constrict0r/latveria>`_.

.. image:: https://gitlab.com/constrict0r/img/raw/master/autodebian/latveria.png
   :alt: latveria


madvillain
==========

Ansible role to apply the ultimate madvillain configuration.

This is capable of:

* Upgrade the system.

* Add `apt <https://wiki.debian.org/Apt>`_ repository sources.

* Update the apt cache.

* Uninstall apt packages.

* Install apt packages.

* Install `npm <http://npmjs.org/>`_ packages.

* Install `pip <https://pypi.org/project/pip/>`_ packages.

* Apply system-wide configuration using git.

* Stop services and disable them.

* Enable services and restart them.

* Create users.

* Add users to groups.

* Apply user-wide configuration using git.

* Run custom user tasks.

By default this role applies the following configuration:

* Installs the base software:

..

   * apt-transport-https

   * bzip2

   * ca-certificates

   * curl

   * sudo

   * unrar-free

   * unzip

   * vim

   * wget

   * xz-utils

* Install the desktop software:

..

   * audacity

   * easytag

   * ffmpeg

   * gedit

   * gimp

   * gnome

   * gparted

   * inkscape

   * kdenlive

   * keepassx

   * obs-studio

   * rhythmbox

   * vlc

* Installs the base developer software:

..

   * bats

   * emacs

   * git

   * libtext-csv-perl

   * make

   * meld

   * retext

   * ssh-askpass

   * tree

* Installs the python developer software:

..

   * Via apt:

   ..

      * direnv

      * python3

      * python3-pip

      * python3-pytest

      * python3-venv

      * python3-virtualenv

      * tox

   * Via pip:

   ..

      * ansible-lint

      * autopep8

      * flake8

      * jedi

      * poetry

      * sphinx

      * sphinx_rtd_theme

      * rope

      * yapf

* Installs the microcontroller developer software:

..

   * Via apt:

   ..

      * clang

      * fritzing

      * fritzing-data

      * fritzing-parts

      * python3

      * python3-pip

   * Via pip:

   ..

      * platformio

* Installs the madvillain software:

..

   * docker

   * docker.io

   * docker-compose

   * qemu-kvm

   * virt-manager

* Configures the base software:

..

   * vim

   ..

      * Creates a *.vimrc* configuration file on each user home
         directory.

      * Enable syntax highlight.

      * Set two spaces instead of tabs.

* Configures the desktop software:

..

   * emacs

   ..

      * Creates a *.emacs.d* configuration folder on each user home
         directory.

      * Enable line numbers.

      * Set themes folder.

      * Set wintermute theme.

      * Use spaces instead of tabs.

* Configures the base developer software:

..

   * emacs

   ..

      * Creates a *.emacs.d* configuration folder on each user home
         directory.

      * Enable line numbers.

      * Set themes folder.

      * Set wintermute theme.

      * Use spaces instead of tabs.

* Configures the python developer software:

..

   * direnv

   ..

      * Enable *direnv* command on *~/.bashrc* file.

   * emacs

   ..

      * Set `elpy <https://is.gd/tPU9gM>`_ plugin.

      * Set `tox.el <https://is.gd/hUqDMw>`_ plugin.

      * Set keybindings:

      ..

         * C-c C-c: Evaluates the current script.

         * C-RET (Enter): Evaluates the curren statement (current
            line plus the
               following nested line).

         * C-c C-z: Switches between your script and the interactive
            shell.

         * C-c C-d: Displays documentation for the thing under cursor
            (function or module). The documentation will pop in a
            different buffer, can be closed with *q*.

         * C-c C-t: Run pytest tests.

         * M-x tox-current-test: Run tox tests for current test.

         * M-x tox-current-class: Run tox tests for current class.

         * M-x pdb: Run PDB on a new window.

         * C-x: Set breakpoint on current line.

   * `poetry <https://poetry.eustace.io/>`_

   ..

      * Add poetry path to the *~/.profile* file to maintain
         dependecies aisolated.

   * `python3-virtualenv <https://virtualenv.pypa.io/en/latest/>`_

   ..

      * Enable elpy virtual enviroments on the *~/.bashrc* file.

* Configures the microcontroller developer software:

..

   * emacs

   ..

      * Set `platformio plugin <https://is.gd/8HIcsb>`_ plugin.

      * Set keybindings:

      ..

         * C-c i b: Build the project without auto-uploading.

         * C-c i c: Clean compiled objects.

         * C-c i u: Build and upload.

   * groups - Adds users to the groups:

      * dialout.

   * udev - Adds the rules file
      */etc/udev/rules.d/99-platformio-udev.rules*.

* Configures the madvillain software:

..

   * *~/.bashrc*

   ..

      * Adds the **changes** bash alias to quickly visualize
         repositories that were modified.

      * Adds the **runit** bash alias to quickly run an Ansible
         playbook.

      * Adds the **gic** bash alias to quickly make a git commit and
         push (lazy lazy villain).

      * Adds the **fixit** bash alias to quickly set monitors
         display.

   * gdm3

      * Disables the Wayland protocol.

   * gnome

   ..

      * Sets the dock to include the launchers:

      ..

         * emacs

         * firefox.

         * libre-office writer.

         * nautilus

         * rhythmbox

         * terminal.

   * nautilus

   ..

      * Adds the following folder bookmarks:

      ..

         * little-lab

         * repos

   * virt

   ..

      * Adds each user to the following groups:

      ..

         * libvirt

         * libvirt-qemu

         * kvm

* Creates the following home directory layout:

..

   ::

      home/
      ├── little-lab
      ├── repos
      ├── .emacs.d
      │   ├── config
      │   │   ├── base.el
      │   │   ├── org.el
      │   │   └── python.el
      │   ├── init.el
      │   └── themes
      │       └── wintermute-theme.el
      └── .vimrc

* Modifies the following files:

..

   ::

      home/
      ├── .bashrc
      ├── .config/gtk-3.0/bookmarks
      └── .profile

Documentation on `madvillain readthedocs
<https://madvillain.readthedocs.io>`_.

Code on `madvillain Gitlab
<https://gitlab.com/constrict0r/madvillain>`_.

Code on `madvillain Github
<https://github.com/constrict0r/madvillain>`_.

.. image:: https://gitlab.com/constrict0r/img/raw/master/autodebian/madvillain.png
   :alt: madvillain


pyp
===

Ansible role to use as a wrapper for pip to install python packages.

This role performs the following actions:

* Ensure the requirements are installed.

* Ensure the current user can obtain administrative (root)
   permissions.

* Update the apt cache.

* Ensure dependencies are installed.

* If the **packages_pip** variable is defined, install the python
   packages listed on it.

* If the **configuration** variable is defined, install the python
   packages listed on it.

Documentation on `pyp readthedocs <https://pyp.readthedocs.io>`_.

Code on `pyp Gitlab <https://gitlab.com/constrict0r/pyp>`_.

Code on `pyp Github <https://github.com/constrict0r/pyp>`_.

.. image:: https://gitlab.com/constrict0r/img/raw/master/autodebian/pyp.png
   :alt: pyp


servicez
========

Ansible role to manage system services.

This role performs the following actions:

* Ensure the requirements are installed.

* Ensure the current user can obtain administrative (root)
   permissions.

* If the **services_disable** variable is defined, stop and disable
   the services listed on it.

* If the **configuration** variable is defined, stop and disable the
   *services_disable* listed on it.

* If the **services** variable is defined, enable and start the
   services listed on it.

* If the **configuration** variable is defined, enable and start the
   services listed on it.

Documentation on `servicez readthedocs
<https://servicez.readthedocs.io>`_.

Code on `servicez Gitlab <https://gitlab.com/constrict0r/servicez>`_.

Code on `servicez Github <https://github.com/constrict0r/servicez>`_.

.. image:: https://gitlab.com/constrict0r/img/raw/master/autodebian/servicez.png
   :alt: servicez


sourcez
=======

Ansible role to add apt repositories to the apt sources.

This role performs the following actions:

* Ensure the requirements are installed.

* Ensure the current user can obtain administrative (root)
   permissions.

* If the **repositories** variable is defined, add to the apt sources
   the repositories listed on it.

* If the **configuration** variable is defined, add to the apt
   sources the repositories listed on it.

Documentation on `sourcez readthedocs
<https://sourcez.readthedocs.io>`_.

Code on `sourcez Gitlab <https://gitlab.com/constrict0r/sourcez>`_.

Code on `sourcez Github <https://github.com/constrict0r/sourcez>`_.

.. image:: https://gitlab.com/constrict0r/img/raw/master/autodebian/sourcez.png
   :alt: sourcez


sysconfig
=========

Ansible role to apply system wide configuration.

This role performs the following actions:

* Ensure the requirements are installed.

* Ensure the current user can obtain administrative (root)
   permissions.

* Update the apt cache.

* Ensure dependencies are installed.

* If the **system_skeleton** variable is defined, clone the git
   repositories listed on it into */*.

* If the **configuration** variable is defined, clone the git system
   repositories listed on it into */*.

This role do not expand files or URLs by default because the most
common case is to specify URLs that points directly to a skeleton
repository, so the default behaviour for this role is to treat file
paths and URLs as plain text.

You can change the default behaviour by:

* Setting the **expand** variable to *true*.

Or

* Add to an item the attribute **item_expand** setted to *true*.

Documentation on `sysconfig readthedocs
<https://sysconfig.readthedocs.io>`_.

Code on `sysconfig Gitlab
<https://gitlab.com/constrict0r/sysconfig>`_.

Code on `sysconfig Github
<https://github.com/constrict0r/sysconfig>`_.

.. image:: https://gitlab.com/constrict0r/img/raw/master/autodebian/sysconfig.png
   :alt: sysconfig


task
====

Ansible role to run arbitrary tasks.

It allows to specify a task file or URL and this role will run it
without having to write a playbook or another role.

This role performs the following actions:

* Ensure the requirements are installed.

* Update the apt cache.

* Ensure dependencies are installed.

* If the **user_tasks** variable is defined run each specified task.

* If the **configuration** variable is defined and the **user_tasks**
   variable is defined, run each specified task.

Inside each specified task is possible to use the **unified** variable
that will have the list of specified users.

This role do not expand files or URLs by default because the most
common case is to specify URLs that points directly to a tasks file,
so the default behaviour for this role is to treat file paths and URLs
as plain text.

You can change the default behaviour by:

* Setting the **expand** variable to *true*.

Or

* Add to an item the attribute **item_expand** setted to *true*.

Documentation on `task readthedocs <https://task.readthedocs.io>`_.

Code on `task Gitlab <https://gitlab.com/constrict0r/task>`_.

Code on `task Github <https://github.com/constrict0r/task>`_.

.. image:: https://gitlab.com/constrict0r/img/raw/master/autodebian/task.png
   :alt: task


unify
=====

Ansible role to unify collections into a single unified collection.
Includes a plugin named **utils** and a module named autodebian.

The items to unify can be single items, collections of items, paths
and URLs to *.yml* files where to load more items.

The variable **items** is used to specify items to unify, the result
is stored on a single **unified** collection variable. Optionally a
secondary **unified_b** collection will be created if the
**secondary** variable is set to *true*. If you need more than two
unified collections you can use the included **unify** module.

If the variable **expand** is set to *true* or if one item specifies
the **item_expand** attribute as *true*, the items on each listed file
path or URL will be loaded using the variable **titles** as index,
therefore when expanding items from files the variable **titles** must
not be empty.

For example if the value of the **items** variable is the path
*/home/username/my-config.yml*, the **titles** variable has the value
*packages* and the **expand** variable is set to *true*, this role
will try to load a list named *packages* from the file
*/home/username/my-config.yml*.

The contents of */home/username/my-config.yml* could be something like
the following:

..

   ::

      ---
      packages:
        - leafpad
        - rolldice
        - /home/username/extra-config.yml
        - https://my-url/my-config.yml

When the variable **expand** is set to *false*, the file paths or URLs
found inside the **items** variable are treated as plain text items,
this is useful to maintain files and directories listings, for example
for backup purposes.

When adding an item to the **unified** variable it will be added only
if is not already present. On the case of boolean values duplicates
are allowed on **unified** because boolean values are commonly used
for checklists.

This role also includes the following functionality:

* Ensure the requirements are installed.

Documentation on `unify readthedocs <https://unify.readthedocs.io>`_.

Code on `unify Gitlab <https://gitlab.com/constrict0r/unify>`_.

Code on `unify Github <https://github.com/constrict0r/unify>`_.

.. image:: https://gitlab.com/constrict0r/img/raw/master/autodebian/unify.png
   :alt: unify


upgrade
=======

Ansible role to apply a system upgrade.

This role performs the following actions:

* Ensure the requirements are installed.

* Ensure the current user can obtain administrative (root)
   permissions.

* Update the apt cache.

* If the **upgrade** variable is set to *true* or if the
   **configuration** file contains a variable **upgrade** setted to
   *true*, perform a full system upgrade.

Documentation on `upgrade readthedocs
<https://upgrade.readthedocs.io>`_.

Code on `upgrade Gitlab <https://gitlab.com/constrict0r/upgrade>`_.

Code on `upgrade Github <https://github.com/constrict0r/upgrade>`_.

.. image:: https://gitlab.com/constrict0r/img/raw/master/autodebian/upgrade.png
   :alt: upgrade


userconfig
==========

Ansible role to apply user wide configuration.

This role performs the following actions:

* Ensure the requirements are installed.

* Ensure the current user can obtain administrative (root)
   permissions.

* Update the apt cache.

* Ensure dependencies are installed.

* If the **user_skeleton** variable is defined and the **users**
   variable is defined, clone the git repositories listed into each
   user home folder.

* If the **configuration** variable is defined and the **users**
   variable is defined, clone the git repositories listed on it into
   each user home folder.

This role do not expand files or URLs by default because the most
common case is to specify URLs that points directly to a skeleton
repository, so the default behaviour for this role is to treat file
paths and URLs as plain text.

You can change the default behaviour by:

* Setting the **expand** variable to *true*.

Or

* Add to an item the attribute **item_expand** setted to *true*.

Documentation on `userconfig readthedocs
<https://userconfig.readthedocs.io>`_.

Code on `userconfig Gitlab
<https://gitlab.com/constrict0r/userconfig>`_.

Code on `userconfig Github
<https://github.com/constrict0r/userconfig>`_.

.. image:: https://gitlab.com/constrict0r/img/raw/master/autodebian/userconfig.png
   :alt: userconfig


users
=====

Ansible role to create users.

This role performs the following actions:

* Ensure the requirements are installed.

* Ensure the current user can obtain administrative (root)
   permissions.

* If the **users** variable is defined, create all users listed on
   it.

* If the **configuration** variable is defined, create all users
   listed on it.

* If the **password** variable is defined, set this password for all
   created users.

* If an user has defined an **item_pass** attribute, it will be
   setted as the password for the user.

* If an user has defined an **item_groups** attribute, it will be
   added to the groups listed on it.

If an user has a **item_pass** or **item_groups** attributes defined,
then it must have a non-empty **item_name** attribute defined too.

Documentation on `users readthedocs <https://users.readthedocs.io>`_.

Code on `users Gitlab <https://gitlab.com/constrict0r/users>`_.

Code on `users Github <https://github.com/constrict0r/users>`_.

.. image:: https://gitlab.com/constrict0r/img/raw/master/autodebian/users.png
   :alt: users


License
*******

MIT. See the LICENSE file for more details.


Links
*****

* `Github <https://github.com/constrict0r/autodebian>`_.

* `Gitlab <https://gitlab.com/constrict0r/autodebian>`_.

* `Readthedocs <https://autodebian.readthedocs.io>`_.


UML
***


Deployment
==========

The full project structure is shown below:

.. image:: https://gitlab.com/constrict0r/img/raw/master/autodebian/deployment.png
   :alt: deployment


Author
******

.. image:: https://gitlab.com/constrict0r/img/raw/master/autodebian/author.png
   :alt: author

The travelling vaudeville villain.

Enjoy!!!

.. image:: https://gitlab.com/constrict0r/img/raw/master/autodebian/enjoy.png
   :alt: enjoy

