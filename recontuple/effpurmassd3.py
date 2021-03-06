import ROOT as rt
import plotfactory as pf
import numpy as np
import sys

pf.setpfstyle()
output_dir = '/afs/cern.ch/work/v/vstampf/plots/' 

fout = rt.TFile('histoseffpurmassd3.root', 'recreate')

######################################### 
# Make Chain from selection of samples
#########################################

# Get the option from the command line, using 'True' as a fallback.

if len(sys.argv)>1 and sys.argv[1] == 'test':
    setting = False
    print('Using a selection of samples')
else:
    setting = True
    print('Using all samples')

tt = pf.makechain(setting)

nentries = tt.GetEntries()
print('number of total entries in chain:\t\t\t%d'%(nentries))

######################################### 
# Produce KPIs
#########################################

n_2OrMoreMuons = tt.GetEntries()
print('number of all events with 2 or more muons:\t\t%d'%(n_2OrMoreMuons))

n_reconstructable = tt.GetEntries('flag_hnl_reconstructable == 1 & abs(l1_pdgId) == 13 & abs(l1_eta) < 2.4 & abs(l2_pdgId) == 13 & abs(l2_eta) < 2.4') 
print('number of events with reconstructable HNLs:\t\t%d'%(n_reconstructable))

n_dimuons = tt.GetEntries('n_dimuon > 0 & abs(l1_pdgId) == 13 & abs(l1_eta) < 2.4 & abs(l2_pdgId) == 13 & abs(l2_eta) < 2.4') 
print('number of events with reconstructed DiMuons:\t\t%d'%(n_dimuons))

n_matchedHNLChi2 = tt.GetEntries('flag_matchedHNLChi2 == 1 & abs(l1_pdgId) == 13 & abs(l1_eta) < 2.4 & abs(l2_pdgId) == 13 & abs(l2_eta) < 2.4') 
print('number of correctly found HNLs using Chi2 method:\t%d'%(n_matchedHNLChi2))

n_matchedHNLDxy = tt.GetEntries('flag_matchedHNLDxy == 1 & abs(l1_pdgId) == 13 & abs(l1_eta) < 2.4 & abs(l2_pdgId) == 13 & abs(l2_eta) < 2.4')
print('number of correctly found HNLs using Dxy method:\t%d'%(n_matchedHNLDxy))

#n_matchedHNLChi2_and_recable = tt.GetEntries('flag_matchedHNLChi2 == 1 & flag_hnl_reconstructable ==1')
eff_Chi2_tot = float(n_matchedHNLChi2) / float(n_reconstructable)
# here it should be n_matchedHNL && n_reconstructable in the numerator
print('Reconstruction efficiency (min Chi2 method):\t\t%.1f%%'%(100*eff_Chi2_tot))

eff_Dxy_tot = float(n_matchedHNLDxy) / float(n_reconstructable)
# here it should be n_matchedHNL && n_reconstructable in the numerator
print('Reconstruction efficiency (max Dxy method):\t\t%.1f%%'%(100*eff_Dxy_tot))

pur_Chi2_tot = float(n_matchedHNLChi2) / float(n_dimuons)
print('Reconstruction purity (min Chi2 method):\t\t%.1f%%'%(100*pur_Chi2_tot))

pur_Dxy_tot = float(n_matchedHNLDxy) / float(n_dimuons)
print('Reconstruction purity (max Dxy method):\t\t\t%.1f%%'%(100*pur_Dxy_tot))

######################################### 
# initializing  histo's
######################################### 

print('Initializing histograms histos')

h_eff_mass_d3_Chi2_sMu_enum = rt.TH1F('h_eff_mass_d3_Chi2_sMu_enum','',10,0,10)
h_eff_mass_d3_Chi2_sMu_denom = rt.TH1F('h_eff_mass_d3_Chi2_sMu_denom','',10,0,10)
h_eff_mass_d3_Chi2_enum = rt.TH1F('h_eff_mass_d3_Chi2_enum','',10,0,10)
h_eff_mass_d3_Chi2_denom = rt.TH1F('h_eff_mass_d3_Chi2_denom','',10,0,10)

