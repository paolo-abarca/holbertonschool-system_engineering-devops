# Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet

exec { 'update shell':
  command  => 'sudo apt-get -y update',
  provider => shell,
}

exec { 'install nginx':
  command  => 'sudo apt-get -y install nginx',
  provider => shell,
}

exec { 'header HTTP':
  command  => 'sed -i "s/a 404./a 404.\n\t\tadd_header X-Served-By $HOSTNAME;/" /etc/nginx/sites-available/default',
  provider => shell,
}

exec { 'restart nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
}
