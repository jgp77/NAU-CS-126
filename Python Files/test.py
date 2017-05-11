def list_numberArray():
    first_number=int(input('Input a number '))
    second_number=int(input('Input a number '))
    third_number=int(input('Input a number '))
    lis=[first_number, second_number, third_number]

def remove_lowest(list):
    return list.remove(min(list))
'''
    To remove the largest number it would be .remove(max(lis)).
    The way the function is set up, any amount of numberArray works
'''

def compare_lists(list1,list2):
    for num in list1:
        if num in list2:
            return True
    else:
        return False
    
def cred_for_class():
    class_level= input('What class level are you in? ').lower()
    credits_needed= {'freshman':0, 'sophomore':30, 'junior':60, 'senior':90}
    return(credits_needed[class_level])
