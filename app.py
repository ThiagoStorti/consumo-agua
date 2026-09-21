"""Sistema de Classificação de Consumo de Água
Classifica o consumo mensal de água de acordo com
o tipo de imóvel informado pelo usuário."""

print("SISTEMA DE CONSUMO DE ÁGUA")
tipo_imovel = input("Digite o tipo de imóvel (comercial, casa ou apartamento):")
consumo = float(input("Digite o consumo mensal de água em m³:"))

# Verifica se o tipo informado está entre as opções permitidas.
tipos_validos = ["comercial", "casa", "apartamento"]

if not tipo_imovel in tipos_validos:
    print("Tipo de imóvel inválido.")
else:
    match tipo_imovel:

        case "comercial":
            print("Tarifa comercial aplicada – " "consulte o plano corporativo.")

        case "apartamento" if (consumo <10):
            print("Consumo econômico – " "excelente controle de água!")

        case "apartamento" | "casa" if ((tipo_imovel == "apartamento" and consumo <= 25) or (tipo_imovel == "casa" and consumo <= 25)):
            print("Consumo moderado – " "dentro do padrão residencial.")

        case _:
            print("Consumo excessivo – " "adote medidas de economia e verifique vazamentos.")