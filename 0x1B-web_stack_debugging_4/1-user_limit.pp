# Puppet scripts that increases the limit of opened files in OS level

exec { 'increase_os_worker_files':
  provider => shell,
  command  => 'sudo sed -i "/holberton hard/s/5/65536/" /etc/security/limits.conf',
  path     => '/usr/bin/:/usr/local/bin/:/bin/'
}
