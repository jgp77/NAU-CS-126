import time
__author__='Nico Demaria and Joshua Pollock'


def update(book, status, audience, userid):
    ''' Creates a unique ID for the post
    combining both the userid and the timestamp'''
    postid=userid + str(time.time())
    book[postid]=[status, audience, userid, "", time.time()]
    return postid


def like(book, postid, userid):
    ''' Puts a like on a post. Multiple likes are ignored '''
    likes=book[postid][3]
    list_likes=list(likes)
    list_likes.append(userid)
    book[postid][3]=set(list_likes)


def unlike(book, postid, userid):
    ''' Takes a like off a post. Multiple unlikes are ignored '''
    if userid in book[postid][3]:
        book[postid][3].remove(userid)


def display(book, postid):
    ''' Displays information on a given format '''
    print('Post created at ' + str(time.time()) +
          ' by ' + str(book[postid][2]))
    print('Time: ' + str(book[postid][4]))
    print('Groups: ' + str(book[postid][1]))
    print('Likes: ' + str(len(book[postid][3])))
    print(str(book[postid][2]) +
          '(mention with @' +
          str(book[postid][2]) +
          ') says: ')
    print(str(book[postid][0]))


def main():
    ''' Main task of given code by lab. '''
    book={}
    barnabus_one=update(
        book, 'Storming the village at 9. Anyone intrested?', [
            'Zombies', 'Vampires]'], 'BarnabusCollins')
    time.sleep(1)
    casper_one=update(book, 'Can I come?', ['Vampires'], 'Casper')
    time.sleep(1)
    barnabus_two=update(
        book,
        'Forgot to include the ghosts! Lol',
        ['Ghosts'],
        'BarnabusCollins')
    time.sleep(1)
    barnabus_three=update(book, 'Lots of villagers with forks here..', [
        'Vampires',
        'Zombies',
                            'Ghosts'], 'BarnabusCollins')
    like(book, barnabus_one, 'Edmund')
    like(book, barnabus_one, 'Grimm')
    like(book, barnabus_one, 'Edmund')
    like(book, casper_one, 'Edmund')
    like(book, casper_one, 'Grimm')
    like(book, casper_one, 'Harry')
    like(book, casper_one, 'Count Chocula')
    like(book, barnabus_two, 'Casper')
    like(book, barnabus_three, 'Casper')
    like(book, barnabus_three, 'Count Chocula')
    like(book, barnabus_three, 'Boo')
    unlike(book, casper_one, 'Edmund')
    unlike(book, barnabus_three, 'Casper')
    unlike(book, casper_one, 'Edmund')
    display(book, barnabus_one)
    display(book, barnabus_three)
    print('-----------------------------------------')
    display(book, casper_one)
main()