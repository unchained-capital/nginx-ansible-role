# Ansible Role for nginx

This is an [Ansible](http://www.ansible.com/home) role for installing
[nginx](http://wiki.nginx.org/Main).

It allows installing nginx from the package manager or from source.
When installing from source, it provides some flexibility for you to
configure the modules you want to compile in (including fetching 3rd
party modules via git).

It only works for Debian-based systems right now.

# Services

Leaves a service `nginx` running without any virtual hosts.

# Usage

Use the role in a playbook like this to install the default nginx from
the package manager.

```yaml
- hosts: webservers
  roles:
    - nginx
```

## Source Installation

When installing from source you can use the variables
`nginx-custom_configure_flags`, `nginx_custom_modules`, and
`nginx_custom_source_packages` to customize the nginx build.  (You can
also mess with the defaults -- see `defaults/main.yml` for more
details.)

The following example shows some custom configure flags and a custom
module (`nginx-auth-ldap`) which will be fetched from GitHub.  The
module requires some packages be available and those are specified as
well (`libldap2-dev`):

```yaml
- hosts: webservers
  roles:
    - nginx
	  nginx_install_source: true
	  nginx_custom_configure_flags: ["--some-option", "--some-other-option with_value", ...]
	  nginx_custom_modules:
	    - https://github.com/kvspb/nginx-auth-ldap
	  nginx_custom_source_packages:
	    - libldap2-dev
```
