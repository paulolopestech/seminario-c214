*** Settings ***
Library        ../../WebServer.py
Library        ../../webserver_keywords.py


*** Test Cases ***
WebServer Should instance with parameters
    ${flaskMock}=    Get Flask Mock Instance
    ${sendFileMock}=    Send File Mock
    ${plotterMock}=   Get Plotter Mock
    ${requestMock}=    Request Mock
    ${instance}=    Get Web Server Instance    ${flaskMock}    ${sendFileMock}    ${requestMock}    ${plotterMock}
    ${parameter}=    Get Flask Instance From Web Server    ${instance}
    Should Be Equal    ${parameter}    ${flaskMock}

WebServer Should Have an active instance
    ${flaskMock}=    Get Flask Mock Instance
    ${sendFileMock}=    Send File Mock
    ${plotterMock}=   Get Plotter Mock
    ${requestMock}=    Request Mock
    ${webServerInstance}=    Get Web Server Instance    ${flaskMock}    ${sendFileMock}    ${requestMock}    ${plotterMock}
    