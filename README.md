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
If you have already constructed a python environment (Python 3.8), you don't need to do things below, but you must install the packages listed in Pipfile.

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

## Pipenv commands
### Create Pipfile and Pipfile.lock in the current directory or install packages written in Pipfile if Pipfile already exists.
```shell
$ pipenv install
```

### Install package in your virtual environment
```shell
$ pipenv install {package}
```

### Unnstall package in your virtual environment
```shell
$ pipenv uninstall {package}
```

### Activate shell mode:
```shell
$ pipenv shell
```
### Deactivate shell mode:
```shell
$ exit
```
### Run command in your virtual environment
```shell
$ pipenv run {command}
```

### Remove virtual environment
```shell
$ pipenv --rm
```

### Confirm the path of virtual environment
```shell
$ pipenv --venv
```


## Converting py/ipynb
You can convert python/jupyter notebook with the commands below.
Note that these commands can be used in the shell mode of `pipenv`.

### jupyter notebook (.ipynb) to python (.py)
```shell
$ ipynb-py-convert hoge.ipynb hoge.py
```

### python (.py) to jupyter notebook (.ipynb)
```shell
$ ipynb-py-convert hoge.py hoge.ipynb
```

## Opening Jupyter Notebook with Google Colabratory
You can open Jupyter Notebook (ipynb file) in github with Google Colaboratory.

1. View Jupyter Notebook in github on your browser.
2. Replace `github.com` with `colab.research.google.com/github`
3. Then, save a copy on your drive.

e.g.,
https://github.com/shigeodayo/ex_design_analysis/blob/master/src/bayes/examples/Monty_Hall_problem.ipynb
->
https://colab.research.google.com/github/shigeodayo/ex_design_analysis/blob/master/src/bayes/examples/Monty_Hall_problem.ipynb

Also see:
https://sekailab.com/wp/2018/05/24/colaboratory-github-jupyter-notebook/

Note taht `nbstripout` package is used to delete meta information in Jupyter Notebook.
The information is automatically deleted when you commit an ipynb file.
Thus, you don't need to worry about the file size of ipynb file (but we cannot check the diffs).

Also see:
https://qiita.com/ctyl/items/bbc04e0b0bd4557d54a6

## Reference
- Research Methods in Human-Computer Interaction
https://dl.acm.org/doi/book/10.5555/1841406
