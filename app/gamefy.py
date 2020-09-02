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
        list_players = object['Responsible'].unique() #This obtains the players's name from the db
        return inter_df

    mid_df = refurbish_df(df_input)
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    mid_df.to_excel(writer, startrow=0, merge_cells=False, sheet_name="Game")
    workbook = writer.book
    writer.close()
    output.seek(0)
    return output