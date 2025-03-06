import requests
from bs4 import BeautifulSoup

def extract_links(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    potato_links = [a for a in soup.find_all('a', class_='animetitle') if 'href' in a.attrs]
    
    return potato_links

def parse_animu(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    entries = soup.find('div', class_='entries-tile')
    if entries:
        related = entries.find_all('div', class_="entry borderClass")
        for entry in related:
            container = entry.find('div', class_='content')
            if container:
                relation = " ".join(container.find('div', class_='relation').text.split())
                title = container.find('div', class_='title').text.strip()
                if "Sequel" in relation:
                    return title
    return None

    #add related or whatev support
    #add stats for how long to finish yada yada
    

if __name__ == "__main__":
    root = "https://myanimelist.net"
    url = "YOUR ANIMULIST URL"
    links = extract_links(url)

    seenurls = [link["href"] for link in links]
    seenanimes = [link.text.strip() for link in links]

    print("Animu links found:")
    for link in links:
        animu = link.text.strip()
        #add rate reduction
        sequel = parse_animu(f"{root}{link["href"]}")
        if sequel:
            if sequel not in seenanimes:
                print(f"Missing {sequel}")

