# Puppet file that install flask 2.1.0

# install python3 if not already installed
package { 'python3':
  ensure => installed,
}

#install pip if not already installed
package { 'python3-pip':
  ensure  => installed,
  require => Package['python3'],
}

# install flask 2.1.0
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => Package['python3-pip'],
}