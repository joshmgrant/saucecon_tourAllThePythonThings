*** Settings ***
Documentation     A test suite with a single test for valid login.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Library          resource.py
Library          resource.SauceDemo


*** Test Cases ***

Invalid Login
	Start Session

	Open Login Page

	Login As User  invalid  invalid
  
  	Page should contain error

	[Teardown]  End Session

Valid Login with Standard User
	Start Session

	Open Login Page

	Login As User  standard_user  secret_sauce

	Should Be On Inventory Page

	[Teardown]  End Session
