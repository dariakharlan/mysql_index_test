import mysql.connector

from faker import Faker

fake = Faker()

test_db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='test',
    auth_plugin='mysql_native_password',
    use_pure=True
)

cursor = test_db.cursor()

cursor.execute("""CREATE TABLE test_date (
id INT AUTO_INCREMENT PRIMARY KEY,
date_no_index DATE,
date_btree_index DATE,
date_hash_index DATE
) ENGINE=INNODB;""")

cursor.execute('CREATE INDEX btree_index ON test_date(date_btree_index) USING BTREE;')
cursor.execute('CREATE INDEX hash_index ON test_date(date_hash_index) USING HASH;')

n_batches = 4000
batch_size = 10000

query = 'INSERT INTO test_date (date_no_index, date_btree_index, date_hash_index) VALUES (%s,%s,%s)'

for i in range(n_batches):
    records_to_insert = []
    for b in range(batch_size):
        date = fake.date_between(start_date='-90y', end_date='today')
        records_to_insert.append((date, date, date))

    cursor = test_db.cursor()
    result = cursor.executemany(query, records_to_insert)
    test_db.commit()
    if i % 10 == 0:
        print(f'Batches executed: {i}')
