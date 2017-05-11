'''
Step 1:
    The problem is asking for a function that takes in the numberArray of this Magic Square and verifies that it is truly a magic square.
    The program must check that the sum of vertical, horizontal, and diagnol rows is the same.

Step 2:
    I will be making a few assumptions for this problem. First I will be assuming that the user will be giving 5 lists, of which are each 5 numberArray long.
    These lists will be put into the function for it to solve. I plan on using simple list manipulation, if statements and possible while/for loops.
'''
def magic_square(list1,list2,list3,list4,list5):
    row_one=sum(list1)
    row_two=sum(list2)
    row_three=sum(list3)
    row_four=sum(list4)
    row_five=sum(list5)
    
    if row_one == row_two == row_three == row_four ==row_five:
        column_one=list1[0]+list2[0]+list3[0]+list4[0]+list5[0]
        column_two=list1[1]+list2[1]+list3[1]+list4[1]+list5[1]
        column_three=list1[2]+list2[2]+list3[2]+list4[2]+list5[2]
        column_four=list1[3]+list2[3]+list3[3]+list4[3]+list5[3]
        column_five=list1[4]+list2[4]+list3[4]+list4[4]+list5[4]
        if column_one == column_two == column_three == column_four == column_five:
            diag_one=list1[0]+list2[1]+list3[2]+list4[3]+list5[4]
            diag_two=list1[4]+list2[3]+list3[2]+list4[1]+list5[0]
            if diag_one == diag_two:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
list1=[11,18,25,2,9]
list2=[10,12,19,21,3]
list3= [4,6,13,20,22]
list4=[23,5,7,14,16]
list5=[17,24,1,8,15]
'''
Step 4:

Overall this code satified my needs. It is a bit complex and should be shortened down.
One way I did this was removing some for statements I used, and instead used the sum function.
In the end the code gives the expected result and would be hard to refactor more.