h_eff_mass_d3_Dxy_sMu_enum = rt.TH1F('h_eff_mass_d3_Dxy_sMu_enum','',10,0,10)
h_eff_mass_d3_Dxy_sMu_denom = rt.TH1F('h_eff_mass_d3_Dxy_sMu_denom','',10,0,10)
h_eff_mass_d3_Dxy_enum = rt.TH1F('h_eff_mass_d3_Dxy_enum','',10,0,10)
h_eff_mass_d3_Dxy_denom = rt.TH1F('h_eff_mass_d3_Dxy_denom','',10,0,10)

h_pur_mass_d3_Chi2_sMu_enum = rt.TH1F('h_pur_mass_d3_Chi2_sMu_enum','',10,0,10)
h_pur_mass_d3_Chi2_sMu_denom = rt.TH1F('h_pur_mass_d3_Chi2_sMu_denom','',10,0,10)
h_pur_mass_d3_Chi2_enum = rt.TH1F('h_pur_mass_d3_Chi2_enum','',10,0,10)
h_pur_mass_d3_Chi2_denom = rt.TH1F('h_pur_mass_d3_Chi2_denom','',10,0,10)

h_pur_mass_d3_Dxy_sMu_enum = rt.TH1F('h_pur_mass_d3_Dxy_sMu_enum','',10,0,10)
h_pur_mass_d3_Dxy_sMu_denom = rt.TH1F('h_pur_mass_d3_Dxy_sMu_denom','',10,0,10)
h_pur_mass_d3_Dxy_enum = rt.TH1F('h_pur_mass_d3_Dxy_enum','',10,0,10)
h_pur_mass_d3_Dxy_denom = rt.TH1F('h_pur_mass_d3_Dxy_denom','',10,0,10)


######################################### 
# Reconstruction Efficiency 
#########################################

print('Filling efficiency vs hn mass histos @ d3')

c_eff_mass_d3 = rt.TCanvas('c_eff_mass_d3', 'c_eff_mass_d3')

tt.Draw('hnl_hn_m >> h_eff_mass_d3_Chi2_sMu_enum','hnl_2d_disp < 350 & hnl_2d_disp > 120 & abs(l0_pdgId) == 11 & flag_matchedHNLChi2 == 1 & dMu1Chi2_reco == 1 & dMu2Chi2_reco == 1 & flag_hnl_reconstructable == 1 & abs(l1_pdgId) == 13 & abs(l1_eta) < 2.4 & abs(l2_pdgId) == 13 & abs(l2_eta) < 2.4')
tt.Draw('hnl_hn_m >> h_eff_mass_d3_Chi2_sMu_denom','hnl_2d_disp < 350 & hnl_2d_disp > 120 & abs(l0_pdgId) == 11 & flag_hnl_reconstructable == 1 & abs(l1_pdgId) == 13 & abs(l1_eta) < 2.4 & abs(l2_pdgId) == 13 & abs(l2_eta) < 2.4')
# probably we shouldn't use the dMu flags in the denominator here

tt.Draw('hnl_hn_m >> h_eff_mass_d3_Chi2_enum','hnl_2d_disp < 350 & hnl_2d_disp > 120 & abs(l0_pdgId) == 11 & flag_matchedHNLChi2 == 1 & flag_hnl_reconstructable == 1 & abs(l1_pdgId) == 13 & abs(l1_eta) < 2.4 & abs(l2_pdgId) == 13 & abs(l2_eta) < 2.4')
tt.Draw('hnl_hn_m >> h_eff_mass_d3_Chi2_denom','hnl_2d_disp < 350 & hnl_2d_disp > 120 & abs(l0_pdgId) == 11 & flag_hnl_reconstructable == 1 & abs(l1_pdgId) == 13 & abs(l1_eta) < 2.4 & abs(l2_pdgId) == 13 & abs(l2_eta) < 2.4')

