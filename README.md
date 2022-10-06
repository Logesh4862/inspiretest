# inspiretest

Steps to Follow
1. Install Python
  https://www.python.org/downloads/
2. Install PIP
    - Download the script, from https://bootstrap.pypa.io/get-pip.py.
    - python get-pip.py
3. Install Virtual Environment
    - python -m pip install virtualenv
4. Create a Virtual environment to Project
    - python -m venv ENVNAME
    - cd ENVNAME
5. Activate Environment
    - For Windows
        - scripts\activate.bat
    - For Linux
        - source scripts/activate
6. Create APP Directory
    - mkdir APPNAME
    - cd APPNAME
7. Clone Code
    - git clone https://github.com/Logesh4862/inspiretest.git
8. Install required Packages
    - pip install -r requirements.txt
9. Run server
    - python manage.py runserver
    - Server by default listed on 8000 port. To change port
        - python manage.py runserver localhost:<PORT>
10. Access Page in Any browser
    - URL : localhost:8000
