# script that fixes nginx error

exec { 'error-nginx2':
  command => 'sed -i s/15/15000/ /etc/default/nginx; sudo service nginx restart',
  path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
}
