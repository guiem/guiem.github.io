---
id: 427
title: 'WP-reCAPTCHA: javascript error in pages without submit button'
date: '2012-02-05T11:13:11+00:00'
author: 'Guiem Bosch'
layout: single
guid: 'http://guiem.info/?p=427'
permalink: /wp-recaptcha-javascript-error-in-pages-without-submit-button/
categories:
    - programming
    - wordpress
tags:
    - javascript
    - plugin
---

**\[UPDATE\]**: it seems that the problemis solved since version 3.1.5 (but I’m not certain if this is version 3.1.5 or since 3.1.6. Anyway, you don’t need to read this post if you are using one of those versions or above.

**Motivation**: I’m using the [WP-reCAPTCHA](http://wordpress.org/extend/plugins/wp-recaptcha/) plugin and there is a javascript error in every page where I didn’t include any post comment box.  
**Solution**: Found [here](http://wordpress.org/support/topic/javascript-error-in-ie8-on-pages-that-do-not-have-submit-button). But I’m copying the solution here anyway:  
“In the recaptcha.php page, there’s a function called “save\_comment\_script”. In the middle of it is a block of code that currently looks like this”

```

<script type="text/javascript">
var sub = document.getElementById('submit');
document.getElementById('recaptcha-submit-btn-area').appendChild (sub);
document.getElementById('submit').tabIndex = 6;
if ( typeof _recaptcha_wordpress_savedcomment != 'undefined') {
	document.getElementById('comment').value = _recaptcha_wordpress_savedcomment;
}
document.getElementById('recaptcha_table').style.direction = 'ltr';
</script>
```

Change that code to look like this:

```

<script type="text/javascript">
if(document.getElementById('submit') != null)
{
	var sub = document.getElementById('submit');
	document.getElementById('recaptcha-submit-btn-area').appendChild (sub);
	document.getElementById('submit').tabIndex = 6;
	if ( typeof _recaptcha_wordpress_savedcomment != 'undefined') {
		document.getElementById('comment').value = _recaptcha_wordpress_savedcomment;
	}
	document.getElementById('recaptcha_table').style.direction = 'ltr';
}
</script>
```