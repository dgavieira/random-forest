import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Carregar os dados do arquivo Excel
data = pd.read_excel('./data/temps_extended.xlsx')

print(data.head())

# Selecionar as variáveis preditoras e a variável alvo
predictors = ['year', 'ws_1', 'temp_2', 'temp_1', 'average']
target = 'actual'

X = data[predictors]
y = data[target]

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Lista de números de estimadores para testar
n_estimators_list = [200, 400, 600]

# DataFrame para armazenar os resultados
results_list = []

# Treinar o modelo e avaliar com diferentes números de estimadores
for n in n_estimators_list:
    rf_model = RandomForestRegressor(n_estimators=n, random_state=42)
    rf_model.fit(X_train, y_train)
    y_pred = rf_model.predict(X_test)
    
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    importances = rf_model.feature_importances_
    
    result_row = {'n_estimators': n, 'MAE': mae, 'MSE': mse}
    result_row.update({predictor: importance for predictor, importance in zip(predictors, importances)})
    
    results_list.append(result_row)

# Convertendo a lista de resultados em DataFrame
results_df = pd.DataFrame(results_list)

print(results_df)
results_df.to_csv('results.csv')