## Api by Cep


### PROJETO

O projeto consiste em busca daods da API via o PyCep.

![Img](https://user-images.githubusercontent.com/63813811/194682655-63c7a583-3f56-4258-bb4c-291416bf97c2.png)


## Aplicabilidade

Realizamos o desenvolvimento para facilitar a busca de ceps manuais no site dos correios pelo usuário. Já que basta o usuário realizar o upload de uma base em excel no Google Colab com os ceps contento uma coluna chamada CEP e em seguir executar o código para  obter as informações de bairro.


### RequesT

 address = get_address_from_cep('65350-000', webservice=WebService.CORREIOS)
  
+ Response 200 (application/json)

    + Body

            {
                 'bairro': None,
                 'cep': '65350000',
                 'cidade': 'Vitória do Mearim',
                 'logradouro': None,
                 'uf': 'MA',
                 'complemento': None
            }


### Tks!
