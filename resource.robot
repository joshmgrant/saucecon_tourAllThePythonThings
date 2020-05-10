*** Settings ***
Library  SeleniumLibrary

*** Variables ***

@{_tmp} 
    ...  browserName: ${browserName},
    ...  platform: ${platform},
    ...  version: ${version},
    ...  username: %{SAUCE_USERNAME},
    ...  accessKey: %{SAUCE_ACCESS_KEY},
    ...  name: ${SUITE_NAME},
    ...  build: Python-Robot-Selenium-VDC

${browser}          ${browserName}
${capabilities}     ${EMPTY.join(${_tmp})} 
${remote_url}       https://ondemand.saucelabs.com/wd/hub/

*** Keywords ***

Open login page
    Open browser  https://www.saucedemo.com  browser=${browser}
    ...  remote_url=${remote_url}
    ...  desired_capabilities=${capabilities}


Login As Standard User

    Input text  id:user-name  standard_user
	Input text  id:password  secret_sauce
	Click button  class:btn_action


Login As Invalid User

    Input text  id:user-name  invalid
	Input text  id:password  invalid
	Click button  class:btn_action


End Session
    Run Keyword If  '${TEST_STATUS}'== 'PASS'  Execute Javascript  sauce:job-result=passed
    ...  ELSE  Execute Javascript  sauce:job-result=failed
    Close Browser
