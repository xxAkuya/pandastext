
"""
导入数据
"""
import pandas as pd

with pd.ExcelFile('data.xls') as data:
    df = pd.read_excel(data, '达成度散点图')
df['done'] = 0.7