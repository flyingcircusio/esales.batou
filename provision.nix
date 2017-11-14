{ config, lib, pkgs, modulesPath, ... }: with config;

{

  flyingcircus.load_enc = false;
  flyingcircus.agent.enable = false;

  networking.extraHosts = ''
    127.0.0.1 default consul-ext.service.services.vgr.consul.local
    ::1 default consul-ext.service.services.vgr.consul.local
    192.168.50.4 shop.192.168.50.4.nip.io.
  '';

  flyingcircus.roles.webgateway.enable = true;
  flyingcircus.roles.webproxy.enable = true;

  # Databases
  flyingcircus.roles.mysql57.enable = true;
  flyingcircus.roles.mysql.rootPassword = "MyRootPW";
  flyingcircus.roles.mysql.extraConfig = ''
    [mysqld]
    # We don't really care about the data and this speeds up things.
    innodb_flush_method = nosync

    innodb_buffer_pool_size         = 200M
    innodb_log_buffer_size          = 64M
    innodb_file_per_table           = 1
    innodb_read_io_threads          = 1
    innodb_write_io_threads         = 1
    # Percentage. Probably needs local tuning depending on the workload.
    innodb_change_buffer_max_size   = 50
    innodb_doublewrite              = 1
    innodb_log_file_size            = 64M
    innodb_log_files_in_group       = 2
  '';

  environment.systemPackages = [
  ];

  networking.firewall.enable = false;

  services.openssh.extraConfig = ''
    UseDNS no
  '';

  swapDevices = [ { device = "/var/swapfile";
                    size = 2048; }];


}
