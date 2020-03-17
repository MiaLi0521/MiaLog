## deployment steps

### 1.为保存程序密钥的SECREAT_KEY生成一个随机字符串
- 方法一<br>
  import os<br>
  os.urandom(12) 
- 方法二<br>
  import secrets<br>
  secrets.token_urlsafe(16)
- 方法三<br>
  import uuid<br>
  uuid.uuid4().hex
  
### 2.将FLASK_CONFIG配置为production，加载生产环境配置
### 3.将FLASK_ENV配置为production
### 4.生产环境专用的程序实例位于wsgi.py脚本
### 5.设置迁移工具
  除非部署测试，负责设置迁移工具必不可少，以便在保留原数据的同时，对数据库结构进行更新
  - flask db init
  - flask db migrate -m "Initial migrate"
  - flask init 初始化应用
### 6.程序日志
### 7.HTTPS转发
### 8.
  