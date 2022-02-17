# using puppet to fix apache

exec {'stack_debug':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/bin:/usr/sbin:/bin',
}
