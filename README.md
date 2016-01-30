This is an [Ansible](http://www.ansible.com/home) role for installing
[nginx](http://wiki.nginx.org/Main) in a relatively secure way.

# What it Does

## Assumptions

This installation is only as secure as you make it.  It assumes you
have an
[SSL certificate](https://www.globalsign.com/ssl-information-center/what-is-an-ssl-certificate.html)
(`nginx_ssl_certificate`, `nginx_ssl_certificate_key`) and an
[htpasswd](https://httpd.apache.org/docs/current/programs/htpasswd.html)
(`nginx_auth_file`) file that you have securely transferred to the
webserver node.

## Software

Installs nginx which provides the following `nginx` command.

Also removes the default nginx virtual hosts.  Disable this by setting
`nginx_disable_default_site` to `false`.  Build your own more secure
virtual hosts using the SSL and firewall definitions provided below.

Also creates a logstash file for nginx logs.  Disable this by settings
`nginx_use_logstash` to `false`.

### SSL

Defines shared SSL parameters at `/etc/nginx/ssl.conf`.  These SSL
parameters can be included into the configuration files of any
subsequent nginx virtual host (=server=) by including the
configuration file `/etc/nginx/ssl.conf`.

It is assumed that the SSL certificate and key have previously been
moved to the remote machine.  The paths defined in the variables
`nginx_ssl_certificate` and `nginx_ssl_certificate_key` are templated
into `/etc/nginx/ssl.conf`.

### Firewall

Creates a firewall definition at `/etc/nginx/firewall.conf` which
forces traffic to either

* be on a whitelist of IPs (`nginx_whitelisted_ips`) or
* to login via HTTP(S) [Basic Authentication](https://en.wikipedia.org/wiki/Basic_access_authentication)

This firewall is useful for (partially) securing a site during
development for example, or for securing an admin interface of a site
during production.

Authorized users are defined in `/etc/nginx/conf.d/users`.  Update
this file separately to manage users.

## Configuration & Logging

Creates the files:

* `/etc/nginx/firewall.conf` -- firewall for virtual hosts needing to restrict access
* `/etc/nginx/ssl.conf` -- shared SSL parameters for virtual hosts needing SSL
* `/var/log/nginx` -- log directory
* `/etc/logstash/conf.d/nginx.conf` -- inputs for logstash

## Services

Leaves a service `nginx` running without any virtual hosts.

# Usage

Use the role in a playbook like this:

```yaml
- hosts: all
  roles:
    - nginx
```

## Variables

The following variables are exposed for configuration:

* `nginx_package` -- the name of the nginx package to install (default: `nginx-full`)
* `nginx_user` -- the user to run nginx worker processes as (default: `www-data`)
* `nginx_group` -- the group to run nginx worker processes as (default: `www-data`)
* `nginx_worker_processes` -- number of nginx worker processes
* `nginx_worker_connections` -- number of nginx worker connections
* `nginx_whitelisted_ips` -- array of IP addresses which will be whitelisted in the firewall
* `nginx_auth_realm` -- name of basic authentication realm for firewall (default: Restricted)
* `nginx_auth_file` -- path to existing nginx auth file
* `nginx_ssl_certificate` -- path to existing nginx SSL certificate
* `nginx_ssl_certificate_key` -- path to existing nginx SSL key
