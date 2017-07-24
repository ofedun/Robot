*** Settings ***
Documentation    Suite description
#Suite Teardown    Close All Browsers
Library    Lib/steps_implementation/LoginSteps.py
Library    Lib/steps_implementation/Browser.py
Resource    Resource/common.robot

*** Variables ***
${BROWSER}    Chrome
${URL}    http://localhost/addressbook/
${username}    admin
${password}    secret
${GLOBAL_TIMEOUT}    10


*** Keywords ***
Open browser to Login page
    [Arguments]    ${URL}    ${BROWSER}
    Open Login page    ${URL}  ${BROWSER}

Attempt to login with valid credentials
    Enter Username    ${username}
    Enter Password    ${password}
    Click Login Button

I am logged in on main page
    Is logged in on main page    ${username}

Close application
    Close browser
