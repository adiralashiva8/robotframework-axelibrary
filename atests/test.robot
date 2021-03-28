*** Settings ***
Library    SeleniumLibrary
Library    AxeLibrary

*** Test Cases ***
Google Accessibility Test
    Open Browser    https://www.google.com/    Chrome
    &{results}=    Run Accessibility Tests    google.json
    Log   Violations Count: ${results.violations}
    Get Json Accessibility Result
    Log Readable Accessibility Result    violations
    Log Readable Accessibility Result    incomplete
    [Teardown]    Close All Browsers