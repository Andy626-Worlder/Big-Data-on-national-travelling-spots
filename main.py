import base64, json
import requests
import pandas as pd

user = "admin"
password = "Complexpass#123"
bas64encoded_creds = base64.b64encode(bytes(user + ":" + password, "utf-8")).decode("utf-8")

headers = {"Content-type": "application/json", "Authorization": "Basic " + bas64encoded_creds}
index = "games3"
zinc_host = "http://localhost:4080"
zinc_url = zinc_host + "/api/" + index + "/document"


# 读取CSV文件
csvData = pd.read_csv(r'clean.csv', header=0)
# 读取CSV文件包含的列名并转换为list
columns = csvData.columns.tolist()

# 创建空字典
outPut = {}

# 将CSV文件转为字典
for index,row in csvData.iterrows():
    for col in columns:
        outPut[col] = str(csvData.loc[index, col])  # 这里一定要将数据类型转成字符串，否则会报错
    jsonData = json.dumps(outPut)
    # print(jsonData)
    res = requests.put(zinc_url, headers=headers, data=jsonData)
    # print(res)



