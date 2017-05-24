1. 新建项目
> django-admin.py startproject [project_name]

2. 新建app
> python manage.py startapp [app_name]

3. 启动应用
> python manage.pu runserver [IP:Port]

4. 连接数据库  

4.1 安装驱动
> pip install mysql-python

4.2 配置settings
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
