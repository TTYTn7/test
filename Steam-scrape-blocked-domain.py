#Web Scrapper

from bs4 import BeautifulSoup
import requests

domain_list = []
with open('domains.txt', 'r') as f:
    line = f.readline().strip()
    while line:
        domain_list.append(line)
        line = f.readline().strip()

blocked = []
for domain in domain_list:
    url = "https://steamcommunity.com/openid/login?openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.mode=checkid_setup&openid.return_to=https%3A%2F%2F{url_domain}%2Fapi%2Fv2%2Flogin%3Fe%3Dp&openid.realm=https%3A%2F%2F{url_domain}&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select".format(url_domain = domain)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    blacklisted = soup.find_all('div', id="blacklist_takeover")
    if len(blacklisted) > 0:
        blocked.append(domain)

print (blocked)