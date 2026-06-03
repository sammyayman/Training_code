import polars as pl
import numpy as np

# 1) Dict of lists
Dict_List ={
    'hiragana': ['あ','い', 'う','え','お','か','き','く','け','こ'],
    'katakana': ['ア','イ', 'ウ','エ','オ','カ','キ','ク','ケ','コ'],
    'romaji': ['a','i', 'u','e','o','ka','ki','ku','ke','ko']
}

kana_data = pl.DataFrame(Dict_List)
print(kana_data)

h= ["ら","り","る","れ","ろ"]
k = ["ラ","リ","ル","レ","ロ"]
r = ["ra","ri","ru","re","ro"]

Dict_List ={
    "hiragana": h,
    "katakana": k,
    "romaji": r
}
df3 = pl.DataFrame(Dict_List)

print(df3)

# 2) List of dicts
List_Dict = [
    {'hira': 'さ', 'kata': 'サ', 'roma': 'sa'},
    {'hira': 'し', 'kata': 'シ', 'roma': 'shi'},
    {'hira': 'す', 'kata': 'ス', 'roma': 'su'},
    {'hira': 'せ', 'kata': 'セ', 'roma': 'se'},
    {'hira': 'そ', 'kata': 'ソ', 'roma': 'so'}
     
]
kana_data= pl.DataFrame(List_Dict)
print(kana_data)


# 3) List of lists/tuples

List_Tuples =  [('た','タ','ta'), 
                ( 'ち','チ','chi'), 
                ('つ','ツ','tsu'),
                ('て','テ','te'), 
                ('と','ト','to')]
col = ['hiragana','katakana', 'romaji']

kana_data = pl.DataFrame(List_Tuples, schema=col , orient="row" )
print(kana_data)




 
# # 4) NumPy array
arr = np.array([['な','ナ','na'], 
                ['に','ニ','ni'],
                ['ぬ','ヌ','nu'],
                 ['ね','ネ','ne'], 
                 ['の','ノ','no']])

kana_data = pl.DataFrame(arr, schema=col)
print(kana_data)

# 5) Dict of Series
 

hira = pl.Series('H',['ん', 'わ','を' ])
kata = pl.Series('K',['ン','ワ','ヲ'])
roma = pl.Series('R',['n', 'wa','wo'])
kana_data = pl.DataFrame([hira ,kata,roma],schema=col)
print(kana_data)



# 6) Series → DataFrame
s = pl.Series('values', [10, 20, 30])
df11 = pl.DataFrame(s)
print(df11)

s1 = pl.Series(name='Hira', values=['ま', 'み', 'む', 'め', 'も'])
s2 = pl.Series(name='Kata', values=['マ', 'ミ', 'ム', 'メ', 'モ'])
s3 = pl.Series(name='Roma', values=['ma', 'mi', 'mu', 'me', 'mo'])

# Convert each Series to a DataFrame (1 column each)
df = pl.concat(
    [s1.to_frame(), s2.to_frame(), s3.to_frame()],
    how="horizontal"
)

print(df)

# # 7) Structured NumPy array

arr = np.array([['な','ナ','na'], ['に','ニ','ni'],
                ['ぬ','ヌ','nu'],['ね','ネ','ne'], 
                ['の','ノ','no'],['ら','ラ','ra'],
                ['り','リ','ri'],['る','ル','ru'],
                ['れ','レ','re'],['ろ','ロ','ro']])

kana_data = pl.DataFrame(arr, schema=col)
print(kana_data)


# # 8) From records
lst_rec = [('ha', 'は', 'ハ'),
     ('hi', 'ひ', 'ヒ'),
     ('fu', 'ふ', 'フ'),
     ('he', 'へ', 'ヘ'),
     ('ho', 'ほ', 'ホ')]

df8 = pl.DataFrame(lst_rec, 
                   schema=['rama', 'hira','kata'], 
                   orient="row" )
print(df8)

# 9) From dict with orient (row-wise)
# d = {
#     'row1': {'a': 1, 'b': 2},
#     'row2': {'a': 3, 'b': 4}
# }
# lst_dvalues = list(d.values())
# lst_dkeys = list(d.keys())
# df9 = pl.DataFrame(lst_dvalues)

