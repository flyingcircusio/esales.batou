from batou.component import Component, Attribute
from batou.lib.file import File
from batou.utils import Address
from batou_ext.nix import Rebuild
import batou_ext.ssl
import os.path


class Nginx(Component):
    """Configures the nginx frontend.
    """

    frontend_address = Attribute(Address, 'shop.192.168.50.4.nip.io:80')

    path = '/etc/local/nginx'

    def configure(self):
        self.varnish = self.require_one('varnish')
        self += File('/etc/local/nginx/shop.conf')

        self += Rebuild()

