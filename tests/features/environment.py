from src.sample.hamming import *


def before_scenario(context, scenario):
    context.hamming = Hamming()


def after_scenario(context, scenario):
    context.hamming = None
