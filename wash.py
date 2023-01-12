import os
import pandas as pd


def scaner_file(url):
    # 遍历当前路径下所有文件
    file = os.listdir(url)
    for f in file:
        yield f


if __name__ == '__main__':
    df = pd.DataFrame()
    for f in scaner_file('./comments/'):
        temp = pd.read_csv('./comments/' + f)
        print(temp.head())
