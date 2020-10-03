import argparse
from GUI import Odin


# TODO give source directory some structure

parser = argparse.ArgumentParser()
parser.add_argument('--image', type=str)

Odin(parser).run()
