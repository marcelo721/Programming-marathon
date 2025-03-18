c = 1
while True:
    C1 = input()
    if C1 == '0':
        break

    list1 = list(C1)
    positionY = int(list1[0])
    positionX = list1[1]

    listT = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    positionX = listT.index(positionX) + 1

    peoes = []
    for _ in range(8):
        entrada = input()
        list2 = list(entrada)
        peaoY = int(list2[0])
        peaoX = listT.index(list2[1]) + 1
        peoes.append((peaoY, peaoX))

    movimentos = [
        (positionY + 2, positionX - 1),
        (positionY + 2, positionX + 1),
        (positionY + 1, positionX + 2),
        (positionY - 1, positionX + 2),
        (positionY - 2, positionX + 1),
        (positionY - 2, positionX - 1),
        (positionY - 1, positionX - 2),
        (positionY + 1, positionX - 2)
    ]

    total = 0
    for move in movimentos:
        if 1 <= move[0] <= 8 and 1 <= move[1] <= 8:
            bloqueado = False
            for peao in peoes:
                if (peao[0] - 1 == move[0] and peao[1] - 1 == move[1]) or (peao[0] - 1 == move[0] and peao[1] + 1 == move[1]):
                    bloqueado = True
                    break
            if not bloqueado:
                total += 1

    print(f"Caso de Teste #{c}: {total} movimento(s).")
    c += 1