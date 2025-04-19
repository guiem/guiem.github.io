---
id: 442
title: 'wp-cv plugin creation'
date: '2012-02-12T05:17:56+00:00'
author: 'Guiem Bosch'
layout: single
guid: 'http://guiem.info/?p=442'
permalink: /wp-cv-plugin-creation/
categories:
    - programming
    - unsolved
---

**Motivation**: I hate standard text-based CVs. They are so boring and I want something that gives you a quick look into the main things somebody has done. And I also want it to be strongly ‘time-based’. Plus: I want a very very simple design and I need to have a functional version very very soon.  
**Motivation(II)**: I want to *play* a little bit with HTML5, the Canvas and making a WP plugin.  
**Disclaimer**: As I need it to be done immediately because I want to apply for a specific candidature I will be doing stuff without thinking very much on code prettiness. Anyway, I’ll promise it will be an iterative process to I’ll be improving it.  
**Solution**:

1. Starting point: googling about I found [this](http://simonsarris.com/blog/510-making-html5-canvas-useful) post. So I must say thanks to [Simon Harris](http://simonsarris.com/about), I’ll start based my work on his example.
2. Changed mouse cursor in mouse EventListeners. I want to have the ‘dragging’, ‘mouseover’ etc. pointers. Example: ```
    
    if (activities[i].contains(mx, my)) {
        e.target.style.cursor = 'pointer'; // My mouse cursor is in the area of an activity, so I change cursor to 'pointer' style.
        return;
    }
    else e.target.style.cursor = 'auto';
    ```
3. <del datetime="2012-02-09T19:45:48+00:00">For the ‘more information’ area, I want to be able to offer rich text edition. I found this one, [Aloha Editor](http://aloha-editor.org/), which I’m going to try.</del>Cancelled this step right now. I’ve tried the editor but format was not appearing as I desired and right now I’m not going to spend time on it. Let’s assume we’ll edit information manually adding html format
4. Once I click on an activity I want to update the ‘More information’ section. I do this using [Prototype](http://www.prototypejs.org/). Very easy to install (by only including the .js file: ```
    <script src="js/prototype.js" type="text/javascript"></script>
    ```
    
    ) and very easy to use (in the activities.js file do something like this
    
    ```
    document.getElementById("information").update("<i>"+MORE_INFO_MSG+"</i>");
    ```
    
    **NOTE**: I finally chose [jQuery](http://docs.jquery.com/Downloading_jQuery) because I want to use jQuery sliders as some browsers don’t support “range” input sliders in HTML5 yet. Using Prototype and jQuery leads to some conflicts (which can be solved) but I prefer not to mix them. Usage now would be:
    
    ```
    $("#information").html("<i>"+MORE_INFO_MSG+"</i>");
    ```
5. I want my Activity elements to move across the screen so I will display a [slider](http://php.quicoto.com/how-to-create-html5-input-range/) and I’ll apply a SCREEN\_OFFSSET to the X position of my activities. This will do the trick.

Right now I publish it as it is, very ad-hoc. But I had a deadline where I wanted to show it. In fact there is much more ‘automatized’ than what you can see (for example, scrolling in horizontal direction). But I promise I’ll keep working on it and finally integrate it as a WordPress plugin.

Some stuff written in catalan, just a TODO list to myself…  
a fer:  
– en un futur desplaçar només en horitzontal seleccionant qualsevol punt de sa pantalla (mostrar maneta de drag)  
– fer zoom de tots a l’hora  
– posar els més antics baix i construir cap amunt (activitats posteriors tenen bases o fonaments amb coses d’abans)  
– en un futur posar totes les activitats en transparent menys la seleccionada (hi ha un ctx.globalAlpha, però no mola perquè ho posa tot)  
– afegir scrolling de nou