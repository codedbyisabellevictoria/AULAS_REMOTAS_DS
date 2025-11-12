# atividade dia 08/11

def calculadora(numero1, numero2, operacao):
    if operacao == '+':
        return numero1 + numero2
    elif operacao == '-':
        return numero1 - numero2
    elif operacao == '*':
        return numero1 * numero2
    elif operacao == '/':
        if numero2 != 0:
            return numero1 / numero2
        else:
            return "Erro: divisao por zero"
    else:
        return "Operacao invalida"