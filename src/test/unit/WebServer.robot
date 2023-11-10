*** Settings ***
Library        ../../WebServer.py
Library        ../../webserver_keywords.py


*** Test Cases ***
Testing WebServer instance
    ${flaskMock}=    Get Flask Mock Instance
    ${instance}=    Get Web Server Instance    ${flaskMock}
    ${parameter}=    Get Flask Instance From Web Server    ${instance}
    Should Be Equal    ${parameter}    ${flaskMock}

Test WebServer Functionality
    ${flaskMock}=    Get Flask Mock Instance
    ${webServerInstance}=    Get Web Server Instance    ${flaskMock}