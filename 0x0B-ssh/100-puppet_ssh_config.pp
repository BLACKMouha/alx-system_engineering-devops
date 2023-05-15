$conf_stmt = "
    PasswordAuthentication no
    IdentityFile ~/.ssh/school
"

$fi = '/etc/ssh/ssh_config'

file_line { 'add_conf_stmt_to_ssh_config':
  ensure  => present,
  path    => $fi,
  line    => $conf_stmt,
}

exec { 'ssh_config_reload':
  command     => '/etc/init.d/ssh reload',
  refreshonly => true,
}
