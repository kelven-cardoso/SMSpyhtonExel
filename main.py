import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC0a3ea51a4d2897f7da3e4d71588d92c0"
# Your Auth Token from twilio.com/console
auth_token  = "cdab3e17712b07331cda61c389c4e936"
client = Client(account_sid, auth_token)

lista_meses = ['janeiro' , 'fevereiro', 'março', 'abril','maio', 'junho']

for mes in lista_meses:
   # print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 50000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas =  tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'\nNo mês {mes}, encontrou {vendedor} com o valor R$ {vendas} ')
        message = client.messages.create(
            to="+5596992054287", 
            from_="+14178157023",
            body=f'No mês {mes}, encontrou {vendedor} com o valor R$ {vendas}')

        print(message.sid)








