class People():

    def __init__(self):
        self.name=''
        self.hair_color=''
        self.age=''
        self.public_access=''
    def get_name(self):
        return self.name
    def get_hair_color(self):
        return self.hair_color
    def get_age(self):
        return self.age
    def get_public_access(self):
        return self.public_access
    def set_name(self,x):
        self.name=x
    def set_hair_color(self,x):
        self.hair_color=x
    def set_age(self,x):
        self.age=x
    def set_public_access(self,x):
        self.public_acces=x

josh=People()
josh.set_age('19')
josh.set_name('Josh')
josh.set_hair_color('Blonde/Brownish')
josh.set_public_access('yes')
