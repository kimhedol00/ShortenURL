import config
import randstr
import os

def shorten_url(url):
    return randstr.generate_rand_token(6)