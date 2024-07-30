# This is a Django application 

# First, you need to set up your environment 

- pip3 install pipenv

# If you need to upgrade your pip, simply run this command: 

- pip install --upgrade pip

# Then, you are going to create the directory in which you store your project 

- mkdir {project}

# Go into the directory that you just created and run the following: 

- pipenv install django 

# After running this, you are going to want to cd into the virtual environment you just created
# The link will be provided by the terminal.

- cd {Users/name/.local/share/virtualenvs/{projectName}}

# In order to start your django project, run the following command: 

- django-admin startproject database

# In order to run your server on a specified port, run this command after: 

- python manage.py runserver

# edit the models.py file and make sure to call the components created in admin.py 
# any changes made to either file, make sure to create migrations, migrate them, then runserver

- python manage.py makemigrations 
- python manage.py migrate 
- python manage.py runserver

