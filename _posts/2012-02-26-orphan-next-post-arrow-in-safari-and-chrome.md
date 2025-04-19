---
id: 560
title: 'Orphan next post arrow in Safari and Chrome'
date: '2012-02-26T12:10:22+00:00'
author: 'Guiem Bosch'
layout: single
guid: 'http://guiem.info/?p=560'
permalink: /orphan-next-post-arrow-in-safari-and-chrome/
categories:
    - programming
    - wordpress
---

**Motivation**: in the single post page, the arrow that points to the next post appears one line below the ‘Next’ text in Safari and Chrome browsers.  
**Solution**: I don’t know if this is a ‘good’ way to solve it or if I should report it somewhere, but as a quick fix I’ve edited my child `style.css` file adding the following:

```

#nav-single .nav-next {    
    float:right;
}
#nav-single .nav-previous {
    float:left;
}  
```