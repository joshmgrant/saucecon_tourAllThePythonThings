*** Settings ***
Documentation     A test suite with a single test for valid login.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
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
