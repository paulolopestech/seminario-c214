*** Settings ***
Library        ../../WebServer.py
Library        ../../webserver_keywords.py


*** Test Cases ***
Testing WebServer instance
    ${flaskMock}=    Get Flask Mock Instance
    ${flaskRequestMock}=    Request Mock
    ${instance}=    Get Web Server Instance    ${flaskRequestMock}    ${flaskMock}
    ${parameter}=    Get Flask Instance From Web Server    ${instance}
    Should Be Equal    ${parameter}    ${flaskMock}

Test WebServer Functionality
    ${flaskMock}=    Get Flask Mock Instance
    ${flaskRequestMock}=    Request Mock
    ${webServerInstance}=    Get Web Server Instance    ${flaskRequestMock}    ${flaskMock}