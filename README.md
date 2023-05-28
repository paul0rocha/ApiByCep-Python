## Api by Cep


 ![Img](https://github.com/steniowagner/mindCast/assets/63813811/4c0f7c9a-4e72-4987-b507-2e5549d6f7a0)



## About this Project

The idea of ​​the program is:

_"The project consists of fetching API data via PyCep"._

**PS:** We carried out the development to facilitate the search for manual zip codes on the postal service website by the user. As the user only has to upload a base in excel on Google Colab with the zip codes containing a column called CEP and then run the code to obtain the neighborhood information.

🤩:**


## Some notes about this app

1 - We use the google colab platform to use the application

## Functionalities

- Query bulk data through the PyCep api and thereby return customer address data  

## Use

- Upload the file excel to google colab
 
 
![Img](https://github.com/steniowagner/mindCast/assets/63813811/6202b53b-5431-4626-a4af-6f66f1b176cc)
   
    

### RequesT

 endereco = pycep_correios.get_address_from_cep(str(cep))
  
+ Response 200 (application/json)

    + Body

            {
                 'bairro': None,
                 'cep': '65350000',
                 'cidade': 'Vitória do Mearim',
                 'logradouro': None,
                 'uf': 'MA',
                 'complemento': None
            },
            {
                 'bairro': None,
                 'cep': '18147000',
                 'cidade': 'Aracariguama',
                 'logradouro': None,
                 'uf': 'SP',
                 'complemento': None
            }
            


**Installing dependencies**


```
pip install pycep-correios==4.0.3
```
 ![Img](https://github.com/steniowagner/mindCast/assets/63813811/46842741-3b16-4ed8-bb08-30cbd75e59d9)




## Contributing

You can send how many PR's do you want, I'll be glad to analyse and accept them! And if you have any question about the project...

Email-me: pauloseng80@gmail.com.com

Connect with me at [LinkedIn](https://www.linkedin.com/in/pauloroch/)

Thank you!

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/paul0rocha/mindCast/blob/master/LICENSE) file for details

