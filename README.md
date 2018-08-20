路书发票管理系统
=============

本项目为公司管理发票打印等任务做个一个实验性项目.

安装环境
-------
到项目目录下运行安装相关依赖包，关于`pipenv`的安装请移步[pipenv](https://pypi.org/project/pipenv/)
```
pipenv install
```
创建数据库
--------

```
python manage.py migrate
```

创建超级管理员
------------
```
python manage.py createsuperuser
```

运行项目
-------
```
python manage.py runserver
```

生产模式
-------
```shell
gunicorn config.wsgi:application -k egg:meinheld#gunicorn_worker -w 4 -b 0.0.0.0:5000
```