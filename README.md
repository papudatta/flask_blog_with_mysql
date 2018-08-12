```
$ sudo /usr/local/mysql/bin/mysql -u root -p
Enter password: amelia
mysql> CREATE DATABASE flaskblog;
mysql> GRANT ALL PRIVILEGES ON flaskblog.* TO 'flaskuser'@'localhost';
mysql> FLUSH PRIVILEGES;

$ python3 manage.py runserver
 * Serving Flask app "blog_with_flask" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat


$ python3 manage.py shell
>>> from blog_with_flask import db
>>> from author.models import *
>>> db.create_all()
>>> author = Author('Papu Datta', 'pdatta@myself.com', 'papu', '123456', True)
>>> author
<Author papu>
>>> db.session.add(author)
>>> db.session.commit()

mysql> show tables;
+---------------------+
| Tables_in_flaskblog |
+---------------------+
| author              |
+---------------------+
1 row in set (0.00 sec)

mysql> select * from author;
+----+------------+-------------------+----------+----------+-----------+
| id | fullname   | email             | username | password | is_author |
+----+------------+-------------------+----------+----------+-----------+
|  1 | Papu Datta | pdatta@myself.com | papu     | 123456   |         1 |
+----+------------+-------------------+----------+----------+-----------+
1 row in set (0.00 sec)

>>> authors = Author.query.all()
>>> authors
[<Author papu>, <Author paps>]
>>> authors[0]
<Author papu>
>>> authors[0].email
'pdatta@myself.com'
>>> authors = Author.query.filter_by(username='Paps').first()
>>> authors
<Author paps>
>>> db.session.commit()
>>> db.drop_all()

 python3 manage.py shell
>>> from blog_with_flask import db
>>> db.session.commit()
>>> db.create_all()

 python3 manage.py db init
  Creating directory /Users/paps/Desktop/flask/blog_with_flask/migrations ... done
  Creating directory /Users/paps/Desktop/flask/blog_with_flask/migrations/versions ... done
  Generating /Users/paps/Desktop/flask/blog_with_flask/migrations/alembic.ini ... done
  Generating /Users/paps/Desktop/flask/blog_with_flask/migrations/env.py ... done
  Generating /Users/paps/Desktop/flask/blog_with_flask/migrations/README ... done
  Generating /Users/paps/Desktop/flask/blog_with_flask/migrations/script.py.mako ... done
  Please edit configuration/connection/logging settings in
  '/Users/paps/Desktop/flask/blog_with_flask/migrations/alembic.ini' before proceeding.
MyiMac:blog_with_flask paps$ 

$ python3 manage.py db migrate
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'author'
INFO  [alembic.autogenerate.compare] Detected added table 'blog'
  Generating /Users/paps/Desktop/flask/blog_with_flask/migrations/versions/d48e2d305f6e_.py ... done

$ python3 manage.py db upgrade
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> d48e2d305f6e, empty message

mysql> select * from alembic_version;
+--------------+
| version_num  |
+--------------+
| d48e2d305f6e |
+--------------+
1 row in set (0.00 sec)

mysql> show tables;
+---------------------+
| Tables_in_flaskblog |
+---------------------+
| alembic_version     |
| author              |
| blog                |
+---------------------+
3 rows in set (0.00 sec)

$ python3 manage.py db migrate
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected type change from TINYINT(display_width=1) to Boolean() on 'author.is_author'
INFO  [alembic.autogenerate.compare] Detected type change from VARCHAR(length=15) to String(length=60) on 'author.password'
  Generating /Users/paps/Desktop/flask/blog_with_flask/migrations/versions/0574633c0a12_.py ... done

$ python3 manage.py db upgrade
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade d48e2d305f6e -> 0574633c0a12, empty message


$ python3 manage.py shell
>>> from blog_with_flask.author.models import Author
>>> author = Author.query.filter_by(username='papu').first()
>>> author
<Author Papu>
>>> 
>>> author.is_author
True
>>> author.is_author = False
>>> from blog_with_flask import db
>>> db.session.commit()

$ python3 manage.py shell
>>> from blog_with_flask.author.models import Author
>>> from blog_with_flask import db
>>> author = Author.query.filter_by(username='papu').first()
>>> author.is_author = True
>>> db.session.commit()

$ python3 manage.py shell
>>> from blog_with_flask.author.models import *
>>> from blog_with_flask.blog.models import *
>>> category = Category('Family')
>>> db.session.add(category)
>>> db.session.commit()
>>> author = Author.query.first()
>>> author
<Author Papu>
>>> 
>>> category = Category.query.first()
>>> category
<Category Family>
>>> blog = Blog.query.first()
>>> blog
<Blog Datta's blog>
>>> post = Post(blog, author, 'Family first', 'My family is so adorable, hardworking and charming.', category)
>>> db.session.add(post)
>>> db.session.commit()
```




