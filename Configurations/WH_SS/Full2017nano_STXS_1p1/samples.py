import os
import subprocess
import string
from LatinoAnalysis.Tools.commonTools import *

samples={}

skim=''
##############################################
###### Tree Directory according to site ######
##############################################

SITE=os.uname()[1]
xrootdPath=''
if    'iihe' in SITE :
  xrootdPath  = 'dcap://maite.iihe.ac.be/'
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015/'
elif  'cern' in SITE :
  #xrootdPath='root://eoscms.cern.ch/'
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'

def makeMCDirectory(var=''):
  if var:
    #nAODv5_SigOnly
    directory = treeBaseDir+'Fall2017_102X_XXXX_Full2017v5/MCl1loose2017v5__MCCorr2017v5__l2loose__l2tightOR2017v5/'+skim
    return directory.replace('XXXX',var)
  else:
    directory = treeBaseDir+'Fall2017_102X_nAODv4_Full2017v5/MCl1loose2017v5__MCCorr2017v5__l2loose__l2tightOR2017v5/'+skim
    return directory


################################################
############ NUMBER OF LEPTONS #################
################################################

Nlep='2'
#Nlep='3'
#Nlep='4'

################################################
############### Lepton WP ######################
################################################


#eleWP='mvaFall17V1Iso_WP90'
#eleWP='mvaFall17V2Iso_WP90'
eleWP='mvaFall17V1Iso_WP90_SS'
muWP='cut_Tight_HWWW'


LepWPCut        = 'LepCut'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP
LepWPweight     = 'LepSF'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP


################################################
############ BASIC MC WEIGHTS ##################
################################################

XSWeight      = 'XSWeight'
SFweight      = 'SFweight'+Nlep+'l*'+LepWPweight+'*'+LepWPCut+'*PrefireWeight'
GenLepMatch   = 'GenLepMatch'+Nlep+'l'


################################################
############## FAKE WEIGHTS ####################
################################################

if Nlep == '2' :
  fakeW = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP
else:
  fakeW = 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l'


################################################
############### B-Tag  WP ######################
################################################

#FIXME b-tagging to be optimized
# Definitions in aliases.py


SFweight += '*btagSF'

################################################
############   MET  FILTERS  ###################
################################################

METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'

################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
            ['B','Run2017B-Nano14Dec2018-v1'] ,
            ['C','Run2017C-Nano14Dec2018-v1'] ,
            ['D','Run2017D-Nano14Dec2018-v1'] ,
            ['E','Run2017E-Nano14Dec2018-v1'] ,
            ['F','Run2017F-Nano14Dec2018-v1']
          ]


DataSets = ['MuonEG','DoubleMuon','SingleMuon','DoubleEG','SingleElectron']

DataTrig = {
            'MuonEG'         : 'Trigger_ElMu' ,
            'DoubleMuon'     : '!Trigger_ElMu && Trigger_dblMu' ,
            'SingleMuon'     : '!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu' ,
            'DoubleEG'       : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && Trigger_dblEl' ,
            'SingleElectron' : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && !Trigger_dblEl && Trigger_sngEl' ,
           }


###########################################
#############  BACKGROUNDS  ###############
###########################################

############ DY ############

ptllDYW_NLO = '((0.623108 + 0.0722934*gen_ptll - 0.00364918*gen_ptll*gen_ptll + 6.97227e-05*gen_ptll*gen_ptll*gen_ptll - 4.52903e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll<45)*(gen_ptll>0) + 1*(gen_ptll>=45))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'

samples['DY'] = {    'name'   :   getSampleFiles(makeMCDirectory(),'DYJetsToLL_M-50',False,'nanoLatino_')
                                + getSampleFiles(makeMCDirectory(),'DYJetsToLL_M-10to50-LO',False,'nanoLatino_'),
 #                               + getSampleFiles(directory,'DYJetsToTT_MuEle_M-50',False,'nanoLatino_'),
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                     'FilesPerJob' : 5,
                 }

addSampleWeight(samples,'DY','DYJetsToLL_M-50',ptllDYW_NLO)
##addSampleWeight(samples,'DY','DYJetsToTT_MuEle_M-50',ptllDYW_NLO)
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO',ptllDYW_LO)



############ Top ############

Top_pTrw = '(TMath::Sqrt( TMath::Exp(0.0615-0.0005*topGenPt) * TMath::Exp(0.0615-0.0005*antitopGenPt) ) )'

