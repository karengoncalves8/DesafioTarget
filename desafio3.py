import json

with open('faturamento.json', 'r') as arquivo:
    dados = json.load(arquivo)

valor_min = 0
valor_max = 0
dias_faturados = 0
soma_valor = 0
for d in dados:
    valor = d['valor']
    if valor < valor_min: 
        valor_min = valor
    if valor > valor_max: 
        valor_max = d['valor']
    if valor != 0:
        soma_valor += valor
        dias_faturados += 1

media_mensal = soma_valor/dias_faturados

dias_maior_media =  sum(1 for d in dados if d['valor'] > media_mensal)

print(f'O menor valor de faturamento foi de R${valor_min}')
print(f'O maior valor de faturamento foi de R${valor_max}')
print(f'O número de dias no mês em que o valor de faturamento diário foi superior à média mensal foi de {dias_maior_media}')