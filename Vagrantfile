# -*- mode: ruby -*-
# vi: set ft=ruby :

$script = <<SCRIPT
sudo su root
cd /home/loadrunner
cat simp
python logger.py &
sleep 3
python net_load.py & 
sleep 3
python tcp_client.py & 
sleep 3
python memory_load.py &
sleep 3
python cpu_load.py &
sleep 3
echo "all scripts started"
echo "to obtain logs use `vagrant ssh` and `cd /home/loadrunner` before running `vagrant destroy` on host"
SCRIPT

Vagrant.configure("2") do |config|
  config.vm.box = "vagrantloadrunner"
  
  config.vm.provider "virtualbox" do |v|
    host = RbConfig::CONFIG['host_os']
    cpus = `wmic cpu get NumberOfLogicalProcessors`.split("\n")[2].to_i
    mem = `wmic OS get TotalVisibleMemorySize`.split("\n")[2].to_i / 1024
    v.customize ["modifyvm", :id, "--memory", mem]
    v.customize ["modifyvm", :id, "--cpus", cpus] 
  end
  config.vm.provision "shell", inline: $script, privileged: "false"
end
