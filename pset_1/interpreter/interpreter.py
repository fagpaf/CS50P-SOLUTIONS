def main():
    result = operation(input("Expression: "))
    print(f"{result:.1f}")

def operation(prompt):
    """
    Esta função recebe uma string como 'expressão matemática' (ex: "-10 - -5"),
    extrai os dois operandos e o operador, trata corretamente sinais negativos
    e realiza a operação aritmética, retornando o resultado como float.
    """
    prompt = prompt.replace(" ", "")  # Remove espaços em branco da string
    x = ""         # Primeiro número
    z = ""         # Segundo número
    operator = ""
    flag = 0       # Flag para indicar quando começar a construir o segundo número (z)

    for i in range(len(prompt)):  # Percorre cada caractere da string
        char = prompt[i]

        # Detecta operador, mas evita confundir com sinal negativo no início dos números
        if char in "+-*/" and i != 0 and prompt[i - 1] not in "+-*/":
            operator = char       # Armazena o operador
            flag = 1              # Sinaliza que a partir de agora começa a montar o segundo número (z)
            continue              # Pula o operador e segue para o próximo caractere

        # Constrói o primeiro ou segundo número com base na flag
        if flag == 0:
            x += char
        else:
            z += char

    # Convertendo para as strings para inteiro
    a = int(x)
    b = int(z)

    # Realiza a operação com match-case
    match operator:
        case "+":
            result = a + b
        case "-":
            result = a - b
        case "*":
            result = a * b
        case "/":
            result = a / b
        case _:
            result = 0  # Caso padrão (operação não reconhecida)

    return float(result)

main()
