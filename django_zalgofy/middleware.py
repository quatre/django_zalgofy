# coding: utf-8
from django.conf import settings
from HTMLParser import HTMLParser
import xml.etree.ElementTree as ET

from random import randint, choice, random


def zalgo(text, intensity=1, zalgo_probability=0.4):
    zalgo_threshold = int(intensity)
    zalgo_chars = [unichr(i) for i in range(0x0300, 0x036F + 1)]
    zalgo_chars.extend([u'\u0488', u'\u0489'])
    source = text.decode('utf8')
    if not _is_narrow_build:
        source = _insert_randoms(source)
    zalgoized = []
    for letter in source:
        divisor = 1
        zalgoized.append(letter)
        if not letter.isalnum():
            divisor = 50
        if random() * divisor > zalgo_probability:
            continue
        letter = letter.upper()
        zalgo_num = randint(0, zalgo_threshold) + 1
        for _ in range(zalgo_num):
            zalgoized.append(choice(zalgo_chars))
    response = choice(zalgo_chars).join(zalgoized)
    response = "".join(zalgoized)
    return response.encode('utf8', 'ignore')


def _insert_randoms(text):
    random_extras = [unichr(i) for i in range(0x1D023, 0x1D045 + 1)]
    newtext = []
    for char in text:
        newtext.append(char)
        if randint(1, 5) == 1:
            newtext.append(choice(random_extras))
    return u''.join(newtext)


def _is_narrow_build():
    try:
        unichr(0x10000)
    except ValueError:
        return True
    return False


def locate_tags(content):
    blocks = []
    for pos, c in enumerate(content):
        if c == "<":
            try:
                blocks.append((begin_not_tag, pos, True))
            except NameError:
                pass
            begin_tag = pos
        elif c == ">":
            blocks.append((begin_tag, pos + 1, False))
            begin_not_tag = pos + 1
    return blocks


class ZalgofyMiddleware(object):

    def process_response(self, request, response):
        if not response["Content-type"].startswith("text/html;"):
            return response
        blocks = locate_tags(response.content)
        content = ""
        zalgo_probability = settings.ZALGO_INITIAL_PROBABILITY
        zalgo_intensity = settings.ZALGO_INITIAL_INTENSITY
        for start, end, act in blocks:
            if act:
                content += zalgo(response.content[start:end],
                        zalgo_intensity,
                        zalgo_probability)
                zalgo_probability += settings.ZALGO_PROBABILITY_INCREASE
                zalgo_intensity += settings.ZALGO_INTENSITY_INCREASE
            else:
                content += response.content[start:end]
        response.content = content
        return response
