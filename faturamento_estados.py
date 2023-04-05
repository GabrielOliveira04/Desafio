faturamento_por_estado = {
    'SP':67836.43,
    'RJ':36678.66,
    'MG':29229.88,
    'ES': 27165.48,
    'OUTROS':19849.53
}

valor_total_mensal = sum(faturamento_por_estado.values())

percentuais = {estado:(faturamento/ valor_total_mensal) * 100 for estado, faturamento in faturamento_por_estado.items()}

for estado,percentual in percentuais.items():
    print(f"Percentual de representação de {estado}: {percentual:.2f}%")
