*** Settings ***
Library    Lib/steps_implementation/LoginSteps.py
Documentation    Login Feature

*** Keywords ***
Open browser to Login page
    Open Login page
Login
    [Arguments]    ${username}    ${password}
#    Open Login page
    Attempt to login with credentials    ${username}    ${password}
    I am logged in on main page

#*** Variables ***
#${Name_of_category} Test Product Category
#${BROWSER} chrome
#${HOMEPAGE}

*** Test Cases ***
Login to AddressBook
    [Tags]    robot
    Open Login page
    Attempt to login with credentials   admin   secret
    I am logged in on main page
