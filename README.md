# PythonQA_Selenium

### Homework to Selenium lesson 

#### PRECONDITION: install webdrivers on you local machine and add path in PATH variable

#### TO RUN TESTS:

`pytest -vs --headless --vlc --logs --video --browser={chrome/firehox/opera} --executor {ip_selenoid_server} --url={opencart_URL}`

where:

`--headless` - enable headless mode

`--vlc` - enable video streaming in Selenoid

`--logs` - enable logging in Selenoid

`--video` - enable video recording in Selenoid

`--browser` - choice browser

`--executor` - add ip address remote service, if "local" execute on local webdriver

`--url` - add opencard URL


#### Logs saved to the `logs/`
#### Screenshots when exceptions saved to the `screenshots/`
#### Tests generate allure report.
