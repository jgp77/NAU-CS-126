import random


class DiceRoller:
    # Utiltiy class for dice rolling

    def roll(self, times, sides):
        total=0
        for i in range(times):
            roll=random.randint(1, sides)
            total += roll
        return total
r=DiceRoller()


class Attack:
    # A class used for calculating attack

    def __init__(self, name, number_of_die, sides_of_die, damage_type):
        self._name=name
        self._sides=sides_of_die
        self._number=number_of_die
        self._type=damage_type

    def get_attack_type(self):
        # Returns the type of attack as a string
        return self._type

    def get_damage(self):
        # Returns a damage value for this attack
        return DiceRoller.roll(DiceRoller, self._number, self._sides)

    def get_name(self):
        return self._name

    def get_sides(self):
        return self._sides

    def get_num_die(self):
        return self._number


class Adventurer:

    def __init__(self, name, hit_points, defense, magic_defense, initiative):
        self._name=name
        self._health=hit_points
        self._defense=defense
        self._mdefense=magic_defense
        self._initiative=initiative

    def is_alive(self):
        if self._health > 0:
            return True
        elif self._health <= 0:
            return False

    def roll_initiative(self):
        return (random.randint(0, self._initiative))

    def take_damage(self, amount, damage_type):
        if damage_type == 'physical':
            damage=self._defense - amount
            if damage < 0:
                self._health += damage
                if self._health < 0:
                    self._health=0
        if damage_type == 'magic':
            damage=self._mdefense - amount
            if damage < 0:
                self._health += damage
                if self._health < 0:
                    self._health=0


class Fighter(Adventurer):
    _HP=40
    _DEF=10
    _MDEF=4

    def __init__(self, name, initiative):
        super().__init__(name, Fighter._HP,
                         Fighter._DEF, Fighter._MDEF, initiative)
        self._melee=Attack('Slash', 1, 8, 'physical')

    def get_hp(self):
        return self._health

    def get_name(self):
        return self._name

    def strike(self):
        damage=self._melee.get_damage()
        damage_type=self._melee.get_attack_type()
        print(str(self._name) +
              ' attacks with ' +
              str(self._melee.get_name()) +
              ' for ' +
              str(damage) +
              ' ' +
              str(damage_type) +
              ' damage.')
        return ((damage, damage_type))

    def __str__(self):
        return(str(self._name) + ' with ' +
               str(Fighter._HP) + ' hit points and a ' +
               str(self._melee.get_name()) + ' attack. (' +
               str(self._melee.get_num_die()) + 'd' +
               str(self._melee.get_sides()) + ')')


class Wizard(Adventurer):
    _HP=20
    _DEF=4
    _MDEF=10

    def __init__(self, name, initiative):
        super().__init__(name, Wizard._HP,
                         Wizard._DEF, Wizard._MDEF, initiative)
        self._magic=Attack('Fireball', 3, 6, 'magic')

    def cast(self):
        damage=self._magic.get_damage()
        damage_type=self._magic.get_attack_type()
        print(self._name + ' attacks with ' + str(self._magic.get_name()) +
              ' for ' + str(damage) + ' ' + str(damage_type) + ' damage.')
        return ((damage, damage_type))

    def get_hp(self):
        return self._health

    def get_name(self):
        return self._name

    def __str__(self):
        return(str(self._name) + ' with ' +
               str(Fighter._HP) + ' hit points and a ' +
               str(self._magic.get_name()) + ' attack. (' +
               str(self._magic.get_num_die()) + 'd' +
               str(self._magic.get_sides()) + ')')

if __name__ == '__main__':
    a=Fighter('Aragorn', 20)
    print('Created: ', a)
    w=Wizard('Gandalf', 15)
    print('Created: ', w)
    rounds=1

    while(w.is_alive() and a.is_alive()):
        print('** ROUND ' + str(rounds))
        while True:
            if(w.roll_initiative() > a.roll_initiative()):
                print(w.get_name() + ' wins initiative!')
                cast=w.cast()
                a.take_damage(cast[0], cast[1])
                print(a.get_name() +
                      ' suffers ' +
                      str(cast[0]) +
                      ' after ' +
                      str(Fighter._MDEF) +
                      ' magic defense and has ' +
                      str(a.get_hp()) +
                      ' health left!')
                break
            elif(a.roll_initiative() > w.roll_initiative()):
                print(a.get_name() + ' wins initiative!')
                strike=a.strike()
                w.take_damage(strike[0], strike[1])
                print(w.get_name() +
                      ' suffers ' +
                      str(strike[0]) +
                      ' damage after ' +
                      str(Wizard._DEF) +
                      ' defense and has ' +
                      str(w.get_hp()) +
                      ' health left!')
                break
        rounds += 1
    if w.is_alive():
        print('\n')
        print(str(w.get_name()) + ' has won with ' +
              str(w.get_hp()) + ' health left!')
    if a.is_alive():
        print('\n')
        print(str(a.get_name()) + ' has won with ' +
              str(a.get_hp()) + ' health left!')
