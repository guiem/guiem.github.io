---
id: 747
title: 'Basic server setup on Ubuntu'
date: '2013-09-28T17:03:10+00:00'
author: 'Guiem Bosch'
layout: single
guid: 'http://guiem.info/?p=747'
permalink: /basic-server-setup-on-ubuntu/
categories:
    - programming
---

\[this section will be properly edited\]

`<br></br>ssh root@ip_address<br></br>passwd # changing initial password<br></br>adduser demo # adding 'demo' user<br></br>visudo<br></br>demo    ALL=(ALL:ALL) ALL # find section called user privilege specification and add this<br></br>`

Optional (changing ssh port for more security)

`<br></br>nano /etc/ssh/sshd_config`

Port 25000  
Protocol 2  
PermitRootLogin no

UseDNS no  
AllowUsers demo

reload ssh