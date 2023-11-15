from requests import session
from requests import get


from requests_html import HTMLSession
session = HTMLSession()
url = "https://kulms.tl.kansai-u.ac.jp/webclass/show_frame.php?set_contents_id=62659d5d98fdcd99b9166bbdfaebb410&language=JAPANESE&acs_=816f63d8"
r = session.get(url)
print(r.htmnl.render())


#login to kulms
#url = "https://kulms.tl.kansai-u.ac.jp/webclass/login.php"
"""
#get html from certain url
def get_html(url):
    r = get(url)
    return r.text"""

#get = get_html()
#print(get)