# import mysql.connector

# # Kết nối đến MySQL
# db = mysql.connector.connect(user='root', password='', host='localhost')

# # Tạo một con trỏ
# mycursor = db.cursor()

# # Câu lệnh SQL để tạo cơ sở dữ liệu
# query = "CREATE SCHEMA test33;"
# # Câu lệnh SQL để tạo bảng
# # query1 = """
# # CREATE TABLE test33.sinh_vien (
# #     id INT NOT NULL AUTO_INCREMENT,
# #     name VARCHAR(255) NOT NULL,
# #     year INT NULL,
# #     PRIMARY KEY (id)
# # );
# # """

# query1 = """
#     insert into test33.sinh_vien (id,name, year) values (2332,"2inh",20023);
#  """
# # Thực thi câu lệnh SQL
# mycursor.execute(query1)
# db.commit()
# # Đóng kết nối
# db.close()


# Read input
l, n = map(int, input().split())
positions = list(map(int, input().split()))

# Calculate minimum and maximum time
min_time = max_time = 0
for pos in positions:
    min_time = max(min_time, min(pos, l - pos))
    max_time = max(max_time, max(pos, l - pos))

# Output the result
print(min_time, max_time)


Vì Huy mới học về cây nhị phân nên Huy sẽ sử dụng một cây nhị phân đơn giản như sau, với mỗi nút
có tối đa 2 nút con (trực tiếp). Với mỗi nút, các nút con bên trái có giá trị nhỏ hơn và các nút con bên
phải có giá trị lớn hơn. Khi chèn một nút vào cây nhị phân, quá trình bắt đầu từ nút gốc. Nếu cây rỗng,
nút mới sẽ trở thành nút gốc. Nếu cây không rỗng, ta so sánh giá trị của nút mới với giá trị của nút gốc.
Nếu giá trị của nút mới nhỏ hơn giá trị của nút gốc, ta tiếp tục so sánh với nút con trái, ngược lại nếu
lớn hơn, ta so sánh với nút con phải. Quá trình này được lặp lại cho đến khi tìm được vị trí phù hợp, tức
là khi gặp một nút con trống (null). Tại đây, nút mới sẽ được chèn vào vị trí đó.
Chị Tua cho Huy một dãy số A gồm N phần tử phân biệt, chị Tua yêu cầu Huy chèn lần lượt các phần
tử trong dãy số A theo thứ tự A1, A2, A3, ..., AN .
Ví dụ với dãy số A = [7, 9, 4, 6, 8, 10, 5, 1] thì ta có cây nhị phân như sau