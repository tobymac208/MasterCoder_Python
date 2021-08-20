import sys
import requests


"""
    Downloads a specified user's profile picture
    Can't currently complete!
    Need to understand:
        - requests
        - image viewing
        - browser driver for logging in
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
