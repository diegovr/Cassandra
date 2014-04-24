import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily

pool = ConnectionPool('ApplicationData',
                      ['localhost:9160'])
col_fam = ColumnFamily(pool, 'UserInfo')
col_fam.insert('Diego', {'email': 'ciegovr@gmail.com'})

readData = col_fam.get('Diego', columns=['email'])

col_fam.remove('Diego', columns=['email'])

#batch

b = col_fam.batch(queue_size=10)

b.insert('John',
         {'email': 'john@gmail.com',
          'state': 'IL',
          'gender': 'M'})

b.insert('Jane',
         {'email': 'jane@python.org',
          'state': 'CA'})

b.remove('John', ['gender'])
b.remove('Jane')
b.send()