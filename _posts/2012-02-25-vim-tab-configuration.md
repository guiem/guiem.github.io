---
id: 554
title: 'VIM tab configuration'
date: '2012-02-25T17:07:47+00:00'
author: 'Guiem Bosch'
layout: single
guid: 'http://guiem.info/?p=554'
permalink: /vim-tab-configuration/
categories:
    - programming
    - server
---

**Motivation**: I like to edit files using [VIM](http://www.vim.org/). In my server ([Bluehost](http://www.bluehost.com/)) the default configuration makes my ‘tab’ to produce really width spaces and I want it to be the size of 4 spaces.  
**Solution**: I edited a file `.vimrc` and I placed in my home directory in my server. The content of this file is the following:

```

set expandtab
set smartindent
set tabstop=4
set softtabstop=4
set shiftwidth=4
```