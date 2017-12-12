OXID eSales on Flying Circus infrastructure - Vagrant demo setup
================================================================

This is an example setup of an OXID eSales shop based on the Flying Circus
infrastructure in a Vagrant VM.

This machine runs the Linux platform as used by the Flying Circus and uses
batou to install the OXID Shop.

Here's **what you need** to use this:

* Vagrant
* VirtualBox
* Python 2.7 and virtualenv

Here's **how to use** this:

	$ git clone https://github.com/flyingcircusio/esales.batou
	$ cd esales.batou
	$ ./batou deploy vagrant
	$ open http://shop.192.168.50.4.nip.io/

This will give you the installed software presenting you the OXID eSales
setup wizard.

The MySQL database connection parameters are:

* Host: 127.0.0.1 (do **not** use "localhost")
* Database: oxid
* Username: oxid
* Password: oxid

> At the moment, you can't run batou twice as you will have to re-run the
installer after that. This will be fixed in the future.

The setup includes:

* nginx with php-fpm
* haproxy
* mysql

To poke around the virtual machine internals, you can connect via ssh:

    $ vagrant ssh

The software is installed in :

    $ cd ~vagrant/deployment/work

And some platform configuration can be found in

    $ cd /etc/local
