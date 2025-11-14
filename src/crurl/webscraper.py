import socket
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup


def get_title(reg_url):
    title = ""
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
        req = Request(url=reg_url, headers=headers)
        html = urlopen(req, timeout=1).read()
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
        raise
        #  pass
    except URLError as e:
# mf commented out as logging module will print message.
        #  print('We failed to reach a server.')
        #  print('Reason: ', e.reason)
        #  pass
        raise
    except socket.timeout as e:
        #  print type(e)    #catched
        #  raise MyException("There was an error: %r" % e)
        #  print('We failed to reach a server.')
        #  print('Reason: socket timeout.')
        #  pass
        raise
    else:
        soup = BeautifulSoup(html, "lxml")
        text = soup.get_text(strip=True)
        title = soup.title.text
        #  print(f"Print the title: {title} ")
    return(title)
