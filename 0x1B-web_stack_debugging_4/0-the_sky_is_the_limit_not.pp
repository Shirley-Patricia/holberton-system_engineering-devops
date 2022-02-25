# How to set nginx max open files?

exec { 'max_files':
  command => 'sed -i s/15/4096/ /etc/default/nginx; service nginx restart',
  path    => ['/usr/bin:/usr/sbin:/bin'],
  }