tt.Draw('hnl_hn_m >> h_eff_mass_d3_Dxy_sMu_enum','hnl_2d_disp < 350 & hnl_2d_disp > 120 & abs(l0_pdgId) == 11 & flag_matchedHNLDxy == 1 & dMu1Dxy_reco == 1 & dMu2Dxy_reco == 1 & flag_hnl_reconstructable == 1 & abs(l1_pdgId) == 13 & abs(l1_eta) < 2.4 & abs(l2_pdgId) == 13 & abs(l2_eta) < 2.4')
tt.Draw('hnl_hn_m >> h_eff_mass_d3_Dxy_sMu_denom','hnl_2d_disp < 350 & hnl_2d_disp > 120 & abs(l0_pdgId) == 11 & flag_hnl_reconstructable == 1 & abs(l1_pdgId) == 13 & abs(l1_eta) < 2.4 & abs(l2_pdgId) == 13 & abs(l2_eta) < 2.4')
# probably we shouldn't use the dMu flags in the denominator here

tt.Draw('hnl_hn_m >> h_eff_mass_d3_Dxy_enum','hnl_2d_disp < 350 & hnl_2d_disp > 120 & abs(l0_pdgId) == 11 & flag_matchedHNLDxy == 1 & flag_hnl_reconstructable == 1 & abs(l1_pdgId) == 13 & abs(l1_eta) < 2.4 & abs(l2_pdgId) == 13 & abs(l2_eta) < 2.4')
tt.Draw('hnl_hn_m >> h_eff_mass_d3_Dxy_denom','hnl_2d_disp < 350 & hnl_2d_disp > 120 & abs(l0_pdgId) == 11 & flag_hnl_reconstructable == 1 & abs(l1_pdgId) == 13 & abs(l1_eta) < 2.4 & abs(l2_pdgId) == 13 & abs(l2_eta) < 2.4')

h_eff_mass_d3_Chi2_sMu_enum.Divide(h_eff_mass_d3_Chi2_sMu_denom)
h_eff_mass_d3_Chi2_sMu_enum.SetTitle(';HNL Mass ; HNL reconstruction efficiency')
h_eff_mass_d3_Chi2_sMu_enum.GetYaxis().SetRangeUser(0.,1.05)
h_eff_mass_d3_Chi2_sMu_enum.SetLineColor(rt.kBlack) ; h_eff_mass_d3_Chi2_sMu_enum.SetMarkerColor(rt.kBlack) 

h_eff_mass_d3_Chi2_enum.Divide(h_eff_mass_d3_Chi2_denom)
h_eff_mass_d3_Chi2_enum.SetTitle(';HNL Mass ; HNL reconstruction efficiency')
h_eff_mass_d3_Chi2_enum.GetYaxis().SetRangeUser(0.,1.05)
h_eff_mass_d3_Chi2_enum.SetLineColor(rt.kRed+2) ; h_eff_mass_d3_Chi2_enum.SetMarkerColor(rt.kRed+2) 

h_eff_mass_d3_Dxy_sMu_enum.Divide(h_eff_mass_d3_Dxy_sMu_denom)
h_eff_mass_d3_Dxy_sMu_enum.SetTitle(';HNL Mass ; HNL reconstruction efficiency')
h_eff_mass_d3_Dxy_sMu_enum.GetYaxis().SetRangeUser(0.,1.05)
h_eff_mass_d3_Dxy_sMu_enum.SetLineColor(rt.kBlue+2) ; h_eff_mass_d3_Dxy_sMu_enum.SetMarkerColor(rt.kBlue+2) 

h_eff_mass_d3_Dxy_enum.Divide(h_eff_mass_d3_Dxy_denom)
h_eff_mass_d3_Dxy_enum.SetTitle(';HNL Mass ; HNL reconstruction efficiency')
h_eff_mass_d3_Dxy_enum.GetYaxis().SetRangeUser(0.,1.05)
h_eff_mass_d3_Dxy_enum.SetLineColor(rt.kGreen+2) ; h_eff_mass_d3_Dxy_enum.SetMarkerColor(rt.kGreen+2) 

h_eff_mass_d3_Chi2_sMu_enum.Draw()
h_eff_mass_d3_Chi2_enum.Draw('same')
h_eff_mass_d3_Dxy_sMu_enum.Draw('same')
h_eff_mass_d3_Dxy_enum.Draw('same')

