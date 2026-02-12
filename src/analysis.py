import pandas as pd


def calculate_churn_rate(df, group_col):
    """
    Calculate churn percentage by a grouping column.

    Parameters:
    df (DataFrame): Dataset
    group_col (str): Column name to group by

    Returns:
    DataFrame: Churn percentage table
    """
    churn_table = pd.crosstab(
        df[group_col],
        df["Churn"],
        normalize="index"
    ) * 100

    return churn_table