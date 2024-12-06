
# import pandas as pd
# import numpy as np

# def clean_data(file_path):
#     """
#     Cleans the data from the uploaded file.
#     :param file_path: Path to the uploaded CSV/Excel file.
#     :return: Cleaned DataFrame.
#     """
    # Load the file
    # if file_path.endswith(".csv"):
    #     df = pd.read_csv(file_path)
    # else:
    #     df = pd.read_excel(file_path)

    # Step 1: Handle Missing Values
    # Fill missing 'name' column with a default value like 'Unknown'
    # if 'name' in df.columns:
    #     df['name'] = df['name'].fillna('Unknown')
    
    # Handle missing values in numeric columns
    # for col in df.select_dtypes(include=[np.number]):  # For numeric columns only
        # Option 1: Impute missing numeric values with the mean of the column
        # df[col] = df[col].fillna(df[col].mean())
        
        # Alternatively, Option 2: Impute with the median if you suspect skewed distribution
        # df[col] = df[col].fillna(df[col].median())
        
        # Alternatively, Option 3: Impute with a specific value (e.g., 0, or the column's minimum)
        # df[col] = df[col].fillna(0)
        # df[col] = df[col].fillna(df[col].min())

    # Step 2: Remove Duplicates
    # df = df.drop_duplicates()

    # Step 3: Standardize Column Names
    # df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace(r"[^\w]", "", regex=True)

    # Step 4: Handle Outliers (using IQR method)
    # for col in df.select_dtypes(include=[np.number]):  # Numeric columns only
    #     q1 = df[col].quantile(0.25)
    #     q3 = df[col].quantile(0.75)
    #     iqr = q3 - q1
    #     lower_bound = q1 - 1.5 * iqr
    #     upper_bound = q3 + 1.5 * iqr
    #     df[col] = np.where((df[col] < lower_bound) | (df[col] > upper_bound), np.nan, df[col])

    # Refill outliers set to NaN (after removing outliers)
    # df = df.fillna(method='ffill').fillna(method='bfill')

    # return df
import pandas as pd
import numpy as np

def clean_data(file_path):
    """
    Cleans the data from the uploaded file.
    :param file_path: Path to the uploaded CSV/Excel file.
    :return: Cleaned DataFrame.
    """
    # Load the file
    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)

    # Step 1: Handle Missing Values
    # Fill missing string columns with 'Unknown'
    for col in df.select_dtypes(include=[object]):  # For columns with string data
        df[col] = df[col].fillna('Unknown')
    
    # Handle missing values in numeric columns
    for col in df.select_dtypes(include=[np.number]):  # For numeric columns only
        # Option 1: Impute missing numeric values with the mean of the column
        df[col] = df[col].fillna(df[col].mean())
        
        # Alternatively, Option 2: Impute with the median if you suspect skewed distribution
        # df[col] = df[col].fillna(df[col].median())
        
        # Alternatively, Option 3: Impute with a specific value (e.g., 0, or the column's minimum)
        # df[col] = df[col].fillna(0)
        # df[col] = df[col].fillna(df[col].min())

    # Step 2: Remove Duplicates
    df = df.drop_duplicates()

    # Step 3: Standardize Column Names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace(r"[^\w]", "", regex=True)

    # Step 4: Handle Outliers (using IQR method)
    for col in df.select_dtypes(include=[np.number]):  # Numeric columns only
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        df[col] = np.where((df[col] < lower_bound) | (df[col] > upper_bound), np.nan, df[col])

    # Refill outliers set to NaN (after removing outliers)
    df = df.fillna(method='ffill').fillna(method='bfill')

    return df

