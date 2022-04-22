"""
提取损失值
"""
import matplotlib.pyplot as plt

f = ['CDnet.txt', 'FCEarlyFusion.txt', 'FCSiamConc.txt', 'FCSiamDiff.txt', '新建.txt','model_DSIFN.txt']


def plot_loss(name):
    with open(name, encoding='utf-8') as data:
        txt = []
        for line in data:
            txt.append(line.strip())

    loss_finished = list()
    loss = list()
    for i in range(len(txt)):
        if 'finished' in txt[i]:
            loss_finished.append(txt[i])

    for j in range(len(loss_finished)):
        a = loss_finished[j].split('=')
        b = a[-1].split(' ')[0]
        loss.append(float(b))

    plt.plot([i for i in range(len(loss))], loss, label=name)
    plt.title(name, fontdict={'size': 20})
    plt.show()


for name in f:
    plot_loss(name)
