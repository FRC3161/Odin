import argparse
from GUI import Odin

parser = argparse.ArgumentParser()
parser.add_argument('--image', type=str)

Odin(parser).run()
