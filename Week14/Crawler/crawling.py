import os
import json
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
from settings import SERVERS_FREQS_JSON, OUR_HEADERS, START_BG_URL


def get_all_links(url=START_BG_URL):
    resp = requests.get(url, headers=OUR_HEADERS)
    soup = BeautifulSoup(resp.content, "html.parser")

    links = []
    for link in soup.find_all('a', href=True):
        if link['href'].startswith("http://"):
            links.append(link['href'])
        if link['href'].startswith('link.'):
            links.append(url + link['href'])
    return links


def make_servers_freq_json():
    links = get_all_links()
    servers_freqs = {}
    for link in links:
        try:
            resp = requests.head(link, headers=OUR_HEADERS)
            server_name = resp.headers['Server']
            if server_name.startswith("Apache"):
                server_name = "Apache"
            if server_name not in servers_freqs:
                servers_freqs[server_name] = 1
            else:
                servers_freqs[server_name] += 1
            print(server_name)
        except Exception:
            pass
    with open(SERVERS_FREQS_JSON, 'w') as f:
        f.write(json.dumps(servers_freqs, indent=4))


def create_hist(servers_freqs):
    keys = list(servers_freqs.keys())
    values = list(servers_freqs.values())

    X = list(range(len(keys)))

    plt.bar(X, list(servers_freqs.values()), align="center")
    plt.xticks(X, keys)

    plt.title(".bg servers")
    plt.xlabel("Server")
    plt.ylabel("Count")

    plt.savefig("histogram.png")


def main():
    if not os.path.exists(SERVERS_FREQS_JSON):
        make_servers_freq_json()

    servers_freqs = {}
    with open(SERVERS_FREQS_JSON, 'r') as f:
        servers_freqs = json.load(f)

    create_hist(servers_freqs)


if __name__ == '__main__':
    main()
