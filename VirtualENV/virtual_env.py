# VIRTUALENX
# A virtual environment in Python is an isolated environment on your computer, where you can run and test your Python projects.
# It allows you to manage project-specific dependencies without interfering with other projects or the original Python installation.

"""
Think of a virtual environment as a separate container for each Python project. Each container:

Has its own Python interpreter
Has its own set of installed packages
Is isolated from other virtual environments
Can have different versions of the same package
"""

"""
Using virtual environments is important because:

It prevents package version conflicts between projects
Makes projects more portable and reproducible
Keeps your system Python installation clean
Allows testing with different Python versions
"""

# Creating a Virtual Environment
python3 -m venv myfirstproject
source myfirstproject/bin/activate

# Install Packages
pip install cowsay

# using package
python3
import cowsay
cowsay.cow("Good Mooooorning!")



pip install art

python3
from art import *
tprint("HELLO")

pip install pyfiglet
python3
import pyfiglet
print(pyfiglet.figlet_format("PYTHON"))

pip install emoji
python3
import emoji
print(emoji.emojize("Python is awesome! :snake: :rocket:"))



# 1
mkdir myfirstproject
cd mythirdproject
python3 -m venv venv
source venv/bin/activate
pip install pyfiglet
python3 -c 'import pyfiglet; print(pyfiglet.figlet_format("Rasesh!"))'


# Delete Virtual Environment
rm -rf myfirstproject