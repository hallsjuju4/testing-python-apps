# Set up

My version of this course has been updated for:
python 3.8 and the latest versions of the requirements at the time including:

- Flask
- behave
- beautifulsoup4
- selenium

We'll need a few things to install for this section:

- https://sites.google.com/a/chromium.org/chromedriver/downloads
- behave (http://pythonhosted.org/behave/)
- selenium (http://selenium-python.readthedocs.io/installation.html)


## Running the tests

To run the tests, you'll need to do this in a terminal (but remember to have the Flask app running!):

```bash
source venv/bin/activate
cd section10/code/
python -m behave tests/acceptance
```

If you want to run the tests in PyCharm, you'll need to create appropriate configurations. We cover this in the course!