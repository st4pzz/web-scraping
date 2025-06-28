# web-scraping

# Projeto de Web Scraping: Análise de Manchetes Econômicas

## Sobre o Projeto

## Este projeto consiste em um scraper em Python que coleta manchetes das seções de Economia de três portais de notícias nacionais e internacionais:

- G1 (Brasil)
- BBC News Brasil (Internacional)
- CNN

### O programa acessa essas páginas e filtra as manchetes com base nas palavras-chave:

- bitcoin
- investimento
- inflação

### As manchetes extraídas são armazenadas em um arquivo .txt com informações sobre a fonte, data da coleta e o título da notícia.

## Objetivo do Projeto

Além da etapa de coleta, este projeto foi estruturado pensando em aplicações futuras. O objetivo é utilizar essas manchetes como dados de entrada para um modelo de Machine Learning, com foco em:

Análise de Sentimento (positivo, neutro, negativo)

Correlação com o comportamento do mercado (por exemplo: decisões de compra/venda de ativos como Bitcoin)

A ideia é prever, com base no tom geral das notícias, se o momento atual tende a ser favorável ou não para investimentos em criptomoedas e mercados correlacionados.

## Arquivos incluídos 

- `main.py`: Código-fonte do coletor de manchetes.
- `result.txt` : Arquivo com os resultados da coleta.
- `README.md` : Este arquivo explicando a estrutura e objetivo do projeto.

