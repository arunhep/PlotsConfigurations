import argparse

'''
This script saves in a TFile the effect of the selected nuisance for the 
given samples and variables. 

The effect is saved as the ratio of variationn/nominal.
'''
parser = argparse.ArgumentParser()
parser.add_argument("-i","--input", help="Input file", type=str)
parser.add_argument("-o","--output", help="Output file", type=str)
parser.add_argument("-s","--samples", help="Samples", type=str, nargs="+")
parser.add_argument("-c","--cuts", help="Cut", type=str, nargs="+")
parser.add_argument("-v","--vars", help="Variables", type=str, nargs="+")
parser.add_argument("-n","--nuisances", help="Nuisances", type=str, nargs="+")
parser.add_argument("-f","--fit", help="Fit",action="store_true")
args = parser.parse_args()

import ROOT as R 
R.gROOT.SetBatch(True)
R.TH1.SetDefaultSumw2()



iF = R.TFile.Open(args.input, "READ")
oF = R.TFile.Open(args.output, "UPDATE")

for cut in args.cuts:
    oF.mkdir(cut)
    print "Cut: ", cut
    if args.vars[0] == "ALL":
        vars = [k.GetName() for k in iF.Get(cut).GetListOfKeys()]
    else:
        vars = args.vars 
        
    for var in vars:
        print "> Var: ", var 
        oF.mkdir(cut + "/"+var)
        for s in args.samples:
            print ">> Sample: ", s 
            h_nom = iF.Get("{}/{}/histo_{}".format(cut, var, s ))

            for n in args.nuisances:
                h_up = iF.Get("{}/{}/histo_{}_{}Up".format(cut, var, s, n)).Clone()
                h_do = iF.Get("{}/{}/histo_{}_{}Down".format(cut, var, s, n)).Clone()

                h_up.Divide(h_nom)
                h_do.Divide(h_nom)
                oF.cd(cut + "/"+var)
                h_up.Write()
                h_do.Write()

                if args.fit:
                    # Try the linear fit
                    lin_up = R.TF1("f_{}_{}Up".format(s, n), "pol1")
                    lin_do = R.TF1("f_{}_{}Do".format(s, n), "pol1")
                    h_up.Fit(lin_up, "W")
                    h_do.Fit(lin_do, 'W')
                    lin_up.Write()
                    lin_do.Write()

        oF.cd()

    print "------------------------------"


oF.Close()