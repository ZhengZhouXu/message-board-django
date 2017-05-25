1. 新建项目
> django-admin.py startproject [project_name]

2. 新建app
> python manage.py startapp [app_name]

3. 启动应用
> python manage.pu runserver [IP:Port]

4. 连接数据库  
* 4.1 安装驱动  
> pip install mysql-python 

* 4.2 配置settings
``` python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testdjango',
        'USER': 'root',
        'PASSWORD': 'asd65830089',
        'HOST': '127.0.0.1'
    }
}
```
* 4.3 windows10, python3.6 安装mysql-python失败
改用pymysql

5. 初始化数据库  
* 先按4.2配置好数据库文件，在配置目录的__init__.py文件中，写入
``` python
import pymysql
pymysql.install_as_MySQLdb()
```
* 然后执行
> python manage.py makemigration  
python manage.py migrate

6. 配置静态文件夹
在setting中写入
``` paython
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```

<hr/>

# 用到的一些包
1. mysql-python
2. pymysql
