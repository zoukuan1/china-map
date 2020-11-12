import pymysql

# return: 连接，游标
def get_conn():
    # 创建连接
    conn = pymysql.connect(host="localhost",
                           user="root",
                           password="a2691948",
                           db="studentinfo",
                           charset="utf8")
    # 创建游标
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
    return conn, cursor


# 关闭连接
def close_conn(conn, cursor):
    cursor.close()
    conn.close()


def query(sql, *args):
    """
    封装通用查询
    :param sql:
    :param args:
    :return: 返回查询到的结果，((),(),)的形式
    """
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res


# 将数据保存到数据库
def insert_data(studentInfo):
    name = studentInfo[0]
    sex = studentInfo[1]
    age = studentInfo[2]
    height = studentInfo[3]
    weight = studentInfo[4]
    province = studentInfo[5]
    parties = studentInfo[6]
    consumption = studentInfo[7]
    havefriend = studentInfo[8]
    playgame = studentInfo[9]
    sql = "insert into studentinfo (name, sex, age, height, weight, province, parties, consumption, havefriend, playgame) " \
          "value('{}', '{}', {}, {}, {}, '{}', '{}', {}, '{}', '{}')".format(name, sex, age, height, weight, province,
           parties, consumption, havefriend, playgame)
    conn, cursor = get_conn()
    cursor.execute(sql)
    conn.commit()
    close_conn(conn, cursor)


# 获取总人数
def get_all_people():
    sql = "select province,count(name) from studentinfo " \
          "group by province"
    res = query(sql)
    x = list(zip(*res))
    return res


# 获取男生数量
def get_nums_man():
    sql = "select province,count(name) from studentinfo " \
          "where sex='男'" \
          "group by province"
    res = query(sql)
    return res


# 获取女生数量
def get_nums_woman():
    sql = "select province,count(name) from studentinfo " \
          "where sex='女'" \
          "group by province"
    res = query(sql)
    return res


# 获取男生名字
def get_names_man():
    provinces = ["北京", "天津", "黑龙江", "吉林", "辽宁", "内蒙古", "山西", "山东", "河北", "河南", "湖北", "湖南", "江西",
                 "江苏", "浙江", "上海", "福建", "广东", "广西", "贵州", "云南", "四川", "重庆", "陕西", "青海", "新疆",
                 "西藏", "甘肃", "安徽", "宁夏", "海南", "香港", "澳门", "台湾"]
    man_names = []
    man_name = ''
    for i in range(0, len(provinces)):
        sql = "select name from studentinfo where province = '{}' and sex = '{}'".format(provinces[i], '男')
        res = query(sql)
        for item in res:
            man_name += "{} ".format(item[0])
        man_names.append((provinces[i], man_name))
        man_name = ''
    return man_names


# 获取女生名字
def get_names_woman():
    provinces = ["北京", "天津", "黑龙江", "吉林", "辽宁", "内蒙古", "山西", "山东", "河北", "河南", "湖北", "湖南", "江西",
                 "江苏", "浙江", "上海", "福建", "广东", "广西", "贵州", "云南", "四川", "重庆", "陕西", "青海", "新疆",
                 "西藏", "甘肃", "安徽", "宁夏", "海南", "香港", "澳门", "台湾"]
    woman_names = []
    woman_name = ''
    for i in range(0, len(provinces)):
        sql = "select name from studentinfo where province = '{}' and sex = '{}'".format(provinces[i], '女')
        res = query(sql)
        for item in res:
            woman_name += "{} ".format(item[0])
        woman_names.append((provinces[i], woman_name))
        woman_name = ''
    return woman_names
