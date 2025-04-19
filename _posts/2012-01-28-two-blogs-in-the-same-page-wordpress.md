---
id: 236
title: 'Two blogs in the same page'
date: '2012-01-28T17:37:39+00:00'
author: 'Guiem Bosch'
layout: single
guid: 'http://guiem.info/?p=236'
permalink: /two-blogs-in-the-same-page-wordpress/
categories:
    - programming
    - unsolved
    - wordpress
---

**Motivation**: I want to show 2 blogs in my WordPress site. A quick search on the web reveals that apparently you must install each blog separately, but I don’t want to do so. In fact I don’t need two different blogs, I just want to split posts in two different pages (by category).

**Solution**: the solution I found consists of using the original posts site for one of the blogs and an extra page (with a specific template) to show the other blog pots. Separation is done by category applied to each post.

1. <del>[Create a Page of Posts template](http://codex.wordpress.org/Pages#A_Page_of_Posts). I’m using a child theme of Twenty Eleven so I just create a *pageofposts.php*file with the code below. Then change the category you want to filter for this blog (blog2).</del><div> </div>```
    
    <?php /*
    Template Name: Page Of Posts
    */
    
    // if you are not using this in a child of Twenty Eleven, you need to replicate the html structure of your own theme.
    
    get_header(); ??>
    <div id="primary">
    <div id="content" role="main">
    
    <?php $paged = (get_query_var('paged')) ? get_query_var('paged') : 1;
    $args= array(
    	'category_name' =?> 'antiquarianism, championship', // Change these category SLUGS to suit your use.
    	'paged' => $paged
    );
    query_posts($args);
    if( have_posts() ) :?>
    
    <?php twentyeleven_content_nav( 'nav-above' );??>
    
    <?php while ( have_posts() ) : the_post(); ??>
    
    <?php get_template_part( 'content', get_post_format() ); ??>
    
    <?php endwhile; ??>
    
    <?php twentyeleven_content_nav( 'nav-below' ); ??>
    
    <?php else : ??>
    <article class="post no-results not-found" id="post-0">
    <header class="entry-header">
    <h1 class="entry-title"><?php _e( 'Nothing Found', 'twentyeleven' ); ??></h1>
    </header>
    
    <div class="entry-content">
    <p><?php _e( 'Apologies, but no results were found for the requested archive. Perhaps searching will help find a related post.', 'twentyeleven' ); ??></p>
    <?php get_search_form(); ??>
    </div>
    </article>
    
    <?php endif; ??>
    
    </div>
    </div>
    
    <?php get_footer();
    </pre?>
    <p><strong>UPDATE</strong>: I finally just filtered it in the <code>index.php</code> file. I'm keeping the code above just in case you want to go for that approach, but what I have really done is to copy the <code>idex.php</code> into my child theme. As the post pages is the home, I have added the following code that omits all the posts from <code>programming</code> category:</p>
    
    <?php $paged = (get_query_var('paged')) ? get_query_var('paged') : 1;
        $id_cat_prog = get_cat_ID('programming');
        $args= array(
            'cat' =?> '-'.$id_cat_prog, 
            'paged' => $paged
        ); 
        query_posts($args);
    ?>
    
    ```
<div> </div>3. [Getting category id](http://codex.wordpress.org/Function_Reference/get_cat_ID). You can just check it from your configuration, but I want to obtain my category id from a category name, so I'm using the function: <div> </div>```
    
    <?php get_cat_ID( $cat_name ) ??>
    ```
<div> </div>5. Excluding posts from blog 2 to appear into my feed. I don't want my feed to be updated with posts I place in blog 2. [Here](http://autoblogged.com/76687/blog/all-the-wordpress-feeds/) I found a list of different WordPress feeds so in my feed address I can filter excluding the category of my second blog posts. By the way, in my case I placed a RSS icon in the menu bar so I manually added the post filter from WP Dashbord (Appearance --&gt; Menus, and edit link from custom option. <div> </div>
6. Once you are in the post view if you click on the 'next' or 'previous' post button by default all the posts (doesn't matter to which category they belong) will appear. But I want only posts of 'my current blog' to appear. To solve this I'm using the [next\_post\_link](http://codex.wordpress.org/Function_Reference/next_post_link#Usage) function to tell that I want to filter next or previous posts by category. You only have to edit a few lines in *single.php*. Here you have an example: <div> </div>```
    
    <?php $cat_prog = get_cat_ID('programming');
    $cat_pers = get_cat_ID('personal');
    $cat_wp = get_cat_ID('wordpress');
    $cat_bh = get_cat_ID('bluehost');
    if (in_category($cat_prog)) {
        $cat_filter = $cat_pers;
    }
    elseif (in_category($cat_pers)){
        $cat_filter = $cat_prog.','.$cat_wp.','.$cat_bh;
    } 
    ??>      
    <span class="nav-previous"><?php previous_post_link( '%link', __( '<span class="meta-nav"?>←</span> Previous', 'twentyeleven' ),FALSE,$cat_filter); ?>
    <span class="nav-next"><?php next_post_link( '%link', __( 'Next <span class="meta-nav"?>→</span>', 'twentyeleven' ),FALSE,$cat_filter ); ?>
    
    ```
<div> </div>8. I want to show a different Archives Page for each blog. In one of them I want to show posts by Year and Month. I used the [Collapsing Archives](http://wordpress.org/extend/plugins/collapsing-archives/) plugin. Of course, I don't want posts from the second blog to be listed here. In order to configure the posts I will show in Archives and their style I created an archives.php file in my child theme. Then you only have to create a new page and apply the new template. Be careful: this plugin also takes into account the 'tags' of the post in order to do the filtering, it treats those tags as if they where post categories. Thus you'll have to exclude them in the options: <div> </div>```
    
    <?php /*
    Template Name: Archives
    */
    get_header(); ??>
    
    <div id="container">
    <div id="content" role="main">
    <?php the_post(); ??>
    <h1 class="entry-title"><?php the_title(); ??></h1>
    <h2>Archives by Year & Month</h2>
    <?php if( function_exists('collapsArch') ) {
      collapsArch('animate=1&inExcludeCat=exclude&inExcludeCats=programming,wordpress,bluehost,code,snippet,widget'); // in my case 'code','snippet' and 'widget' are tags and not categories
    } else {
        wp_get_archives();
    }
    ??>
    </div>
    </div>
    <?php get_sidebar(); ??>
    <?php get_footer(); ??>
    ```
    
    <div> </div>
9. Finally I wanted to show my programming posts divided by category. Tried to use Collapsing Categories plugin but it won't expand properly. I posted on [WordPress forum](http://wordpress.org/support/topic/collapsing-categories-plugin-wont-expand-categories?replies=0) and I'm currently waiting for any hints on this.*And just as a mental note if I finally solve this point: by using this plugin I found another error which is solved [here](http://wordpress.org/support/topic/plugin-collapsing-categories-javascript-error?replies=1).*