*** Settings ***
Documentation    Suite description
Test Setup    Open browser to Login page    ${URL}  ${BROWSER}
#Test Teardown    Close application
Library    Lib/steps_implementation/AddAddressSteps.py
Library    Lib/steps_implementation/LoginSteps.py
Resource   Resource/common.robot
#Variables    Variables  /variable.robot
#Test Template    I edit an address


*** Variables ***
${item_name}


*** Test Cases ***
Add new AddressBook
    [Tags]    wip
    Open browser to Login page    ${URL}  ${BROWSER}
    Attempt to login with valid credentials
    I add new address
    The address should be created

*** Test Cases ***
Edit AddressBook
    [Tags]    wip
    Open browser to Login page    ${URL}  ${BROWSER}
    Attempt to login with valid credentials
    I edit an address
#    I edit an address     First name      Last name            Address
#    [Arguments]           Updated Name    Updated Last Name    Updated address
#    The address should be edited


*** Keywords ***
I add new address
    Open Add address page    add new
    Enter valid data

The address should be created
    Search an address    Address

I edit an address
    Open Edit address page    Address7
#    I edit an address with the details    Updated Name    Last name   Address
#    [Arguments]    ${First name}    ${Last name}    ${Address}
#    | First name   | Last name         | Address         |
#    | Updated Name | Updated Last Name | Updated address |

#The address should be edited
#    The address should be edited with appropriate details
