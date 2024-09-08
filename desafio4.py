faturamento = {'SP': 67836.43, 'RJ': 36678.66, 'MG':29229.88, 'ES':27165.48, 'Outros': 19849.53}

total_mensal = sum([faturamento[d] for d in faturamento])

for d in faturamento:
    percentual = (faturamento[d] / total_mensal) * 100
    print(f'Percentual de representação - {d}: {percentual:.2f}%')