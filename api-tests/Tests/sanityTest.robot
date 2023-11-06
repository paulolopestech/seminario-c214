*** Settings ***
Library           RequestsLibrary

*** Test Cases ***
Get Pokemon Details
    [Documentation]    Get details of a specific Pokémon from the PokeAPI
    Create Session    PokeAPI    https://pokeapi.co/api/v2

Check Status Code
    [Documentation]    Verify the status code of a GET request to the PokeAPI
    Create Session    PokeAPI    https://pokeapi.co/api/v2
    ${RESPONSE}    Get Request    PokeAPI    /pokemon/pikachuW
    Should Be Equal As Strings    ${200}    200



