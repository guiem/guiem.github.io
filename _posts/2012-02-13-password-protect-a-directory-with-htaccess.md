---
id: 547
title: 'Password Protect a Directory with .htaccess'
date: '2012-02-13T16:16:54+00:00'
author: 'Guiem Bosch'
layout: single
guid: 'http://guiem.info/?p=547'
permalink: /password-protect-a-directory-with-htaccess/
categories:
    - programming
    - server
---

**Motivation**: protect some directories from being accessed without authorisation.  
**Solution**: using the .httaccess file. You just have to configure one and place it into the directory you want to protect. The code inside the file would look something like this:

```

AuthType Basic
AuthName "guest"
AuthUserFile "/home/user/.htpasswds/public_html/directory2storepass/passwd"
require valid-user
```

Then you have to place the password in the directory you have chosen.  
The [source](http://www.addedbytes.com/lab/password-protect-a-directory-with-htaccess/) I’ve used.