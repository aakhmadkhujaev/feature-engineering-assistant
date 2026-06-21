# Feature Engineering Assistant v1.0

A modular Python application that automatically generates new machine learning features from cleaned datasets. The project creates polynomial, interaction, and ratio features, then saves the engineered dataset along with a feature engineering report.

---

## Features

- Polynomial feature generation
- Interaction feature generation
- Ratio feature generation
- Safe division by zero handling
- Automatic dataset saving
- Automatic report generation
- Output folder creation
- Error handling for invalid files
- Modular project architecture

---

## Project Structure

```
feature-engineering-assistant/
│
├── datasets/
│   ├── cleaned_data.csv
│   └── processed_titanic.csv
│
├── outputs/
│   ├── engineered_cleaned_data.csv
│   └── feature_engineering_report.txt
│
├── feature_engineering.py
├── report.py
├── utils.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Workflow

```
Cleaned Dataset
        │
        ▼
Load Dataset
        │
        ▼
Feature Engineering
│
├── Polynomial Features
├── Interaction Features
└── Ratio Features
        │
        ▼
Engineered Dataset
        │
        ▼
Feature Engineering Report
```

---

## Example

### Input Dataset

```
age
fare
```

### Generated Features

```
age_squared
fare_squared
age_x_fare
age_per_fare
```

---

## Output

The application automatically creates:

```
outputs/
├── engineered_cleaned_data.csv
└── feature_engineering_report.txt
```

---

## Technologies

- Python
- Pandas
- NumPy
- Pathlib

---

## Features

- Load cleaned datasets
- Generate polynomial features
- Generate interaction features
- Generate ratio features
- Save engineered datasets
- Generate feature engineering reports
- Prevent target leakage by excluding the target column from engineered features

## Future Improvements

- Ignore identifier columns automatically
- User-selectable feature types
- Date feature engineering
- Text feature engineering
- Custom feature selection
- Statistical feature generation
- Performance optimization for large datasets

---

## Author

Developed by **Abror Akhmadkhujaev** as part of a Machine Learning portfolio project series.