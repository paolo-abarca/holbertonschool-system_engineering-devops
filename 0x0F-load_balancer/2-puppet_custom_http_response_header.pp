# Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet

exec { 'install nginx':
	command  => 'sudo apt-get update -y;
	sudo apt-get install nginx -y;
}

exec { 'header HTTP':
	command => sed -i "s/a 404./a 404.\n\t\tadd_header X-Served-By $HOSTNAME;/" /etc/nginx/sites-available/default
	sudo service nginx restart,
}
