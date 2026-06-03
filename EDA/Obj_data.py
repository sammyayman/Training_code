import array
import numpy as np, polars as pl, pandas as pd
from IPython.display import display
print('\033[1;32m' + "Pandas DataFrame with Various Data Types" + '\033[0m')
Dict_List ={
    'string' : ['one', 'two', 'three', 'four', 'five'],
    'category': pd.Categorical(['A', 'B', 'A', 'B', 'C']),
    
    'integer': [1, 2, 3, 4, 5],
    'float'  : [1.1, 2.2, 3.3, 4.4, 5.5],
    'complex': [complex(1,1), complex(2,2), 3+2j, complex(4,4), 5-3.14j],
    
    'boolean': [True, False, True, False, True],
    'date'   : pd.date_range('20230101', periods=5),
    'object' : [{'a':np.nan}, [1,2], (3,4), "text", None],
    'json'   : ['{"key1": "value1"}', '{"key2": 2}', '{"key3": [1,2,3]}', '{"key4": true}', '{"key5": null}'],
    'dict'   : [{'key1': 'value1'}, {'key2': 2}, {'key3': [1,2,3]}, {'key4': True}, {'key5': None}],
    'list'   : [[1,2,3], ['a','b'], [True, False], [(1.1), (2.2)], [complex(1,1), complex(2,2)]]
    
      
}
pd= pd.DataFrame(Dict_List)
print(pd)

print('\033[1;32m' + "Polars DataFrame with Various Data Types" + '\033[0m')
from datetime import date, datetime, time

# Create a DataFrame with all main Polars data types, no pl.Series needed
df = pl.DataFrame({
    # Numeric types
    "int8": [1, 2, 3], 
    "float64": [1.11, 2.22, 3.33],

    # Boolean
    "boolean": [True, False, True],

    # Strings and categorical
    "string": ["Alice", "Bob", "Charlie"],
    "category": pl.Categorical(["A", "B", "A"]),  # Need pl.Categorical to specify category

    # Date/Time
    "date": [date(2025, 1, 1), date(2025, 1, 2), date(2025, 1, 3)],
    "datetime": [datetime(2025,1,1,10,0), datetime(2025,1,2,12,30), datetime(2025,1,3,15,45)],
    "time": [time(10,0), time(12,30), time(15,45)],

    # List
    "list": [[1,2,3], [4,5], [6]],

    # Struct
    "struct": [
        {"x": 1, "y": "a"}, 
        {"x": 2, "y": "b"}, 
        {"x": 3, "y": "c"}
    ],

    # Complex (split into real + imaginary)
    "complex_real": [1.0, 2.0, 3.0],
    "complex_imag": [0.5, -1.0, 2.0]
})

# Show all columns
pl.Config.set_tbl_cols(-1)

print(df)
print("\nData Types:")
print(df.dtypes)


import pandas as pd
import numpy as np

"""
Creating DataFrame with 5 rows and 5 columns:
- col1: Integer
- col2: String
- col3: Boolean
- col4: Float
- col5: Japanese numbers (一, 二, 三, 四, 五)
"""

print("=" * 80)
print("METHOD 1: From Dictionary of Lists")
print("=" * 80)

df1 = pd.DataFrame({
    'col1': [1, 2, 3, 4, 5],
    'col2': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'],
    'col3': [True, False, True, True, False],
    'col4': [10.5, 20.3, 30.7, 40.2, 50.9],
    'col5': ['一', '二', '三', '四', '五']
})
print(df1)
print("\nData types:\n", df1.dtypes)

print("\n" + "=" * 80)
print("METHOD 2: From List of Dictionaries (Row-oriented)")
print("=" * 80)

data2 = [
    {'col1': 1, 'col2': 'Apple', 'col3': True, 'col4': 10.5, 'col5': '一'},
    {'col1': 2, 'col2': 'Banana', 'col3': False, 'col4': 20.3, 'col5': '二'},
    {'col1': 3, 'col2': 'Cherry', 'col3': True, 'col4': 30.7, 'col5': '三'},
    {'col1': 4, 'col2': 'Date', 'col3': True, 'col4': 40.2, 'col5': '四'},
    {'col1': 5, 'col2': 'Elderberry', 'col3': False, 'col4': 50.9, 'col5': '五'}
]
df2 = pd.DataFrame(data2)
print(df2)

