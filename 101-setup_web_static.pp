# Bash script that sets up your web servers for the deployment of
# web_static using Puppet

exec { 'update':
command  => 'sudo apt-get update',
provider => shell,
}

package { 'nginx':
ensure => installed,
}

file {['/data/', '/data/web_static', '/data/web_static2/releases',
      '/data/web_static/releases/test', '/data/web_static/shared']:
ensure => 'directory',
owner  => 'ubuntu',
group  => 'ubuntu',
}

file { '/data/web_static/releases/test/index.html':
content => "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>",
owner   => 'ubuntu',
group   => 'ubuntu',
}

file { '/data/web_static/current':
ensure => 'link',
target => '/data/web_static/releases/test/',
force  => yes,
owner  => 'ubuntu',
group  => 'ubuntu',
}

exec { 'sed':
command => 'sudo sed -i "/listen 80 default_server/a location /hbnb_static/ {\
\talias /data/web_static/current/;}" /etc/nginx/sites-available/default',
require => Package['nginx'],
}

service { 'nginx':
ensure  => running,
require => Package['nginx'],
}