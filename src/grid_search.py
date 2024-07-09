import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from tqdm import tqdm
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Carregar os dados do arquivo Excel
data = pd.read_excel('./data/temps_extended.xlsx')

# Selecionar as variáveis preditoras e a variável alvo
predictors = ['year', 'ws_1', 'temp_2', 'temp_1', 'average']
target = 'actual'

X = data[predictors]
y = data[target]

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Definir os parâmetros para Grid Search
param_grid = {
    'bootstrap': [True, False],
    'max_depth': [3, 5, 10, 20, 30, None],
    'min_samples_leaf': [1, 2, 4],
    'min_samples_split': [2, 5, 10],
    'n_estimators': [200, 400, 600]
}

# Lista para armazenar os resultados
results_list = []

# Contador de iterações
total_iterations = len(param_grid['bootstrap']) * len(param_grid['max_depth']) * \
                    len(param_grid['min_samples_leaf']) * len(param_grid['min_samples_split']) * \
                    len(param_grid['n_estimators'])
progress = tqdm(total=total_iterations, desc='Grid Search Progress', position=0)

# Executar o Grid Search e salvar os resultados para cada combinação de hiperparâmetros
for bootstrap in param_grid['bootstrap']:
    for max_depth in param_grid['max_depth']:
        for min_samples_leaf in param_grid['min_samples_leaf']:
            for min_samples_split in param_grid['min_samples_split']:
                for n_estimators in param_grid['n_estimators']:
                    rf_model = RandomForestRegressor(bootstrap=bootstrap,
                                                     max_depth=max_depth,
                                                     min_samples_leaf=min_samples_leaf,
                                                     min_samples_split=min_samples_split,
                                                     n_estimators=n_estimators,
                                                     random_state=42)
                    rf_model.fit(X_train, y_train)
                    y_pred = rf_model.predict(X_test)
                    
                    mae = mean_absolute_error(y_test, y_pred)
                    mse = mean_squared_error(y_test, y_pred)
                    importances = rf_model.feature_importances_
                    
                    result_row = {'n_estimators': n_estimators, 'max_depth': max_depth,
                                  'min_samples_leaf': min_samples_leaf, 'min_samples_split': min_samples_split,
                                  'bootstrap': bootstrap, 'MAE': mae, 'MSE': mse}
                    result_row.update({predictor: importance for predictor, importance in zip(predictors, importances)})
                    
                    results_list.append(result_row)
                    
                    # Atualizar barra de progresso
                    progress.update(1)
                    progress.set_postfix_str(f"MAE: {mae:.2f}, MSE: {mse:.2f}")

# Converter a lista de resultados em DataFrame
results_df = pd.DataFrame(results_list)

# Salvar os resultados em um arquivo CSV
results_df.to_csv('results_grid_search.csv', index=False)

# Fechar barra de progresso
progress.close()

# Exibir os resultados
logging.info(f"Grid Search concluído. Resultados salvos em 'results_grid_search.csv'.")
print(results_df)