print("\n" + "=" * 80)
print("METHOD 3: From List of Lists with Column Names")
print("=" * 80)

data3 = [
    [1, 'Apple', True, 10.5, '一'],
    [2, 'Banana', False, 20.3, '二'],
    [3, 'Cherry', True, 30.7, '三'],
    [4, 'Date', True, 40.2, '四'],
    [5, 'Elderberry', False, 50.9, '五']
]
df3 = pd.DataFrame(data3, columns=['col1', 'col2', 'col3', 'col4', 'col5'])
print(df3)

print("\n" + "=" * 80)
print("METHOD 4: From NumPy Array (Mixed dtype)")
print("=" * 80)

# NumPy structured array for mixed types
data4 = np.array([
    (1, 'Apple', True, 10.5, '一'),
    (2, 'Banana', False, 20.3, '二'),
    (3, 'Cherry', True, 30.7, '三'),
    (4, 'Date', True, 40.2, '四'),
    (5, 'Elderberry', False, 50.9, '五')
], dtype=object)
df4 = pd.DataFrame(data4, columns=['col1', 'col2', 'col3', 'col4', 'col5'])
print(df4)

print("\n" + "=" * 80)
print("METHOD 5: From Tuples")
print("=" * 80)

data5 = [
    (1, 'Apple', True, 10.5, '一'),
    (2, 'Banana', False, 20.3, '二'),
    (3, 'Cherry', True, 30.7, '三'),
    (4, 'Date', True, 40.2, '四'),
    (5, 'Elderberry', False, 50.9, '五')
]
df5 = pd.DataFrame(data5, columns=['col1', 'col2', 'col3', 'col4', 'col5'])
print(df5)

print("\n" + "=" * 80)
print("METHOD 6: From Dictionary of Series")
print("=" * 80)

df6 = pd.DataFrame({
    'col1': pd.Series([1, 2, 3, 4, 5], dtype=int),
    'col2': pd.Series(['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'], dtype=str),
    'col3': pd.Series([True, False, True, True, False], dtype=bool),
    'col4': pd.Series([10.5, 20.3, 30.7, 40.2, 50.9], dtype=float),
    'col5': pd.Series(['一', '二', '三', '四', '五'], dtype=str)
})
print(df6)

print("\n" + "=" * 80)
print("METHOD 7: From Dictionary of NumPy Arrays")
print("=" * 80)

df7 = pd.DataFrame({
    'col1': np.array([1, 2, 3, 4, 5], dtype=int),
    'col2': np.array(['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'], dtype=object),
    'col3': np.array([True, False, True, True, False], dtype=bool),
    'col4': np.array([10.5, 20.3, 30.7, 40.2, 50.9], dtype=float),
    'col5': np.array(['一', '二', '三', '四', '五'], dtype=object)
})
print(df7)

print("\n" + "=" * 80)
print("METHOD 8: Using pd.DataFrame Constructor with Data and Index")
print("=" * 80)

df8 = pd.DataFrame(
    data=[
        [1, 'Apple', True, 10.5, '一'],
        [2, 'Banana', False, 20.3, '二'],
        [3, 'Cherry', True, 30.7, '三'],
        [4, 'Date', True, 40.2, '四'],
        [5, 'Elderberry', False, 50.9, '五']
    ],
    columns=['col1', 'col2', 'col3', 'col4', 'col5'],
    index=['row1', 'row2', 'row3', 'row4', 'row5']
)
print(df8)

print("\n" + "=" * 80)
print("METHOD 9: From Records (Structured Array)")
print("=" * 80)

records = [
    (1, 'Apple', True, 10.5, '一'),
    (2, 'Banana', False, 20.3, '二'),
    (3, 'Cherry', True, 30.7, '三'),
    (4, 'Date', True, 40.2, '四'),
    (5, 'Elderberry', False, 50.9, '五')
]
df9 = pd.DataFrame.from_records(
    records, 
    columns=['col1', 'col2', 'col3', 'col4', 'col5']
)
print(df9)

print("\n" + "=" * 80)
print("METHOD 10: From Dict with from_dict() - Orient='columns'")
print("=" * 80)

