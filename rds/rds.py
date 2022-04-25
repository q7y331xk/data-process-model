from config import RDS_HOST, RDS_USER_NAME, RDS_USER_PW, RDS_DB
import pymysql

def conn_db():
    conn = pymysql.connect(host=RDS_HOST, user=RDS_USER_NAME, password=RDS_USER_PW, charset='utf8', port=3306, db=RDS_DB)
    return conn

def read(table):
    conn = conn_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    rows_exist = cursor.fetchall()
    conn.commit()
    return rows_exist
    
def create_table_if_exists_drop(table):
    conn = conn_db()
    cursor = conn.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {table}")
    cursor.execute(f"CREATE TABLE {table} (\
        id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,\
        title TEXT,\
        cost INT,\
        nickname TEXT,\
        `status` TEXT,\
        use_cnt INT,\
        `condition` TEXT,\
        pay_methods TEXT,\
        delivery TEXT,\
        location TEXT,\
        main TEXT,\
        views INT,\
        date TEXT,\
        likes TEXT,\
        comments_cnt INT,\
        comments TEXT,\
        `div` TEXT,\
        `gu` TEXT,\
        `color` TEXT,\
        `brand` TEXT,\
        `model` TEXT\
    )")
    conn.commit()

def write(table, selling):
    conn = conn_db()
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {table} VALUES(\
        \"{selling[0]}\",\
        \"{selling[1]}\",\
        \"{selling[2]}\",\
        \"{selling[3]}\",\
        \"{selling[4]}\",\
        \"{selling[5]}\",\
        \"{selling[6]}\",\
        \"{selling[7]}\",\
        \"{selling[8]}\",\
        \"{selling[9]}\",\
        \"{selling[10]}\",\
        \"{selling[11]}\",\
        \"{selling[12]}\",\
        \"{selling[13]}\",\
        \"{selling[14]}\",\
        \"{selling[15]}\",\
        \"{selling[16]}\",\
        \"{selling[17]}\",\
        \"{selling[18]}\",\
        \"{selling[19]}\",\
        \"{selling[20]}\"\
    )")
    conn.commit()