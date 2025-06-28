from scraping.main import sites_filtro, coletar_manchetes, salvar_resultados

def main():
    todos_resultados = []

    for fonte, url in sites_filtro.items():
        titulos = coletar_manchetes(fonte, url)
        todos_resultados.append((fonte, titulos))

    salvar_resultados(todos_resultados)
    

if __name__ == "__main__":
    main()
