import ROOT as rt
import plotfactory as pf
import numpy as np
import sys
import ntup_dir as nt

from os.path import normpath, basename

pf.setpfstyle()
output_dir = '/afs/cern.ch/work/v/vstampf/plots/candidates/gentuple/' 

ntdr = basename(normpath(nt.getntupdir()))

fout = rt.TFile(output_dir+'histosvtxresolu_'+ntdr+'.root', 'recreate')

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
# initializing  histo's
######################################### 

c_vtx_reldiff = rt.TCanvas('vtx_reldiff', 'vtx_reldiff')
c_vtx_diff = rt.TCanvas('vtx_diff', 'vtx_diff')

print('Initializing histograms')

diffdxybins = np.arange(-40.,300,25)
reldiffdxybins = np.arange(-3.,1.5,0.25)
dxybins = np.logspace(-1,2.78,15)

dxy_diff = rt.TH2F("dxy_diff","dxy_diff",len(dxybins)-1,dxybins,len(diffdxybins)-1,diffdxybins)
dxy_reldiff = rt.TH2F("dxy_reldiff","dxy_reldiff",len(dxybins)-1,dxybins,len(reldiffdxybins)-1,reldiffdxybins)

######################################### 
# Filling Histograms 
#########################################

print('Filling vertex resolution histograms')

tt.Draw("hnl_2d_disp - hnl_2d_reco_disp:hnl_2d_disp >> dxy_diff", "abs(l2_pdgId) == 13 & abs(l1_pdgId) == 13 & is_in_acc == 1 & hnl_2d_reco_disp > -90")

tt.Draw("(hnl_2d_disp - hnl_2d_reco_disp)/hnl_2d_disp:hnl_2d_disp >> dxy_reldiff", "abs(l2_pdgId) == 13 & abs(l1_pdgId) == 13 & is_in_acc == 1 & hnl_2d_reco_disp > -90")

c_vtx_diff.cd()
dxy_diff.Draw('colztext')

c_vtx_reldiff.cd()
dxy_reldiff.Draw('colztext')

hupd8lst = [dxy_diff,dxy_reldiff]

for hh in hupd8lst:
   hh.GetXaxis().SetTitle('HNL 2D displacement')
   hh.GetZaxis().SetTitle('Events')
   hh.GetXaxis().SetTitleOffset(1.2)
   hh.GetYaxis().SetTitleOffset(1.4)
   hh.GetZaxis().SetTitleOffset(1.4)
   hh.GetXaxis().SetRangeUser(0.,605)
#   hh.SetAxisRange(1,1e5,"Z")
for hh in [dxy_diff,dxy_diff]:
   hh.GetYaxis().SetTitle('vtx_{xy,gen}-vtx_{xy,reco}')
   hh.GetYaxis().SetRangeUser(-40.,305)

for hh in [dxy_reldiff,dxy_reldiff]:
   hh.GetYaxis().SetTitle('#frac{vtx_{xy,gen}-vtx_{xy,reco}}{vtx_{xy,gen}}')
   hh.GetYaxis().SetRangeUser(-3.,1.5)

print('Updating and saving pads')
for cc in [c_vtx_diff,c_vtx_reldiff]:
   cc.cd()
#   cc.SetLogz()
   cc.SetLogx()
   pf.showlogoprelimsim('CMS')
#   rt.gStyle.SetOptStat(0)
   cc.Modified()
   cc.Update()
   cc.SaveAs(output_dir+cc.GetTitle()+'_'+ntdr+'.root')
   cc.SaveAs(output_dir+cc.GetTitle()+'_'+ntdr+'.pdf')

fout.Write()

