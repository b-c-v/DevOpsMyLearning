# venv module uses for creating virtual environments.

# ***Creating a virtual environment***
# To create a virtual environment on your computer, open the command prompt, and navigate to the folder where you want to create your project, then type this command:
"""
python -m venv myfirstproject
"""
# This will set up a virtual environment, and create a folder named "myfirstproject". The file/folder structure will look like this:
"""
myfirstproject
  bin/
  include
  lib
  lib64
  pyvenv.cfg
"""
# ***Activate virtual environment***
# To use the virtual environment, you have to activate it with this command:
"""
source myfirstproject/bin/activate
"""
# After activation, your prompt will change to show that you are now working in the active environment: (myfirstproject) ser@hostname
# Once a virtual environment is activated, you can install packages in it, using pip.
"""
pip install cowsay
"""
# Now that the 'cowsay' module is installed in the virtual environment, lets use it to display a talking cow.
import cowsay

cowsay.cow("Good Mooooorning!")

# ***Deactivate virtual environment***
# To deactivate the virtual environment use this command:
"""
deactivate
"""
# If you try to execute code outside of the virtual environment, you will get an error because 'cowsay' is missing.

# ***Delete virtual environment***
# To delete a virtual environment, you can simply delete its folder with all its content. Either directly in the file system, or use the command line interface:
"""
rm -rf myfirstproject
"""
