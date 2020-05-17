# Experimental Design and Analysis


## Environment
- Python 3.7.7
- pipenv, version 2018.11.26

## How to construct environment (optional)

### 1. Install `pyenv`

```shell
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
$ echo 'eval "$(pyenv init -)"' >> ~/.zshrc
$ pyenv --version
pyenv 1.2.17
```

### 2. Install `Python 3.7.7` via pyenv

```shell
$ pyenv install 3.7.7
$ pyenv local 3.7.7
$ python --version
Python 3.7.7
$ pip --version
pip 19.2.3 from /Users/{USERNAME}/.pyenv/versions/3.7.7/lib/python3.7/site-packages/pip (python 3.7)
```

### 3. Install `pipenv`

```shell
$ pip install --upgrade pip
$ pip install pipenv
pipenv, version 2018.11.26
```

## Install packages

```shell
$ pipenv install {PACKAGE}
```

## How to run python

```shell
$ pipenv run python {PYTHON_FILE_PATH} {ARGUMENTS}
```

## How to open jupyter notebook or lab

```shell
$ pipenv run jupyter {notebook or lab}
```

## Activate the virtual environment
```shell
$ pipenv shell
```

## Deactivate the virtual environment
```shell
$ exit
```

## How to convert jupyter notebook (.ipynb) to python (.py)
```shell
$ ipynb-py-convert hoge.ipynb hoge.py
```

## How to convert python (.py) to jupyter notebook (.ipynb)
```shell
$ ipynb-py-convert hoge.py hoge.ipynb
```
