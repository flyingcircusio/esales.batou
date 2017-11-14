import batou.component
import batou.utils
import batou.lib.file
import batou.lib.mysql


class MySQL(batou.component.Component):

    admin_password = 'MyRootPW'

    def configure(self):
        self.provide('mysql', self)
        self.address = batou.utils.Address(self.host.fqdn, 3306)


class MySQLBase(batou.component.Component):

    def configure(self):
        self.mysql = self.require_one('mysql')
        self.provide(self.expand('mysql:{{component.tag}}'), self)
        self.address = self.mysql.address
        self += batou.lib.mysql.User(
            self.user,
            password=self.password,
            allow_from_hostname='%',
            admin_password=self.mysql.admin_password)

        self += batou.lib.mysql.Database(
            self.database,
            admin_password=self.mysql.admin_password)

        self += batou.lib.mysql.Grant(
            self.database,
            user=self.user,
            allow_from_hostname='%',
            admin_password=self.mysql.admin_password)


class MySQLOxid(MySQLBase):

    tag = 'oxid'
    user = 'oxid'
    password = 'oxid'
    database = 'oxid'


