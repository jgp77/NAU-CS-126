def concatenation(lst, indice_one, indice_two):
    while True:
        try:
            result=''
            while indice_one == (indice_two +1) or indice_one == (indice_two-1):
                print('Those indices are next to each other! Try again!')
                indice_one=int(input('Please enter a new first indice: '))
                indice_two=int(input('Please enter a new second indice: '))
            result += str(lst[indice_one])+str(lst[indice_two])
            break
            
        except IndexError:
            print('Those indices are incorrect!')
            indice_one=int(input('Please enter a new first indice: '))
            indice_two=int(input('Please enter a new second indice: '))

        except:
            print('Unknown Error! Try running the function again!')
            break
    return(result)
    

peanuts=concatenation(['peanut ','brittle','butter'], 1, 0)
print(peanuts)
