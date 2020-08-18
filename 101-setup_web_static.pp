# Bash script that sets up your web servers for the deployment of
# web_static using Puppet

exec { 'update':
command  => 'sudo apt-get update',
provider => shell,
}

package { 'nginx':
ensure => installed,
}

d1 = 'data'
d2 = 'web_static'
d3 = 'releases'
d3_1 = 'test'
d4 = 'shared'
file {['/d1/d2/d3', '/d1/d2/d3/d3_1', '/d1/d2/d4']:
ensure => 'directory',
owner  => 'ubuntu',
group  => 'ubuntu',
}

file { '/d1/d2/d3/d3_1/index.html':
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

file { '/d1/d2/current':
ensure => 'link',
target => '/d1/d2/d3/d3_1/',
force  => yes,
owner  => 'ubuntu',
group  => 'ubuntu',
}

exec { 'sed':
command => 'sudo sed -i "/listen 80 default_server/a location /hbnb_static/ {\
\talias /data/web_static/current/;\
}" /etc/nginx/sites-available/default',
require => Package['nginx'],
}

service { 'nginx':
ensure => running,
require Package['nginx'],
}