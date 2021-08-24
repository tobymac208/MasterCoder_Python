import requests as rq
from bs4 import BeautifulSoup


def main():
    request = rq.get('https://www.msn.com/')
    
    # grab the content
    soup = BeautifulSoup(request.content, 'html.parser')

    #print(soup.prettify)

    fetched_links = []

    for anchor in soup.find_all('a'):
        fetched_links.append( anchor.get('href') )

    #print(fetched_links)

    # REFACTOR. Instead of printing, add links to a file. Only add 20
    with open('links.txt', 'w+') as f:
        for link in fetched_links[:20]:
            f.write(f'->{link}\n')
            print('*link added*')


if __name__ == '__main__':
    main()