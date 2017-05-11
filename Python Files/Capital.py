def capitalletter(str):
    capital='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if str[0] in capital:
        return True
    else:
        return False

def capital(str):
    if str==str.capitalize():
        return True
    else:
        return False
