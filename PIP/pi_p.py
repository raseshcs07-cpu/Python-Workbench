# PIP
# PIP is a package manager for Python packages, or modules if you like.

# A package contains all the files you need for a module.
# Modules are Python code libraries you can include in your project.

# Check if PIP is Installed
# Navigate your command line to the location of Python's script directory, and type the following:
# C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip --version

# Downloading a package is very easy.
# Open the command line interface and tell PIP to download the package you want.
# C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip install camelcase
# python3 -m pip install requests
# python3 -m pip install numpy.    - python3 -m pip install package_name



# camelcase
# python3 -m pip install camelcase
# python3 -m pip show camelcase
import camelcase
c = camelcase.CamelCase()
txt = "lorem ipsum dolor sit amet"
print(c.hump(txt))
#This method capitalizes the first letter of each word.


# Remove a Package
# python3 -m pip uninstall camelcase
# List Packages
# python3 -m pip list