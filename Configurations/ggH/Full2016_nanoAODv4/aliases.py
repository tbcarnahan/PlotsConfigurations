#aliases = {}

mc = [skey for skey in samples if skey not in ('Fake_em', 'Fake_me', 'DATA')]

bAlgo = 'DeepB'
bWP = '0.2217'

aliases['bVeto'] = {
'expr': '(Sum$(CleanJet_pt > 20. && abs(CleanJet_eta)<2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.2217) == 0)'
}

aliases['btag0'] = {
'expr': '( Alt$(CleanJet_pt[0],0)<30  \
           && Sum$(CleanJet_pt > 20. && abs(CleanJet_eta)<2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.2217)>0 \
         )'
}

aliases['btag1'] = {
'expr': '(    Alt$(CleanJet_pt[0],0)>30 && Alt$(abs(CleanJet_eta[0]),99)<2.5\
           && Alt$(CleanJet_pt[1],0)<30 \
           && Alt$(Jet_btagDeepB[CleanJet_jetIdx[0]], 0) > 0.2217 )'
}

aliases['btag2'] = {
'expr': '(    Alt$(CleanJet_pt[0],0)>30 \
           && Alt$(CleanJet_pt[1],0)>30 \
           && ( ( Alt$(abs(CleanJet_eta[0]),99)<2.5 && Alt$(Jet_btagDeepB[CleanJet_jetIdx[0]],0) > 0.2217 ) \
             || ( Alt$(abs(CleanJet_eta[1]),99)<2.5 && Alt$(Jet_btagDeepB[CleanJet_jetIdx[1]],0) > 0.2217 ) ) \
         )' 
}

# Temporary patch for BTV postprocessor bug (no SF for eta < 0, <= 102X_nAODv5_Full2018v5)

btagSFSource = '%s/src/PhysicsTools/NanoAODTools/data/btagSF/DeepCSV_2016LegacySF_V1.csv' % os.getenv('CMSSW_BASE')

aliases['Jet_btagSF_shapeFix'] = {
    'linesToAdd': [
        'gSystem->Load("libCondFormatsBTauObjects.so");',
        'gSystem->Load("libCondToolsBTau.so");',
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
        '.L %s/src/PlotsConfigurations/Configurations/btagsfpatch.cc+' % os.getenv('CMSSW_BASE')
    ],
    'class': 'BtagSF',
    'args': (btagSFSource,),
    'samples': mc
}

aliases['bVetoSF'] = {
#'expr': '( TMath::Exp(Sum$( TMath::Log( (CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shape[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5) ) ) ) )',
'expr': '( TMath::Exp(Sum$( TMath::Log( (CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shapeFix[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5) ) ) ) )',
'samples': mc
}


aliases['btag0SF'] = {
#'expr': '( TMath::Exp(Sum$( TMath::Log( (CleanJet_pt>20 && CleanJet_pt<30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shape[CleanJet_jetIdx]+1*(CleanJet_pt<20 || CleanJet_pt>30 || abs(CleanJet_eta)>2.5) ) ) ) )',
'expr': '( TMath::Exp(Sum$( TMath::Log( (CleanJet_pt>20 && CleanJet_pt<30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shapeFix[CleanJet_jetIdx]+1*(CleanJet_pt<20 || CleanJet_pt>30 || abs(CleanJet_eta)>2.5) ) ) ) )',
'samples': mc
}

aliases['btag1SF'] = {
#'expr': '( ( Alt$(CleanJet_pt[0], 0)>30 && Alt$(abs(CleanJet_eta[0]),99)<2.5 )*( Alt$(Jet_btagSF_shape[CleanJet_jetIdx[0]], 1) ) + ( Alt$(CleanJet_pt[0], 0)<30 || Alt$(abs(CleanJet_eta[0]),99)>2.5 ) )',
'expr': '( ( Alt$(CleanJet_pt[0], 0)>30 && Alt$(abs(CleanJet_eta[0]),99)<2.5 )*( Alt$(Jet_btagSF_shapeFix[CleanJet_jetIdx[0]], 1) ) + ( Alt$(CleanJet_pt[0], 0)<30 || Alt$(abs(CleanJet_eta[0]),99)>2.5 ) )',
'samples': mc
}

