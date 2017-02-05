while True:
    ano = int(input("Insira um ano: "))

    if (ano % 4 == 0) and (ano % 100 > 0):
        print("é bissexto")
    elif (ano % 400 == 0):
        print("É bissexto")
    else:
        print("não é bissexto")
