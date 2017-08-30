import argparse
from calculate_spectra import calculate_spectra

parser = argparse.ArgumentParser()
parser.add_argument("--input", "-i", help="The input file", default="spectra_flu.in")
parser.add_argument("--output", "-o", help="The output file", default="spectra_flu.out")
parser.add_argument("--number_states", help="The number of excited states you want to extract",
                    default=1, type=int)
parser.add_argument("--number_gauss", help="The number of gaussians", default=100, type=int)
parser.add_argument("--fwhm", help="Full witdh half max", default=0.05, type=float)
parser.add_argument("--number_bins", help="The number of bins you wish to distribute over",
                    default=1000, type=int)
parser.add_argument("--xmin", help="The minimum energy in eV", default=2.0, type=float)
parser.add_argument("--xmax", help="The maximum energy in eV", default=3.0, type=float)
args = parser.parse_args()

calculate_spectra(args.number_states, args.number_gauss, args.fwhm, args.number_bins,
                  args.xmin, args.xmax, args.input, args.output)
