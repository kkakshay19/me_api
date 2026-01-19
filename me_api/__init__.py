import pymysql

# Tell PyMySQL to act like mysqlclient
pymysql.install_as_MySQLdb()

# Fix version check for Django 6.0+ compatibility
import sys
if hasattr(pymysql, 'version_info'):
    pymysql.version_info = (2, 2, 1, "final", 0)
