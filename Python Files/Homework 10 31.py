def pig_sentence():
    vowels=['a','e','i','o','u']
    sentence=input('Enter a sentence: ').lower()
    sentence=sentence.split(' ')
    final_sentence=''
    for word in sentence:
        if word[0] in vowels:
            final_sentence += word + "yay" + " "
        else:
            count=0
            for letter in word:
                if letter not in vowels: 
                    count += 1
                    continue
                else: 
                    break
            final_sentence+= word[count:] + word[:count] + 'ay' + ' '
    return final_sentence[:len(final_sentence) - 1]

def pig_file(file_name):
    vowels=['a','e','i','o','u']
    not_translated=open(file_name,'r')
    translated=[]
    words=[]
    for line in not_translated:
        words += line.split()
    final_sentence=''
    for word in words:
        if word[0] in vowels:
            final_sentence += word + "yay" + " "
        else:
            count=0
            for letter in word:
                if letter not in vowels: 
                    count += 1
                    continue
                else: 
                    break
            final_sentence+= word[count:] + word[:count] + 'ay' + ' '
    return final_sentence[:len(final_sentence) - 1]

def population():
    file=('PEP_2013_PEPANNRES_with_ann.csv','r')
    line_counter=0
    for line_counter, line in enumerate(file):
        if line_counter<3:
            continue
        data=line.split(',')
        state=data[2]
        population=data[8]
        formated_number=format(int(data[8]),',d')
        return(state+': '+formated_number)
