# Puppet script that fixes a bug in a WordPress website
$wp__setttings = '/var/www/html/wp-settings.php'

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${wp__settings}",
  path    => ['/bin','/usr/bin']
}
