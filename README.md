# Experimental Design and Analysis

Sample programs for analyzing experimental data.

The data in data folder is not the actual data used in the papers, but the samples.

## Environment
- Python 3.7.7
- pipenv, version 2018.11.26

## How to run program

Go to a directry where the program you want to run. Then, type below in the terminal to run the program.

```shell
$ python {PYTHON_FILE_NAME}
```
(Note that you have to install the packages that are used in the program before running.)


If you are `pipenv` user, you can run program with a command below.
```shell
$ pipenv run python {PYTHON_FILE_NAME}
```


## How to construct environment
If you have constructed python environment (Python 3.7) yet, you don't need to do things below, but you must install the packages listed in Pipfile.

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

## Converting py/ipynb
You can convert python/jupyter notebook with the commands below.
Note that these commands can be used in the shell mode of `pipenv`.

### Activate shell mode:
```shell
$ pipenv shell
```
### Deactivate shell mode:
```shell
$ exit
```

### jupyter notebook (.ipynb) to python (.py)
```shell
$ ipynb-py-convert hoge.ipynb hoge.py
```

### python (.py) to jupyter notebook (.ipynb)
```shell
$ ipynb-py-convert hoge.py hoge.ipynb
```
