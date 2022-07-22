#!/usr/bin/env python
from importlib import import_module
import os
import sys
import math
import ROOT

from ROOT import TCanvas, TSystem, TFile, TProfile, TNtuple, TH1F, TH2F
from ROOT import gROOT, gBenchmark, gRandom, gSystem, Double

#create a new canvas, and customize it
h1 = TCanvas( 'h1', "ggH" , 200, 10, 700, 500)
h1.SetFillColor(0)
h1.GetFrame().SetFillColor(21)
h1.GetFrame().SetBorderSize(6)
h1.GetFrame().SetBorderMode(-1)

##Read input files:
dir1 = '/afs/cern.ch/work/t/tcarnaha/HWW/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/ggH/Full2018_v7/rootFile/'
file_name = dir1+"plots_ggH2018_v7_11_11.root"
#print('Loading file: '+file_name)

myfile = ROOT.TFile.Open(file_name, "READ")
root_dir = myfile.GetDirectory("test/gen_mVV") #returns a TDirectory - save this TDirectory to get histos using root_GetListOfKeys()
root_keys = root_dir.GetListOfKeys()
h1.cd() #go to this directory to access keys / histos attached

#now we can define parameters for histo
color = 1 #so can evolve colors
legend = ROOT.TLegend(0.65 ,0.6 ,0.85 ,0.75) #location

for key in root_keys:
    k = key.GetName()
    histo = myfile.Get("test/gen_mVV/" + k)
    histo.SetTitle("ggH d{\sigma}/d{E} vs. m{_H}")
    histo.SetLineColor(color)
    histo.Draw("SAME") #add statistical uncertainties / Legend (define objects before loop, then in loop Legends.Entry()
    color = color + 1

    histo.GetXaxis().SetTitle("pole mass [GeV]")
    histo.GetYaxis().SetTitle("d{\sigma}/d{E}")

    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextSize(0.04)
    latex.DrawLatex(0.12 ,0.85 , "CMS #font[52]{Preliminary Simulation}")
    latex.SetTextSize(0.03)
    legend.SetLineWidth(0)
    legend.SetHeader("Legend", "C") #center legend
    legend.AddEntry(histo, histo.GetTitle())
    legend.Draw("SAME")

###Better way to loop over all hists (and get names) in pyROOT:

# fname = 'histos.root'
# hnames = []
 
# tfile = TFile.Open(fname)
# for key in tfile.GetListOfKeys():
#     h = key.ReadObj()
#     if h.ClassName() == 'TH1F' or h.ClassName() == 'TH2F':
#         hnames.append(h.GetName())



# hist = []
#file loaded with TFile.Open
#for TH1D in file.listKey() #check this method = list all objects in file... file/
# in the for loop: hist.append(TH1D) - list of TH1 objects
#c1.cd()
#for histo in histos:
#histo.Draw("SAME") #same canvases
#legend.Add("...")
#out of loop: 
h1.SaveAs(".png")

# c1.cd()
# histo1.Draw()
# c1.SaveAs('test.png')
##Read the TH1D from file:
