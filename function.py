# def perkalian(a, b):
#     return a * b

# hasil = perkalian(90, 2)
# print(hasil)

def derdor(a) :
    i = 1
    for i in range(a) :
        if i % 4 == 0 or i % 7 == 0 :
            if i % 4 == 0 and i % 7 == 0 :
                print('derdor')
            elif i % 4 == 0 :
                print('dor')
            elif i % 7 == 0 :
                print('der')
        else :
            print(i)
        i += 1

derdor(29)