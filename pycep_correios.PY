!pip install -q pycep_correios

import pandas as pd 
import numpy as np

df = pd.read_excel('LOCCCC.xlsx')

from pycep_correios import get_address_from_cep, WebService

address = get_address_from_cep('65350-000', webservice=WebService.CORREIOS)

address

def tryget(cep):

   try:
     return get_address_from_cep(cep, webservice=WebService.CORREIOS)['bairro']
   except:
     None
     
   dados = df['bairro'] = df['CEP'].apply(lambda x: (tryget(x)))
   
   df.to_excel('do.xlsx')
