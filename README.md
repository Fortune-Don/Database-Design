# 系统使用说明


## 修改参数
* 将 config.py 文件中的MySql密码替换成本机数据库密码

## 数据库操作步骤
* 登录自己的MySql数据库

  >mysql -u 'root' -p
  >
  >Enter password:

* 插入数据到数据库

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
* 运行 main.py
* 在浏览器访问：http://127.0.0.1:8088/

**由于学生信息包含学生的隐私，故本仓库并未上传该信息，有需要者请联系**```kongmingtangfc@gmail.com```
