# Chain Spy BackEnd

This project calculates the current cost of gas and returns the value in your currency. It is the Backend for [this project](https://github.com/OladeleSeyi/chainSpy-client)

This is a Python Project built on the [Serverless Framework](https://serverless.com/framework/) with support for dependencies (using [virtualenv](https://pypi.python.org/pypi/virtualenv) & [serverless-python-requirements](https://github.com/UnitedIncome/serverless-python-requirements)) and tests (using [unittest](https://docs.python.org/2/library/unittest.html#module-unittest)).

### How to Use.

---

A thorough overview of the repo at [Notion](https://denim-icebreaker-af6.notion.site/Backend-x-Data-78f66c1a02d843928bf263b9f370950c).

In order to promote a healthy and collaborative repo, please fork the repo and clone your fork to you machine to begin. Follow this [guide on collaborating](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/).

---

### Requirements

- [Install Python](https://www.python.org/downloads/release/python-363/)
- [Install Pipx](https://pypi.org/project/pipx/)
- [Install Virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
- [Install NodeJs](https://nodejs.org/en/download/)
- [Install the Serverless Framework](https://serverless.com/framework/docs/providers/aws/guide/installation/)
- [Configure your AWS CLI](https://serverless.com/framework/docs/providers/aws/guide/credentials/)

### Installation

Create a new project

```sh
$  git clone https://github.com/OladeleSeyi/chainSpy-backend.git
```

Create a virtual environment for your project for Windows

```sh
$ cd chainSpy-backend
$ python -m venv venv
```

---

For Intel Macs

```sh
$ cd chainSpy-backend
$ virtualenv -p /usr/bin/python3 venv
```

For M1 Macs using Homebrew installed Python

```sh
$ cd chainSpy-backend
$ virtualenv -p /opt/homebrew/bin/python3.9 venv
```

Activate the virtual environment

MAC

```sh
$ source venv/bin/activate
```

`Windows`

```sh
$  source myenv/Scripts/activate
```

Install Serverless plugin: serverless-python-requirements

```sh
$ npm install
```

### Usage

Install a Python dependency (for example, [Requests](http://docs.python-requests.org/en/master/))

```sh
$ pip install requests
```

Run on your Machine

```sh
sls offline start
```

While this may be buggy on M1 macs, I hope it works for you.

Store a reference to your dependencies

```sh
$ pip freeze > requirements.txt
```

Re-install your dependencies from your requirements

```sh
$ pip install -r requirements.txt
```

Invoke a function locally

```
$ serverless invoke local -f hello
```

Run your tests

```
$ python -m unittest discover -s tests
```

Deactivate your virtual environment

```sh
$ deactivate
```

### Deploying

Deploy your project

```sh
$ serverless deploy
```

Deploy a single function

```sh
$ serverless deploy function --function hello
```

To compile non-pure Python modules, install [Docker](https://docs.docker.com/engine/installation/) and the [Lambda Docker Image](https://github.com/lambci/docker-lambda). Enable **dockerizePip** in **serverless.yml** and `serverless deploy` again.

```yml
# enable dockerize Pip
custom:
  pythonRequirements:
    dockerizePip: true
```

**Note**, if you are deploying using [SEED](https://seed.run), you don't need to enable **dockerizePip** or install Docker. [SEED](https://seed.run) does it automatically.
