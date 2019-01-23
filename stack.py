#! python3
# lucky.py opens multiple google search results



import requests, sys, webbrowser, bs4


print('let me consult the stack overflow masters for you...')
res = requests.get('https://www.stackoverflow.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()


#retrieve top search result links
soup = bs4.BeautifulSoup(res.text, features="html.parser")

#open browser tab for each result
linkElms = soup.select('.question-hyperlink')
numOpen = min(5, len(linkElms))
for i in range(numOpen) :
    webbrowser.open('https://www.stackoverflow.com' + linkElms[i].get('href'))

