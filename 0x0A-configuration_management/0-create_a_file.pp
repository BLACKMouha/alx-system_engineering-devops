# Puppet file that create a file name school in the tmp directory 
file { '/tmp/school':
  ensure  => present,
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
}
