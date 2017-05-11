import random


class DiceRoller:
    # a utility class for dice rolling.

    def roll(self, times, sides):
        # rolls times number of sides-sided dice; returns the total
        total=0
        for i in range(times):
            roll=random.randint(1, sides)
            total += roll
        return total

r=DiceRoller()


class Attack:
    # encapsulates the concept of an attack

    def __init__(self, name, number_of_dice, sides_of_die, damage_type):
        # creates an attack with private attributes
        self._name=name
        self._sides=sides_of_die
        self._number=number_of_dice
        self._type=damage_type

    # getters
    def get_attack_type(self):
        # returns the type of attack as a string
        return self._type

    def get_damage(self):
        # returns a damage value for this attack
        # rolls _number number of _sides sided dice, using DiceRoller r, and
        # returns the resulting value.
        self.damage_value=r.roll(self._number, self._sides)
        return self.damage_value

    def get_name(self):
        # returns the name of attack as a string
        return self._name

    def get_sides_of_die(self):
        # returns the number of sides on the die as a string
        return str(self._sides)

    def get_number_of_die(self):
        # returns the number of die as a string
        return str(self._number)

    # setters
    def set_attack_type(self, damage_type):
        # sets the type of attack
        self._type=damage_type

    def set_damage(self):
        # sets a damage value for the attack
        # rolls _number number of _sides sided dice, using DiceRoller r, and
        # returns the resulting value.
        self.damage_value=r.roll(self._number, self._sides)

    def set_name(self, name):
        # sets the name of attack
        self._name=name

    def set_sides_of_die(self, sides_of_die):
        # sets the number of sides on the die
        self._sides=sides_of_die

    def set_number_of_die(self, number_of_dice):
        # sets the number of dice
        self._number=number_of_dice


class Adventurer:
    # encapsulates the concept of an adventurer

    def __init__(self, name, hit_points, defense, magic_defense, initiative):
        # creates an adventurer w private attributes
        self._name=name
        self._hit_points=hit_points
        self._defense=defense
        self._magic_defense=magic_defense
        self._initiative=initiative

    def is_alive(self):
        # returns True if object has more than 0 hit points
        if self._hit_points > 0:
            return True
        else:
            return False

    def roll_initiative(self):
        # returns a random integer between 0 and object's initiative value
        roll_initiative=random.randint(0, self._initiative)
        return roll_initiative

    def take_damage(self, amount, damage_type):
        # applies damage to object's attributes
        '''
        if damage type is 'physical',
        reduce the object's hit points by
        what is left after reducing
        amount by the object's defense.
        '''
        if damage_type.lower() == 'physical':
            new_amount=amount - self._defense
            # makes sure hit points do not get added to
            if new_amount < 0:
                new_hit_points=self._hit_points
            else:
                new_hit_points=self._hit_points - new_amount
            # makes sure hit points can not be negative
            if new_hit_points < 0:
                new_hit_points=0
            self._hit_points=new_hit_points
            print(self._name +
                  ' suffers ' +
                  str(new_amount) +
                  ' damage after ' +
                  str(self._defense) +
                  ' magic defense and has ' +
                  str(self._hit_points) +
                  ' hit points left.')
        '''
        if damage type is ”magic”,
        reduce the object’s hit points
        by what is left after reducing
        amount by the object’s magic defense.
        '''
        if damage_type.lower() == 'magic':
            new_amount=amount - self._magic_defense
            # makes sure hit points do not get added to
            if new_amount < 0:
                new_amount=0
                new_hit_points=self._hit_points - new_amount
            else:
                new_hit_points=self._hit_points - new_amount
            # makes sure hit points can not be negative
            if new_hit_points < 0:
                new_hit_points=0
            self._hit_points=new_hit_points
            print(self._name.capitalize() +
                  ' suffers ' +
                  str(new_amount) +
                  ' damage after ' +
                  str(self._magic_defense) +
                  ' magic defense and has ' +
                  str(self._hit_points) +
                  ' hit points left.')

    # getters
    def get_name(self):
        # returns name of adventurer as string
        return self._name

    def get_hit_points(self):
        # returns hit points of adventurer as string
        return str(self._hit_points)

    def get_defense(self):
        # returns defense of adventurer as string
        return str(self._defense)

    def get_magic_defense(self):
        # returns magic defense of adventurer as string
        return str(self._magic_defense)

    def get_initiative(self):
        # returns initiative of adventurer as string
        return self._initiative

    # setters
    def set_name(self, name):
        # sets name of adventurer
        self._name=name

    def set_hit_points(self, hit_points):
        # sets hit points of adventurer
        self._hit_points=hit_points

    def set_defense(self, defense):
        # sets defense of adventurer
        self._defense=defense

    def set_magic_defense(self, magic_defense):
        # sets magic defense of adventurer
        self._magic_defense=magic_defense

    def set_initiative(self, initiative):
        # sets initiative of adventurer
        self._initiative=initiative


