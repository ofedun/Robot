*** Settings ***
Documentation    Suite description
Library    Lib/steps_implementation/AddAddressSteps.py
Library    Lib/steps_implementation/LoginSteps.py
Resource   Resource/common.robot
#Variables    Variables/common.robot


*** Variables ***
${item_name}    add new


*** Test Cases ***
Add new AddressBook
    [Tags]    wip
    Open browser to Login page    ${URL}  ${BROWSER}
    Attempt to login with valid credentials
    I add new address
#    The address should be created


*** Keywords ***
I add new address
#    [Arguments]    ${item_name}
    Open Add address page    ${item_name}
    Enter valid data

#The address should be created
