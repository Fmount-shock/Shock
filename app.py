import streamlit as st

st.title('初めてのstreamlit')
st.write('これから作品を作っていきます')
st.write('Hello, World')
st.write('小作争議と労働争議')
st.write('レーニンとプーチン')
st.write('偉大なるスターリン')
st.write('治安維持法はうんこ')

text = st.text_input('あなたの名前を入力してください')
'あなたの名前は. ', text, 'です'

condition = st.slider('あなたの今の調子は？',0, 100, 50)
'コンディション：',condition

option = st.selectbox(
    '好きな数字を教えてください',
    list(['1番','2番','3番','4番'])
)
'あなたが選択したのは, ',option,'です'

st.sidebar.write('プログレスバーの表示')
'Start!'