# print(df9)  
# df9 = df9.with_columns(row_id=pl.Series(lst_dkeys))
# print(df9)

# 10) Using zip
roma =['ba','bi','bu','be','bo']
hira = ['ば','び','ぶ','べ','ぼ']
kata = ['バ','ビ','ブ','ベ','ボ']
list_zip= list(zip(roma,hira,kata))

df10 = pl.DataFrame(list_zip, 
                    schema=['R', 'H', 'K'],
                    orient="row")
print(df10)


# # 12) Empty DataFrame
# df12 = pl.DataFrame(schema=['a', 'b'])
# print(df12)
 
 
 
 

 


# # 18) Dict of Series (rows)

dict_ser = {
    
    'y1': {'H': 'や', 'K': 'ヤ', 'R': 'ya'},
    'y2': {'H': 'ゆ', 'K': 'ユ', 'R': 'yu'},
    'y3': {'H': 'よ', 'K': 'ヨ', 'R': 'yo'},
    
    'w1': {'H': 'わ', 'K': 'ワ', 'R': 'wa'},
    'w2': {'H': 'を', 'K': 'ヲ', 'R': 'wo'},
    
    'n':  {'H': 'ん', 'K': 'ン', 'R': 'n'},
}

# Convert dict → rows → Polars DataFrame
df = pl.DataFrame([
    {"row": key, **val}
    for key, val in dict_ser.items()
])

print(df)




# 16) Generator
gen = ({'i': i, 'square': i*i} for i in range(10))


df20 = pl.DataFrame(gen)
print(df20)


gen = [{'i': i} for i in range(11)]

hiragana = ["ぜろ","いち","に","さん","よん","ご","ろく","なな","はち","きゅう","じゅう"]
kanji     = ["零" , "一" , "二","三","四","五","六","七","八","九","十"]
romaji    = ["zero","ichi","ni","san","yon","go","roku","nana","hachi","kyuu","juu"]

df20 = pl.DataFrame(gen).with_columns([
    pl.Series("hiragana", hiragana),
    pl.Series("kanji", kanji),
    pl.Series("romaji", romaji)
])

print(df20)

# 17) Collect rows manually
rows = []
for i in range(10):
    rows.append({'num': i, 'double': i*2})
df21 = pl.DataFrame(rows)
print(df21)

rows = []
hiragana = ['にじゅう','さんじゅう','よんじゅう','ごじゅう','ろくじゅう','ななじゅう','はちじゅう','きゅうじゅう','ひゃく']
kanji = ['二十','三十','四十','五十','六十','七十','八十','九十','百']
romaji = ['nijuu','sanjuu','yonjuu','gojuu','rokujuu','nanajuu','hachijuu','kyuujuu','hyaku']
for i in range(10,91,10):
    rows.append({'num':i})
df21 = pl.DataFrame(rows).with_columns([
    pl.Series("hiragana", hiragana),
    pl.Series("kanji", kanji),
    pl.Series("romaji", romaji)
])
print(df21)




# Object type examples :
 
# df = pl.DataFrame(
#     {
#         "id": [1, 2, 3, 4, 5,6],
#         "data": [{"a": 1}, [1, 2, 3], (9**2, 8),"Sonic",3/5,False]   # objects
#     },
#     schema=[
#         ("id", pl.Int64),
#         ("data", pl.Object)
#     ]
# )

# print(df)


# rows = [
#     (1, {"x": 10}),
#     (2, [1, 2, 3]),
#     (3, ("A", "B")),
#     (4, None),
#     (5, 42),
#     (6, 3.14),
#     (7, True),
   
#     (9,"Crash Bandicoot"),
#     (8, 5%6)
    
    
# ]

# df = pl.DataFrame(
#     rows,
#     schema=[("id", pl.Int64), ("payload", pl.Object)],
#     orient="row"
# )

# print(df)