data10 = {
    'col1': [1, 2, 3, 4, 5],
    'col2': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'],
    'col3': [True, False, True, True, False],
    'col4': [10.5, 20.3, 30.7, 40.2, 50.9],
    'col5': ['一', '二', '三', '四', '五']
}
df10 = pd.DataFrame.from_dict(data10, orient='columns')
print(df10)

print("\n" + "=" * 80)
print("METHOD 11: From Dict with from_dict() - Orient='index'")
print("=" * 80)

data11 = {
    'row1': [1, 'Apple', True, 10.5, '一'],
    'row2': [2, 'Banana', False, 20.3, '二'],
    'row3': [3, 'Cherry', True, 30.7, '三'],
    'row4': [4, 'Date', True, 40.2, '四'],
    'row5': [5, 'Elderberry', False, 50.9, '五']
}
df11 = pd.DataFrame.from_dict(
    data11, 
    orient='index',
    columns=['col1', 'col2', 'col3', 'col4', 'col5']
)
print(df11)

print("\n" + "=" * 80)
print("METHOD 12: Empty DataFrame + Row Assignment")
print("=" * 80)

df12 = pd.DataFrame(columns=['col1', 'col2', 'col3', 'col4', 'col5'])
df12.loc[0] = [1, 'Apple', True, 10.5, '一']
df12.loc[1] = [2, 'Banana', False, 20.3, '二']
df12.loc[2] = [3, 'Cherry', True, 30.7, '三']
df12.loc[3] = [4, 'Date', True, 40.2, '四']
df12.loc[4] = [5, 'Elderberry', False, 50.9, '五']
print(df12)

print("\n" + "=" * 80)
print("METHOD 13: Using Concat with Series")
print("=" * 80)

s1 = pd.Series([1, 2, 3, 4, 5], name='col1')
s2 = pd.Series(['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'], name='col2')
s3 = pd.Series([True, False, True, True, False], name='col3')
s4 = pd.Series([10.5, 20.3, 30.7, 40.2, 50.9], name='col4')
s5 = pd.Series(['一', '二', '三', '四', '五'], name='col5')
df13 = pd.concat([s1, s2, s3, s4, s5], axis=1)
print(df13)

print("\n" + "=" * 80)
print("METHOD 14: From CSV String (StringIO)")
print("=" * 80)

from io import StringIO
csv_data = """col1,col2,col3,col4,col5
1,Apple,True,10.5,一
2,Banana,False,20.3,二
3,Cherry,True,30.7,三
4,Date,True,40.2,四
5,Elderberry,False,50.9,五"""

df14 = pd.read_csv(StringIO(csv_data))
print(df14)

print("\n" + "=" * 80)
print("METHOD 15: From JSON String")
print("=" * 80)

json_data = """[
    {"col1": 1, "col2": "Apple", "col3": true, "col4": 10.5, "col5": "一"},
    {"col1": 2, "col2": "Banana", "col3": false, "col4": 20.3, "col5": "二"},
    {"col1": 3, "col2": "Cherry", "col3": true, "col4": 30.7, "col5": "三"},
    {"col1": 4, "col2": "Date", "col3": true, "col4": 40.2, "col5": "四"},
    {"col1": 5, "col2": "Elderberry", "col3": false, "col4": 50.9, "col5": "五"}
]"""

df15 = pd.read_json(json_data)
print(df15)

print("\n" + "=" * 80)
print("METHOD 16: Using zip() to Combine Lists")
print("=" * 80)

col1_data = [1, 2, 3, 4, 5]
col2_data = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
col3_data = [True, False, True, True, False]
col4_data = [10.5, 20.3, 30.7, 40.2, 50.9]
col5_data = ['一', '二', '三', '四', '五']

df16 = pd.DataFrame(
    list(zip(col1_data, col2_data, col3_data, col4_data, col5_data)),
    columns=['col1', 'col2', 'col3', 'col4', 'col5']
)
print(df16)

print("\n" + "=" * 80)
print("METHOD 17: Using List Comprehension")
print("=" * 80)

fruits = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
japanese = ['一', '二', '三', '四', '五']
bools = [True, False, True, True, False]

data17 = [
    [i+1, fruits[i], bools[i], (i+1)*10 + 0.5 + i*0.2, japanese[i]]
    for i in range(5)
]
df17 = pd.DataFrame(data17, columns=['col1', 'col2', 'col3', 'col4', 'col5'])
print(df17)

