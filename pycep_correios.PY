

import pandas as pd
import pycep_correios

# Read the CEPs from an Excel file
df = pd.read_excel('CEP.xlsx')

# Create an empty DataFrame to store the address information
address_df = pd.DataFrame(columns=['CEP', 'Endereço', 'Bairro', 'Cidade', 'UF'])

# Iterate over each CEP
for cep in df['CEP']:
    try:
        # Retrieve the address information for the current CEP
        endereco = pycep_correios.get_address_from_cep(str(cep))
        # Extract the required fields from the address information
        cep_data = {
            'CEP': cep,
            'Endereço': endereco['logradouro'],
            'Bairro': endereco['bairro'],
            'Cidade': endereco['cidade'],
            'UF': endereco['uf']
        }
        # Append the address data to the DataFrame
        address_df = address_df.append(cep_data, ignore_index=True)
    except:
        # Handle any exceptions that occur during address retrieval
        pass

# Save the address data to a new Excel file
address_df.to_excel('address_data.xlsx', index=False)
