def train_baseline():
    df = pd.read_csv(PROCESSED_PATH)

    features = ['Lag_1', 'Lag_2', 'Rolling_Mean_4']
    target = 'Weekly_Sales'

    X = df[features]
    y = df[target]

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    return model, y_test, y_pred