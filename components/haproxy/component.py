import batou.component
import batou.lib.file
from batou.utils import Address
import batou_ext.nix


@batou_ext.nix.rebuild
class HAProxy(batou.component.Component):


    def configure(self):
        self.address = batou.utils.Address('localhost:8000')
        self.provide('haproxy', self.address)

        self.backends = self.require('oxid')

        self += batou.lib.file.File(
            '/etc/local/haproxy/haproxy.cfg', source='haproxy.cfg')
        


