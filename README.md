# robotframework-axelibrary

Wrapper of [axe-selenium-python](https://github.com/mozilla-services/axe-selenium-python) for accessibility testing using robotframework

![PyPI version](https://badge.fury.io/py/robotframework-axelibrary.svg)
[![Downloads](https://pepy.tech/badge/robotframework-axelibrary)](https://pepy.tech/project/robotframework-axelibrary)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)
![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)

## Installation:

 To install robotframework-axelibrary
 ```
 $ pip install robotframework-axelibrary==0.1.3
 ```
 Keyword documentation [link](https://robotframework-axelibrary.netlify.app/)

## Usage:

 ```
*** Settings ***
Library    SeleniumLibrary
Library    AxeLibrary

*** Test Cases ***
Google Accessibility Test
    Open Browser    https://www.google.com/    Chrome
    
    # execute accessibility tests
    &{results}=    Run Accessibility Tests    google.json
    Log   Violations Count: ${results.violations}

    # log violation result to log.html
    Log Readable Accessibility Result    violations
    [Teardown]    Close All Browsers
 ```

### Robot Result

<img src="https://i.ibb.co/nkBqjXb/Robotframework-Axe-Library.png" alt="Robotframework-Axe-Library" border="0">

### Helpful Link

 - [Result Arrays](https://github.com/dequelabs/axe-core/blob/master/doc/API.md#result-arrays)