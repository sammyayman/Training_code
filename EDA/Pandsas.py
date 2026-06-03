import pandas as pd
import numpy as np
from IPython.display import display

# 1) Dict of lists
Dict_List ={
    'hiragana': ['あ','い', 'う','え','お','か','き','く','け','こ'],
    'katakana': ['ア','イ', 'ウ','エ','オ','カ','キ','ク','ケ','コ'],
    'romaji': ['a','i', 'u','e','o','ka','ki','ku','ke','ko']
    
}
kana_data = pd.DataFrame(Dict_List)
print(kana_data)

# 2) List of dicts
List_Dict = [
    {'hira': 'さ', 'kata': 'サ', 'roma': 'sa'},
    {'hira': 'し', 'kata': 'シ', 'roma': 'shi'},
    {'hira': 'す', 'kata': 'ス', 'roma': 'su'},
    {'hira': 'せ', 'kata': 'セ', 'roma': 'se'},
    {'hira': 'そ', 'kata': 'ソ', 'roma': 'so'}
     
]
kana_data= pd.DataFrame(List_Dict)
print(kana_data)

# 3) List of lists/tuples
List_Tuples =  [('た','タ','ta'), 
     ( 'ち','チ','chi'), 
     ('つ','ツ','tsu'),
     ('て','テ','te'), 
     ('と','ト','to')]
col = ['hiragana','katakana', 'romaji']

kana_data = pd.DataFrame(List_Tuples,  columns=col )

# 4) NumPy array
arr = np.array([['な','ナ','na'], ['に','ニ','ni'],['ぬ','ヌ','nu'],
                ['ね','ネ','ne'], ['の','ノ','no']])
kana_data = pd.DataFrame(arr, columns=col)
print(kana_data)


# 5) Structured NumPy array
rec = np.array([(1, 'や','ヤ','ya'), (2, 'ゆ','ユ','yu'), (3, 'よ', 'ヨ','yo')])
kana_data = pd.DataFrame.from_records(rec)
print(kana_data)


# 6) From records
rec = [('ん',' ン','n') , ('な','ナ','na'), ('に','ニ','ni'),('ぬ','ヌ','nu'),
     ('ね','ネ','ne'), ('の','ノ','no')]
cols=['H','K','R']

kana_data = pd.DataFrame.from_records(rec, columns=cols)
    

# 7) From dict with orient
d = {
    'ha': {'H': 'は', 'K': 'ハ'},
    'hi': {'H': 'ひ', 'K': 'ヒ'},
    'fu': {'H': 'ふ', 'K': 'フ'},
    'he': {'H': 'へ', 'K': 'ヘ'},   
    'ho': {'H': 'ほ', 'K': 'ホ'}
}
kana_data = pd.DataFrame.from_dict(d, orient='index')
print(kana_data)

# 8) Using zip
R =['ba','bi','bu','be','bo']
H = ['ば','び','ぶ','べ','ぼ']
K = ['バ','ビ','ブ','ベ','ボ']
list_zip= list(zip(H,K,R))

 
kana_data = pd.DataFrame(list_zip, columns=col)
print(kana_data)



#9) Dict of Series
hira = pd.Series(['ん', 'わ','を' ], index=['n', 'wa', 'wo'])
kata = pd.Series(['ン','ワ','ヲ'], index=['n', 'wa', 'wo'])

kana_data = pd.DataFrame({'H': hira ,'K': kata})
print(kana_data)

# 10) Series → DataFrame

s1 = pd.Series(['ま' ,'み', 'む','め','も'], name='Hira')
s2 = pd.Series(['マ','ミ','ム','メ','モ'], name='Kata')
s3 = pd.Series(['ma','mi','mu','me','mo'], name='Roma')

df = pd.concat([s1, s2, s3], axis=1)

display(df)


# 11)  Dict of Series (rows)
dict_ser = {
    'y1': pd.Series({'H': 'や', 'K': 'ヤ' , 'R': 'ya'}),
    'y2' : pd.Series({'H': 'ゆ', 'K': 'ユ' , 'R': 'yu'}),
    'y3' : pd.Series({'H': 'よ', 'K': 'ヨ' , 'R': 'yo'}),
    
    'w1': pd.Series({'H': 'わ', 'K': 'ワ' , 'R': 'wa'}),
    'w2' : pd.Series({'H': 'を', 'K': 'ヲ' , 'R': 'wo'}),
    
    'n' : pd.Series({'R': 'n','H': 'ん', 'K': 'ン' }),
}

kana_data = pd.DataFrame(dict_ser).T
print(kana_data)
 
 
 
 
from math import pi, e, sqrt
import polars as pl
# 12) Using arange
df_1 = pd.DataFrame( e, index=range(1,4), columns=['a', 'b'])
print(df_1)


# 13) Generator
gen = ({'i': i, 'square': sqrt(i)} for i in range(4,11,2))
List = list(gen)

df_2 = pd.DataFrame(List)

print(df_2,List,pl.DataFrame(List))


gen = [{'i': i} for i in range(11)]

hiragana = ["ぜろ","いち","に","さん","よん","ご","ろく","なな","はち","きゅう","じゅう"]
kanji     = ["零" , "一" , "二","三","四","五","六","七","八","九","十"]
romaji    = ["zero","ichi","ni","san","yon","go","roku","nana","hachi","kyuu","juu"]

df20 = pd.DataFrame(gen)
df20["hiragana"] = hiragana
df20["kanji"] = kanji
df20["romaji"] = romaji

print(df20)



# 16) Collect rows manually
rows = []
for i in range(10,40,10):  rows.append({'num': i, 'num x pi': i*pi})
df_3 = pd.DataFrame(rows)
display(df_3,rows)

print("\n\n------------------------")
 

rows = []
hiragana = ['にじゅう','さんじゅう','よんじゅう','ごじゅう','ろくじゅう','ななじゅう','はちじゅう','きゅうじゅう','ひゃく']
kanji = ['二十','三十','四十','五十','六十','七十','八十','九十','百']
romaji = ['nijuu','sanjuu','yonjuu','gojuu','rokujuu','nanajuu','hachijuu','kyuujuu','hyaku']
for i in range(10,91,10):  rows.append({'num': i})
df_3 = pd.DataFrame(rows)
df_3["hiragana"] = hiragana
df_3["kanji"] = kanji   
df_3["romaji"] = romaji
print(df_3)

