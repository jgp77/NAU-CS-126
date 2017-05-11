def contains_apples(list_of_strings):
    for strings in list_of_strings:
        strings=str(strings).lower()
        if 'apple' in strings:
            return True

def day_of_week(current_day, number):
    day_to_numberArray={'Monday':1,'Tuesday':2,'Wenesday':3,'Thursday':4,'Friday':5,'Saturday':6,'Sunday':7}
    number_to_days={1:'Monday',2:'Tuesday',3:'Wenesday',4:'Thursday',5:'Friday',6:'Saturday',7:'Sunday'}
    current_number=day_to_numberArray[current_day.capitalize()]
    total_number=(current_number + number) % 7
    return number_to_days[total_number]

class Backpack():
    def __init__(self):
        self.backpack =[]

    def add_item(self,item):
        item=item.lower().capitalize()
        for items in self.backpack:
            if items == item:
                print(item + ' is already in your backpack, silly!')
                return''
        self.backpack.append(item)
        print(str(item) + ' has/have been added to your backpack!')

    def remove_item(self, item):
        item=item.lower().capitalize()
        self.backpack.remove(item)
        print(str(item) + ' has/have been removed to your backpack!')

    def __str__(self):
        for items in self.backpack:
            print(items)
        return ('Those are all the items in your backpack!')

if __name__=='__main__':
    list_of_strings=['Peanut Butter', 'Chocolate Cake', 'Apple Pie']
    print(contains_apples(list_of_strings))
    print(day_of_week('Monday', 5))
    back=Backpack()
    back.add_item('Book')
    print(back)
    back.add_item('Scroll')
    print(back)
    back.add_item('Mug')
    print(back)
    back.add_item('boOK')
    print(back)
    back.remove_item('Scroll')
    print(back)
