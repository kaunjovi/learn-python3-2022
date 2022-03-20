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


## Unit testing in Python 

- [Unit Testing in Python Tutorial](https://www.datacamp.com/community/tutorials/unit-testing-python)
- [Getting Started With Testing in Python](https://realpython.com/python-testing/)


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

