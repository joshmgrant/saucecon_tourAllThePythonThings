# SauceCon Online - tour.AllThePythonThings() Code Samples

Hello there! If you're reading this, you have likely heard of [SauceCon](www.saucecon.com) and may have attended the [tour.allThePythonThings()](https://saucecon.com/agenda-2020/) talk. Here are the accompanying code samples. 

These samples are all written using Python 3.7. I recommend using a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/). 

To install all needed dependencies, run

```bash
pip install -r requirements.txt
```

To run the simple, unit-style Pytest tests, run

```bash
pytest test_unit.py
```

To run the plain old Selenium tests, run

```bash
pytest test_basic_selenium.py
```

To run the [Nerodia](https://github.com/watir/nerodia) tests, run

```bash
pytest test_nerodia.py
```

To run the [pytest-selenium](https://github.com/watir/nerodia) tests, run

```bash
pytest --driver Saucelabs --variables CHOICE_OF_JSON test_pytest_selenium.py
```

where `CHOICE_OF_JSON` is one of `chrome.json`, `safari.json` or `firefox.json`.

To run the Robot test using SeleniumLibrary, run

```bash
robot -A chrome_config.txt using_selenium_library.robot
```

To run the Robot test using the custom Python library, run

```bash
robot using_python_keywords.robot
```
