import ROOT as rt
import numpy as np
import plotfactory as pf
import sys
from pdb import set_trace
from os.path import normpath, basename
####################################################################################################
indir = '/afs/cern.ch/work/v/vstampf/public/ntuples/dr_study/'
ver = 'HN3L_M_2p5_V_0p0173205080757_e_onshell_3/'
outdir = '/afs/cern.ch/work/v/vstampf/plots/recontuple/'
####################################################################################################
ntdr = basename(normpath(ver))
####################################################################################################
fin = rt.TFile(indir+ver+'HNLTreeProducer/tree.root')
####################################################################################################
t = fin.Get('tree')
####################################################################################################
pf.setpfstyle()
####################################################################################################
####################################################################################################
####################################################################################################
b_dr = np.arange(0.,0.18,0.005)
b_deta = np.arange(-0.18,0.18,0.005)
b_dphi = np.arange(-0.18,0.18,0.005)
####################################################################################################
####################################################################################################
####################################################################################################
h_dr_recos = rt.TH1F('dr_recos','dr_recos',len(b_dr)-1,b_dr)
h_dr_recos_l1 = rt.TH1F('dr_recos_l1','dr_recos_l1',len(b_dr)-1,b_dr)
h_dr_recos_l2 = rt.TH1F('dr_recos_l2','dr_recos_l2',len(b_dr)-1,b_dr)
####################################################################################################
h_dr_recos_bar = rt.TH1F('dr_recos_bar','dr_recos_bar',len(b_dr)-1,b_dr)
h_dr_recos_l1_bar = rt.TH1F('dr_recos_l1_bar','dr_recos_l1_bar',len(b_dr)-1,b_dr)
h_dr_recos_l2_bar = rt.TH1F('dr_recos_l2_bar','dr_recos_l2_bar',len(b_dr)-1,b_dr)
####################################################################################################
h_dr_recos_cap = rt.TH1F('dr_recos_cap','dr_recos_cap',len(b_dr)-1,b_dr)
h_dr_recos_l1_cap = rt.TH1F('dr_recos_l1_cap','dr_recos_l1_cap',len(b_dr)-1,b_dr)
h_dr_recos_l2_cap = rt.TH1F('dr_recos_l2_cap','dr_recos_l2_cap',len(b_dr)-1,b_dr)
####################################################################################################
####################################################################################################
h_deta_recos = rt.TH1F('deta_recos','deta_recos',len(b_deta)-1,b_deta)
h_deta_recos_l1 = rt.TH1F('deta_recos_l1','deta_recos_l1',len(b_deta)-1,b_deta)
h_deta_recos_l2 = rt.TH1F('deta_recos_l2','deta_recos_l2',len(b_deta)-1,b_deta)
####################################################################################################
####################################################################################################
h_dphi_recos = rt.TH1F('dphi_recos','dphi_recos',len(b_dphi)-1,b_dphi)
h_dphi_recos_l1 = rt.TH1F('dphi_recos_l1','dphi_recos_l1',len(b_dphi)-1,b_dphi)
h_dphi_recos_l2 = rt.TH1F('dphi_recos_l2','dphi_recos_l2',len(b_dphi)-1,b_dphi)
####################################################################################################
####################################################################################################
####################################################################################################
t.Draw('dr_recos_l1 >> dr_recos_l1', 'is_in_acc > 0 & dr_recos_l1 > -1 & abs(l1_pdgId) == 13')
t.Draw('dr_recos_l2 >> dr_recos_l2', 'is_in_acc > 0 & dr_recos_l2 > -1 & abs(l2_pdgId) == 13')
####################################################################################################
t.Draw('dr_recos_l1 >> dr_recos_l1_bar', 'is_in_acc > 0 & dr_recos_l1 > -1 & abs(l1_pdgId) == 13 & abs(l1_eta) < 0.8')
t.Draw('dr_recos_l2 >> dr_recos_l2_bar', 'is_in_acc > 0 & dr_recos_l2 > -1 & abs(l2_pdgId) == 13 & abs(l2_eta) < 0.8')
####################################################################################################
t.Draw('dr_recos_l1 >> dr_recos_l1_cap', 'is_in_acc > 0 & dr_recos_l1 > -1 & abs(l1_pdgId) == 13 & abs(l1_eta) > 1.2')
t.Draw('dr_recos_l2 >> dr_recos_l2_cap', 'is_in_acc > 0 & dr_recos_l2 > -1 & abs(l2_pdgId) == 13 & abs(l2_eta) > 1.2')
####################################################################################################
####################################################################################################
t.Draw('deta_recos_l1 >> deta_recos_l1', 'is_in_acc > 0 & deta_recos_l1 > -1 & abs(l1_pdgId) == 13')
t.Draw('deta_recos_l2 >> deta_recos_l2', 'is_in_acc > 0 & deta_recos_l2 > -1 & abs(l2_pdgId) == 13')
####################################################################################################
####################################################################################################
t.Draw('dphi_recos_l1 >> dphi_recos_l1', 'is_in_acc > 0 & dphi_recos_l1 > -1 & abs(l1_pdgId) == 13')
t.Draw('dphi_recos_l2 >> dphi_recos_l2', 'is_in_acc > 0 & dphi_recos_l2 > -1 & abs(l2_pdgId) == 13')
####################################################################################################
####################################################################################################
####################################################################################################
h_dr_recos.Add(h_dr_recos_l1)
h_dr_recos.Add(h_dr_recos_l2)
####################################################################################################
h_dr_recos_bar.Add(h_dr_recos_l1_bar)
h_dr_recos_bar.Add(h_dr_recos_l2_bar)
####################################################################################################
h_dr_recos_cap.Add(h_dr_recos_l1_cap)
h_dr_recos_cap.Add(h_dr_recos_l2_cap)
####################################################################################################
####################################################################################################
h_deta_recos.Add(h_deta_recos_l1)
h_deta_recos.Add(h_deta_recos_l2)
####################################################################################################
####################################################################################################
h_dphi_recos.Add(h_dphi_recos_l1)
h_dphi_recos.Add(h_dphi_recos_l2)
####################################################################################################
####################################################################################################
hlist = [h_dr_recos,h_dr_recos_bar,h_dr_recos_cap,h_deta_recos,h_dphi_recos]
####################################################################################################
####################################################################################################
for h in hlist:
    h.GetYaxis().SetTitle('events')
    h.GetXaxis().SetTitle('#Deltar(s#mu,dSA#mu)')
    h.SetMarkerColor(rt.kBlue+2)
