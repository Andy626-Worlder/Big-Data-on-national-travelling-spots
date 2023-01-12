from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType
import pandas as pd



city_list = ['厦门', '北京', '香港', '丽江', '三亚', '成都', '上海', '大理', '大理', '西安']
zip_list = list()
for city in city_list:
    sum = 0
    csv = pd.read_csv(f'list/{city}.csv')
    for index, row in csv.iterrows():
        sum += int(csv.loc[index, '评论数量'])

    print(city + str(sum))
    zip_list.append((city, sum))

c = (
    Geo()
        .add_schema(maptype="china")
        .add(
        "geo",
        zip_list,
        type_=ChartType.HEATMAP,
    )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(),
        title_opts=opts.TitleOpts(title="中国十大景点人气值"),
    )
)

c.render(path='geo_heatmap.html')
