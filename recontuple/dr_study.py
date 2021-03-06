import ROOT as rt
import numpy as np
import plotfactory as pf
import sys
from pdb import set_trace
from os.path import normpath, basename
####################################################################################################
indir = '/afs/cern.ch/work/v/vstampf/public/ntuples/dr_cut/'
ver = 'HN3L_M_2p5_V_0p0173205080757_e_onshell/'
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
b_DR = np.arange(0.,0.5,0.025)
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
h_dr_smu = rt.TH1F('dr_smu','dr_smu',len(b_DR)-1,b_DR)
h_dr_smu_l1 = rt.TH1F('dr_smu_l1','dr_smu_l1',len(b_DR)-1,b_DR)
h_dr_smu_l2 = rt.TH1F('dr_smu_l2','dr_smu_l2',len(b_DR)-1,b_DR)
####################################################################################################
h_dr_dsmu = rt.TH1F('dr_dsmu','dr_dsmu',len(b_DR)-1,b_DR)
h_dr_dsmu_l1 = rt.TH1F('dr_dsmu_l1','dr_dsmu_l1',len(b_DR)-1,b_DR)
h_dr_dsmu_l2 = rt.TH1F('dr_dsmu_l2','dr_dsmu_l2',len(b_DR)-1,b_DR)
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
t.Draw('l1_smatch_dr >> dr_smu_l1', 'is_in_acc > 0 & l1_smatch_dr > -1 & abs(l1_pdgId) == 13')
t.Draw('l2_smatch_dr >> dr_smu_l2', 'is_in_acc > 0 & l2_smatch_dr > -1 & abs(l2_pdgId) == 13')
####################################################################################################
t.Draw('l1_dsmatch_dr >> dr_dsmu_l1', 'is_in_acc > 0 & l1_dsmatch_dr > -1 & abs(l1_pdgId) == 13')
t.Draw('l2_dsmatch_dr >> dr_dsmu_l2', 'is_in_acc > 0 & l2_dsmatch_dr > -1 & abs(l2_pdgId) == 13')
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
h_dr_smu.Add(h_dr_smu_l1)
h_dr_smu.Add(h_dr_smu_l2)
####################################################################################################
h_dr_dsmu.Add(h_dr_dsmu_l1)
h_dr_dsmu.Add(h_dr_dsmu_l2)
####################################################################################################
####################################################################################################
hlist_d = [h_dr_recos,h_dr_recos_bar,h_dr_recos_cap,h_deta_recos,h_dphi_recos]
hlist_r = [h_dr_smu,h_dr_dsmu]
hlist = hlist_d + hlist_r
####################################################################################################
####################################################################################################
for h in hlist:
    h.GetYaxis().SetTitle('events')
    h.SetMarkerColor(rt.kBlue+2)
    h.SetMarkerSize(1)
####################################################################################################
for h in hlist_d:
    h.GetXaxis().SetTitle('#Deltar(s#mu,dSA#mu)')
####################################################################################################
h_dr_smu.GetXaxis().SetTitle('#Deltar(reco,gen)')
h_dr_dsmu.GetXaxis().SetTitle('#Deltar(reco,gen)')
h_dr_dsmu.SetMarkerColor(rt.kRed+2)
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
c_dr_gen_reco = rt.TCanvas('gen_reco','gen_reco')
####################################################################################################
####################################################################################################
clist = [c_dr_recos,c_dr_recos_cap,c_dr_recos_bar,c_deta_recos,c_dphi_recos,c_dr_gen_reco]
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
c_dr_gen_reco.cd()
h_dr_smu.Draw()
h_dr_dsmu.Draw('same')
c_dr_gen_reco.BuildLegend()
pf.showlogoprelimsim('CMS')
c_dr_gen_reco.Modified()
c_dr_gen_reco.Update()
c_dr_gen_reco.SaveAs(outdir+c_dr_gen_reco.GetTitle()+'_'+ntdr+'.root')
c_dr_gen_reco.SaveAs(outdir+c_dr_gen_reco.GetTitle()+'_'+ntdr+'.png')
####################################################################################################
####################################################################################################
for c in clist:
    c.cd()
    pf.showlogoprelimsim('CMS')
#    rt.gStyle.SetOptStat()
    c.Modified()
    c.Update()
#    c.SaveAs(outdir+c.GetTitle()+'_'+ntdr+'.root')
#    c.SaveAs(outdir+c.GetTitle()+'_'+ntdr+'.png')
