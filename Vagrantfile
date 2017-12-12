# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box_check_update = false
  config.vm.box = "flyingcircus/nixos-15.09-dev-x86_64"
  config.vm.box_version = ">= 3084"
  config.vm.provider "virtualbox" do |v|
      v.memory = 2048
      v.cpus = 1
  end

  config.vm.network "private_network", ip: "192.168.50.4"

  config.vm.provision :shell, \
    :inline => "
      nix-channel --add https://hydra.flyingcircus.io/channels/branches/fc-15.09-production/ nixos
      nix-channel --update
      "

  config.vm.provision :nixos,
    :verbose => true,
    :path => "provision.nix"
end
