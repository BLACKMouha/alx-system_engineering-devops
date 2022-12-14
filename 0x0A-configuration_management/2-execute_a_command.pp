# kills a process named 'killmenow'
exec { 'kill-me-now':
  command => '/usr/bin/pkill -f killmenow',
}
