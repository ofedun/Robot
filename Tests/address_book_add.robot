*** Settings ***
Documentation    Suite description
Library    Lib/steps_implementation/AddAddressSteps.py
Library    Lib/steps_implementation/LoginSteps.py
Resource   Resource/common.robot
##Documentation    Add new AddressBook Feature
#Variables    /login.robot

*** Test Cases ***
Add new AddressBook
    [Tags]    robot
    Open browser to Login page
    Attempt to login with valid credentials
    I add new address
#    The address should be created

*** Keywords ***
I add new address
    Open Add New address page
    Enter valid data

#The address should be created
