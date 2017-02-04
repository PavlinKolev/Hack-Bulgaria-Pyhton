import json
from bs4 import BeautifulSoup
import requests


def get_all_links(url="http://register.start.bg/"):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")

    links = []
    for link in soup.find_all('a', href=True):
        if link['href'].startswith("http://"):
            links.append(link['href'])
        if link['href'].startswith('link.'):
            links.append(url + link['href'])
    return links


def make_servers_freq_json():
    session = requests.session()
    session.keep_alive = False
    links = get_all_links()
    servers_freqs = {}
    for link in links:
        try:
            resp = session.get(link)
            server_name = resp.headers['Server']
            print(server_name)
            if server_name not in servers_freqs:
                servers_freqs[server_name] = 1
            else:
                servers_freqs[server_name] += 1
        except Exception:
            pass
    with open("servers_freqs.json", 'w') as f:
        f.write(json.dumps(servers_freqs, indent=4))


if __name__ == '__main__':
    make_servers_freq_json()