print("\n" + "=" * 80)
print("METHOD 18: From Dictionary with Different Lengths (Auto-fills NaN)")
print("=" * 80)

# Note: All columns must have same length, showing explicit data
df18 = pd.DataFrame({
    'col1': range(1, 6),
    'col2': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'],
    'col3': [i % 2 == 0 for i in range(5)],  # False, True, False, True, False
    'col4': [10.5, 20.3, 30.7, 40.2, 50.9],
    'col5': ['一', '二', '三', '四', '五']
})
print(df18)

print("\n" + "=" * 80)
print("METHOD 19: Using assign() Method (Chaining)")
print("=" * 80)

df19 = pd.DataFrame({'col1': [1, 2, 3, 4, 5]})
df19 = df19.assign(
    col2=['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'],
    col3=[True, False, True, True, False],
    col4=[10.5, 20.3, 30.7, 40.2, 50.9],
    col5=['一', '二', '三', '四', '五']
)
print(df19)

print("\n" + "=" * 80)
print("METHOD 20: Explicit Type Conversion")
print("=" * 80)

df20 = pd.DataFrame({
    'col1': pd.array([1, 2, 3, 4, 5], dtype='int32'),
    'col2': pd.array(['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'], dtype='string'),
    'col3': pd.array([True, False, True, True, False], dtype='boolean'),
    'col4': pd.array([10.5, 20.3, 30.7, 40.2, 50.9], dtype='float64'),
    'col5': pd.array(['一', '二', '三', '四', '五'], dtype='string')
})
print(df20)
print("\nExplicit data types:\n", df20.dtypes)

print("\n" + "=" * 80)
print("SUMMARY: All Methods Comparison")
print("=" * 80)
print("""
1.  Dictionary of Lists               - Most common and readable
2.  List of Dictionaries              - Row-oriented, good for APIs
3.  List of Lists                     - Simple 2D structure
4.  NumPy Array (object)              - When working with NumPy
5.  List of Tuples                    - Similar to lists
6.  Dictionary of Series              - Fine control over data types
7.  Dictionary of NumPy Arrays        - Combine pandas with NumPy
8.  Constructor with Index            - Custom row labels
9.  from_records()                    - Database-style records
10. from_dict() - columns             - Standard dictionary
11. from_dict() - index               - Row-oriented dictionary
12. Empty + Assignment                - Build incrementally
13. Concat Series                     - Combine Series objects
14. From CSV String                   - Parse CSV data
15. From JSON String                  - Parse JSON data
16. Using zip()                       - Combine separate lists
17. List Comprehension                - Generate data dynamically
18. range() Function                  - Generate numeric sequences
19. assign() Method                   - Method chaining
20. Explicit Type Conversion          - Control exact data types
""")



import polars as pl
import numpy as np

"""
Creating Polars DataFrame with 5 rows and 5 columns:
- col1: Integer
- col2: String
- col3: Boolean
- col4: Float
- col5: Japanese numbers (一, 二, 三, 四, 五)

Installation: pip install polars
"""

print("=" * 80)
print("METHOD 1: From Dictionary of Lists")
print("=" * 80)

df1 = pl.DataFrame({
    'col1': [1, 2, 3, 4, 5],
    'col2': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'],
    'col3': [True, False, True, True, False],
    'col4': [10.5, 20.3, 30.7, 40.2, 50.9],
    'col5': ['一', '二', '三', '四', '五']
})
print(df1)
print("\nData types (schema):")
print(df1.schema)

print("\n" + "=" * 80)
print("METHOD 2: From List of Dictionaries (Row-oriented)")
print("=" * 80)

data2 = [
    {'col1': 1, 'col2': 'Apple', 'col3': True, 'col4': 10.5, 'col5': '一'},
    {'col1': 2, 'col2': 'Banana', 'col3': False, 'col4': 20.3, 'col5': '二'},
    {'col1': 3, 'col2': 'Cherry', 'col3': True, 'col4': 30.7, 'col5': '三'},
    {'col1': 4, 'col2': 'Date', 'col3': True, 'col4': 40.2, 'col5': '四'},
    {'col1': 5, 'col2': 'Elderberry', 'col3': False, 'col4': 50.9, 'col5': '五'}
]
df2 = pl.DataFrame(data2)
print(df2)

