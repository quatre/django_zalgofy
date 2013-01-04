What does it do?
##################

django_zalgofy's middleware turns everything that's not a tag in a text/html
respoonse to ZALGO speech.

How can I Use it?
###################

run python setup.py install


Add the following middleware to your Django ``settings.py`` file::

       MIDDLEWARE_CLASSES = (
           # ...
           'django_zalgofy.middleware.ZalgofyMiddleware',
           # ...
       )

Can I configure something?
############################

Absolutely, you can set the following settings (and figure out what they change
by yourself!) :

 - ``ZALGO_INITIAL_PROBABILITY = 0.0001``
 - ``ZALGO_PROBABILITY_INCREASE = 0.0004``
 - ``ZALGO_INITIAL_INTENSITY = 2``
 - ``ZALGO_INTENSITY_INCREASE = 0.2``

These are their default values.

Thanks
#######

Thanks to Michael J. Giarlo
for pyzalgo (https://github.com/mjgiarlo/pyzalgo), used here!