class Fighter(Adventurer):
    # encapsulates a a fighter class inheriting from adventurer
    # class member variables
    # health points/hit points
    _HP=40
    # defense
    _DEF=10
    # magic defense
    _MAG_DEF=4

    def __init__(self, name, initiative):
        # creates a fighter object
        # calls super class __init__ method
        super().__init__(name, Fighter._HP,
                         Fighter._DEF, Fighter._MAG_DEF, initiative)
        # variable _melee references an instance of attack class (a fixed
        # attack)
        self._melee=Attack('Slash', 2, 16, 'physical')

    def strike(self):
        '''
        calculates and returns info about a physical strike from object:
        returns a tuple of damage value and damage type
        damage value is obtained by calling get_damage() method on _melee
        damage type is obtained by calling get_attack_type() on _melee
        prints information about strike
        '''
        self._damage_value=self._melee.get_damage()
        self._damage_type=self._melee.get_attack_type()
        print(self._name +
              ' attacks with ' +
              self._damage_type.capitalize() +
              ' for ' +
              str(self._damage_value) +
              ' physical damage.')
        return (self._damage_value, self._damage_type)

    def __str__(self):
        # returns a string representation of this object
        return self._name + ' with '\
            + str(self._hit_points) + ' hit points and a '\
            + self._melee.get_name().capitalize() + ' attack ('\
            + str(self._melee.get_number_of_die()) + 'd'\
            + str(self._melee.get_sides_of_die()) + ').'


class Wizard(Adventurer):
    # encapsulates a wizard class inheriting from adventurer
    # class member variables
    # health points/hit points
    _HP=20
    # defense
    _DEF=4
    # magic defense
    _MAG_DEF=10

    def __init__(self, name, initiative):
        # creates wizard object
        # calls super class __init__ method
        super().__init__(name, Wizard._HP,
                         Wizard._DEF, Wizard._MAG_DEF, initiative)
        # variable _spell that references an instance of attack class (a fixed
        # attack)
        self._spell=Attack('Vortex', 4, 6, 'magic')

    def cast(self):
        '''
        calculates and returns info about a spell from object:
        returns a tuple of damage value and damage type
        damage value is obtained by calling get_damage() method on _spell
        damage type is obtained by calling get_attack_type() on _spell
        prints information about strike
        '''
        self._damage_value=self._spell.get_damage()
        self._damage_type=self._spell.get_attack_type()
        print(self._name +
              ' attacks with ' +
              self._damage_type.capitalize() +
              ' for ' +
              str(self._damage_value) +
              ' physical damage.')
        return (self._damage_value, self._damage_type)

    def __str__(self):
        # returns a string representation of this object
        return self._name + ' with ' \
            + str(self._hit_points) + ' hit points and a '\
            + self._spell.get_name().capitalize() + ' attack ('\
            + str(self._spell.get_number_of_die()) + 'd'\
            + str(self._spell.get_sides_of_die()) + ').'


if __name__ == '__main__':
    # create a fighter object
    ajax=Fighter('Ajax', 50)
    # print fighter object out
    print('Created:', ajax)
    # create a wizard object
    akb=Wizard('AbbraKaddaBruh', 100)
    # print wizard object out
    print('Created:', akb)
    # create variable to keep track of rounds of combat
    rounds=0
    # as long as both combatants are alive– keep fighting rounds
    while akb._hit_points > 0 and ajax._hit_points > 0:
        # round counter
        print('Round ', str(rounds))
        rounds += 1
        # roll initiative for both combatants
        fighter_init=ajax.roll_initiative()
        print("Ajax's initiative is: ", fighter_init)
        wizard_init=akb.roll_initiative()
        print("AbbraKaddaBruh's initiative is: ", wizard_init)
        # higher init gets to attack this round
        if fighter_init == wizard_init:
            # roll initiative for both combatants until different
            while fighter_init == wizard_init:
                fighter_init=ajax.roll_initiative()
                # print("Ajax's initiative is: ", fighter_init)
                wizard_init=akb.roll_initiative()
                # print("AbbraKaddaBruh's initiative is: ", wizard_init)
        # if fighter init greater than wizard init
        if fighter_init > wizard_init:
            print('Ajax wins initiaive!')
            # ajax strikes
            strike=ajax.strike()
            # print(strike)
            # akb takes damage
            akb.take_damage(strike[0], strike[1])

        # if fighter init lesser than wizard init
        if fighter_init < wizard_init:
            print('AbbraKaddaBruh wins initiative!')
            # akb strikes
            spell=akb.cast()
            # print(spell)
            # ajax takes damage
            ajax.take_damage(spell[0], spell[1])
    # print message indicating which combatant won and remaining hit points
    final_fighter_hp=ajax.get_hit_points()
    final_wizard_hp=akb.get_hit_points()
    if final_fighter_hp > final_wizard_hp:
        print('Ajax wins with ' + final_fighter_hp + ' hit points left.')
    else:
        print(
            'AbbraKaddaBruh wins with ' +
            final_wizard_hp +
            ' hit points left.')
