# zappa-demo [![Build Status](https://travis-ci.org/scottx611x/zappa-demo.svg?branch=master)](https://travis-ci.org/scottx611x/zappa-demo) <a target='_blank' rel='nofollow' href='https://app.codesponsor.io/link/gyj4KVn6fRKmyQv9inh3CFeR/scottx611x/zappa-demo'>
  <img alt='Sponsor' width='888' height='68' src='https://app.codesponsor.io/embed/gyj4KVn6fRKmyQv9inh3CFeR/scottx611x/zappa-demo.svg' />
</a>

Demo of Zappa's functionality w a basic Flask app.

See [this great Pycon talk](https://www.youtube.com/watch?v=vGphzPLemZE) for more cool ways to deploy your web apps.

# What is [Zappa](https://github.com/Miserlou/Zappa) ?
Zappa makes it super easy to build and deploy all Python WSGI applications on AWS Lambda + API Gateway. Think of it as "serverless" web hosting for your Python apps. 

That means: 
  - infinite scaling
  - zero downtime
  - zero maintenance
  - pay a fraction of the cost of your current deployments!

If you've got a Python web app (including Django and Flask apps), it's as easy as:

`$ pip install zappa`

`$ zappa init`

`$ zappa deploy`

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
- Zappa allows for extremely simple staging of different enviornments
- To deploy an environment, simply: `zappa deploy <enviornment_name>`
- Ex: `zappa deploy development`
- To update an already deployed instance with new code: `zappa update <enviornment_name>`

> **NOTE: Currently all commits to `master` will trigger an update of the currently deployed `zappa` production site, so be cautious.**

> **ANOTHER NOTE: A prior Zappa deployment is required for Travis auto-updating to work**

> **ONE MORE NOTE: AWS_ACCESS_KEY_ID & AWS_SECRET_ACCESS_KEY env. variables need to be set in travis for the auto-updating to work properly.**

# **BONUS**
**[Ngrok](https://ngrok.com/):** is a cool tool to expose a local server behind a NAT or firewall to the internet.

- `brew cask install ngrok`
- After following the flask installation instructions above as well as the ngrok ones, you can run:

  `ngrok http 5000`

  and should recieve a link to a internet accessible instance of your app!
