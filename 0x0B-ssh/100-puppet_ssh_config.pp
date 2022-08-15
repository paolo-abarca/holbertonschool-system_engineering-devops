#adding puppet file which makes changes to our config file

file { '/etc/ssh/ssh_config':
  path => '/etc/ssh/ssh_config',
  line => '#   IdentityFile ~/.ssh/school'
}

file { '/etc/ssh/ssh_config':
  path => '/etc/ssh/ssh_config',
  line => '#   PasswordAuthentication no'
}
