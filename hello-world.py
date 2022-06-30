## Using pipenv 
# kaunjovi@devbook learn-python3-2022 % brew list --version pipenv
# pipenv 2022.6.7
# 
## Uses python of pipenv in this case 3.10
# kaunjovi@devbook learn-python3-2022 % pipenv run which python 
# /Users/kaunjovi/code/learn-python3-2022/.venv/bin/python
# kaunjovi@devbook learn-python3-2022 % pipenv run python --version 
# Python 3.10.2
# 
## And there is the hello world. 
# kaunjovi@devbook learn-python3-2022 % prp hello-world.py 
# Hello world from Python 3

import pandas as pd 

simpsons = pd.read_html("https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes")

print(f"{len(simpsons)}")


# print(f"Hello world from Python 3")