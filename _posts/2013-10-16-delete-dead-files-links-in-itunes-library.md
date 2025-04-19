---
id: 776
title: 'Delete &#8220;dead&#8221; files (links) in iTunes library'
date: '2013-10-16T16:29:49+00:00'
author: 'Guiem Bosch'
layout: single
guid: 'http://guiem.info/?p=776'
permalink: /delete-dead-files-links-in-itunes-library/
categories:
    - programming
---

**Problem**: some songs appear marked with the ‘!’ sign in my iTunes and I just want to get rid of them (in my case I know the original source was an external drive I’m not using anymore).

**Ideas**: I learned that `/Users/username/Music/iTunes/iTunes Music Library.xml` contains a list with all songs and their path, so eager to make it quick I planned to create a python script to modify this file till I realized there was no need to program.

**Solution:**

- everything here is related to iTunes v 11.x &amp; on Mac OS

1. If running, stop iTunes and reopen it pressing Option key (alt)
2. A prompt will ask you to change iTunes library (if not you weren’t holding the right key)
3. Choose the ‘create’ new library button*At this point you’ll have an iTunes empty version. No songs listed at all.*
4. Finally, go to File&gt;Library&gt;Import playlist and choose the .xml file I told you before (`/Users/username/Music/iTunes/iTunes Music Library.xml` ). This way you’ll import all the files except from those having unreachable links to disk (which turns to be exactly what I wanted)

Some useful links i checked before I came up with a solution:

– [apple suport](http://support.apple.com/kb/HT1451)

– [programming example](http://stefaanlippens.net/itunes-library-parsing-with-python) (in case your need to do something more complex)

<span style="line-height: 1.5;"> </span>