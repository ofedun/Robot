*** Settings ***
Documentation    Example suite
Suite Setup
Force Tags       example
Library          Lib/steps_implementation/LoginSteps.py
Library    pages.login.login_page

*** Variables ***
${MESSAGE}       Hello, world!

*** Test Cases ***
Login to AddressBook
    [Tags]    robot
    Open Login page
    Attempt to login with credentials   admin   secret
    I am logged in on main page

*** Keywords ***
Login
    [Arguments]    ${username}    ${password}
    Attempt to login with credentials    ${username}    ${password}
    I am logged in on main page
