## Api by Cep


### PROJETO

O projeto consiste em busca daods da API via o PyCep.

![Img](https://user-images.githubusercontent.com/63813811/194682655-63c7a583-3f56-4258-bb4c-291416bf97c2.png)


## Aplicabilidade

Realizamos o desenvolvimento para facilitar a busca de ceps manuais no site dos correios pelo usuário. Já que basta o usuário realizar o upload de uma base em excel no Google Colab com os ceps contento uma coluna chamada CEP e em seguir executar o código para  obter as informações de bairro.


+ Request (application/json)

    + Body

            {
                "code": "1rbUURjcp1KErn7Jgx7d",
                "client_id": "e70654d7f568d0",
                "client_secret": "156762a28c007a64ff",
                "redirect_uri": "urn:ietf:wg:oauth:2.0:oob:auto",
                "grant_type": "authorization_code"
            }

+ Response 200 (application/json)

    + Body

            {
                "access_token": "[access_token]",
                "token_type": "Bearer",
                "expires_in": 900,
                "refresh_token": "[refresh_token]",
                "personal_token": "[token_string]"
            }


## Tks!
