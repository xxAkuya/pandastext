"""
导入excel数据，
完成单项目标超过平均值人数、done_ave_1-4
单项目标未达成人数、un_done1-4
所有目标超过平均值人数、 all_ave
所有目标均达成人数、all_done
所有目标均未达成人数计算；all_undone
画出散点图；

"""
import pandas as pd

total = 143
start, end = 5, 148


def count_num(acc, ave, done, df):
    """
    :param acc: 达成度
    :param ave: 平均值
    :param done: 完成率
    :return: done_ave, un_done
    """
    done_ave = list(df[acc][start:end].ge(df[ave][start:end])).count(True)  # ge大于等于

    un_done = list(df[acc][start:end].lt(df[done][start:end])).count(True)  # lt 小于

    return done_ave, un_done


def all_count_num(*args, done, df):
    """

    :param args: acc_li,ave_li
    :param done: 0.7
    :return: all_ave, all_done, all_undone
    """
    all_ave_li = [0] * 4
    all_done_li = [0] * 4
    all_undone_li = [0] * 4
    all_ave, all_done, all_undone = 0, 0, 0

    for i in range(len(args[0])):
        all_ave_li[i] = df[args[0][i]][start:end].ge(df[args[1][i]][start:end])  # ge 大于等于
        all_done_li[i] = df[args[0][i]][start:end].gt(df[done][start:end])  # gt 大于
        all_undone_li[i] = df[args[0][i]][start:end].lt(df[done][start:end])  # lt 小于

    df_ave = pd.concat([*all_ave_li], axis=1)
    df_done = pd.concat([*all_done_li], axis=1)
    df_undone = pd.concat([*all_undone_li], axis=1)

    for j in range(total):
        if list(df_ave.loc[j + 5]).count(True) == 4:
            all_ave += 1
        if list(df_done.loc[j + 5]).count(True) == 4:
            all_done += 1
        if list(df_undone.loc[j + 5]).count(True) == 4:
            all_undone += 1

    return all_ave, all_done, all_undone
