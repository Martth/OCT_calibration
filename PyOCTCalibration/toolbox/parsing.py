

import argparse
import sys


def parse_arguments():

    parser = argparse.ArgumentParser()

    parser.add_argument('-f',
                        '--filename',
                        help='Input .Raw Bscan file',
                        dest='input_file',
                        type=str,
                        default='test.raw',
                        required=False)

    parser.add_argument('-i',
                        '--interactive_shift-plots',
                        help='interactive_shift',
                        dest='interactive',
                        default = False,
                        action='store_true',
                        required=False)

    parser.add_argument('-d',
                        '--dispersion',
                        help='Dispersion normal or anormal',
                        dest='dispersion',
                        type=str,
                        default='pos',
                        required=False)

    arguments = parser.parse_args()

    if arguments.dispersion == 'normal':
        arguments.dispersion = 1
    elif arguments.dispersion == 'anormal':
        arguments.dispersion = -1
    else:
        raise ValueError('\n \n Invalide disperions [-d] input. try [-d=normal] or [-d=anormal]\n \n')


    return arguments
