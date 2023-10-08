import streamlit as st
from PIL import Image

st.title('テストアプリ')
st.caption('これはテストアプリです。')

st.subheader('自己紹介')
st.text('外部ライブラリ「streamlit」を使って簡単にwebアプリを作成してみようと思います。\n'
        '宜しくお願いします。')

# 画像
image = Image.open('./data/スライム.jpg')
st.image(image, width=300)