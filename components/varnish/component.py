from batou.component import Component, Attribute
from batou.lib.file import File
from batou.utils import Address
from batou_ext.nix import Rebuild
import batou_ext.ssl
import os.path


class Varnish(Component):
    """Configures the Varnish proxy.
    """

    address = Attribute(Address, 'localhost:8008')

    def configure(self):
    	self.provide('varnish', self.address)
    	self.haproxy = self.require_one('haproxy')
    	self += File('/etc/local/varnish/default.vcl')
        self += Rebuild()
