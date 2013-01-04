What does it do?
##################

django_zalgofy's middleware turns everything that's not a tag in a text/html
respoonse to ZALGO speech.

How can I Use it?
###################

add 'django_zalgofy.middleware.ZalgofyMiddleware', to MIDDLEWARE_CLASSES
in your Django settings.

Can I configure something?
############################

Absolutely, you can set the following settings (and figure out what they change
by yourself!) :

 - ZALGO_INITIAL_PROBABILITY = 0.0001
 - ZALGO_PROBABILITY_INCREASE = 0.0004
 - ZALGO_INITIAL_INTENSITY = 2
 - ZALGO_INTENSITY_INCREASE = 0.2

These are their default values.