efleg = rt.TLegend(.4,.75,.8,.88)
efleg.AddEntry(h_eff_mass_d3_Chi2_sMu_enum, 'Chi2, sMu'            ,'EP')
efleg.AddEntry(h_eff_mass_d3_Chi2_enum, 'Chi2, sMu && dSAMu'            ,'EP')
efleg.AddEntry(h_eff_mass_d3_Dxy_sMu_enum, 'Dxy, sMu'            ,'EP')
efleg.AddEntry(h_eff_mass_d3_Dxy_enum, 'Dxy, sMu && dSAMu'            ,'EP')
efleg.Draw('apez same')

pf.showlumi('%d entries'%(h_eff_mass_d3_Dxy_enum.GetEntries()))
pf.showlogopreliminary('CMS', 'Simulation Preliminary')

c_eff_mass_d3.Modified()
c_eff_mass_d3.Update()
c_eff_mass_d3.SaveAs(output_dir + 'c_eff_mass_d3.pdf')
c_eff_mass_d3.SaveAs(output_dir + 'c_eff_mass_d3.root')

######################################### 
# Reconstruction Purity
#########################################

print('Filling purity vs hn mass histos @ d3')

c_pur_mass_d3 = rt.TCanvas('c_pur_mass_d3', 'c_pur_mass_d3')

tt.Draw('hnl_hn_m >> h_pur_mass_d3_Chi2_sMu_enum','hnl_2d_disp < 350 & hnl_2d_disp > 120 & abs(l0_pdgId) == 11 & flag_matchedHNLChi2 == 1 & dMu1Chi2_reco == 1 & dMu2Chi2_reco == 1 & abs(l1_pdgId) == 13 & abs(l1_eta) < 2.4 & abs(l2_pdgId) == 13 & abs(l2_eta) < 2.4')
tt.Draw('hnl_hn_m >> h_pur_mass_d3_Chi2_sMu_denom','hnl_2d_disp < 350 & hnl_2d_disp > 120 & abs(l0_pdgId) == 11 & n_dimuon > 0 & abs(l1_pdgId) == 13 & abs(l1_eta) < 2.4 & abs(l2_pdgId) == 13 & abs(l2_eta) < 2.4')
# probably we shouldn't use the dMu flags in the denominator here

tt.Draw('hnl_hn_m >> h_pur_mass_d3_Chi2_enum','hnl_2d_disp < 350 & hnl_2d_disp > 120 & abs(l0_pdgId) == 11 & flag_matchedHNLChi2 == 1 & abs(l1_pdgId) == 13 & abs(l1_eta) < 2.4 & abs(l2_pdgId) == 13 & abs(l2_eta) < 2.4')
tt.Draw('hnl_hn_m >> h_pur_mass_d3_Chi2_denom','hnl_2d_disp < 350 & hnl_2d_disp > 120 & abs(l0_pdgId) == 11 & n_dimuon > 0 & abs(l1_pdgId) == 13 & abs(l1_eta) < 2.4 & abs(l2_pdgId) == 13 & abs(l2_eta) < 2.4')

tt.Draw('hnl_hn_m >> h_pur_mass_d3_Dxy_sMu_enum','hnl_2d_disp < 350 & hnl_2d_disp > 120 & abs(l0_pdgId) == 11 & flag_matchedHNLDxy == 1 & dMu1Dxy_reco == 1 & dMu2Dxy_reco == 1 & abs(l1_pdgId) == 13 & abs(l1_eta) < 2.4 & abs(l2_pdgId) == 13 & abs(l2_eta) < 2.4')
tt.Draw('hnl_hn_m >> h_pur_mass_d3_Dxy_sMu_denom','hnl_2d_disp < 350 & hnl_2d_disp > 120 & abs(l0_pdgId) == 11 & n_dimuon > 0 & abs(l1_pdgId) == 13 & abs(l1_eta) < 2.4 & abs(l2_pdgId) == 13 & abs(l2_eta) < 2.4')
# probably we shouldn't use the dMu flags in the denominator here

