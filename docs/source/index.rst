.. pip_tkinter documentation master file, created by
   sphinx-quickstart on Mon Jul 11 06:57:00 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pip_tkinter!
=======================================
`Github <https://github.com/upendra-k14/pip_gui>`_


Motivation
----------

    This project is intended to provide a GUI version for "pip".
    It is currently a command line based package manager used to install
    and manage software packages written in Python.
    But, many users are not familiar with the command line and thus
    find difficulties using and accessing PIP.
    People who still don’t have enough exposure to command line
    tools(specially in case of Windows) find installing packages using PIP very
    cumbersome. Therefore, the main motivation behind this project is to make
    various functionalities provided by PIP accessible to Windows/LINUX/Mac
    based users through a tkinter based GUI interface which could be further
    integrated with IDLE. As a whole, it would help beginners to focus more on
    learning and using new Python packages rather than getting in unavoidable
    trouble of configuring various paths and configurations in order to install
    new Python Packages from PyPI.

    The product developed will be a GUI for pip to make various functionalities
    of pip ( a command line tool for installing Python packages) easily
    accessible to users. Main motivation behind the need for GUI version of
    Python Package Manager is :

    -   Make various functionalities provided by PIP easily accessible to
        Windows/LINUX/Mac based users

    -   Help people to focus only on fulfilling the task of installing
        Python packages rather than getting in unavoidable trouble of
        configuring various paths, versions and configurations

Target Users
------------

    -   Windows Users ( who have difficulty using command prompt )
    -   Novice Python users ( on MacOS or Linux )

Targeted Tasks
--------------

    -   Search, select version and install package
    -   Check for new updates and install them
    -   Uninstall a package
    -   Support different installation methods :
        -   Requirements.txt files
        -   .whl files
        -   From local archives
        -   From Pythonlibs

Documentation
-------------
    .. toctree::
        :maxdepth: 2

        installation
        developer_guide
        modules
