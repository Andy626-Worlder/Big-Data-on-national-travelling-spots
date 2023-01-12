import pandas as pd

# 读取CSV文件
csvData = pd.read_csv(r'clean.csv', header=0)
with open('out.txt', 'w', encoding='utf-8') as out_file:
    for index, row in csvData.iterrows():
        # 读取景点名
        site = str(csvData.loc[index, 'site'])
        # 向文件中写入景点名
        out_file.write(site + ' ')
