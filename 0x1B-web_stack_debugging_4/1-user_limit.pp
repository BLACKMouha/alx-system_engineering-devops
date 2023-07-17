# Puppet scripts that increases the limit of opened files in OS level

exec { 'increase_os_worker_files':
  command => 'sudo sed -ie "$a\fs.file-max = 65536" /etc/sysctl.conf'
  path    => '/usr/local/bin/:/bin/',
}
