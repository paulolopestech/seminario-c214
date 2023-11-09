*** Settings ***
Library         ../../Plotter.py

*** Variables ***
${PLOTINPUT}    [1]
${BUFFERPATHRESPONSE}    ./src/buffer/data_plot.png

*** Test Cases ***

Testing returned path from buffer
    ${response}=    Plot    ${PLOTINPUT}
    Should Be Equal As Strings    ${response}    ${BUFFERPATHRESPONSE}