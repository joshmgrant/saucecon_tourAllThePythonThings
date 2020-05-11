*** Settings ***
Documentation     A test suite with two login test cases.
Resource          resource.robot


*** Test Cases ***

Invalid Login
	Open Login Page

	Login As Invalid User
  
  	Page should contain element  class:error-button

	[Teardown]  End Session

Valid Login with Standard User
	Open Login Page

	Login As Standard User

	Page should contain element  id:shopping_cart_container

	[Teardown]  End Session
