---
id: 577
title: 'remove_filter function in WordPress'
date: '2012-03-24T23:15:21+00:00'
author: 'Guiem Bosch'
layout: single
guid: 'http://guiem.info/?p=577'
permalink: /remove_filter-function-in-wordpress/
categories:
    - programming
    - wordpress
---

**Motivation**: In a specific website I am using the [simplex](http://wordpress.org/extend/themes/simplex) theme. If one tries to place a static page as home instead of the blog, simplex keeps showing the Home page.  
**Solution**: as you can see, people have already [reported](http://wordpress.org/support/topic/static-home-page-8) this. But in the current version of the theme the line is introduced in `functions.php` and functions are not really overridden, they can be just replaced.  
In the codex it is described how to remove actions and [filters](http://codex.wordpress.org/Function_Reference/remove_filter) but it turned out that the solution didn’t work for me. As usually, it was really easy but cost me a bit to figure out:

```

function unhook_simplex_function() {
    if(has_filter( 'wp_nav_menu_items', 'simplex_nav_menu_items' )){
        remove_filter( 'wp_nav_menu_items', 'simplex_nav_menu_items' );
    }
}
add_action('init','unhook_simplex_function');
```

Instead of calling the remove\_filter function directly in my `functions.php` I just added an action that calls the function that will remove the filter from the ‘init’.