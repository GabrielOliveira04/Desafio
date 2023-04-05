import json


with open('faturamento.json', 'r') as file:
    faturamento_data = json.load(file)


faturamento_diario = [dia['valor'] for dia in faturamento_data]
menor_faturamento = min(faturamento_diario)


maior_faturamento = max(faturamento_diario)


media_mensal = sum(faturamento_diario) / len(faturamento_diario)


dias_acima_da_media = len([dia for dia in faturamento_diario if dia > media_mensal])


print(f"Menor faturamento diário: R$ {menor_faturamento:.2f}")
print(f"Maior valor de faturamento em um dia do mês: R$ {maior_faturamento:.2f}")
print(f"Média mensal de faturamento: R$ {media_mensal:.2f}")
print(f"Número de dias acima da média mensal: {dias_acima_da_media}")
