from time import sleep
import os, os.path


def error_message(message, wait_time=2):
    print(message)
    sleep(wait_time)


def check_length_of_list(ls):
    if not len(ls) > 0:
        error_message('Well, there\'s nothing in the list.')
        return False
    return True


def write_data(ls):
    with open('notes.txt', 'w+') as f:
        for note in ls:
            f.write(f'{note}\n')


def read_data():
    note_data = []

    with open('notes.txt', 'a+') as f:
        f.seek(0)
        for note in f.readlines():
            note_data.append(note)

    return note_data


""" Iterates over a list and returns if the item you selected is a match """
def is_match(ls, item):
    if item in ls:
        return True
    return False


def main():
    notes = read_data()

    print('<---> Managed Notes Application <--->')
    while True:
        print('notes:')

        if len(notes) > 0:
            count = 0
            for note in notes:
                count += 1
                print(f'{count}. {note}')
        else:
            print('no notes')
        
        # take input
        print()
        print('1) add note')
        print('2) edit note')
        print('3) delete note')
        print('4) exit')
        choice = 0

        # Catch any issues with input. Don't do anything if there's an exception.
        try:
            choice = int(input('> '))
        except ValueError as e:
            pass

        # process choice
        if choice == 1:
            note_value = input('Let\'s store that note for you: ')
            if is_match(notes, note_value):
                # let the user know they can't do that
                error_message('Hmmm... look\'s like you\'ve added that as a note. I can\'t add that :/ Sorry')
            else:
                notes.append(note_value)
        elif choice == 2:
            if not len(notes) > 0:
                error_message('Well, there\'s nothing in the list.')
                continue
            try:
                choice = int(input('Which note (numberical)? '))
                new_note = input('What do you want to change it to? ')
                if not is_match(notes, new_note):
                    notes[notes.index(notes[choice-1])] = new_note
                else:
                    print('Ooops! That won\'t work.')

            except ValueError:
                pass
        elif choice == 3:
            if not check_length_of_list(notes):
                continue
            try:
                choice = int(input('Which note? '))
            except ValueError:
                continue

            notes.remove(notes[choice-1])
        elif choice == 4:
            break
        else:
            error_message('C\'mon, that wasn\'t an option.')

    # write data to a file
    write_data(notes)


if __name__ == "__main__":
    main()
