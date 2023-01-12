import os

from pyecharts import options as opts
from pyecharts.charts import Geo
import pandas as pd


def scaner_file(url):
    # 遍历当前路径下所有文件
    file = os.listdir(url)
    return file

zip_list = []
all_sum = 0
for city_csv in scaner_file('./list/site'):
    sum = 0
    csv = pd.read_csv('./list/site/'+city_csv)
    for index, row in csv.iterrows():
        sum += int(csv.loc[index, '评论数量'])
    all_sum += sum
print(all_sum)
for city_csv in scaner_file('./list/site'):
    sum = 0
    csv = pd.read_csv('./list/site/'+city_csv)
    for index, row in csv.iterrows():
        sum += int(csv.loc[index, '评论数量'])
    city = city_csv.replace('.csv', '')
    zip_list.append([city, int(sum / all_sum * 900)])  # 调整参数
print(zip_list)

c = (
    Geo()
    .add_schema(maptype="china")
    .add("省份受欢迎程度", zip_list)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(is_piecewise=True),
        title_opts=opts.TitleOpts(title="旅游热力图"),
    )
    .render("geo_visualmap_piecewise.html")
)
