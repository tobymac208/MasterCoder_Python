import os

def main():
    input_text = input('Input text: ')
    path_text = input('Path: ')

    # for each file we find in the path, search the file for the text
    for file in os.listdir(path_text):
        with open(f'{path_text}/{file}', 'r') as f:
            # go through each line and find the string
            for line in f.readlines():
                if input_text in line:
                    # we found the text!
                    # print the absolute path to the file
                    print('We found the text!')
                    print(f'{file}' )
                    break


if __name__ == '__main__':
    main()
