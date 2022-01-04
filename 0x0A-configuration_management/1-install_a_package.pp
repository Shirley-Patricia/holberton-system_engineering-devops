# Using Puppet, install puppet-lint

package { 'puppet-lint -v 2.5.0':
    ensure => 'installed',
  }
