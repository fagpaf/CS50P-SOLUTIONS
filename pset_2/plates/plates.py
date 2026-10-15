def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    """
    Verifica se a placa é válida conforme as regras:
    - 2 a 6 caracteres
    - Só letras e números
    - Começa com pelo menos 2 letras
    - Números, se existirem, devem estar no final e não começar com 0
    """

    # Verifica tamanho e se só tem letras e números
    if not (2 <= len(plate) <= 6) or not plate.isalnum():
        return False

    # Verifica se os dois primeiros são letras
    if not (plate[0].isalpha() and plate[1].isalpha()):
        return False

    # Localiza o primeiro dígito (se houver)
    for i in range(len(plate)):
        if plate[i].isdigit():
            # Se o primeiro número é zero → inválido
            if plate[i] == "0":
                return False
            # Depois do primeiro número, todos devem ser números
            if not plate[i:].isdigit():
                return False
            break

    return True


main()
