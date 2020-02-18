## Pitch
## Author
phelisia jeruto
## Description
This is an app that shows diffrent pitches posted by diffrent users


## Features
Log in and Sign up
Welcome Mail
Create pitch
Update Profile
User Stories
As a user of the web application you will be able to:

View pitches based on categories
Sign up and log in
Receive welcome mail
Add a pitch based on category
Comment on a pitch and view other comments
Edit user profile: View all your posted pitches; Update bio and profile image
Getting started
Prerequisites
python3.6
virtual environment
pip
Clone the repository and cd to Pitch

Running the App
Create a virtual environment $ python3.6 -m venv --without-pip virtual

Activate the virtual environment using $ source virtual/bin/activate

Download pip in our environment using $ curl https://bootstrap.pypa.io/get-pip.py | python

Install all the dependencies from the requirements.txt file by running python3.6 pip install -r requirements.txt

Add a secret_key, mail_username and mail_password to your environment. In a folder named instance, file named config.py

(optional) Create a start.sh to easily run the app:

  export MAIL_USERNAME=<your-email-address>
  export MAIL_PASSWORD=<your-email-password>
  export SECRET_KEY=<your-secret-key>

  python3 manage.py server
Make the start.sh an executable by changing permissions:

  $ chmod a+x start.sh
Start the app using: $ ./start.sh

In the config.py choose which mode to run your app(use development or test at first)

Testing the Application
To run the tests for the class file:

  $ python3.6 manage.py test
Technologies Used
Python3.6
Flask
Developed by
Mutugi Mutuma

## License
MIT License MIT License
