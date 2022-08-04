*** Settings ***
Library                 AxeLibrary
Library                 Zoomba.GUILibrary


*** Test Cases ***
Google Accessibility Test With Zoomba
    [Documentation]     Test Run Accessibility Tests lib_instance variable with alternate library.
    [Teardown]                  Close All Browsers
    Open Browser                https://www.google.com/         Chrome
    Maximize Browser Window
    &{results}                  Run Accessibility Tests         google.json
    ...                         lib_instance=Zoomba.GUILibrary
    Log                         Violations Count: ${results.violations}
    Get Json Accessibility Result
    Log Readable Accessibility Result  violations
    Log Readable Accessibility Result  incomplete
