# Experimental Design and Analysis

Sample programs for analyzing experimental data.

The csvs in the data folder are not the actual data used in the papers, but the samples.

## Environment
- Python 3.8.1
- pipenv, version 2020.8.13
## How to run program

Go to the directory where the program you want to run in the terminal. Then, type below to run the program.

```shell
$ python {PYTHON_FILE_NAME}
```
(Note that you have to install the packages that are used in the program before running.)


If you are `pipenv` user, you can run the program with the command below.
```shell
$ pipenv run python {PYTHON_FILE_NAME}
```


## How to construct environment
If you have already constructed a python environment (Python 3.7), you don't need to do things below, but you must install the packages listed in Pipfile.

### 1. Install `pyenv`

```shell
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
$ echo 'eval "$(pyenv init -)"' >> ~/.zshrc
$ pyenv --version
pyenv 1.2.17
```

### 2. Install `Python 3.8.1` via pyenv

```shell
$ pyenv install 3.8.1
$ pyenv local 3.8.1
$ python --version
Python 3.8.1
$ pip --version
pip 21.0.1 from /Users/{USERNAME}/.pyenv/versions/3.8.1/lib/python3.8/site-packages/pip (python 3.8)
```

### 3. Install `pipenv`

```shell
$ pip install --upgrade pip
$ pip install pipenv
pipenv, version 2020.8.13
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

## Reference
- Research Methods in Human-Computer Interaction
https://dl.acm.org/doi/book/10.5555/1841406
