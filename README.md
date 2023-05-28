## Api by Cep


![Img](https://user-images.githubusercontent.com/63813811/194682655-63c7a583-3f56-4258-bb4c-291416bf97c2.png)


## About this Project

The idea of ​​the program is:

_"The project consists of fetching API data via PyCep"._

**PS:** We carried out the development to facilitate the search for manual zip codes on the postal service website by the user. As the user only has to upload a base in excel on Google Colab with the zip codes containing a column called CEP and then run the code to obtain the neighborhood information.

🤩:**


## Some notes about this app

1 - We use the google colab platform to use the application

## Functionalities

- Query bulk data through the PyCep api and thereby return customer address data
     

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

## Contributing

You can send how many PR's do you want, I'll be glad to analyse and accept them! And if you have any question about the project...

Email-me: pauloseng80@gmail.com.com

Connect with me at [LinkedIn](https://www.linkedin.com/in/pauloroch/)

Thank you!

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/paul0rocha/mindCast/blob/master/LICENSE) file for details

