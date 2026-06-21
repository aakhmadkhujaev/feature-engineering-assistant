import numpy as np

def create_polynomial_features(df, target_column):
    numeric_df = df.select_dtypes(include="number")
    
    for column in numeric_df.columns:
       if column == target_column:
            continue

       new_column = f"{column}_squared"
       df[new_column] = df[column] ** 2

    return df

def create_interaction_features(df, target_column):
    
    numeric_columns = df.select_dtypes(include="number").columns
    num_columns = len(numeric_columns)
    for i in range(num_columns):
        column1 = numeric_columns[i]
        for j in range(i + 1, num_columns):
            column2 = numeric_columns[j]
            if column1 == target_column or column2 == target_column:
                continue
            new_column = f"{column1}_x_{column2}"
            df[new_column] = df[column1] * df[column2]

            
    return df


def create_ratio_features(df, target_column):
    numeric_columns = df.select_dtypes(include="number").columns
    num_columns = len(numeric_columns)

    for i in range(num_columns):
        column1 = numeric_columns[i]
        safe_denominator1 = df[column1].replace(0, np.nan)

        for j in range(i + 1, num_columns):
            column2 = numeric_columns[j]
            safe_denominator2 = df[column2].replace(0, np.nan)
            if column1 == target_column or column2 == target_column:
                continue
            # Age_per_Salary
            new_column1 = f"{column1}_per_{column2}"
            df[new_column1] = df[column1] / safe_denominator2

            # Salary_per_Age
            new_column2 = f"{column2}_per_{column1}"
            df[new_column2] = df[column2] / safe_denominator1

    return df


def engineer_features(df, target_column):

    # Polynomial features
    df = create_polynomial_features(df, target_column)

    # Interaction features
    df = create_interaction_features(df, target_column)

    # Ratio features
    # df = create_ratio_features(df, target_column)

    return df
