from src.sample.hamming import *
from src.sample.user_class import *


def before_scenario(context, scenario):
    context.hamming = Hamming()
    context.user = User()


def after_scenario(context, scenario):
    context.hamming = None
    context.user = None
