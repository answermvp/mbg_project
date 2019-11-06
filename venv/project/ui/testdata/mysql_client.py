import pymysql

class mysql_client():
    """操作mysql"""
    def connect_mysql(self):
        """连接mysql"""
        # 连接database
        # self.conn = pymysql.connect(host='localhost', user='root', password='123456789aA', database='test', charset='utf8')
        # 连接 au2 测试环境数据库
        self.conn = pymysql.connect(host='aws-autest.cmcxqhkyobwe.ap-southeast-1.rds.amazonaws.com', user='aws_root', password='SekL539F', database='aetos4', charset='utf8')
        # 得到一个可以执行SQL语句的光标对象
        self.cursor = self.conn.cursor()

    def clear_data(self):
        """清理数据"""
        self.connect_mysql()
        # 关闭光标对象
        self.cursor.close()
        # 关闭数据库连接
        self.conn.close()
    
    def create_datebase(self):
        """创建数据库"""
        self.connect_mysql()
        # 定义要执行的SQL语句
        sql = "create database test;"
        # 执行 sql 语句
        self.cursor.execute(sql)
        self.clear_data()

    def create_table(self):
        """创建表"""
        self.connect_mysql()
        sql = """
        create table test3(
            id int auto_increment PRIMARY KEY,
            email CHAR(20) NOT NULL UNIQUE
            );
        """
        self.cursor.execute(sql)
        self.clear_data()

    def insert_data(self):
        """插入数据"""
        self.connect_mysql()
        sql = """
        insert into test3(id, email) value(1, "test_answer@email.com");
        """
        self.cursor.execute(sql)
        self.clear_data()

    def get_data(self, sql):
        """获取数据"""
        self.connect_mysql()
        # 获取最新注册的用户的用户名
        self.cursor.execute(sql)
        test_data = self.cursor.fetchall()
        self.clear_data()
        return test_data
