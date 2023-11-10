*** Settings ***
Library         ../../Plotter.py
Library         ../../plotter_keywords.py

*** Variables ***
${PLOTINPUT}    [1]
${PLOTINPUTERROR}    -1
${BUFFERPATHRESPONSE}    buffer/data_plot.png

*** Test Cases ***

Testing Plotter instance
    ${instance}=      PlotterInstance   data_plot.png
    ${parameter}=     GetPlotPath       ${instance}
    Should Be Equal    ${parameter}    data_plot.png

Testing returned path from buffer
    ${response}=    Plot    ${PLOTINPUT}
    Should Be Equal As Strings    ${response}    ${BUFFERPATHRESPONSE}

Testing returned path from buffer when data is error
    ${response}=    Plot    ${PLOTINPUTERROR}
    Should Be Equal As Strings    ${response}    ${BUFFERPATHRESPONSE}