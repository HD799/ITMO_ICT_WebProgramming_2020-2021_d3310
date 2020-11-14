import pymysql
#pymysql.version_info = (1, 4, 0, "final", 0)
  ##用此代码指定版本，如版本不对且不指定版本则会报错
  ##(django.core.exceptions.ImproperlyConfigured: mysqlclient 1.4.0 or newer is required; you have 0.10.1.)
#pymysql.install_as_MySQLdb()