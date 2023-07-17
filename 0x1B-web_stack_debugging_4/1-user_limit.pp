# Puppet scripts that increases the limit of opened files in OS level

exec { 'increase_os_worker_files'
  provider => shell,
  command  => 'sudo sed -ie "$a\fs.file-max = 65536" /etc/sysctl.conf'
}
