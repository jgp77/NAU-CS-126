class People:
    count=0
    def __init__(self, name, race, eye_color):
        People.count +=1
        self._name=name
        self._race=race
        self._eye_color=eye_color
        self._is_public=True
    def setPublic(self):
        self._is_public=True
    def setPrivate(self):
        self._is_public=False
    def _displayinformation(self):
        if self._is_public == True:
            return ('Name: '+self._name+'\nRace: '+self._race+'\nEye color: '+
                    self._eye_color+'.\nThere are/is ' + str(People.count)+' people/person.\n')
        elif self._is_public == False:
            return('Private information, sorry.')
    def _getname(self):
        return self._name
    def __str__(self):
        if self._is_public == True:
            return self._displayinformation()
        elif self._is_public == False:
            return self._getname()
    def __eq__(self, other):
        if self._name == other._name and self._race==other._race and \
           self._eye_color==other._eye_color:
            return True
        else:
            return False
josh=People('Josh','White','Green')
print(josh)
jacob=People('Jacob', 'White', 'Brown')
print(jacob)
pollock=People('Josh','White','Green')
print(pollock)
if josh == jacob or josh == pollock or jacob == pollock:
    print('There are similar people here!')

else:
    print('Wow, you are all unique!')

        
