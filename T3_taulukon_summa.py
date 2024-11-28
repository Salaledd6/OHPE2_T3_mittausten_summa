
luvut = [[3,1,4,1,5], [9,2,6,5,3], [5,8,9,7,9], [3,2,3,8,4], [6,2,6,4,3]]

def listan_summa(lista:list):
    summa = 0

    for alilista in lista:
        summa += sum(alilista)

    
    return summa

print(listan_summa(luvut))