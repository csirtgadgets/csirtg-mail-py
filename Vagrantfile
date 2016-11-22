#e -*- mode: ruby -*-
# vi: set ft=ruby :

# This will setup a clean Ubuntu1404 LTS env

$script = <<SCRIPT
add-apt-repository ppa:fkrull/deadsnakes-python2.7
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo add-apt-repository ppa:cython-dev/master-ppa
apt-get update
apt-get install -y python-pip python-dev git htop virtualenvwrapper python2.7 python-virtualenv python-support cython git build-essential libtool pkg-config autotools-dev autoconf automake cmake libpcre3-dev valgrind libffi-dev zip uuid-dev libxml2-dev python-lxml libxslt1-dev zlib1g-dev
SCRIPT

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"
VAGRANTFILE_LOCAL = 'Vagrantfile.local'

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = 'ubuntu/trusty64'
  config.vm.provision "shell", inline: $script

  config.vm.provider :virtualbox do |vb, override|
    vb.customize ["modifyvm", :id, "--cpus", "2", "--ioapic", "on", "--memory", "1024" ]
  end

  config.vm.provider :aws do |aws|
    aws.tags = { 'Name' => 'pyzyre' }
  end

  if File.file?(VAGRANTFILE_LOCAL)
    external = File.read VAGRANTFILE_LOCAL
    eval external
  end
end
