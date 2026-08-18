import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'
}

def fetch_page(url):
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    return resp.text

def parse_rscripts(html):
    soup = BeautifulSoup(html, 'html.parser')
    scripts = []
    for item in soup.select('.script-item'):
        titulo_elem = item.select_one('.title')
        link_elem = item.select_one('a')
        img_elem = item.select_one('img')
        if titulo_elem and link_elem:
            scripts.append({
                'titulo': titulo_elem.get_text(strip=True),
                'link': link_elem['href'],
                'imagem': img_elem['src'] if img_elem else '',
                'fonte': 'rscripts'
            })
    return scripts

def parse_scriptsblox(html):
    soup = BeautifulSoup(html, 'html.parser')
    scripts = []
    for item in soup.select('.card'):
        titulo_elem = item.select_one('h2, h3')
        link_elem = item.select_one('a')
        img_elem = item.select_one('img')
        if titulo_elem and link_elem:
            scripts.append({
                'titulo': titulo_elem.get_text(strip=True),
                'link': link_elem['href'],
                'imagem': img_elem['src'] if img_elem else '',
                'fonte': 'scriptsblox'
            })
    return scripts

def parse_mzscripts(html):
    soup = BeautifulSoup(html, 'html.parser')
    scripts = []
    for item in soup.select('.script-card'):
        titulo_elem = item.select_one('.title')
        link_elem = item.select_one('a')
        img_elem = item.select_one('img')
        if titulo_elem and link_elem:
            scripts.append({
                'titulo': titulo_elem.get_text(strip=True),
                'link': link_elem['href'],
                'imagem': img_elem['src'] if img_elem else '',
                'fonte': 'mzscripts'
            })
    return scripts

def main():
    all_scripts = []
    try:
        html = fetch_page('https://rscripts.net/scripts')
        all_scripts.extend(parse_rscripts(html))
    except Exception as e:
        print(f"Erro rscripts: {e}")

    try:
        html = fetch_page('https://scriptsblox.com/scripts')
        all_scripts.extend(parse_scriptsblox(html))
    except Exception as e:
        print(f"Erro scriptsblox: {e}")

    try:
        html = fetch_page('https://mzscripts.com/scripts')
        all_scripts.extend(parse_mzscripts(html))
    except Exception as e:
        print(f"Erro mzscripts: {e}")

    data = {
        'atualizado_em': datetime.now().isoformat(),
        'scripts': all_scripts
    }
    with open('scripts.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    main()