# df = pl.DataFrame(
#     {
#         "name": ["A", "B", "C"],
#         "value": [10, 20, 30],
#         "meta": [{"ok": True}, {"ok": False}, {"ok": None}],
#     },
#     schema=[
#         ("name", pl.Utf8),
#         ("value", pl.Int64),
#         ("meta", pl.Object)
#     ]
# )

# print(df)




# import pandas as pd


# pdf = pd.DataFrame({
#     "x": np.arange(1, 6),          # x = 1, 2, 3, 4, 5
#     "y": np.arange(6, 11)          # y = 6, 7, 8, 9, 10
# })
# print("Pandas DataFrame:")
# print(pdf)

# df = pl.from_pandas(pdf)
# print("\nPolars DataFrame:")
# print(df)


# df = df.with_columns(
#     (pl.col("x")**2 + pl.col("y")**2).alias("z")
# )
# print("\nPolars DataFrame after adding column 'z':")
# print(df)


# stats = df.select([
#     pl.sum("z").alias("sum_z"),
#     pl.mean("z").alias("mean_z"),
#     pl.min("z").alias("min_z"),
#     pl.max("z").alias("max_z")
# ])

# print("\nPolars DataFrame with z column:")
# print(df)


# print("\nStatistics of z column:")
# print(stats)

# # --- Step 5: Filter rows where z > 50 ---
# df_filtered = df.filter(pl.col("z") > 50)
# print("\nRows where z > 50:")
# print(df_filtered)

# df_polars = pl.DataFrame(
#     {
#         "hiragana": [
#             "あ","い","う","え","お",
#             "か","き","く","け","こ",
#             "が","ぎ","ぐ","げ","ご",
#             "さ","し","す","せ","そ",
#             "ざ","じ","ず","ぜ","ぞ",
#             "た","ち","つ","て","と",
#             "だ","ぢ","づ","で","ど",
#             "な","に","ぬ","ね","の",
#             "は","ひ","ふ","へ","ほ",
#             "ば","び","ぶ","べ","ぼ",
#             "ぱ","ぴ","ぷ","ぺ","ぽ",
#             "ま","み","む","め","も",
#             "や","ゆ","よ",
#             "ら","り","る","れ","ろ",
#             "わ","を",
#             "ん"
#         ],
#         "katakana": [
#             "ア","イ","ウ","エ","オ",
#             "カ","キ","ク","ケ","コ",
#             "ガ","ギ","グ","ゲ","ゴ",
#             "サ","シ","ス","セ","ソ",
#             "ザ","ジ","ズ","ゼ","ゾ",
#             "タ","チ","ツ","テ","ト",
#             "ダ","ヂ","ヅ","デ","ド",
#             "ナ","ニ","ヌ","ネ","ノ",
#             "ハ","ヒ","フ","ヘ","ホ",
#             "バ","ビ","ブ","ベ","ボ",
#             "パ","ピ","プ","ペ","ポ",
#             "マ","ミ","ム","メ","モ",
#             "ヤ","ユ","ヨ",
#             "ラ","リ","ル","レ","ロ",
#             "ワ","ヲ",
#             "ン"
#         ],
#         "romaji": [
#             "a","i","u","e","o",
#             "ka","ki","ku","ke","ko",
#             "ga","gi","gu","ge","go",
#             "sa","shi","su","se","so",
#             "za","ji","zu","ze","zo",
#             "ta","chi","tsu","te","to",
#             "da","ji","zu","de","do",
#             "na","ni","nu","ne","no",
#             "ha","hi","fu","he","ho",
#             "ba","bi","bu","be","bo",
#             "pa","pi","pu","pe","po",
#             "ma","mi","mu","me","mo",
#             "ya","yu","yo",
#             "ra","ri","ru","re","ro",
#             "wa","wo",
#             "n"
#         ]
#     }
# )

# # try a big integer instead of `None` if terminal doesn't like None
# pl.Config.set_tbl_rows(1000)          # show up to 1000 rows
# pl.Config.set_tbl_cols(200)           # show up to 200 columns
# pl.Config.set_tbl_width_chars(4000)   # allow a wide table


# print(df_polars)
