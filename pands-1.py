import pymysql
#连接数据库
conn = pymysql.connect(host='180.76.154.249',user='root',passwd='1223514@yll',db='employees',port=59545,charset='utf8')
#获取游标
cur=conn.cursor()

sql="select * from departments"
try:
    cur.execute(sql)
    date =  cur.fetchall()
    for i in date:
        number = i[0]
        print("number=%s" %number)
except:
    print ("error:unable to fecth data")
conn.close()