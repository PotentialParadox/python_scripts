import numpy as np
import argparse
from python_scripts.libbla import *

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("n_trajs", help="number of trajectories", type=int)
    parser.add_argument("traj_time", help="time of each trajectory in PS", type=float)
    parser.add_argument("--flu", help="apply to fluorescence", action="store_true")
    parser.add_argument("--plot", help="print graph", action="store_true")
    parser.add_argument("--solvent", help="solvent used in calculation", default="")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()
    suffix = 'flu' if args.flu else 'abs'
    if args.plot:
        dss = remove_failures(np.load("bla_{}.npy".format(suffix)))
        plotter(dss[:, :args.n_trajs, ::1], suffix, args.traj_time, args.solvent)
    else:
        d1 = getDistances(args.n_trajs, suffix, 17, 16)
        d2 = getDistances(args.n_trajs, suffix, 16, 15)
        d3 = getDistances(args.n_trajs, suffix, 15, 14)
        bla = np.array([d1, d2, d3])
        if args.debug:
            print(bla.shape)
        np.save("bla_{}.npy".format(suffix), bla)

main()