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
#
*** Test Cases ***
Edit AddressBook
    [Tags]    wip
    I add new address
    I edit an address
    The address should be edited

*** Test Cases ***
Delete AddressBook
    [Tags]    wip
    I add new address
    I delete an address
    The address should be deleted


*** Keywords ***
I add new address
    Open Add address page    add new
    Enter valid data

The address should be created
    Search an address    Address

I edit an address
    Open Edit address page with address name    Address
    I edit an address with the details
#    [Arguments]    ${First name}    ${Last name}    ${Address}
#    | First name   | Last name         | Address         |
#    | Updated Name | Updated Last Name | Updated address |

The address should be edited
    Search an address    AddressNew York
    Open Edit address page with address name    AddressNew York
    The address should be updated with appropriate details

I delete an address
    Delete an address    Middle name Last First name

The address should be deleted
    Search an address    Middle name Last First name
    Address should be deleted    Middle name Last First name