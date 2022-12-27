import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from datetime import timedelta


class UserSessionSeparation():
    
    
    def __init__(self, max_session_minutes: float=3.):
        self.max_session_minutes = max_session_minutes
        self.df = pd.DataFrame()
    
    
    @classmethod
    def _add_preparation_columns(cls, df: pd.DataFrame) -> pd.DataFrame:
        """
        Method adds preparation columns to DF
        
        :param df: initial data frame for preparation
        :return:   pandas data frame with time_diff and dummy session_id columns
        """
        
        df['time_diff'] = df.groupby('customer_id')['timestamp'].diff().fillna(value=pd.to_timedelta(0))
        df['session_id'] = 0
        return df
    
    
    def _session_maker(self, df_group: pd.DataFrame) -> pd.Series:
        """
        Method split sessions relying on max_session_minutes for specific customer
        
        :param df_group: input data frame part with data for 1 customer
        :return:         pandas series with session_id for 1 customer
        """
        
        df = df_group[['time_diff']].reset_index(drop=True)
        session = 1
        for i in range(len(df)):
            if df.loc[i, 'time_diff']<=timedelta(minutes=self.max_session_minutes):
                df.loc[i, 'session_id'] = session
            else:
                session += 1
                df.loc[i, 'session_id'] = session
        return df['session_id'].astype('int8')
    
    
    def df_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Method transforms DF adding session_id
        
        :param df: input data frame for transformation
        :return:   transformed data frame with session_id
        """
        
        df = self._add_preparation_columns(df)
        for key in df.groupby('customer_id').groups.keys():
            df_grouped = df.groupby('customer_id').get_group(key)
            df.loc[df['customer_id']==key, 'session_id'] = self._session_maker(df_grouped).values
        
        return df
    
    
    @staticmethod
    def plot_graph(df: pd.DataFrame, customer: int=1) -> None:
        """
        Method plots testing graph
        
        :param df:       input transformed data frame  
        :param customer: choosen the customer for visualization 
        """
        
        fig_df = df.loc[df['customer_id']==customer, :].reset_index(drop=True)
        fig_df['minutes'] = fig_df['time_diff'].astype('timedelta64[s]') / 60
        fig_df['minutes'] = fig_df['minutes'].round(1)
        fig_df['cum_minutes'] = fig_df['time_diff'].astype('timedelta64[s]').cumsum() / 60

        plt.figure(figsize=(18, 8))
        plt.suptitle(f"CUSTOMER-{customer} SESSIONS", color='yellow')
        plt.title("numbers on graph corresponds to minutes delay after previous session_id", color='gold')
        sns.scatterplot(data=fig_df, x='cum_minutes', y='session_id', hue='session_id', palette='Paired')
        plt.xlabel('Cumulated minutes scince the 1st enter')
        flag = 0
        for line in range(0, fig_df.shape[0]):
            if fig_df['session_id'][line] != flag:
                flag = fig_df['session_id'][line]
                plt.text(fig_df['cum_minutes'][line]-2.4, fig_df['session_id'][line], fig_df['minutes'][line], horizontalalignment='left', size='medium', color='yellow')
        plt.show()
