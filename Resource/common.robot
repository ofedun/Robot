*** Settings ***
Documentation    Suite description
Documentation     An example resource file
Library           Selenium2Library
Library    Lib/steps_implementation/LoginSteps.py
Resource    Resource/common.robot

*** Variables ***
${BROWSER}    Chrome
${URL}    http://localhost/addressbook/
${username}    admin
${password}    secret


*** Test Cases ***
Login to AddressBook
    Open browser to Login page    ${URL}  ${BROWSER}
    Attempt to login with valid credentials
    I am logged in on main page


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