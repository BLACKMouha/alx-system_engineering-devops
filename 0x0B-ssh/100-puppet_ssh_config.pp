# Connect to SSH without typing password for `school` private key
include stdlib
file_line {'Set connect with password to `no`':
  ensure             => present,
  path               => '/etc/ssh/sshd_config',
  line               => '\tPasswordAuthentication no',
  match              => '^PasswordAuthentication',
  append_on_no_match => true,
}

file_line {'Set identity file school':
  ensure             => present,
  path               => '/etc/ssh/ssh_config',
  line               => '\tIdentityFile ~/.ssh/school',
  match              => '^IdentityFile',
  append_on_no_match => true,
}
