import sys
import requests


"""
    CURRENTLY UNABLE TO DO THIS PROJECT
"""

def main():
    username = ""

    try:
        username = sys.argv[1]
    except IndexError:
        print('You need to provide a username.')
        sys.exit(-1)
    
    # TEST: attempt to sign-in to github
    req_github = requests.get('https://www.instagram.com/_nik_fernandez_/')
    print(req_github.status_code)


if __name__ == '__main__':
    main()
