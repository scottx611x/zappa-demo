# zappa-demo [![Build Status](https://travis-ci.com/scottx611x/zappa-demo.svg?token=EkzyvwdZ2jcY78ErmS88&branch=master)](https://travis-ci.com/scottx611x/zappa-demo)

Demo of Zappa's functionality w a basic Flask app

# Pre-reqs:
- Valid AWS credentials for [`boto3` usage](http://boto3.readthedocs.io/en/latest/guide/configuration.html#configuring-credentials)
- `python`
- `pip`
- [`virtualenvwrapper`](https://virtualenvwrapper.readthedocs.io/en/latest/install.html#installation) (optional, but reccomended)

# Installation:
- `mkvirtualenv zappa-demo && workon zappa-demo` (optional)
- `pip install -r requirements.txt`
- `export FLASK_APP=index.py`
- `flask run`

You should be able to view the site @ http://localhost:5000

# Running Tests:
- `python tests.py`

# Deploying & Updating:
We are deployed on AWS using a nifty tool called: [Zappa](https://github.com/Miserlou/Zappa) 

In short, this allows for great horizontal scaling, zero server maintenance/downtime, and we are only charged for the time that people access the site.

- To deploy, simply: `zappa deploy`
- To update an already deployed instance with new code: `zappa update`

> **NOTE: Currently all pushes to `master` will trigger an update of the currently deployed `zappa` site, so be cautious.**

> **ANOTHER NOTE: A prior Zappa deployment is required for Travis auto-updating to work**
