import batou
import batou.component
from batou.lib.file import File
from batou.lib.download import Download
from batou.lib.archive import Extract
from batou.utils import Address
from batou.lib.service import Service
from batou_ext.nix import Rebuild

import batou.utils
import batou_ext.config
import batou_ext.git
import batou_ext.nix
import hashlib
import os.path


@batou_ext.nix.rebuild
class Oxid(batou.component.Component):
    """Application environment to install and configure Oxid eSales Code."""

    features = ()

    fpm_address = Address('localhost:8081')

    def configure(self):
        self.require('mysql:oxid')
        self.provide('oxid', batou.utils.Address(self.host.fqdn, port=8080))

        self += Download('http://download.oxid-esales.com/ce',
                         target='shop.zip',
                         checksum='md5:510417acc807c9d0f8194387f2fd785e')

        self += Extract('shop.zip')

        self += File('php.ini')
        self += File('php-fpm.ini')

        self += File('php-fpm', mode=0o755)
        self += Service('php-fpm', systemd=dict(Type='simple'))

        self += File('/etc/local/nginx/fpm.conf', source='nginx-fpm.conf')
        self += File('/etc/local/nginx/fastcgi_params.oxid')

        self += Rebuild()