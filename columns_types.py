import pandas as pd
import numpy as np

a = [['a', '1.2', '4.2'], ['b', '70', '0.03'], ['x', '5', '0']]

df = pd.DataFrame(a)

# 1）在创建DF时可以直接指定数值类型
#df = pd.DataFrame(a, dtype='float') 
#df = pd.DataFrame(data=a, dtype=np.int8) 
#df = pd.read_csv("somefile.csv", dtype = {'column_name' : str})

# 2)对于单列series可以使用pd.to_numeric()转换为数值
pd.to_numeric(df[2])
pd.to_numeric(df[0], errors='ignore')  # errors='ignore'忽略错误信息，非数字类型以字符保留
# pandas.to_datetime可转换为日期格式

# 对于多列，可以使用apply进行处理
df[[1,2]].apply(pd.to_numeric, errors='ignore')

# 3）类型自动推断
df.infer_objects()

# 4）astype强制转换
df[[1,2]].astype(float)
