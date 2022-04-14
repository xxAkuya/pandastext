"""
主程序
"""
from getdata import get_data
from question import *


if __name__ == '__main__':

    df = get_data()
    acc_li = ['Unnamed: 4', 'Unnamed: 9', 'Unnamed: 14', 'Unnamed: 21']
    ave_li = ['Unnamed: 5', 'Unnamed: 10', 'Unnamed: 15', 'Unnamed: 22']

    for acc, ave, i in zip(acc_li, ave_li, range(4)):
        done_ave, un_done = count_num(acc, ave, 'done', df)
        print('目标 {} 超过平均值人数：{}'.format(i + 1, done_ave))
        print('目标 {} 未达成人数：{}'.format(i + 1, un_done))

    all_ave, all_done, all_undone = all_count_num(acc_li, ave_li, done='done', df=df)

    print('所有目标超过平均值人数: ', all_ave)
    print('所有目标达成人数：', all_done)
    print('所有目标未达成人数：', all_undone)
