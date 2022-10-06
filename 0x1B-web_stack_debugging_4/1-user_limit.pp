# script that fixes holberton error

exec { 'error-holberton':
  command => 'sudo sed -i s/hard nofile/hard nofile 50000/ /etc/security/limits.conf',
  path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
}

exec { 'error-holberton-part2':
  command => 'sudo sed -i s/soft nofile/soft nofile 40000 /etc/security/limits.conf',
  path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
}
