*** Settings ***
Documentation    Suite description
Test Setup    Open browser to Login page    ${URL}  ${BROWSER}
Test Teardown    Close application
Library    Lib/steps_implementation/AddAddressSteps.py
Library    Lib/steps_implementation/LoginSteps.py
Resource   Resource/common.robot
#Variables    Variables  /variable.robot


*** Variables ***
${item_name}
${address_name}    Address


*** Test Cases ***
Add new AddressBook
    [Tags]    wip
    Open browser to Login page    ${URL}  ${BROWSER}
    Attempt to login with valid credentials
    I add new address
    The address should be created

Edit AddressBook
    [Tags]    wip
    Open browser to Login page    ${URL}  ${BROWSER}
    Attempt to login with valid credentials
    I edit an address
    The address should be edited


*** Keywords ***
I add new address
    Open Add address page    add new
    Enter valid data

The address should be created
    Search an address    ${address_name}    Address

I edit an address
    Open Edit address page    ${item_name}    home
    I edit the address

The address should be edited
    The address should be edited with appropriate details
