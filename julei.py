# -*- coding: utf8 -*-
import MySQLdb
import random,string
import time
import math


def creat_mysql(tablename):
    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "admin", "TEST")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 使用execute方法执行SQL语句
    cursor.execute("""use mydb; """)
    sql = """CREATE TABLE `%s` (  user_id varchar(20),good_id varchar(20),goods_cagory varchar(20),buying_time varchar(20),arv_shop_time varchar(20),lef_shop_time varchar(20),address varchar(20),price int,goods_name varchar(20),gender varchar(20),payment varchar(20),pay_all varchar(20),age varchar(20),costing  varchar(20),consume_cont varchar(20),buy_power varchar(20),loyalty  varchar(20),vitality varchar(20),satisfaction varchar(20) )  DEFAULT CHARSET=utf8;    """ % tablename
    cursor.execute(sql)
    db.commit()
    # 使用 fetchone() 方法获取一条数据
    # data = cursor.fetchone()
    # 关闭数据库连接
    db.close()

def insert_mysql(tablename):
    #打开数据库连接
    db = MySQLdb.connect("localhost","root","admin","TEST" )
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 使用execute方法执行SQL语句
    cursor.execute("""use mydb; """)
    #创建表
    #sql = """CREATE TABLE `shopping_info` (  user_id varchar(20),good_id varchar(20),goods_cagory varchar(20),buying_time varchar(20),arv_shop_time varchar(20),lef_shop_time varchar(20),address varchar(20),price int,goods_name varchar(20),gender varchar(20),payment varchar(20),pay_all varchar(20),age varchar(20),costing  varchar(20),consume_cont varchar(20),buy_power varchar(20),loyalty  varchar(20),vitality varchar(20),satisfaction varchar(20) )  DEFAULT CHARSET=utf8;    """
    #创建数据
    #用户id	商品id 	商品种类	购买时间	入店时间	离店时间	地址	商品价格	商品名称	性别	支付形式	支付总价格	年龄	商品成本	消费贡献	购买力	忠诚度	活跃度	满意度
    src_digits = string.digits              #string_数字
    src_uppercase = string.ascii_uppercase  #string_大写字母
    # src_lowercase = string.ascii_lowercase  #string_小写字母
    count=7
    new_Id=''
    for i in range(count):
        # 随机生成数字、大写字母、小写字母的组成个数（可根据实际需要进行更改）
        digits_num = random.randint(1, 6)
        uppercase_num = random.randint(1, 8 - digits_num - 1)
        digits_num2 = 8 - (digits_num + uppercase_num)

        # 生成字符串
        password = random.sample(src_digits, digits_num) + random.sample(src_uppercase, uppercase_num) + random.sample(
            src_digits, digits_num2)

        # 打乱字符串
        random.shuffle(password)

        # 列表转字符串
        new_Id = ''.join(password)
    user_id =new_Id


    count1=11
    new_goods_Id=''
    for e in range(count1):
        # 随机生成数字、大写字母、小写字母的组成个数（可根据实际需要进行更改）
        digits_num = random.randint(1, 6)
        uppercase_num = random.randint(1, 8 - digits_num - 1)
        digits_num2 = 8 - (digits_num + uppercase_num)

        # 生成字符串
        password = random.sample(src_digits, digits_num) + random.sample(src_digits, uppercase_num) + random.sample(
            src_digits, digits_num2)

        # 打乱字符串
        random.shuffle(password)

        # 列表转字符串
        new_goods_Id = ''.join(password)
    good_id =new_goods_Id

    goods_cory_dict={1:'生鲜',2:'肉类',3:'生活用品',4:'奶制品',5:'零食',6:'母婴',7:'其他',8:'干货',9:'酒水',10:'辅料',11:'水果',12:'熟食',13:'蔬菜'}



    ram_num=random.randint(1,13)
    #中文编码问题  用数字代替
    #goods_cagory=goods_cory_dict[ram_num]
    goods_cagory = ram_num



    a1=(2017,1,1,0,0,0,0,0,0)              #设置开始日期时间元组（1976-01-01 00：00：00）
    a2=(2018,1,1,23,59,59,0,0,0)    #设置结束日期时间元组（1990-12-31 23：59：59）
    start=time.mktime(a1)    #生成开始时间戳
    end=time.mktime(a2)      #生成结束时间戳
    #随机生成10个日期字符串
    for rt in range(10):
        t=random.randint(start,end)    #在开始和结束时间戳中随机取出一个
        date_touple=time.localtime(t)          #将时间戳生成时间元组
        date=time.strftime("%Y-%m-%d %H:%M:%S",date_touple)  #将时间元组转成格式化字符串（1976-05-21）

    buying_time=date
    leve=0
    time_leve=date.split(" ")[-1]
    time_leve=time_leve.split(":")[0]
    ju=int(time_leve)
    if 6<ju<10:
        leve=1
    elif 10<=ju<13:
        leve = 2
    elif 13 <= ju < 16:
        leve = 3
    elif 16 <= ju < 18:
        leve = 4
    elif 18 <= ju < 22:
        leve = 5
    elif 22<= ju < 24 or 0<= ju < 6:
        leve = 6
    buying_time=leve
    tmp=date.split(' ')
    tmp_1=tmp[0].split('-')
    tmp_2=tmp[1].split(':')
    # a3=(int(tmp_1[0]),int(tmp_1[1]),int(tmp_1[2]),int(tmp_2[0]),int(tmp_2[1])-30,int(tmp_2[2]),0,0,0)
    # a4=(int(tmp_1[0]),int(tmp_1[1]),int(tmp_1[2]),int(tmp_2[0]),int(tmp_2[1]),int(tmp_2[2]),0,0,0)
    # start=time.mktime(a3)    #生成开始时间戳
    # end=time.mktime(a4)      #生成结束时间戳
    # for rt in range(10):
    #     t=random.randint(start,end)    #在开始和结束时间戳中随机取出一个
    #     date_touple=time.localtime(t)          #将时间戳生成时间元组
    #     date=time.strftime("%Y-%m-%d %H:%M:%S",date_touple)  #将时间元组转成格式化字符串（1976-05-21）
    # arv_shop_time=date
    # timecur=date.split(" ")[-1].split(":")[0]
    # if math.fabs(timecur-tmp[1].split(':')[0])<1:
    #     arv_shop_time=1
    # elif math.fabs(timecur-tmp[1].split(':')[0])<2:
    #     arv_shop_time=0
    # else:
    #     arv_shop_time = 2
    arv_shop_time = 1

    # a5=(int(tmp_1[0]),int(tmp_1[1]),int(tmp_1[2]),int(tmp_2[0]),int(tmp_2[1]),int(tmp_2[2]),0,0,0)
    # a6=(int(tmp_1[0]),int(tmp_1[1]),int(tmp_1[2]),int(tmp_2[0]),int(tmp_2[1])+30,int(tmp_2[2]),0,0,0)
    # start=time.mktime(a5)    #生成开始时间戳
    # end=time.mktime(a6)      #生成结束时间戳
    # for rt in range(10):
    #     t=random.randint(start,end)    #在开始和结束时间戳中随机取出一个
    #     date_touple=time.localtime(t)          #将时间戳生成时间元组
    #     date=time.strftime("%Y-%m-%d %H:%M:%S",date_touple)  #将时间元组转成格式化字符串（1976-05-21）
    # lef_shop_time=date
    lef_shop_time = 1

    address_dict={1:'beijing',2:'shanghai',3:'guangzhou',4:'shengzhen',5:'hangzhou',6:'xiamen',7:'fuzhou',8:'wuxi',9:'quanzhou',10:'qingdao',11:'tianjing'}
    #address=address_dict[random.randint(1,11)]
    address=random.randint(1,11)
    price=random.randint(1,60)
    goods_name=random.randint(1,1000)
    gender = random.randint(0,1)

    aplay_dict={1:'zhifubao',2:'weixin',3:'xianjin',4:'qita'}
    #payment=aplay_dict[random.randint(1,4)]
    payment=random.randint(1,4)

    pay_all=random.randint(price,200)

    age=random.randint(10,60)
    costing=price*0.75
    #消费贡献	购买力	忠诚度	活跃度	满意度
    #支付总价格  后面sql计算
    consume_cont=random.randint(1,7)
    buy_power=random.randint(1,7)
    loyalty =random.randint(1,7)
    vitality=random.randint(1,7)
    satisfaction=random.randint(1,7)
    sql="""insert into %s(user_id ,good_id ,goods_cagory,buying_time ,arv_shop_time,lef_shop_time,address ,price ,goods_name ,gender ,payment ,age ,costing ,consume_cont ,buy_power,loyalty ,vitality ,satisfaction ,pay_all) values ('%s','%s',%s,'%s','%s','%s','%s',%s,%s,%s,'%s',%s,%s,%s,%s,%s,%s,%s,%s); """ % (tablename,user_id ,good_id ,goods_cagory,buying_time ,arv_shop_time,lef_shop_time,address ,price ,goods_name ,gender ,payment ,age ,costing ,consume_cont ,buy_power,loyalty ,vitality ,satisfaction,pay_all)
    cursor.execute(sql)
    db.commit()
    # 使用 fetchone() 方法获取一条数据
    #data = cursor.fetchone()
    # 关闭数据库连接
    db.close()

def select_mysql(tablename):
    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "admin", "TEST")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 使用execute方法执行SQL语句
    cursor.execute("""use mydb; """)
    sql = """select * from %s limit 100""" % tablename
    result=cursor.execute(sql)
    # 使用 fetchone() 方法获取一条数据
    data = cursor.fetchall()
    for i in data:
        print i
    # 关闭数据库连接
    db.close()

def truncate_mysql(tablename):
    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "admin", "TEST")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 使用execute方法执行SQL语句
    cursor.execute("""use mydb; """)
    sql = """truncate table %s""" % tablename
    result=cursor.execute(sql)
    # 使用 fetchone() 方法获取一条数据
    db.commit()
    # 关闭数据库连接
    db.close()



if __name__ == '__main__':
    #creat_mysql("shops_onehot")
    for i in range(0,10000):
        insert_mysql("shops_onehot")
    #select_mysql("shops_onehot")
    #truncate_mysql("shops_onehot")
