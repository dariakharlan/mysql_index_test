# mysql_index_test

`queries.py` output

```
Count records: 20280000

1 month range
No index: 8 s
BTREE: 5 s
HASH: 11 s

1 year range
No index: 9 s
BTREE: 7 s
HASH: 10 s

10 years range
No index: 8 s
BTREE: 7 s
HASH: 10 s

Specific date
No index: 8 s
BTREE: 0 s
HASH: 0 s
```