####################################################################################################
####################################################################################################
    h_deta_recos.GetXaxis().SetTitle('#Delta#eta(s#mu,dSA#mu)')
    h_dphi_recos.GetXaxis().SetTitle('#Delta#phi(s#mu,dSA#mu)')
####################################################################################################
####################################################################################################
####################################################################################################
c_dr_recos = rt.TCanvas('dr_recos','dr_recos')
c_dr_recos_bar = rt.TCanvas('dr_recos_bar','dr_recos_bar')
c_dr_recos_cap = rt.TCanvas('dr_recos_cap','dr_recos_cap')
c_deta_recos = rt.TCanvas('deta_recos','deta_recos')
c_dphi_recos = rt.TCanvas('dphi_recos','dphi_recos')
####################################################################################################
####################################################################################################
clist = [c_dr_recos,c_dr_recos_cap,c_dr_recos_bar,c_deta_recos,c_dphi_recos]
####################################################################################################
####################################################################################################
c_dr_recos.cd()
h_dr_recos.Draw()
####################################################################################################
c_dr_recos_bar.cd()
h_dr_recos_bar.Draw()
####################################################################################################
c_dr_recos_cap.cd()
h_dr_recos_cap.Draw()
####################################################################################################
####################################################################################################
c_dr_recos.cd()
h_dr_recos.Draw()
####################################################################################################
####################################################################################################
c_dphi_recos.cd()
h_dphi_recos.Draw()
####################################################################################################
####################################################################################################
c_deta_recos.cd()
h_deta_recos.Draw()
####################################################################################################
####################################################################################################
for c in clist:
    c.cd()
    pf.showlogoprelimsim('CMS')
#    rt.gStyle.SetOptStat()
    c.Modified()
    c.Update()
    c.SaveAs(outdir+c.GetTitle()+'_'+ntdr+'.root')
    c.SaveAs(outdir+c.GetTitle()+'_'+ntdr+'.png')