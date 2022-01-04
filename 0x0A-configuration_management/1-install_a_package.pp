# Using Puppet, install puppet-lint

package { 'puppet-lint':
    ensure   => 'installed',
    provider => 'gem'
    install_options => '-v 2.5.0'
  }
