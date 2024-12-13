import pandas as pd

# Carregar o arquivo Excel
excel_file = 'C:/Users/B901916/Documents/Local/artigo/csvdataset.xlsx'
df = pd.read_excel(excel_file, engine='openpyxl')

# Salvar o DataFrame em um arquivo CSV
csv_file = 'csvdataset.csv'
df.to_csv(csv_file, sep=';', index=False)

print(f"Arquivo Excel '{excel_file}' foi convertido com sucesso para o arquivo CSV '{csv_file}'.")