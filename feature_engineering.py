

def create_polynomial_features(df):
    numeric_df = df.select_dtypes(include="number")
    
    for column in numeric_df.columns:
       new_column = f"{column}_squared"
       df[new_column] = df[column] ** 2

    return df

def create_interaction_features(df):
    # We'll build this next
    return df


def create_ratio_features(df):
    # We'll build this later
    return df


def engineer_features(df):

    # Polynomial features
    df = create_polynomial_features(df)

    # Interaction features
    # df = create_interaction_features(df)

    # Ratio features
    # df = create_ratio_features(df)

    return df