tt.Draw('hnl_hn_m >> h_pur_mass_d3_Dxy_enum','hnl_2d_disp < 350 & hnl_2d_disp > 120 & abs(l0_pdgId) == 11 & flag_matchedHNLDxy == 1 & abs(l1_pdgId) == 13 & abs(l1_eta) < 2.4 & abs(l2_pdgId) == 13 & abs(l2_eta) < 2.4')
tt.Draw('hnl_hn_m >> h_pur_mass_d3_Dxy_denom','hnl_2d_disp < 350 & hnl_2d_disp > 120 & abs(l0_pdgId) == 11 & n_dimuon > 0 & abs(l1_pdgId) == 13 & abs(l1_eta) < 2.4 & abs(l2_pdgId) == 13 & abs(l2_eta) < 2.4')

h_pur_mass_d3_Chi2_sMu_enum.Divide(h_pur_mass_d3_Chi2_sMu_denom)
h_pur_mass_d3_Chi2_sMu_enum.SetTitle(';HNL Mass ; HNL reconstruction purity')
h_pur_mass_d3_Chi2_sMu_enum.GetYaxis().SetRangeUser(0.,1.05)
h_pur_mass_d3_Chi2_sMu_enum.SetLineColor(rt.kBlack) ; h_pur_mass_d3_Chi2_sMu_enum.SetMarkerColor(rt.kBlack) 

h_pur_mass_d3_Chi2_enum.Divide(h_pur_mass_d3_Chi2_denom)
h_pur_mass_d3_Chi2_enum.SetTitle(';HNL Mass ; HNL reconstruction purity')
h_pur_mass_d3_Chi2_enum.GetYaxis().SetRangeUser(0.,1.05)
h_pur_mass_d3_Chi2_enum.SetLineColor(rt.kRed+2) ; h_pur_mass_d3_Chi2_enum.SetMarkerColor(rt.kRed+2) 

h_pur_mass_d3_Dxy_sMu_enum.Divide(h_pur_mass_d3_Dxy_sMu_denom)
h_pur_mass_d3_Dxy_sMu_enum.SetTitle(';HNL Mass ; HNL reconstruction purity')
h_pur_mass_d3_Dxy_sMu_enum.GetYaxis().SetRangeUser(0.,1.05)
h_pur_mass_d3_Dxy_sMu_enum.SetLineColor(rt.kBlue+2) ; h_pur_mass_d3_Dxy_sMu_enum.SetMarkerColor(rt.kBlue+2) 

h_pur_mass_d3_Dxy_enum.Divide(h_pur_mass_d3_Dxy_denom)
h_pur_mass_d3_Dxy_enum.SetTitle(';HNL Mass ; HNL reconstruction purity')
h_pur_mass_d3_Dxy_enum.GetYaxis().SetRangeUser(0.,1.05)
h_pur_mass_d3_Dxy_enum.SetLineColor(rt.kGreen+2) ; h_pur_mass_d3_Dxy_enum.SetMarkerColor(rt.kGreen+2) 

h_pur_mass_d3_Chi2_sMu_enum.Draw()
h_pur_mass_d3_Chi2_enum.Draw('same')
h_pur_mass_d3_Dxy_sMu_enum.Draw('same')
h_pur_mass_d3_Dxy_enum.Draw('same')

puleg = rt.TLegend(.4,.75,.8,.88)
puleg.AddEntry(h_pur_mass_d3_Chi2_sMu_enum, 'Chi2, sMu'            ,'EP')
puleg.AddEntry(h_pur_mass_d3_Chi2_enum, 'Chi2, sMu && dSAMu'            ,'EP')
puleg.AddEntry(h_pur_mass_d3_Dxy_sMu_enum, 'Dxy, sMu'            ,'EP')
puleg.AddEntry(h_pur_mass_d3_Dxy_enum, 'Dxy, sMu && dSAMu'            ,'EP')
puleg.Draw('apez same')

pf.showlumi('%d entries'%(h_pur_mass_d3_Dxy_enum.GetEntries()))
pf.showlogopreliminary('CMS','Simulation Preliminary')

c_pur_mass_d3.Modified()
c_pur_mass_d3.Update()
c_pur_mass_d3.SaveAs(output_dir + 'c_pur_mass_d3.pdf')
c_pur_mass_d3.SaveAs(output_dir + 'c_pur_mass_d3.root')

fout.Write()
#fout.Close()
















