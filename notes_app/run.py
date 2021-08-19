from time import sleep


""" Iterates over a list and returns if the item you selected is a match """
def is_match(ls, item):
    if item in ls:
        return True
    return False


def main():
    notes = []

    print('<---> Managed Notes Application <--->')
    while True:
        print('notes:')

        if len(notes) > 0:
            for note in notes:
                print(note)
        else:
            print('no notes')
        
        # take input
        print()
        print('1) add note')
        print('2) edit note')
        print('3) delete note')
        print('4) exit')
        choice = 0

        try:
            choice = int(input('> '))
        except ValueError as e:
            pass

        # process choice
        if choice == 1:
            note_value = input('Let\'s store that note for you: ')
            if not is_match(notes, note_value):
                notes.append(note_value)
            else:
                # let the user know they can't do that
                print('Hmmm... look\'s like you\'ve added that as a note. I can\'t add that :/ Sorry')
                sleep(2)
        # elif choice == 2:
        # elif choice == 3:
        elif choice == 4:
            break
        else:
            print('C\'mon, that wasn\'t an option.')


if __name__ == "__main__":
    main()
