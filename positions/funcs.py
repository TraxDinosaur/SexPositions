import requests
from bs4 import BeautifulSoup as bs


def getSoup(position):
    position = int(position)
    url = f"https://sexpositions.club/positions/{position}.html"
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    return soup


def getNumber(soup):
    entry_title = soup.find('h1', class_='entry-title').text.strip()
    parts = entry_title.split()

    for part in parts:
        if part.startswith('#'):
            number = part.lstrip('#').rstrip('.')
            return number
    return None


def getName(soup):
    entry_title = soup.find('h1', class_='entry-title').text.strip()
    parts = entry_title.split()
    name_parts = []
    found_number = False
    for part in parts:
        if found_number:
            name_parts.append(part)
        elif part.startswith('#'):
            found_number = True
    name = ' '.join(name_parts)
    return name


def getDescription(soup):
    description = soup.find('p').text.strip()
    return description


def getImageUrl(soup):
    meta_tag = soup.find('meta', property='og:image')
    img_url = meta_tag['content']
    return img_url


def getSimilar(soup):
    links = soup.find_all('a', href=True)
    position_names = []
    for link in links:

        if link.get('href').startswith('https://sexpositions.club/positions/'):
            text = link.get_text(strip=True)

            if 'Position' in text:
                name = text.split(' ', 2)[2]  # Splits on 'Position' and keeps the name part
                position_names.append(name)

    return ', '.join(position_names)


def getSft(soup):
    parent_div = soup.find('div', class_='sp_wrap')

    if parent_div:
        child_div = parent_div.find('div')
        if child_div:
            sft = child_div.get_text(strip=True)
            return sft


def positions(position: int) -> dict:
    position = int(position)
    soup = getSoup(position)
    positionNumber = getNumber(soup)
    positionName = getName(soup)
    positionDescription = getDescription(soup)
    positionImageUrl = getImageUrl(soup)
    positionSimilar = getSimilar(soup)
    sft = getSft(soup)

    Schema = {
        'position': positionNumber,
        'name': positionName,
        'description': positionDescription,
        'img_url': positionImageUrl,
        'similar': positionSimilar,
        'sft': sft
    }

    return Schema


if __name__ == '__main__':
    print(positions(1))
    print(positions(22))
