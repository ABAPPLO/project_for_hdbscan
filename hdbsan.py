#coding:utf-8
import hdbscan
import numpy as np
import MySQLdb
import matplotlib.pyplot as plt


def download_data(tablename):
    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "admin", "TEST")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 使用execute方法执行SQL语句
    cursor.execute("""use mydb; """)
    sql = """select * from  %s""" % tablename
    result = cursor.execute(sql)
    # 使用 fetchone() 方法获取一条数据
    data = cursor.fetchall()
    data_dict=[]
    lable_dict=[]
    for i in data:
        data_dict.append(i[1:-1])
        lable_dict.append(i[0])
    # 关闭数据库连接
    db.close()
    return data_dict,lable_dict


if __name__ == '__main__':
    dataSet,labelSet = download_data("shops_onehot")
    data=np.array(dataSet).astype(np.float64)
    clusterer = hdbscan.HDBSCAN(min_cluster_size=100,prediction_data=True)
    cluster_labels = clusterer.fit_predict(data)
    result_dict={}
    for i in range(len(dataSet)):
        result_dict.setdefault(labelSet[i],cluster_labels[i])

    print result_dict

    #统计结果个数
    # clusterID_and_count={}
    # for i in cluster_labels:
    #     if i not in clusterID_and_count.keys():
    #         clusterID_and_count.setdefault(i,1)
    #     else:
    #         value =clusterID_and_count[i]
    #         clusterID_and_count[i]=value+1
    # print len(clusterID_and_count)
    # print clusterID_and_count
