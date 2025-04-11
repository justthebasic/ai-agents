import requests 
from bs4 import BeautifulSoup

def get_text_from_url(url):
    response= requests.get(url)

    if response.status_code == 200:
        # Analisa o conteudo HTML da pagina
        soup = BeautifulSoup(response.content, "html.parser")

        # Remove scripts e styles do conteudo
        for script_or_style in soup(["script", "style"]):
            script_or_style.decompose()

        # Obtem o texto puro da pagina
        text = soup.get_text()

        #Remove espaco em branco excessivo
        lines = (lines.strip() for line in text.splitlines())
        chuncks = (phrase.strip() for line in lines for phrase in line.split(" "))
        text = "\n".join(chunk for chunk in chunks if chunk)

        return text
    else:
        return f"Erro ao acessar a pagina: {response.status_code}"