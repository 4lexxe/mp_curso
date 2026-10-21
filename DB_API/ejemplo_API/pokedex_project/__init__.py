import pymysql
from django.db.backends.base.base import BaseDatabaseWrapper

pymysql.install_as_MySQLdb()

# Desactiva la verificación de versión mínima de MySQL
BaseDatabaseWrapper.check_database_version_supported = lambda self: None