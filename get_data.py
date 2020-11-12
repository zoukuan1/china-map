'''
导入需要用到的python包
'''
import numpy as np
import random
import utils
import csv
import codecs

'''
变量释义：
  count：记录筛选性别后的人数
  all_names：筛选后的所有名字分布
  names：从all_names中提取部分名字
  all_sex：筛选后的所有性别分布
  sex：从all_sex中提取部分性别
  province：省名列表
  parties：党派列表
  havefriend：有无男/女朋友
  playgame：是否打游戏
'''
count = 0
all_names = []; names = []
all_sex = []; sex = []
province = ["北京", "天津", "黑龙江", "吉林", "辽宁", "内蒙古", "山西", "山东", "河北", "河南", "湖北", "湖南", "江西", "江苏", "浙江",
            "上海", "福建", "广东", "广西", "贵州", "云南", "四川", "重庆", "陕西", "青海", "新疆", "西藏", "甘肃", "安徽", "宁夏",
            "海南", "香港", "澳门", "台湾"]
parties = ["群众", "共青团员", "中共党员", "其他党派"]
havefriend = ["有", "没有"]
playgame = ["玩", "不玩"]

# 读取姓名和性别
with open("Info.txt", "r", encoding="utf-8") as f:
    for data in f.readlines():
        temp = data.strip('\n')         # 去掉换行符
        temp = temp.split(',')          # 以逗号做区分
        if temp[1] != "未知":            # 筛选性别
            count = count + 1
            all_names.append(temp[0])   # 保留确定性别的名字
            all_sex.append(temp[1])     # 保留名字对应的性别

# 随机抽样500个下标值，提取相应下标的姓名和性别
indexs = random.sample(range(0, count), 500)
names = [all_names[index] for index in indexs]
sex = [all_sex[index] for index in indexs]

# 从0 - 33 中随机生成500份下标，提取相应的省份名
province_indexs = np.random.randint(0, 34, size=500)

# 从0 1中随机生成500份下标
two_flag = np.random.randint(0, 2, size=500)

# 从0 - 3 中随机生成500份下标
four_flag = np.random.randint(0, 4, size=500)

# 将学生的相关信息组合，使用上面获取的下标向对应的列表获取数据，并保存到数据库里
studentInfos = []
for i in range(0, 500):
    studentInfo = [names[i], sex[i], np.random.randint(18, 23), np.random.uniform(1.50, 2.00),
                   np.random.uniform(70, 200), province[province_indexs[i]], parties[four_flag[i]],
                   np.random.randint(100, 2000), havefriend[two_flag[i]], playgame[two_flag[i]]]
    studentInfos.append(studentInfo)
    utils.insert_data(studentInfo)

# 将所有学生信息写出为.csv文件
file_csv = codecs.open("studentInfo.csv", 'w+', 'utf-8')
writer = csv.writer(file_csv, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
writer.writerow(["姓名", "性别", "年龄", "身高", "体重", "省份", "党派", "消费", "有无男/女朋友", "是否打游戏"])
for studentInfo in studentInfos:
    writer.writerow(studentInfo)

# 运行该.py，完成数据获取和保存
if __name__ == '__main__':
    print("完成数据集获取，并保存到MySQL数据库")