aliases['btag2SF'] = {
#'expr': '( ( ( Alt$(CleanJet_pt[0], 0)>30 && Alt$(abs(CleanJet_eta[0]),99)<2.5 )*( Alt$(Jet_btagSF_shape[CleanJet_jetIdx[0]], 1) ) + ( Alt$(CleanJet_pt[0], 0)<30 || Alt$(abs(CleanJet_eta[0]),99)>2.5 ) )* \
#           ( ( Alt$(CleanJet_pt[1], 0)>30 && Alt$(abs(CleanJet_eta[1]),99)<2.5 )*( Alt$(Jet_btagSF_shape[CleanJet_jetIdx[1]], 1) ) + ( Alt$(CleanJet_pt[1], 0)<30 || Alt$(abs(CleanJet_eta[1]),99)>2.5 ) ) )\
#        ',
'expr': '( ( ( Alt$(CleanJet_pt[0], 0)>30 && Alt$(abs(CleanJet_eta[0]),99)<2.5 )*( Alt$(Jet_btagSF_shapeFix[CleanJet_jetIdx[0]], 1) ) + ( Alt$(CleanJet_pt[0], 0)<30 || Alt$(abs(CleanJet_eta[0]),99)>2.5 ) )* \
           ( ( Alt$(CleanJet_pt[1], 0)>30 && Alt$(abs(CleanJet_eta[1]),99)<2.5 )*( Alt$(Jet_btagSF_shapeFix[CleanJet_jetIdx[1]], 1) ) + ( Alt$(CleanJet_pt[1], 0)<30 || Alt$(abs(CleanJet_eta[1]),99)>2.5 ) ) )\
        ',
'samples': mc
}

aliases['btagSF'] = {
'expr': '( bVetoSF*bVeto + btag0SF*btag0 + btag1SF*btag1 + btag2SF*btag2 + ( (!bVeto) && (!btag0) && (!btag1) && (!btag2) ) )',
'samples': mc
}


systs = ['jes','lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']

for s in systs:
    aliases['Jet_btagSF_shapeFix_up_%s' % s] = {
        'class': 'BtagSF',
        'args': (btagSFSource, 'up_' + s),
        'samples': mc
    }
    aliases['Jet_btagSF_shapeFix_down_%s' % s] = {
        'class': 'BtagSF',
        'args': (btagSFSource, 'down_' + s),
        'samples': mc
    }

    #aliases['btagSF'+s+'up'] = { 'expr': '( bVeto*'+aliases['bVetoSF']['expr'].replace('shape','shape_up_'+s)+'+btag0*'+aliases['btag0SF']['expr'].replace('shape','shape_up_'+s)+'+btag1*'+aliases['btag1SF']['expr'].replace('shape','shape_up_'+s)+'+btag2*'+aliases['btag2SF']['expr'].replace('shape','shape_up_'+s)+' + ( (!bVeto) && (!btag0) && (!btag1) && (!btag2) ) )', 'samples':mc  }
    aliases['btagSF'+s+'up'] = { 'expr': '( bVeto*'+aliases['bVetoSF']['expr'].replace('shapeFix','shapeFix_up_'+s)+'+btag0*'+aliases['btag0SF']['expr'].replace('shapeFix','shapeFix_up_'+s)+'+btag1*'+aliases['btag1SF']['expr'].replace('shapeFix','shapeFix_up_'+s)+'+btag2*'+aliases['btag2SF']['expr'].replace('shapeFix','shapeFix_up_'+s)+' + ( (!bVeto) && (!btag0) && (!btag1) && (!btag2) ) )', 'samples':mc  }
    #aliases['btagSF'+s+'down'] = { 'expr': '( bVeto*'+aliases['bVetoSF']['expr'].replace('shape','shape_down_'+s)+'+btag0*'+aliases['btag0SF']['expr'].replace('shape','shape_down_'+s)+'+btag1*'+aliases['btag1SF']['expr'].replace('shape','shape_down_'+s)+'+btag2*'+aliases['btag2SF']['expr'].replace('shape','shape_down_'+s)+' + ( (!bVeto) && (!btag0) && (!btag1) && (!btag2) ) )', 'samples':mc  }
    aliases['btagSF'+s+'down'] = { 'expr': '( bVeto*'+aliases['bVetoSF']['expr'].replace('shapeFix','shapeFix_down_'+s)+'+btag0*'+aliases['btag0SF']['expr'].replace('shapeFix','shapeFix_down_'+s)+'+btag1*'+aliases['btag1SF']['expr'].replace('shapeFix','shapeFix_down_'+s)+'+btag2*'+aliases['btag2SF']['expr'].replace('shapeFix','shapeFix_down_'+s)+' + ( (!bVeto) && (!btag0) && (!btag1) && (!btag2) ) )', 'samples':mc  }

