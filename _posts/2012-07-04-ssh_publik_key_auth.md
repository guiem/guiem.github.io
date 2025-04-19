---
id: 614
title: 'SSH Public Key Based Authentication'
date: '2012-07-04T18:14:45+00:00'
author: 'Guiem Bosch'
layout: single
guid: 'http://guiem.info/?p=614'
permalink: /ssh_publik_key_auth/
categories:
    - bluehost
    - programming
    - server
---

**Motivation**: I want to acces to my Bluehost server from my local computer, make some file copies ‘scp’ but from a script executed by Crontab, so I don’t want to introduce my password manually.  
**Solution**:

- Generate the key from your local machine (I don’t think it’s needed but, store the keys in ~/.ssh ```
    
    ssh-keygen -t rsa
    ```
- Copy the public key to your server: ```
    
    scp .ssh/id_rsa.pub username@server_name_address:.ssh/authorized_keys2
    ```

**Source**: [ciberciti](http://www.cyberciti.biz/tips/ssh-public-key-based-authentication-how-to.html)