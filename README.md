# Random Forest

Este é um projeto de implementação de busca de hiperparâmetros ótimos em uma
arquitetura de Regressor Random Forest. O objetivo é realizar a regressão para que se preveja a máxima temperatura na cidade de Seattle.

Este código trata-se da implementação do quarto trabalho da discipina de
Aprendizado de Máquina no curso de mestrado em Engenharia Elétrica pelo
Programa de Pós-Graduação em Engenharia Elétrica da Universidade Federal do
Amazonas.

* Tema: Random Forest
* Disciplina: PGENE 556 - Aprendizado de Máquina
* PPGEE - Programa de Pós Graduação em Engenharia Elétrica
* UFAM - Universidade Federal do Amazonas
* Autor: Diego Giovanni de Alcântara Vieira.

## Instalação

1. Clone este repositório:

```
https://github.com/dgavieira/random-forest
```

2. Instale as dependências:

```
pip install -r requirements.txt
```

# Execução

1. Rodar o algoritmo de Random Forest para uma execução única com número de estimadores conhecidos.

```
python src/main.py
```

2. Rodar o algoritmo de otimização por Busca de Hiperparâmetros (grid search) com base em um espaço de busca definido para o modelo regressor Random Forest.

```
python src/grid_search.py
```

3. Para tratar os resultados, rode as células do jupyter notebook `notebooks/post_processing.ipynb`.

# Visualização dos resultados

Após rodar os algoritmos, são gerados dois arquivos na pasta `data`:

- `results.csv` - referente aos resultados de `src/main.py`.
- `results_grid_search.csv` - referente aos resultados de `src/results_grid_search.csv`.

# Estrutura do Repositório

- `data` - pasta em que são salvos os resultados do experimento
  - `results.csv` - referente aos resultados de `src/main.py`.
  - `results_grid_search.csv` - referente aos resultados de `src/results_grid_search.csv`.
  - `temps_extended.xlsx` - base de dados utilizada no experimento.
- `notebooks` - pasta para notebook de pós-processamento das métricas
  - `post_processing.ipynb` - notebook para tratamento dos resultados
- `src` - pacote com o código fonte
  - `main.py` - Execução do treinamento do RandomForest para um conjunto de parâmetros.
  - `grid_search.py` - Execução do algoritmo de busca pelos melhores hiperparametros por meio da técnica de Grid Search.


## Contribuição

Contribuições são bem-vindas! Para sugestões, abra uma issue. Para mudanças significativas, abra um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.