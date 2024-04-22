# WM9L3-PMA

L7 DTS Apprenticeship - User Experience and Solution Design module - PMA website prototype

## Setup for Windows

> Install Modules

```bash
$ virtualenv .venv
$ .\.venv\Scripts\activate
$ pip3 install -r requirements.txt
```

<br />

> Setup Flask Environment

```bash
$ # CMD
$ set FLASK_APP=run.py
$
$ # Powershell
$ $env:FLASK_APP = ".\run.py"
```

<br />

> Start App

```bash
$ flask run
```

The app runs at http://127.0.0.1:5000
