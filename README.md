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
> python manage.py makemigrations  
python manage.py migrate

6. 配置静态文件夹
在setting中写入
``` paython
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```

7. 创建数据库model
* 7.1 进入创建的app的文件夹，找到models
* 7.2 写入例如以下格式的model
``` python
class UserMessage(models.Model):
    name = models.CharField(max_length=20, verbose_name='用户名')
    email = models.EmailField(verbose_name='邮箱')
    address = models.CharField(max_length=100, verbose_name='联系地址')
    message = models.CharField(max_length=500, verbose_name='用户留言')

    class Meta:
        verbose_name = '用户留言信息'
```
model对应的类型有：
```python
models.CharField # 字符
models.ForeignKey # 外键
models.DateTimeField # 日期
models.IntegerField # 整型
models.EmailField # 邮箱
models.IPAddressFiled # ip类型
models.FileFiled # 文件
models.ImageField # 图片

# 赋值字符类型时必须指定
max_length = 20
# 是否可为空
null = True
# 是否能空白
blank = True
# 默认值
default = ''
# 指定主键
primary_key=True

# meta信息
# 指定表名
db_table = '表名'
# 默认排序,前面叫负号是倒序
ordering = '-字段名'
```
* 7.3 进入settings.py 修改 INSTALLED_APPS
``` python
INSTALLED_APPS = [
    # ... 自带的一些内容
    'message'
]
```
* 7.4 执行第5步，记得后面加新添加的app名

<hr/>

# 用到的一些包
1. mysql-python
2. pymysql
