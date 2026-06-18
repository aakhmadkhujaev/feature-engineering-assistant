

def create_polynomial_features(df):
    numeric_df = df.select_dtypes(include="number")
    
    for column in numeric_df.columns:
       new_column = f"{column}_squared"
       df[new_column] = df[column] ** 2
    return df
