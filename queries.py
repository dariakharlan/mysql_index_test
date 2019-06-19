import mysql.connector
import time

test_db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='test',
    auth_plugin='mysql_native_password',
    use_pure=True
)

cursor = test_db.cursor()


def query_range_time(column, start_date, end_date):
    start = time.time()
    cursor.execute(f"SELECT id, {column} FROM test_date WHERE {column} BETWEEN {start_date} AND {end_date}")
    cursor.fetchall()
    return int(time.time() - start)


def query_date_time(column, date_to_select):
    start = time.time()
    cursor.execute(f"SELECT id, {column} FROM test_date WHERE {column} = {date_to_select}")
    cursor.fetchall()
    return int(time.time() - start)


def compare_range_queries(start_date, end_date):
    qt = query_range_time('date_no_index', start_date, end_date)
    print(f'No index: {qt} s')
    qt = query_range_time('date_btree_index', start_date, end_date)
    print(f'BTREE: {qt} s')
    qt = query_range_time('date_hash_index', start_date, end_date)
    print(f'HASH: {qt} s')


cursor.execute('SELECT COUNT(id) FROM test_date')
print(f'Count records: {cursor.fetchone()[0]}\n')

print('1 month range')
compare_range_queries('2010-01-01', '2010-02-01')

print('')
print('1 year range')
compare_range_queries('2010-01-01', '2011-02-01')

print('')
print('10 years range')
compare_range_queries('2000-01-01', '2010-01-01')

print('Specific date')
date_from = '2000-01-01'
qt = query_date_time('date_no_index', date_from)
print(f'No index: {qt} s')
qt = query_date_time('date_btree_index', date_from)
print(f'BTREE: {qt} s')
qt = query_date_time('date_hash_index', date_from)
print(f'HASH: {qt} s')
