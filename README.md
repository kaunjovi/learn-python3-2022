# learn-python3-2022
Learn Python3. Year 2022. 

First set of changes.
Python 3.10.2, documentation released on 14 January 2022.


```batch
brew --version 
Homebrew 3.3.16
...
brew install pyenv
Running `brew update --preinstall`...
...
pyenv versions
* system (set by /Users/kaunjovi/.pyenv/version)

pyenv install 3.10.2

python --version 
Python 2.7.16

pyenv global 3.10.2
```

This did not work. Lets 
## penv 

- https://github.com/pyenv/pyenv#basic-github-checkout
- [How to Install Python 3 on Mac and Update the Version with Pyenv](https://www.freecodecamp.org/news/how-to-install-python-3-on-mac-and-update-the-python-version-macos-homebrew-command-guide/)
- How does it compare with pyenv ?? 

## pyenv vs pipenv
Pyenv is used to manage different Python versions, whereas Pipenv is used to manage Python packages

## pipenv 

- Use pipenv to create a virtual environment, download dependencies locally and manage them as well. 
- Create the folder for your project and in it create the .venv folder and Pipfile file. 
- cd to your project folder and try the following commands. 

```batch
brew install pipenv
pipenv install --python 3.10.2
pipenv install flake8 --dev
pipenv shell 
python hello-world.py
exit    
pipenv uninstall flake8
pipenv --rm
```

print("Hello, World!")

## variable_name 

my_string = "Hello, World!"
print(my_string)

## How to show hidden files in mac 
- Cmd + Shift + .




## Minimum Path Sum
- [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
```

## self 

- self is an object like any other and may be used in any context 
- Self is always pointing to Current Object.

## Naming convention 

- A Python package is directory of Python module(s) / files(s)
    - Packages should also have short, all-lowercase names, although the use of underscores is discouraged.
- Module is simply a Python source file, which can expose classes, functions and global variables.
    - Modules should have short, all-lowercase names. 
    - Underscores can be used in the module name if it improves readability.
- Class names should normally use the CapWords convention

```batch
import mypackage.my_module
from mypackage.my_module import MyClass 
from mypackage.my_module import my_method
```

## https://www.youtube.com/watch?v=s8XjEuplx_U

## https://www.youtube.com/watch?v=PXMJ6FS7llk

```
cd my_project
pipenv --three
pipenv run which python

pipenv install
pipenv uninstall beautifulsoup4
pipenv lock
pipenv install
pipenv install --dev
pipenv install coverage --dev
-- unit testing frameworks 
pipenv install --dev nose2 

-- test coverage 

-- web scraping 
pipenv install beautifulsoup4   


-- run your project 
-- prp is the same as pipenv run python 
pipenv run python my_project.py
```

## Python dev setup on Mac. Python3. Pip3.  

- Mac has both Python 2 and 3. 
- It needs Python 2 for its own stuff. 
- We need Python 3 for coding projects. 

```code 
kaunjovi@devbook learn-python3-2022 % python --version 
Python 2.7.16

kaunjovi@devbook learn-python3-2022 % python3 --version 
Python 3.9.13

kaunjovi@devbook learn-python3-2022 % where python3
/usr/local/bin/python3
/usr/local/bin/python3
/usr/bin/python3

kaunjovi@devbook learn-python3-2022 % python3 -m pip install pip --upgrade
... 

kaunjovi@devbook learn-python3-2022 % pip3 --version 
pip 22.2.2 from /usr/local/lib/python3.9/site-packages/pip (python 3.9)

kaunjovi@devbook learn-python3-2022 % pip3 install pipenv --upgrade
...

kaunjovi@devbook learn-python3-2022 % pipenv --version 
pipenv, version 2022.8.19


kaunjovi@devbook learn-python3-2022 % export PIPENV_VENV_IN_PROJECT=1

kaunjovi@devbook learn-python3-2022 % pipenv --three 
Creating a virtualenv for this project...
Pipfile: /Users/kaunjovi/code/learn-python3-2022/Pipfile
...

kaunjovi@devbook learn-python3-2022 % pipenv run python --version 
Python 3.9.13



```

- https://newdevzone.com/posts/how-to-use-pipenv-on-mac - there is some longish steps involving some .zhrc file. 

## What is .zhrc file? 
- zshrc file is used to configure your terminal prompt if you're using zsh (z-shell) login shell 
- If you're using a standard OSX terminal, then you're probably using bash (the BASH Shell)

## What is the terminal shelll I am running on mac ? 
- Every Mac comes with a Unix shell that provides a command line interface. 
- Macs running macOS 10.15 and later use Zsh by default.

```code 
kaunjovi@devbook learn-python3-2022 % echo $0
-zsh
```

## Unit testing in Python 

- [Unit Testing in Python Tutorial](https://www.datacamp.com/community/tutorials/unit-testing-python)
- [Getting Started With Testing in Python](https://realpython.com/python-testing/)
- https://machinelearningmastery.com/a-gentle-introduction-to-unit-testing-in-python/
- PyUnit, PyTest 
- pytest +, 

```code 
-- unit testing frameworks 
pipenv install --dev nose2 

-- test coverage 

pipenv install pytest --dev

kaunjovi@devbook learn-python3-2022 % pipenv run pytest bhav_copy.py
===================================== test session starts =====================================
platform darwin -- Python 3.10.2, pytest-7.1.2, pluggy-1.0.0
rootdir: /Users/kaunjovi/code/learn-python3-2022
collected 1 item                                                                              

bhav_copy.py .                                                                          [100%]

====================================== 1 passed in 0.34s ======================================


```
