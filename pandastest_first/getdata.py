"""
导入数据
"""
import pandas as pd
import random


def get_data():
    with pd.ExcelFile('data.xls') as data:
        df = pd.read_excel(data, '达成度散点图')
    df['done'] = 0.7
    ach_judge = 0.7
    return df, ach_judge
