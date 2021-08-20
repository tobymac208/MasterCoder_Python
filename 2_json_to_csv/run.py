"""
    JSON to CSV convert
"""

from json2 import *
import os.path

def main():
    # load the .json file into a dictionary
    file_dict = load_file(r'.\sample.json')
    file_list = []

    for key in file_dict:
        # add all key/value pairs as a new item to the list
        file_list.append([key, file_dict[key]])

    # now generate a csv file
    with open('sample.csv', 'w+') as f:
        for data in file_list:
            f.write(f'{data[0]},{data[1]}\n')

if __name__ == '__main__':
    main()