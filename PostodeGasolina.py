# --------Compahia de Taxi Tabajara-------#

gasolina = float(input(" Dígite o preço da gasolina R$ \n"))
alcool = float(input("Dígite o preço do álcool R$ \n"))
km = float(input("Quantos quilometros é pretendido percorrer: \n"))
print(f'{km :.2f} \n')
litro_cidade =  km / 12
litro_estrada = km / 8

resultado_gasolina_cidade = gasolina / litro_cidade * km
resultado_gasolina_estrada = gasolina / litro_estrada * km

resultado_alcool_cidade = alcool / litro_cidade * km
resultado_alcool_estrada = alcool / litro_estrada * km

print("---Gasolina na cidade---")
print(f'Seu carro para percorrer {km :.1f} km, gastará {litro_cidade :.2f} litros, que custará o valor de R$ {resultado_gasolina_cidade :.2f} quando usado na cidade. \n')

print("---Gasolina na estrada---")
print(f'Seu carro para percorrer {km :.2f} km, gastará {litro_estrada :.2f} litros, que custará o valor de R$ {resultado_gasolina_estrada :.2f} quando usado na estrada. \n')

print("---Alcool na cidade---")
print(f'Seu carro para percorrer {km :.2f} km, gastará {litro_cidade :.2f} litros, que custará o valor de R$ {resultado_alcool_cidade :.2f} quando usado na cidade. \n')

print("---Acool na estrada---")
print(f'Seu carro para percorrer {km :.2f} km, gastará {litro_estrada :.2f} litros, que custará o valor de R$ {resultado_alcool_estrada :.2f} quando usado na cidade. \n')
