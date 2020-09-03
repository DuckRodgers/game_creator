import pandas as pd
import numpy as np
from io import BytesIO


def game_maker(df_input):
    """
    Mother function which returns a dataframe
    """

    def refurbish_df(object):
        """
        Child function which chooses the columns for
        the new game
        """
        players = object['Responsible'].unique() #This obtains the players's name from the db
        count = 0
        df_res = pd.DataFrame()
        df_half = pd.DataFrame()
        copy = object.copy()
        for player in players:
            if (count==0):
                df_res = copy.loc[copy['Responsible'] == player]
                df_res['Random'] = np.random.uniform(0.0000,0.9999,size=len(df_res.index))
                df_res = df_res.sort_values(by=['Random'])
                df_res = df_res.iloc[:4,:]
                count += 1
            else:
                df_half = copy.loc[copy['Responsible'] == player]
                df_half['Random'] = np.random.uniform(0.0000,0.9999,size=len(df_half.index))
                df_half = df_half.sort_values(by=['Random'])
                list_df = [df_res,df_half]
                res = pd.concat(list_df)
        return res

    mid_df = refurbish_df(df_input)
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    mid_df.to_excel(writer, startrow=0, merge_cells=False, sheet_name="Game")
    workbook = writer.book
    writer.close()
    output.seek(0)
    return output