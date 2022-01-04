# Using Puppet, install puppet-lint

package { 'puppet-lint':
    ensure   => '2.5.0',
    require  => Exec['apt-get update'],
  }
