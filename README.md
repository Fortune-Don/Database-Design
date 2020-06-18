# 系统使用说明


## 修改参数
* 将 config.py 文件中的MySql密码替换成本机数据库密码

## 数据库操作步骤
* 1. 登录自己的MySql数据库

>mysql -u 'root' -p
>
>Enter password:

* 2. 插入数据到数据库

>create database studenttrainplan;
>
>use studenttrainplan;
>
>source table.sql;
>
>set SESSION sql_mode='';
>
>set names 'utf8';
>
>source Student.sql;
>
>source Stu_Login.sql;
>
>source Lecture.sql;
>
>source Class.sql;
>
>source stu_plan.sql;
>
>source Teacher.sql;


## 运行方法
* 1. 运行 main.py
* 2. 在浏览器访问：http://127.0.0.1:5000/