samples['top'] = {    'name'   :   getSampleFiles(makeMCDirectory(),'TTTo2L2Nu',False,'nanoLatino_')
                                 + getSampleFiles(makeMCDirectory(),'ST_s-channel',False,'nanoLatino_')
                                 + getSampleFiles(makeMCDirectory(),'ST_t-channel_antitop',False,'nanoLatino_')
                                 + getSampleFiles(makeMCDirectory(),'ST_t-channel_top',False,'nanoLatino_')
                                 + getSampleFiles(makeMCDirectory(),'ST_tW_antitop',False,'nanoLatino_')
                                 + getSampleFiles(makeMCDirectory(),'ST_tW_top',False,'nanoLatino_') ,
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                     'FilesPerJob' : 1,
                 }

addSampleWeight(samples,'top','TTTo2L2Nu',Top_pTrw)

############ WW ############

#FIXME Add nllW weight to WW
samples['WW'] = {    'name'   :   getSampleFiles(makeMCDirectory(),'WWTo2L2Nu',False,'nanoLatino_') ,
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*nllW' ,
                 }


samples['WWewk'] = {   'name'  : getSampleFiles(makeMCDirectory(), 'WpWmJJ_EWK',False,'nanoLatino_'),
                       'weight': XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+ '*(Sum$(abs(GenPart_pdgId)==6)==0)' #filter tops
                   }


samples['ggWW']  = {  'name'   :   getSampleFiles(makeMCDirectory(),'GluGluToWWToENEN',False,'nanoLatino_')
                                 + getSampleFiles(makeMCDirectory(),'GluGluToWWToENMN',False,'nanoLatino_')
                                 + getSampleFiles(makeMCDirectory(),'GluGluToWWToENTN',False,'nanoLatino_')
                                 + getSampleFiles(makeMCDirectory(),'GluGluToWWToMNEN',False,'nanoLatino_')
                                 + getSampleFiles(makeMCDirectory(),'GluGluToWWToMNMN',False,'nanoLatino_')
                                 + getSampleFiles(makeMCDirectory(),'GluGluToWWToMNTN',False,'nanoLatino_')
                                 + getSampleFiles(makeMCDirectory(),'GluGluToWWToTNEN',False,'nanoLatino_')
                                 + getSampleFiles(makeMCDirectory(),'GluGluToWWToTNMN',False,'nanoLatino_')
                                 + getSampleFiles(makeMCDirectory(),'GluGluToWWToTNTN',False,'nanoLatino_'),
                      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                   }

############ Vg ############

samples['Vg']  =  {     'name'   :   getSampleFiles(makeMCDirectory(),'Wg_MADGRAPHMLM',False,'nanoLatino_')
                                   + getSampleFiles(makeMCDirectory(),'ZGToLLG',False,'nanoLatino_'),
                        'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC + '* !(Gen_ZGstar_mass > 0 && Gen_ZGstar_MomId == 22 )',
                        'FilesPerJob' : 5 ,
                  }

######## VgS ########
#FIXME: k-factor?
samples['VgS']  = {    'name':   getSampleFiles(makeMCDirectory(),'Wg_MADGRAPHMLM',False,'nanoLatino_')
                               + getSampleFiles(makeMCDirectory(),'ZGToLLG',False,'nanoLatino_')
                               + getSampleFiles(makeMCDirectory(),'WZTo3LNu_mllmin01',False,'nanoLatino_') ,
                       'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                       'FilesPerJob' : 15 ,
                  }
