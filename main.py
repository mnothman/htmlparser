import requests
from bs4 import BeautifulSoup

def decode_message(doc_url):
    response = requests.get(doc_url)
    html_content = response.text

    soup = BeautifulSoup(html_content, "html.parser")

    rows = soup.find_all("tr")

    data = []
    for row in rows[1:]:
        columns = row.find_all("td")
        if len(columns) >= 3:
            x_val = int(columns[0].text.strip())
            ch = columns[1].text.strip()
            y_val = int(columns[2].text.strip())
            data.append((x_val, y_val, ch))

    if not data:
        print("No valid data extracted.")
        return

    min_x = min(d[0] for d in data)
    max_x = max(d[0] for d in data)
    min_y = min(d[1] for d in data)
    max_y = max(d[1] for d in data)

    width = max_x - min_x + 1
    height = max_y - min_y + 1

    grid = [[" " for _ in range(width)] for _ in range(height)]

    for (x, y, ch) in data:
        grid[y - min_y][x - min_x] = ch

    for row in grid:
        print("".join(row))

if __name__ == "__main__":
    url = "https://docs.google.com/document/d/e/2PACX-1vQ7w2USQl8ocBCKZYYHfVn4ViT76Px9Pqr8olbpY72CluZxL4h-R3rBDeSC_PWFoAQ_UH2qR-lx73xd/pub"
    decode_message(url)
