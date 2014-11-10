This is an Ansible role that installs and secures nginx.  It is
convenient to use as a base role upon which to let other roles define
specific virtual servers for nginx.

Other than just running `apt-get install nginx-full`, this role will

1. Disable the default website that ships with nginx.
2. Create an nginx configuration file that can be used for SSL.
  * File will be in `/etc/nginx/conf.d/ssl.conf` and can be included
    by subsequent virtual server definitions.
  * This assumes that the values of the variables
    `nginx_ssl_certificate` and `nginx_ssl_certificate_key` have been
    set to paths on disk where the SSL certificate and private key can
    be found.
3. Create an nginx configuration file that can be used for for a
   simple firewall
   * File will be in `/etc/nginx/conf.d/firewall.conf` and can be
     included by subsequent virtual server definitions.
   * Assumes the value of the variable `nginx_auth_file` has been set
     to a path on disk where an nginx user password file can be found.
   * Whitelists IPs in in `nginx_whitelisted_ips` and denys all other
     traffic.
   * Traffic must satisfy either the basic authentication or the IP
     whitelist to proceed.
4. Configures a logstash input file for the logs produced by nginx.

Tasks are tagged with

* nginx
* ssl
* firewall
* logstash

as appropriate.

