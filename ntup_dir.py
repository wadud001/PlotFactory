#Set the location where all ntuples are stored. Adapt the location to your path
def getntupdir():
    # ntup_dir = '/afs/cern.ch/user/d/dezhu/workspace/public/ntuples/201804_HNL/' # location on lxplus
    # ntup_dir = '/afs/cern.ch/user/d/dezhu/workspace/public/ntuples/201805_HNL/' # location on lxplus
    # ntup_dir = '/eos/user/m/manzoni/HNL/gentuple_050318_v4/' # first version from riccardo
    # ntup_dir = '/Users/dehuazhu/Dropbox/PhD/5_Projects/analysis/180419_NTuples/201804_HN3L/' # location on local machine
<<<<<<< HEAD
    ntup_dir = '/eos/user/d/dezhu/HNL/ntuple/20180608_HNLreco/ntuple/' # global
    # ntup_dir = '/eos/user/v/vstampf/ntuple/' # eos 
    # ntup_dir = '/afs/cern.ch/user/v/vstampf/CMSSW_8_0_30/src/CMGTools/HNL/cfg/cherry1/' # around 700k evts cherry1
    # ntup_dir = '/eos/user/v/vstampf/ntupleN/' #full statistics modulo nonexistent vector<reco::Track> dSAmu
    # ntup_dir = '/eos/user/v/vstampf/ntuplesfull/' # more evts, but not full and no idea what's inside
    # ntup_dir = '/afs/cern.ch/work/v/vstampf/ntuples/useable_full/' # latest (6/14) ntuples
    # ntup_dir = '/afs/cern.ch/work/v/vstampf/ntuples/gen/' # latest (6/18) ntuples
=======
    ntup_dir = '/eos/user/d/dezhu/HNL/ntuple/20180608_HNLreco/ntuple/' # location on local machine
    # ntup_dir = '/eos/user/v/vstampf/ntuple/' # eos 
    # ntup_dir = '/afs/cern.ch/user/v/vstampf/CMSSW_8_0_30/src/CMGTools/HNL/cfg/cherry1/' # around 700k evts cherry1
    # ntup_dir = '/eos/user/v/vstampf/ntupleN/' #full statistics modulo nonexistent vector<reco::Track> dSAmu
    #ntup_dir = '/eos/user/v/vstampf/ntuplesfull/' # more evts, but not full and no idea what's inside
    # ntup_dir = '/afs/cern.ch/work/v/vstampf/ntuples/useable_full/' # latest (6/14) ntuples
>>>>>>> 6e0e6ac729f7993453cc506d5ae1e797ee836189
    return ntup_dir
