# Puppet file that kills a process named killmenow
exec { 'kill_me_now':
  command => 'pkill killmenow',
  path    => '/usr/bin:/bin',
  onlyif  => '/usr/bin/pgrep killmenow',
}