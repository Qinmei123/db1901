import pymysql
def main():
    conn=pymysql.connect(host='localhost',port=3306,user='root',password='',db='db1',charset='utf8')
    print(conn)#1.建立连接，能打印conn
    try:
        with conn.cursor() as cursor:#with ...as...上下文语法，自动关
            result=cursor.execute('insert into table1 values(1)')
            if result==1:#表示数据库有一行受影响
                print('添加成功')
                conn.commit()#成功就要提交事物
    except pymysql.MySQLError as error:
        print(error)
        conn.rollback()#失败了回滚，事物撤销
    finally:
        conn.close()


if __name__=='__main__':
    main()
