import streamlit as st
import pandas as pd 
import numpy as np
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from st_aggrid.shared import JsCode


st.set_page_config(page_title="Red State Vs Blue State", layout="wide") 
st.markdown("<h1 style='text-align: center; color: grey;'>Red State Vs Blue State</h1>", unsafe_allow_html=True)

b =['California', 'Colorado', 'Connecticut', 'Delaware', 'Hawaii', 'Illinois', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Nevada', 'New Hampshire', 'New Jersey', 'New York', 'Oregon', 'Pennsylvania', 'Rhode Island', 'Vermont', 'Washington']
r = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'Florida', 'Georgia', 'Idaho', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'New Mexico', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Virginia', 'West Virginia', 'Wisconsin', 'Wyoming']

data= pd.read_excel('/home/ismail/Downloads/redblu.xlsx', header=[2])


jscode = JsCode("""
            function(params) {
                if (params.data.Index === 1) {
                    return {
                        'color': 'white',
                        'backgroundColor': '#52b7e9'
                    }
                } else {
                    return {
                        'color': 'white',
                        'backgroundColor': '#ff8a80'
        }
    }
            };
            """)

df = pd.DataFrame(data)
df.rename(columns = {'Unnamed: 0':'Index'}, inplace = True)
df['average net worth'].astype(float)

gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_pagination()
gb.configure_side_bar()
gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="max", editable=True)
gb.configure_column("average net worth", type=["numericColumn", "numberColumnFilter", "customCurrencyFormat"], custom_currency_symbol="$ ")
gridOptions = gb.build()
gridOptions['getRowStyle'] = jscode
AgGrid(df,
              gridOptions=gridOptions,
              allow_unsafe_jscode=True, 
              fit_columns_on_grid_load=True,
              update_mode=GridUpdateMode.SELECTION_CHANGED)