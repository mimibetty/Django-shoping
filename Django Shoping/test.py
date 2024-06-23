import mysql.connector

# Kết nối đến MySQL
db = mysql.connector.connect(user='root', password='', host='localhost')

# Tạo một con trỏ
mycursor = db.cursor()

# Câu lệnh SQL để tạo cơ sở dữ liệu
query = "CREATE SCHEMA test33;"
# Câu lệnh SQL để tạo bảng
# query1 = """
# CREATE TABLE test33.sinh_vien (
#     id INT NOT NULL AUTO_INCREMENT,
#     name VARCHAR(255) NOT NULL,
#     year INT NULL,
#     PRIMARY KEY (id)
# );
# """

query1 = """
    insert into test33.sinh_vien (id,name, year) values (2332,"2inh",20023);
 """
# Thực thi câu lệnh SQL
mycursor.execute(query1)
db.commit()
# Đóng kết nối
db.close()