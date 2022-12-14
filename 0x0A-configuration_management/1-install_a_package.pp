# installing a flask package with pip3
exec { 'flask-pip':
  command => '/usr/bin/pip3 install Flask==2.1.0',
}
