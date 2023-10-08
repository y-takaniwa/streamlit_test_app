import streamlit as st
from PIL import Image

with st.form(key='profile_form'):
        # テキストボックス
        name = st.text_input('名前')
        address = st.text_input('住所')
        
        # セレクトボックス
        # 第一引数はラベル、第二引数は選択肢
        age_category = st.selectbox('年齢層', ('18歳未満', '18歳以上'))
        
        # ラジオボタン
        # 第一引数はラベル、第二引数は選択肢
        gender = st.radio('性別', ('男性', '女性'))
        if gender == '男性':
                gender = 'ミスター'
        else:
                gender = 'ミセス'
        
        # マルチセレクト
        # 第一引数はラベル、第二引数は選択肢
        hobbys = st.multiselect('趣味',('スポーツ', '読書', '映画', '釣り', '料理'))

        # スライダー
        height = st.slider('身長', min_value=110, max_value=200)

        # 日付
        start_date = st.date_input('開始日')

        # ボタン
        submit_btn = st.form_submit_button('送信')
        cancel_btn = st.form_submit_button('キャンセル')

        if submit_btn:
                st.text(f'ようこそ、{gender}{name}。{address}に郵送しました。')
                st.text(f'年齢層：{age_category}')
                st.text(f'趣味：{"と".join(hobbys)}')
                st.text(f'身長：{height}cm')
                st.text(f'開始日：{start_date}')
