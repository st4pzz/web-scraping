import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urljoin
import time

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    )
}

sites_filtro = {
    "G1": "https://g1.globo.com/economia/",
    "CNN": "https://edition.cnn.com/business",
    "BBC": "https://www.bbc.com/portuguese/topics/cvjp2jr0k9rt",
}

keywords = ["bitcoin", "investimento","juros","taxa","inflação","imposto",
            "tarifa","economia","tarifas","econômico","dólar","dólares",
            "crise","milionário","milionária","golpe","bilionário","bilionários",
            "bilionária","bilionárias","milionários","milionárias",
            "investment","interest", "rate", "inflation", "tax",
            "fee", "tariff", "economy", "economic",
            "dollar", "dollars", "crisis", "millionaire",
            "millionaires", "scam", "coup",
            "billionaire", "billionaires","IPCA"]

def remover_duplicatas(lista: list[str]) -> list[str]:
    """
    Remove manchetes ou conteúdos duplicados.
    """
    return list(dict.fromkeys(lista))

def coletar_manchetes(site: str, base_url: str) -> list[str]:
    """
    Acessa até 3 páginas do site, extrai o conteúdo das notícias e filtra com base em palavras-chave.
    """
    resultados = []

    for pagina in range(1, 4):  
        if pagina == 1:
            url = base_url
        else:
            
            if "bbc" in base_url:
                url = base_url + f"?page={pagina}"
            else:
                url = base_url

        try:
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")

            links = soup.find_all("a", href=True)
            noticias_urls = set()

            
            for link in links:
                href = link["href"]
                titulo = link.text.strip().lower()
                if any(k in titulo for k in keywords):
                    full_url = urljoin(base_url, href)
                    noticias_urls.add((full_url, link.text.strip()))

            for noticia_url, titulo in noticias_urls:
                try:
                    time.sleep(1)
                    print(f"Visitando: {noticia_url}")
                    noticia_res = requests.get(noticia_url, headers=headers, timeout=10)
                    noticia_soup = BeautifulSoup(noticia_res.text, "html.parser")
                    paragrafos = noticia_soup.find_all("p")
                    texto_completo = " ".join(p.get_text().strip() for p in paragrafos)
                    resultados.append(f"Título: {titulo}\nConteúdo: {texto_completo}")
                except Exception as e:
                    print(f"Erro ao acessar conteúdo de {noticia_url}: {e}")

        except Exception as e:
            print(f"Erro ao acessar {site} (página {pagina}): {e}")

    return remover_duplicatas(resultados)

def salvar_resultados(manchetes: list[str]):
    """
    Salva as manchetes coletadas em um arquivo .txt com fonte e data.
    """
    data_hoje = datetime.today().strftime('%d/%m/%Y')
    caminho = "data/result.txt"

    with open(caminho, "w", encoding="utf-8") as f:
        for fonte, titulos in manchetes:
            for titulo in titulos:
                f.write(f"Fonte: {fonte}\nData: {data_hoje}\nNotícia: {titulo}\n\n")

    print(f"Arquivo salvo em {caminho}")
