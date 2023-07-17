# Puppet script that increases the limit of Nginx worker file
exec {'increas_nginx_workerfile':
  command => 'sed -i "s/15/10000/" /etc/default/nginx; sudo service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin'
}
