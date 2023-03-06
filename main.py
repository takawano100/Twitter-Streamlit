import streamlit as st
import numpy as np
import pandas as pd


st.title('プログラミング教室 Twitter 分析結果')

"""
# これまでの作業の説明

１．３月４日
  (1)Twitter_APIを使って「プログラミング教育」「プログラミング教室　小学生」で
  つぶやきを検索
  - 「プログラミング教育」 → 956件（過去１周間）
  - 「プログラミング教室　小学生」 → 107件（過去１周間）

  (2)発言の多い人を週出
  - 「プログラミング教育」 → 16人
  - 「プログラミング教室　小学生」 → 7人

  (3)発言者の内、フォロワーが多い（1,000人以上）に絞る
  7人がフォロワー 1,000 人以上

  (4)7人をフォローをしているユーザーを抽出
 
   - 98507061 : 2,018 人
   - 1100479543 : 10,000 人(上限)
   - 1595290706 : 1,923 人
   - 4485056533 : 2,837 人
   - 1083565539933315072 : 8,663 人
   - 1086130739932844033 : 2,960 人
   - 1230342829706137601 : 3,558 人
   - 合計  31,959 人 フォロワー（重付呪があるかも）

２．３月５日
 (1)上記の中から、name または description に「ママ」がある人を抽出
   - 98507061 : 33 人
   - 1100479543 : 175 人
   - 1595290706 : 6 人
   - 4485056533 : 4 人
   - 1083565539933315072 : 2,061 人
   - 1086130739932844033 : 21 人
   - 1230342829706137601 : 246 人
   - 合計  2,546 人

   思った以上に「ママ」がいるのでどうしたものか思案中です。
"""
"""
# Twitter 一覧表の見かた
- id : 内部コード（通常は見えない）
- name : 名前
- username : @に続くID
- created_at : 作成年月
- protected : ？
- whitheld : ？
- location : 場所（任意）
- url : リンク
- description : プロフィール（事故紹介）
- verified : ？
- entities : ？
- profile_images_url : 画像
- public_metrics : 各種指標
-  followers_count : フォロワー数
-  folling_count : フォロー数
-  tweet_count : tweet数
-  listed_count : ？
- pinned_tweetd_id : 固定したID
"""
"""
# 抽出したフォロワーさん一覧
"""

df_1 = pd.read_csv('twitter_user_info_1.csv')
df_2 = pd.read_csv('twitter_user_info_2.csv')

st.text('「プログラミング教室　小学生」 : 9 人')
st.dataframe(df_1)
st.text('「プログラミング教育」 : 16 人')
st.dataframe(df_2)

"""
# 抽出したママさんの一覧
"""
df1 = pd.read_csv('df1_new.csv')
df2 = pd.read_csv('df2_new.csv')
df3 = pd.read_csv('df3_new.csv')
df4 = pd.read_csv('df4_new.csv')
df5 = pd.read_csv('df5_new.csv')
df6 = pd.read_csv('df6_new.csv')
df7 = pd.read_csv('df7_new.csv')

st.text('鎌田裕二『何でも相談できるパソコン駆込み寺』（横浜市鶴見区）(98507061) : 33 人')
st.dataframe(df1)
st.text('ICT教育ニュース(1100479543) : 175 人')
st.dataframe(df2)
st.text('名古屋文理大学 情報メディア学科(1595290706) : 6 人')
st.dataframe(df3)
st.text('nest＋＋(4485056533) : 4 人')
st.dataframe(df4)
st.text('ららこ＠子供プログラミング教室口コミいっぱい書きました。(1083565539933315072) : 2,061 人')
st.dataframe(df5)
st.text('現役エンジニアが選ぶ@プログラミングスクール比較bot(1086130739932844033) : 21 人')
st.dataframe(df6)
st.text('キャリアハブ(1230342829706137601) : 246 人')
st.dataframe(df7)


# img = Image.open(https://pbs.twimg.com/profile_images/1594177059127193601/jvT7GnkE_normal.jpg)
# st.image(img, caption='test')

