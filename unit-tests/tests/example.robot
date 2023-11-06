*** Settings ***
Documentation             Primeiro teste robot
Library                   ../api-functions/example.py

*** Test Cases ***
Teste Soma Básica
    ${resultado} =  Somar  ${2}   ${3}
    Should Be Equal  ${resultado}  ${5}  # Compara o resultado com o valor esperado como strings


