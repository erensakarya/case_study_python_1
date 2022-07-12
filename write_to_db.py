import psycopg2

schema_name = "public"

conn = psycopg2.connect(database='bigdata',
                        user='bdp',
                        password='bdp',
                        host='127.0.0.1',
                        port='5432'
                        )

conn.autocommit = True
cursor = conn.cursor()

with open('data/post.csv', 'r') as f:
    # Skip the header row
    next(f)
    cursor.copy_from(f, 'posts', sep=',')

with open('data/comments.csv', 'r') as f:
    # Skip the header row
    next(f)
    cursor.copy_from(f, 'post_comments', sep=',')

"""sql = '''select * from {}.posts;'''.format(db_name)
cursor.execute(sql)
for i in cursor.fetchall():
    print(i)"""

conn.commit()
conn.close()
