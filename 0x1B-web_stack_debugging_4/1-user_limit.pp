# Puppet scripts that increases the limit of opened files in OS level

exec { 'increase_os_worker_files'
  command  => 'sudo /bin/sed -i "s/nofile 4/nofile 6000/g; s/nofile 5/nofile 6000/g" /etc/security/limits.conf'
}
