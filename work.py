import streamlit as st
import pandas as pd
import numpy as np


yuhi = 'src/yuhi02.csv'
yakei = 'src/yakei02.csv'
onsen = 'src/onsen02.csv'
yuho = 'src/yuho02.csv'
meijo = 'src/shiro02.csv'

@st.cache
def load_data(file):
    df_load = pd.read_csv(file,encoding='shift-jis')
    # 経度緯度をmapで認識できるように修正
    df1 = df_load.rename(columns={'北緯': 'lat','東経':'lon'})
    # 所在地を都道府県と市区町村に分割
    df2 = pd.concat([df1,df1['所在地'].str.extract('(?P<都道府県>...??[都道府県])(?P<市区町村>.*)', expand=True)], axis=1).drop('所在地', axis=1)
    return df2

def main():
    st.title('ドライブで行ってみたいスポット')
    st.markdown('左のボックスからジャンルを選ぶ')
    block_list = ['夕陽', '夜景', '温泉', '遊歩道', '名城']
    control_features = st.sidebar.selectbox('何を楽しみたい？',block_list)
    st.header(f'{control_features}100選')
    if control_features == '夕陽':
        visualize(yuhi)
    elif control_features == '夜景':
        visualize(yakei)
    elif control_features == '温泉':
        visualize(onsen)
    elif control_features == '遊歩道':
        visualize(yuho)
    elif control_features == '名城':
        visualize(meijo)


def visualize(file):
    df = load_data(file)
    st.dataframe(df[['名称','都道府県','市区町村']])
    if st.sidebar.checkbox('mapを表示',):
        
        st.subheader('map')
        st.map(df)

import webbrowser
url = "https://www.google.co.jp/maps/?hl=ja"
webbrowser.open(url, 2)



        


if __name__ == "__main__":
    main()
    