addSampleWeight(samples,'VgS','Wg_MADGRAPHMLM',    '(Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples,'VgS','ZGToLLG',                '(Gen_ZGstar_mass >0)*(Sum$(GenPart_pdgId == 22 && TMath::Odd(GenPart_statusFlags) && GenPart_pt < 20.) == 0)')
addSampleWeight(samples,'VgS','WZTo3LNu_mllmin01', '(Gen_ZGstar_mass>=0.1)')

############ VZ ############

#FIXME Add normalization k-factor
samples['VZ']  = {  'name'   :   getSampleFiles(makeMCDirectory(),'ZZTo2L2Nu',False,'nanoLatino_')
                               + getSampleFiles(makeMCDirectory(),'ZZTo2L2Q',False,'nanoLatino_')
                               + getSampleFiles(makeMCDirectory(),'ZZTo4L',False,'nanoLatino_')
                               + getSampleFiles(makeMCDirectory(),'WZTo2L2Q',False,'nanoLatino_'),
                    'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                    'FilesPerJob' : 4,
                 }


############ VVV ############

samples['VVV']  = {  'name'   :   getSampleFiles(makeMCDirectory(),'ZZZ',False,'nanoLatino_')
                                + getSampleFiles(makeMCDirectory(),'WZZ',False,'nanoLatino_')
                                + getSampleFiles(makeMCDirectory(),'WWZ',False,'nanoLatino_')
                                + getSampleFiles(makeMCDirectory(),'WWW',False,'nanoLatino_'),
                                #+ getSampleFiles(makeMCDirectory(),'WWG',False,'nanoLatino_'), #should this be included? or is it already taken into account in the WW sample?
                    'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                  }



##########################################
################ SIGNALS #################
##########################################

############ ggH H->WW ############
#FIXME Add reweighting to MiNLO NNLOPS or use NNLOPS sample when available
#samples['ggH_hww']  = {  'name'   :   getSampleFiles(makeMCDirectory(),'GluGluHToWWTo2L2NuPowheg_M125',False,'nanoLatino_'),
#                        'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
#                     }

############ VBF H->WW ############
#samples['qqH_hww']  = {  'name'   :   getSampleFiles(makeMCDirectory(),'VBFHToWWTo2L2NuPowheg_M125',False,'nanoLatino_'),
#                        'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
#                     }

############ ZH H->WW ############

#samples['ZH_hww']  = {  'name'   :   getSampleFiles(makeMCDirectory(),'HZJ_HToWWTo2L2Nu_M125',False,'nanoLatino_'), #FIXME replace with 125 GeV sample when available
#                        'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
#                     }

#samples['ggZH_hww']  = {  'name'   :   getSampleFiles(makeMCDirectory(),'GluGluZH_HToWW_M125',False,'nanoLatino_'),
#                        'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
#                     }

############ WH H->WW ############

#samples['WH_hww']  = {  'name'   :   getSampleFiles(makeMCDirectory(),'HWplusJ_HToWW_M125',False,'nanoLatino_')
#                                   + getSampleFiles(makeMCDirectory(),'HWminusJ_HToWW_M125',False,'nanoLatino_'),
#                        'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
#                     }

if os.path.exists('HTXS_stage1_categories.py'):
  handle = open('HTXS_stage1_categories.py','r')
  exec(handle)
  handle.close()
  SigOnly=treeBaseDir+'Summer16_102X_nAODv5_SigOnly_Full2016v5/MCl1loose2016v5__MCCorr2016v5__l2loose__l2tightOR2016v5/'

for cat,num in HTXSStage1_1Categories.iteritems():
    if 'QQ2HLNU_' in cat:
        samples['WH_hww_'+cat.replace('QQ2HLNU_','')] = { 'name'   :
                                    getSampleFiles(makeMCDirectory('nAODv5_SigOnly'),'HWplusJ_HToWW_M125_PrivateNano',False,'nanoLatino_')
                                    + getSampleFiles(makeMCDirectory('nAODv5_SigOnly'),'HWminusJ_HToWW_M125_PrivateNano',False,'nanoLatino_'),
                                    'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*(HTXS_stage1_1_cat_pTjet30GeV=='+str(num)+')',
                                    }

############ ttH ############

#samples['ttH_hww']  = {  'name'   :   getSampleFiles(makeMCDirectory(),'ttHToNonbb_M125',False,'nanoLatino_'),
#                         'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
#                     }

############ bbH ############
#FIXME Missing samples


############ H->TauTau ############

splitHtt=False
if not splitHtt:

  samples['H_htt'] = {  'name'   :   getSampleFiles(makeMCDirectory(),'GluGluHToTauTau_M125',False,'nanoLatino_')
                                   + getSampleFiles(makeMCDirectory(),'VBFHToTauTau_M125',False,'nanoLatino_')
                                   + getSampleFiles(makeMCDirectory(),'HZJ_HToTauTau_M125',False,'nanoLatino_')
                                   + getSampleFiles(makeMCDirectory(),'HWplusJ_HToTauTau_M125',False,'nanoLatino_')
                                   + getSampleFiles(makeMCDirectory(),'HWminusJ_HToTauTau_M125',False,'nanoLatino_'),
                         'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                         'suppressNegative' :['all'],
                         'suppressNegativeNuisances' :['all'],
                     }
else:

  samples['ggH_htt']  = {  'name'   : getSampleFiles(makeMCDirectory(),'GluGluHToTauTau_M125',False,'nanoLatino_'),
                           'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                           'suppressNegative' :['all'],
                           'suppressNegativeNuisances' :['all'],
                        }

  samples['qqH_htt']  = {  'name'   : getSampleFiles(makeMCDirectory(),'VBFHToTauTau_M125',False,'nanoLatino_'),
                           'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                           'suppressNegative' :['all'],
                           'suppressNegativeNuisances' :['all'],
                        }

  samples['ZH_htt']  = {  'name'   : getSampleFiles(makeMCDirectory(),'HZJ_HToTauTau_M125',False,'nanoLatino_'),
                           'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                           'suppressNegative' :['all'],
                           'suppressNegativeNuisances' :['all'],
                        }

  samples['WH_htt']  = {  'name'   :  getSampleFiles(makeMCDirectory(),'HWplusJ_HToTauTau_M125',False,'nanoLatino_')
                                    + getSampleFiles(makeMCDirectory(),'HWminusJ_HToTauTau_M125',False,'nanoLatino_'),
                           'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                           'suppressNegative' :['all'],
                           'suppressNegativeNuisances' :['all'],
                        }


###########################################
################## FAKE ###################
###########################################



#samples['Fakes']  = {  'name'   :   getSampleFiles(makeMCDirectory(),'WJetsToLNu-LO',False,'nanoLatino_')
#                                  + getSampleFiles(makeMCDirectory(),'TTToSemiLeptonic',False,'nanoLatino_'),
#                       'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC,
#                       'FilesPerJob': 3,
#                    }
#
'''
samples['Fakes']  = {   'name': [ ] ,
                       'weight' : fakeW+'*'+METFilter_DATA+'*((Lepton_pdgId[0]*Lepton_pdgId[1]==11*13) || (Lepton_pdgId[0]*Lepton_pdgId[1]==11*11) || (Lepton_pdgId[0]*Lepton_pdgId[1]==13*13))',              #   weight/cut
                       'weights' : [ ] ,
                       'isData': ['all'],
                       'FilesPerJob' : 15 ,
                     }
'''
samples['Fakes_ee']  = {   'name': [ ] ,
                       'weight' : fakeW+'*'+METFilter_DATA+'*(Lepton_pdgId[0]*Lepton_pdgId[1]==11*11)',              #   weight/cut
                       'weights' : [ ] ,
                       'isData': ['all'],
                       'FilesPerJob' : 15 ,
                     }

samples['Fakes_mm']  = {   'name': [ ] ,
                       'weight' : fakeW+'*'+METFilter_DATA+'*(Lepton_pdgId[0]*Lepton_pdgId[1]==13*13)',              #   weight/cut
                       'weights' : [ ] ,
                       'isData': ['all'],
                       'FilesPerJob' : 15 ,
                     }


samples['Fakes_em']  = {   'name': [ ] ,
                       'weight' : fakeW+'*'+METFilter_DATA+'*(Lepton_pdgId[0]*Lepton_pdgId[1]==11*13)',              #   weight/cut
                       'weights' : [ ] ,
                       'isData': ['all'],
                       'FilesPerJob' : 15 ,
                     }



for Run in DataRun :
  directory = treeBaseDir+'Run2017_102X_nAODv4_Full2017v5/DATAl1loose2017v5__l2loose__fakeW/'
#  directory = treeBaseDir+'Run2017_102X_nAODv4_Full2017v5/DATAl1loose2017v5__l2loose__fakeW_CutBasedTest/'
  for DataSet in DataSets :
    FileTarget = getSampleFiles(directory,DataSet+'_'+Run[1],True,'nanoLatino_')
    for iFile in FileTarget:
    #  samples['Fakes']['name'].append(iFile)
    #  samples['Fakes']['weights'].append(DataTrig[DataSet])
      samples['Fakes_ee']['name'].append(iFile)
      samples['Fakes_ee']['weights'].append(DataTrig[DataSet])
      samples['Fakes_mm']['name'].append(iFile)
      samples['Fakes_mm']['weights'].append(DataTrig[DataSet])
      samples['Fakes_em']['name'].append(iFile)
      samples['Fakes_em']['weights'].append(DataTrig[DataSet])


###########################################
################## DATA ###################
###########################################

samples['DATA']  = {   'name': [ ] ,
                       'weight' : METFilter_DATA+'*'+LepWPCut,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : 20 ,
                  }

for Run in DataRun :
  directory = treeBaseDir+'Run2017_102X_nAODv4_Full2017v5/DATAl1loose2017v5__l2loose__l2tightOR2017v5/'
  for DataSet in DataSets :
    FileTarget = getSampleFiles(directory,DataSet+'_'+Run[1],True,'nanoLatino_')
    for iFile in FileTarget:
      samples['DATA']['name'].append(iFile)
      samples['DATA']['weights'].append(DataTrig[DataSet])