print("\n" + "=" * 80)
print("METHOD 3: From Dictionary with Explicit Schema")
print("=" * 80)

df3 = pl.DataFrame(
    {
        'col1': [1, 2, 3, 4, 5],
        'col2': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'],
        'col3': [True, False, True, True, False],
        'col4': [10.5, 20.3, 30.7, 40.2, 50.9],
        'col5': ['一', '二', '三', '四', '五']
    },
    schema={
        'col1': pl.Int64,
        'col2': pl.Utf8,
        'col3': pl.Boolean,
        'col4': pl.Float64,
        'col5': pl.Utf8
    }
)
print(df3)

print("\n" + "=" * 80)
print("METHOD 4: From NumPy Arrays")
print("=" * 80)

df4 = pl.DataFrame({
    'col1': np.array([1, 2, 3, 4, 5], dtype=np.int64),
    'col2': np.array(['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']),
    'col3': np.array([True, False, True, True, False], dtype=bool),
    'col4': np.array([10.5, 20.3, 30.7, 40.2, 50.9], dtype=np.float64),
    'col5': np.array(['一', '二', '三', '四', '五'])
})
print(df4)

print("\n" + "=" * 80)
print("METHOD 5: From List of Tuples")
print("=" * 80)

data5 = [
    (1, 'Apple', True, 10.5, '一'),
    (2, 'Banana', False, 20.3, '二'),
    (3, 'Cherry', True, 30.7, '三'),
    (4, 'Date', True, 40.2, '四'),
    (5, 'Elderberry', False, 50.9, '五')
]
df5 = pl.DataFrame(
    data5,
    schema=['col1', 'col2', 'col3', 'col4', 'col5'],
    orient='row'
)
print(df5)

print("\n" + "=" * 80)
print("METHOD 6: Using pl.Series")
print("=" * 80)

df6 = pl.DataFrame({
    'col1': pl.Series([1, 2, 3, 4, 5], dtype=pl.Int64),
    'col2': pl.Series(['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'], dtype=pl.Utf8),
    'col3': pl.Series([True, False, True, True, False], dtype=pl.Boolean),
    'col4': pl.Series([10.5, 20.3, 30.7, 40.2, 50.9], dtype=pl.Float64),
    'col5': pl.Series(['一', '二', '三', '四', '五'], dtype=pl.Utf8)
})
print(df6)

print("\n" + "=" * 80)
print("METHOD 7: From Dictionary with orient='row'")
print("=" * 80)

data7 = {
    'col1': [1, 2, 3, 4, 5],
    'col2': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'],
    'col3': [True, False, True, True, False],
    'col4': [10.5, 20.3, 30.7, 40.2, 50.9],
    'col5': ['一', '二', '三', '四', '五']
}
df7 = pl.DataFrame(data7, orient='col')  # Default is 'col'
print(df7)

print("\n" + "=" * 80)
print("METHOD 8: From List of Lists with Schema")
print("=" * 80)

data8 = [
    [1, 'Apple', True, 10.5, '一'],
    [2, 'Banana', False, 20.3, '二'],
    [3, 'Cherry', True, 30.7, '三'],
    [4, 'Date', True, 40.2, '四'],
    [5, 'Elderberry', False, 50.9, '五']
]
df8 = pl.DataFrame(
    data8,
    schema=['col1', 'col2', 'col3', 'col4', 'col5'],
    orient='row'
)
print(df8)

print("\n" + "=" * 80)
print("METHOD 9: From CSV String")
print("=" * 80)

from io import StringIO
csv_data = """col1,col2,col3,col4,col5
1,Apple,True,10.5,一
2,Banana,False,20.3,二
3,Cherry,True,30.7,三
4,Date,True,40.2,四
5,Elderberry,False,50.9,五"""

df9 = pl.read_csv(StringIO(csv_data))
print(df9)

print("\n" + "=" * 80)
print("METHOD 10: From JSON String")
print("=" * 80)

json_data = """[
    {"col1": 1, "col2": "Apple", "col3": true, "col4": 10.5, "col5": "一"},
    {"col1": 2, "col2": "Banana", "col3": false, "col4": 20.3, "col5": "二"},
    {"col1": 3, "col2": "Cherry", "col3": true, "col4": 30.7, "col5": "三"},
    {"col1": 4, "col2": "Date", "col3": true, "col4": 40.2, "col5": "四"},
    {"col1": 5, "col2": "Elderberry", "col3": false, "col4": 50.9, "col5": "五"}
]"""

