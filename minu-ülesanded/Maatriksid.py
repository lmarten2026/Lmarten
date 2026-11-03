def print_maatriks(matrix):
    for el in matrix:
        print(el)

def print_peadiagonaal(matrix):
    suurus = len(matrix)
    for el in range (suurus):
        #print(el, suurus - el -1)
        print(matrix[el][- el -1]) #el tähendab length -1 on tgalt poolt esimene number

maatriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#print_maatriks(maatriks)
print_peadiagonaal(maatriks)