def tip(lis):
    money_spent=float(sum(lis))
    tip=input('Would you like to leave a tip? Yes or no? ').lower()
    if tip == 'yes':
        service=input('How was your service? '
                        'Great, Good, Average, Bad, or Terrible?').lower()
        if service == 'great':
            tip=.2 * money_spent
            total=money_spent + tip
            return ('Your tip is $ %d. Your total is $ %d' % (tip, total))
        if service == 'good':
            tip=.18 * money_spent
            total=money_spent + tip
            return ('Your tip is $ %d. Your total is $ %d' % (tip, total))
        if service == 'average':
            tip=.15 * money_spent
            total=money_spent + tip
            return ('Your tip is $ %d. Your total is $ %d' % (tip, total))
        if service == 'bad':
            tip=.12 * money_spent
            total=money_spent + tip
            return ('Your tip is $ %d. Your total is $ %d' % (tip, total))
        if service == 'terrible':
            tip=.10 * money_spent
            total=money_spent + tip
            return ('Your tip is $ %d. Your total is $ %d' % (tip, total))
    elif tip == 'no':
        return ('Your tip is $ %d. Your total is $ %d' % (0, money_spent))


def tax(lis, tax):
    total=sum(lis)
    total=total * tax + total
    return total


def tip_and_tax(lis, tax):
    tax_amount=float(sum(lis)) * tax
    total_amount=float(sum(lis)) + (float(sum(lis)) * tax)
    leave_a_tip=input('Would you like to leave a tip? Yes or no? ').lower()
    if leave_a_tip == 'yes':
        service=input('How was your service? '
                        'Great, Good, Average, Bad, or Terrible?').lower()
        if service == 'great':
            tip=.2 * total_amount
            total_amount=total_amount + tip
            return ('Your tip is $' +
                    str((round(tip, 2))) +
                    '. Your tax is $' +
                    str(round(tax_amount, 2)) +
                    '. Your total is $' +
                    str(round(total_amount, 2)))
        if service == 'good':
            tip=.18 * total_amount
            total_amount=total_amount + tip
            return ('Your tip is $' +
                    str((round(tip, 2))) +
                    '. Your tax is $' +
                    str(round(tax_amount, 2)) +
                    '. Your total is $' +
                    str(round(total_amount, 2)))
        if service == 'average':
            tip=.15 * total_amount
            total_amount=total_amount + tip
            return ('Your tip is $' +
                    str((round(tip, 2))) +
                    '. Your tax is $' +
                    str(round(tax_amount, 2)) +
                    '. Your total is $' +
                    str(round(total_amount, 2)))
        if service == 'bad':
            tip=.12 * total_amount
            total_amount=total_amount + tip
            return ('Your tip is $' +
                    str((round(tip, 2))) +
                    '. Your tax is $' +
                    str(round(tax_amount, 2)) +
                    '. Your total is $' +
                    str(round(total_amount, 2)))
        if service == 'terrible':
            tip=.1 * total_amount
            total_amount=total_amount + tip
            return ('Your tip is $' +
                    str((round(tip, 2))) +
                    '. Your tax is $' +
                    str(round(tax_amount, 2)) +
                    '. Your total is $' +
                    str(round(total_amount, 2)))
    elif leave_a_tip == 'no':
        tip=0
        return ('Your tip is $' +
                str((round(tip, 2))) +
                '. Your tax is $' +
                str(round(tax_amount, 2)) +
                '. Your total is $' +
                str(round(total_amount, 2)))