df10 = pl.read_json(StringIO(json_data))
print(df10)

print("\n" + "=" * 80)
print("METHOD 11: Using Struct (Nested Data)")
print("=" * 80)

# Create from struct - useful for nested data
df11 = pl.DataFrame({
    'col1': [1, 2, 3, 4, 5],
    'col2': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'],
    'col3': [True, False, True, True, False],
    'col4': [10.5, 20.3, 30.7, 40.2, 50.9],
    'col5': ['一', '二', '三', '四', '五']
})
print(df11)

print("\n" + "=" * 80)
print("METHOD 12: From Range and Lists")
print("=" * 80)

df12 = pl.DataFrame({
    'col1': range(1, 6),
    'col2': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'],
    'col3': [True, False, True, True, False],
    'col4': [10.5, 20.3, 30.7, 40.2, 50.9],
    'col5': ['一', '二', '三', '四', '五']
})
print(df12)

print("\n" + "=" * 80)
print("METHOD 13: From Multiple Series (using DataFrame constructor)")
print("=" * 80)

s1 = pl.Series('col1', [1, 2, 3, 4, 5])
s2 = pl.Series('col2', ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'])
s3 = pl.Series('col3', [True, False, True, True, False])
s4 = pl.Series('col4', [10.5, 20.3, 30.7, 40.2, 50.9])
s5 = pl.Series('col5', ['一', '二', '三', '四', '五'])

# Create DataFrame from Series (they must have names)
df13 = pl.DataFrame([s1, s2, s3, s4, s5])
print(df13)

print("\n" + "=" * 80)
print("METHOD 14: Empty DataFrame + with_columns()")
print("=" * 80)

df14 = pl.DataFrame()
df14 = df14.with_columns([
    pl.Series('col1', [1, 2, 3, 4, 5]),
    pl.Series('col2', ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']),
    pl.Series('col3', [True, False, True, True, False]),
    pl.Series('col4', [10.5, 20.3, 30.7, 40.2, 50.9]),
    pl.Series('col5', ['一', '二', '三', '四', '五'])
])
print(df14)

print("\n" + "=" * 80)
print("METHOD 15: Using Specific Integer Types")
print("=" * 80)

df15 = pl.DataFrame({
    'col1': pl.Series([1, 2, 3, 4, 5], dtype=pl.Int32),  # Can be Int8, Int16, Int32, Int64
    'col2': pl.Series(['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']),
    'col3': pl.Series([True, False, True, True, False]),
    'col4': pl.Series([10.5, 20.3, 30.7, 40.2, 50.9], dtype=pl.Float32),  # Or Float64
    'col5': pl.Series(['一', '二', '三', '四', '五'])
})
print(df15)
print("\nSchema:", df15.schema)

print("\n" + "=" * 80)
print("METHOD 16: From Dictionary of NumPy Arrays with Schema")
print("=" * 80)

df16 = pl.DataFrame(
    {
        'col1': np.array([1, 2, 3, 4, 5]),
        'col2': np.array(['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']),
        'col3': np.array([True, False, True, True, False]),
        'col4': np.array([10.5, 20.3, 30.7, 40.2, 50.9]),
        'col5': np.array(['一', '二', '三', '四', '五'])
    },
    schema={
        'col1': pl.Int64,
        'col2': pl.Utf8,
        'col3': pl.Boolean,
        'col4': pl.Float64,
        'col5': pl.Utf8
    }
)
print(df16)

print("\n" + "=" * 80)
print("METHOD 17: Using List Comprehension")
print("=" * 80)

fruits = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
japanese = ['一', '二', '三', '四', '五']
bools = [True, False, True, True, False]

df17 = pl.DataFrame({
    'col1': [i+1 for i in range(5)],
    'col2': fruits,
    'col3': bools,
    'col4': [(i+1)*10 + 0.5 + i*0.2 for i in range(5)],
    'col5': japanese
})
print(df17)

print("\n" + "=" * 80)
print("METHOD 18: From Records (orient='row')")
print("=" * 80)

records = [
    [1, 'Apple', True, 10.5, '一'],
    [2, 'Banana', False, 20.3, '二'],
    [3, 'Cherry', True, 30.7, '三'],
    [4, 'Date', True, 40.2, '四'],
    [5, 'Elderberry', False, 50.9, '五']
]

df18 = pl.DataFrame(
    records,
    schema={
        'col1': pl.Int64,
        'col2': pl.Utf8,
        'col3': pl.Boolean,
        'col4': pl.Float64,
        'col5': pl.Utf8
    },
    orient='row'
)
print(df18)

print("\n" + "=" * 80)
print("METHOD 19: From PyArrow Table")
print("=" * 80)

try:
    import pyarrow as pa
    
    # Create PyArrow table
    pa_table = pa.table({
        'col1': [1, 2, 3, 4, 5],
        'col2': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'],
        'col3': [True, False, True, True, False],
        'col4': [10.5, 20.3, 30.7, 40.2, 50.9],
        'col5': ['一', '二', '三', '四', '五']
    })
    
    df19 = pl.from_arrow(pa_table)
    print(df19)
except ImportError:
    print("PyArrow not installed. Skip this method.")
    print("Install with: pip install pyarrow")

print("\n" + "=" * 80)
print("METHOD 20: From Pandas DataFrame")
print("=" * 80)

try:
    import pandas as pd
    
    # Create pandas DataFrame
    pd_df = pd.DataFrame({
        'col1': [1, 2, 3, 4, 5],
        'col2': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'],
        'col3': [True, False, True, True, False],
        'col4': [10.5, 20.3, 30.7, 40.2, 50.9],
        'col5': ['一', '二', '三', '四', '五']
    })
    
    # Convert to Polars
    df20 = pl.from_pandas(pd_df)
    print(df20)
except ImportError:
    print("Pandas not installed. Skip this method.")

print("\n" + "=" * 80)
print("METHOD 21: Using LazyFrame (for Lazy Evaluation)")
print("=" * 80)

lf = pl.LazyFrame({
    'col1': [1, 2, 3, 4, 5],
    'col2': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'],
    'col3': [True, False, True, True, False],
    'col4': [10.5, 20.3, 30.7, 40.2, 50.9],
    'col5': ['一', '二', '三', '四', '五']
})
df21 = lf.collect()  # Execute and convert to DataFrame
print(df21)

print("\n" + "=" * 80)
print("POLARS vs PANDAS: Key Differences")
print("=" * 80)
print("""
POLARS ADVANTAGES:
1. Much faster performance (written in Rust)
2. Better memory efficiency
3. Lazy evaluation support (LazyFrame)
4. Strict schema enforcement
5. Better handling of large datasets
6. Parallel processing by default
7. More consistent API

KEY DIFFERENCES:
- Polars uses 'schema' instead of 'dtypes'
- Data types: pl.Int64, pl.Utf8, pl.Boolean, pl.Float64 (not int64, object, bool)
- orient parameter: 'row' or 'col' (not 'index' or 'columns')
- No index by default (more like SQL table)
- Immutable operations (returns new DataFrame)
- with_columns() instead of assign()
- select() for column selection
""")

print("\n" + "=" * 80)
print("SUMMARY: All Polars Methods")
print("=" * 80)
print("""
1.  Dictionary of Lists              - Most common
2.  List of Dictionaries             - Row-oriented
3.  Dictionary with Schema           - Explicit types
4.  NumPy Arrays                     - From NumPy data
5.  List of Tuples                   - With orient='row'
6.  Using pl.Series                  - Fine control
7.  Dictionary with orient           - Specify orientation
8.  List of Lists with Schema        - 2D array structure
9.  From CSV String                  - pl.read_csv()
10. From JSON String                 - pl.read_json()
11. Using Struct                     - Nested data
12. From Range                       - Generate sequences
13. pl.concat (horizontal)           - Combine Series
14. with_columns()                   - Add columns
15. Specific Integer Types           - Int8, Int16, Int32, Int64
16. NumPy with Schema                - Combined approach
17. List Comprehension               - Dynamic generation
18. From Records                     - Database style
19. From PyArrow                     - pl.from_arrow()
20. From Pandas                      - pl.from_pandas()
21. LazyFrame                        - Lazy evaluation
""")