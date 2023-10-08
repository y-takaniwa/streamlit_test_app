import streamlit as st
from PIL import Image
import pandas as pd

# データフレーム
df = pd.read_csv('./data/人口動態.csv', index_col='西暦（年）', encoding='shift-jis')
st.dataframe(df)

# テーブル
st.table(df)

# 折れ線グラフ
st.line_chart(df)

# 棒グラフ
st.bar_chart(df)