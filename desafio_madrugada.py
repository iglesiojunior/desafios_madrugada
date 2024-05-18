def militar_to_AMPM(hrs, min):
    horas_convertidas = 0
    formato_hora = ""
    if hrs > 12:
        formato_hora = "PM"
        horas = hrs - 12
    else:
        formato_hora = "AM"
        horas_convertidas = hrs
    return[horas_convertidas, min, formato_hora]

def AMPM_to_militar(hrs, min, formato_hora):
    horas_convertidas = 0
    if formato_hora.lower() == "am":
        horas_convertidas = hrs
    elif formato_hora.lower() == "pm":
        horas_convertidas = hrs+12
    return[horas_convertidas, min]

def main():
    menu = """
==========================================================
Escolha um serviço:
1 - Converter horas militares para formato AM/PM
2 - Converter horas em formato AM/PM para formato militar
0 - Encerrar programa
==========================================================
"""

    tipo_serviço = 1
    hrs = 0
    min = 0
    formato_hora = ""

    while tipo_serviço != 0:
         
        tipo_serviço = int(input(menu))

        if tipo_serviço == 1:
            hrs, min = map(int, input("Insira as horas e minutos militares(Use o sinal "":"" para dividir horas de minutos):").split(":"))
            conversao = militar_to_AMPM(hrs, min)
            print(f"Olá, a sua conversão é equivalente a: {conversao[0]}:{conversao[1]} {conversao[2]}")
        elif tipo_serviço == 2:
            hrs, min, formato_hora = input("Insira as horas e minutos no formato: horas:min:am/pm(Use o sinal "":"" para dividir horas de minutos):").split(":")
            hrs, min = int(hrs), int(min)
            conversao = AMPM_to_militar(hrs, min, formato_hora)
            print(f"Olá, a sua conversão é equivalente a: {conversao[0]}:{conversao[1]}")
        
        tipo_serviço = int(input('Deseja fazer outra conversão?(Digite 0 para encerrar o programa): '))
main()