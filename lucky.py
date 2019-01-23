#! python3
# lucky.py opens multiple google search results


# debug logging practice 
import requests, sys, webbrowser, bs4


print('let me shake the google magic 8 ball real quick...')
res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()


#retrieve top search result links
soup = bs4.BeautifulSoup(res.text, features="html.parser")

#open browser tab for each result
linkElms = soup.select('.r a')
numOpen = min(5, len(linkElms))
for i in range(numOpen) :
    webbrowser.open('https://www.google.com' + linkElms[i].get('href'))

