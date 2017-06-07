# zappa-demo [![Build Status](https://travis-ci.org/scottx611x/zappa-demo.svg?branch=master)](https://travis-ci.org/scottx611x/zappa-demo)

Demo of Zappa's functionality w a basic Flask app.

See [this great Pycon talk](https://www.youtube.com/watch?v=vGphzPLemZE) for more cool ways to deploy your web apps.

# Pre-reqs:
- Valid AWS credentials for [`boto3` usage](http://boto3.readthedocs.io/en/latest/guide/configuration.html#configuring-credentials)
- `python`
- `pip`
- [`virtualenvwrapper`](https://virtualenvwrapper.readthedocs.io/en/latest/install.html#installation) (optional, but reccomended)

# Installation:
- `mkvirtualenv zappa-demo-env && workon zappa-demo-env` (optional)
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

# **BONUS**
**Ngrok:** is a cool tool to expose a local server behind a NAT or firewall to the internet.

-`brew cask install ngrok`
- After following the flask installation instructions above as well as the ngrok ones, you can run:
  `ngrok http 5000`
  and should recieve a link to a internet accessible instance of your app!
