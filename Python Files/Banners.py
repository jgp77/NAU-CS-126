def print_banner():
    string=input('What do you want to print? ').lower()
    orientation=input('Is the banner Horizontal or Vertical? ').lower()
    letters={
        'a': ['#####',
              '#      #',
              '#####',
              '#      #',
              '#      #'],
        'b': ['#####',
              '#      #',
              '#####',
              '#      #',
              '#####'],
        'c': ['#####',
              '#        ',
              '#        ',
              '#        ',
              '#####'],
        'd': ['###  ',
              '#  #  ',
              '#   # ',
              '#  #  ',
              '###  '],
        'e': ['#####',
              '#        ',
              '#####',
              '#        ',
              '#####'],
        'f': ['#####',
              '#        ',
              '#####',
              '#        ',
              '#        '],
        'g': ['#####',
              '#        ',
              '#    ##',
              '#      #',
              '#####'],
        'h': ['#    #',
              '#    #',
              '####',
              '#    #',
              '#    #'],
        'i': ['###',
              '  #  ',
              '  #  ',
              '  #  ',
              '###'],
        'j': ['      #',
              '      #',
              '      #',
              '#    #',
              '####'],
        'k': ['#  #',
              '# # ',
              '##  ',
              '# # ',
              '#  #'],
        'l': ['#    ',
              '#    ',
              '#    ',
              '#    ',
              '###'],
        'm': ['#       #',
              '# # # #',
              '#   #  #',
              '#       #',
              '#       #'],
        'n': ['##  # ',
              '# # # ',
              '# # # ',
              '#  ## ',
              '#    # '],
        'o': ['###',
              '#  #',
              '#  #',
              '#  #',
              '###'],
        'p': ['###',
              '#  #',
              '###',
              '#    ',
              '#    '],
        'q': ['### ',
              '#  # ',
              '#  # ',
              '### ',
              '     #'],
        'r': ['###',
              '#  #',
              '###',
              '# # ',
              '#  #'],
        's': ['###',
              '#    ',
              '###',
              '    #',
              '###'],
        't': ['#####',
              '    #    ',
              '    #    ',
              '    #    ',
              '    #    '],
        'u': ['#  #',
              '#  #',
              '#  #',
              '#  #',
              '###'],
        'v': ['#      #',
              ' #    # ',
              '  #  #  ',
              '   ##   ',
              '    #    '],
        'w': ['#  #  #',
              '#  #  #',
              '#  #  #',
              '#  #  #',
              ' ## ##'],
        'x': ['#   #',
              ' # # ',
              '  #   ',
              ' # # ',
              '#   #'],
        'y': ['#    #',
              '#    #',
              ' ### ',
              '   #   ',
              '   #   '],
        'z': ['####',
              '    #  ',
              '   #   ',
              '  #    ',
              '####'],
        ' ': ['         ',
              '         ',
              '         ',
              '         ',
              '         ']}
    '''
Asks the user for the desired orientation and string.
Creates a dictionary to define what a letter translate to in banner form
    '''
    if orientation == 'vertical':
        '''
  If the desired orientation is vertical, This will print the desired
  banner by accessing the dictonary and printing out the
  final result
    '''
        for i in string:
            for i in letters[i]:
                print(i)
    if orientation == 'horizontal':
        '''
    if the desired orientation is horizontal, this creates the
    variable display, which contains 5 empty strings.
    This function then uses a for loop to insert the necessary
    string into the display variable.
    Finally this function uses a for look to print
    out the final result/banner
'''
        display=['', '', '', '', '']
        for i in string:
            for letter in range(len(letters[i])):
                display[letter] += letters[i][letter] + ' '
        for i in display:
            print(i)
print_banner()
