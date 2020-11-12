from flask import Flask
from flask import render_template
from flask import jsonify
import utils

app = Flask(__name__)


# 进入界面
@app.route('/')
def hello_world():
    return render_template("china_map.html")


# 当链接到路由地址map，返回地图数据
@app.route('/map')
def get_map_data():
    # 各省学生总人数
    total_nums = []
    for item in utils.get_all_people():
        total_nums.append({'name': item[0], 'value': int(item[1])})

    # 各省男学生人数
    man_nums = []
    for item in utils.get_nums_man():
        man_nums.append({'name': item[0], 'value': int(item[1])})

    # 各省女学生人数
    woman_nums = []
    for item in utils.get_nums_woman():
        woman_nums.append({'name': item[0], 'value': int(item[1])})

    # 各省男学生名字
    man_names = []
    for item in utils.get_names_man():
        man_names.append({'name': item[0], 'value': str(item[1])})

    # 各省女学生名字
    woman_names = []
    for item in utils.get_names_woman():
        woman_names.append({'name': item[0], 'value': str(item[1])})

    # 将上述数据以字典形式存储
    res = {}
    res['total_nums'] = total_nums
    res['man_nums'] = man_nums
    res['woman_nums'] = woman_nums
    res['man_names'] = man_names
    res['woman_names'] = woman_names

    # 以json形式返回结果给controller.js
    return jsonify(res)


# 运行该.py，进入网页
if __name__ == '__main__':
    app.run(debug=True)
