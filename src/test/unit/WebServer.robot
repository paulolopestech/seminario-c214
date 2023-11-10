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

WebServer should be return a string at the flaskMock variable
    ${flaskMock}=    Get Flask Mock Instance
    ${sendFileMock}=    Send File Mock
    ${plotterMock}=   Get Plotter Mock
    ${requestMock}=    Request Mock
    ${instance}=    Get Web Server Instance    ${flaskMock}    ${sendFileMock}    ${requestMock}    ${plotterMock}
    ${flaskInstance}=   Get Flask Instance From WebServer   ${instance}
    Should Be Equal As Strings   ${flask_instance}   ${flaskMock}

Test Execute WebServer Router Handler
    ${flaskMock}=    Get Flask Mock Instance
    ${sendFileMock}=    Send File Mock
    ${plotterMock}=   Get Plotter Mock
    ${requestMock}=    Request Mock
    ${instance}=    Get Web Server Instance    ${flaskMock}    ${sendFileMock}    ${requestMock}    ${plotterMock}
    ${flaskInstance}=   Get Flask Instance From WebServer   ${instance}
    Execute WebServer Router Handler    ${flaskInstance}
