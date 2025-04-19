---
id: 987
title: 'DNI electrónico (dnie) + Mac + Chrome'
date: '2018-12-07T13:39:04+00:00'
author: 'Guiem Bosch'
layout: single
guid: 'https://guiem.info/?p=987'
permalink: /dni-electronico-dnie-mac-chrome/
categories:
    - programming
tags:
    - Chrome
    - DNIe
    - electronico
    - Mac
---

Antes que nada, si vas con prisas te recomiendo que enchufes tu lector de DNI con un sistema Windows (te puedes ahorrar muchos dolores de cabeza!).

Si por lo contrario eres tan tozudo como yo, aquí te pongo un poco en contexto sobre mi caso:

- Ya había conseguido hacer login con mi **Mac y Firefox** sin salir de casa con mi lector de DNI siguiendo [estas instrucciones](https://www.dnielectronico.es/PortalDNIe/PRF1_Cons02.action?pag=REF_1113).
- Necesitaba usar el software [Autofirma](https://firmaelectronica.gob.es/Home/Descargas.html) que en Mac solamente fuciona en **Chrome** ya que en posteriores versiones de Firefox el soporte para Java hacía que no funcionase.
- Por un lado, podía leer el DNI y entrar a ciertos servicios con Firefox, pero a la hora de adjuntar y firmar documentos (con el programa Autofirma) el Firefox no funcionaba (sólamente Chrome).
- La solución que aquí te planteo implica obtener el certificado FNMT de Persona Física, así que tendrás que personarte físicamente para que te manden el certificado personal.

1. Solicitud del Certificado de Persona física desde Mac y Firefox [aquí](https://www.sede.fnmt.gob.es/certificados/persona-fisica/obtener-certificado-software/solicitar-certificado) (Chrome no es un navegador soportado y la página se quejará de ello si intentas hacerlo con Chrome). Aunque recordemos que el objetivo final de este tutorial es ser capaz de hacerlo todo a través de Chrome y Mac. 
    1. Recibirás un e-mail con un código de solicitud.
    2. Debes presentarte con tu DNI a cualquiera de las Oficinas de Registro Autorizadas. En mi caso me daba mucha pereza salir, pero intentarlo hacerlo todo desde casa supuso muchas horas de frustración con el Mac sin obtener resultados. Finalmente la oficina más cercana resultó estar a 2 minutos de casa, no había cola y en 5 minutos ya lo tenía resuelto.
2. Habrás recibido un e-mail para descargar el certificado, sin embargo, para descargarlo tienes que hacerlo desde Firefox. Sigue las instrucciones.
3. Hasta ahora se ha instalado tu certificado en el navegador Firefox, ahora deberás exportarlo para poder transferirlo a tu llavero y que Chrome lo pueda usar. 
    1. Para ello debes ir a Firefox -&gt; Preferencias -&gt; Privacidad &amp; Seguridad y darle a Ver Certificados  
        ![](https://guiem.info/wp-content/uploads/Screenshot-2018-12-07-at-13.36.26.png)
    2. Seleccionar el certificado y click en “Hacer copia”, guardar el ficher con la extensión “.p12”  
        ![](https://guiem.info/wp-content/uploads/Screenshot-2018-12-07-at-14.24.47.png)
    3. Por fin nos podemos olvidar del navegador Firefox. **Chrome en Mac** funciona con el llavero. Finder -&gt; Ir -&gt; Utilidades -&gt; Acceso a Llaveros.
    4. En el llavero hay que ir a la pestaña “Login”, categoría “Mis certificados”.  
        ![](https://guiem.info/wp-content/uploads/Screenshot-2018-12-07-at-14.31.31.png)
    5. Después en el mismo llavero: “Archivo” -&gt; “Importar items”. Seleccionas el certificado que acabas de exportar.
    6. Doble click en el certificado y añadir “Permitir Siempre”  
        ![](https://guiem.info/wp-content/uploads/Screenshot-2018-12-07-at-14.35.19.png)

Ya está, una vez intentes acceder a la sede con el DNI en Chrome y Mac, el navegador debería reconocer tu certificado. Nota: puede que necesites otros certificados si no los tienes ya instalados, incluso puede que el navegador te pida permiso para confiar en ellos, pero esto queda fuera del alcance de este mini-tutorial.

De todas formas, si tienes alguna duda, escríbeme un mensaje. Créeme, sé cuánta frustración uno puede llegar a experimentar con estos temas, así que intentaré ayudarte encantado! :)