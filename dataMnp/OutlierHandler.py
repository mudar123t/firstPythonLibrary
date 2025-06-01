import pandas as pd

class OutlierHandler:

    @staticmethod
    def remove_outliers_iqr(df, threshold=1.5):
        """
        Remove outliers from the DataFrame using the interquartile range method.
        Parameters:
        - df: pandas DataFrame
            The DataFrame containing the data.
        - threshold: float, optional (default=1.5)
            The threshold value to determine outliers.
        Returns:
        - df: pandas DataFrame
            DataFrame with outliers removed.
        """
        Q1 = df.quantile(0.25)
        Q3 = df.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - threshold * IQR
        upper_bound = Q3 + threshold * IQR
        return df[~((df < lower_bound) | (df > upper_bound)).any(axis=1)]

    @staticmethod
    def change_outliers_value(df, threshold=1.5, replace_value=None):
        """
        Remove outliers from the DataFrame using the interquartile range method and replace them with a specified value.
        Parameters:
        - df: pandas DataFrame
            The DataFrame containing the data.
        - threshold: float, optional (default=1.5)
            The threshold value to determine outliers.
        - replace_value: float or None, optional (default=None)
            The value to replace outliers with. If None, outliers are removed without replacement.
        Returns:
        - df: pandas DataFrame
            DataFrame with outliers removed or replaced.
        """
        Q1 = df.quantile(0.25)
        Q3 = df.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - threshold * IQR
        upper_bound = Q3 + threshold * IQR
        if replace_value is not None:
            df = df.mask(df < lower_bound, replace_value)
            df = df.mask(df > upper_bound, replace_value)
        else:
            df = df[~((df < lower_bound) | (df > upper_bound)).any(axis=1)]
        return df
