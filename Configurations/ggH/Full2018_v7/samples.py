import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2018
configurations = os.path.dirname(configurations) # Differential
configurations = os.path.dirname(configurations) # Configurations

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight, getBaseWnAOD

def nanoGetSampleFiles(inputDir, sample):
    try:
        if _samples_noload:
            return []
    except NameError:
        pass

    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')

# samples

try:
    len(samples)
except NameError:
    import collections
    samples = collections.OrderedDict()

################################################
################# SKIMS ########################
################################################

mcProduction = 'Autumn18_102X_nAODv7_Full2018v7'

dataReco = 'Run2018_102X_nAODv7_Full2018v7'

fakeReco = dataReco

embedReco = 'Embedding2018_102X_nAODv7_Full2018v7'

mcSteps = 'MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7{var}'

fakeSteps = 'DATAl1loose2018v7__l2loose__fakeW'

dataSteps = 'DATAl1loose2018v7__l2loose__l2tightOR2018v7'

embedSteps = 'DATAl1loose2018v7__l2loose__l2tightOR2018v7__Embedding'

##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
elif  'cern' in SITE:
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'

def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__trigFix'))

mcDirectory = makeMCDirectory()
fakeDirectory = os.path.join(treeBaseDir, fakeReco, fakeSteps)
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)
embedDirectory = os.path.join(treeBaseDir, embedReco, embedSteps)
signalDirectory = '/eos/user/t/tcarnaha/Summer_2022/HWW_Ntuples/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7__AddLHE_MEs/'

#########################################
############ MC COMMON ##################
#########################################

mcCommonWeightNoMatch = 'XSWeight*SFweight*METFilter_MC'
#mcCommonWeight = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC'
mcCommonWeight = 'XSWeight'
mcSMHiggsWeight = 'XSWeight*p_Gen_GG_SIG_kappaTopBot_1_ghz1_1_MCFM'
mcSMHiggsPropWeight = 'XSWeight*p_Gen_GG_SIG_kappaTopBot_1_ghz1_1_MCFM*p_Gen_CPStoBWPropRewgt'

signals = []

#### ggH -> WW

### mcCommonWeight

samples['ggH_hww_125'] = {
    'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}


samples['ggH_hww_200'] = {
    'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M200'),
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}

samples['ggH_hww_300'] = {
    'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M300'),
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}

samples['ggH_hww_500'] = {
    'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M500'),
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}

samples['ggH_hww_600'] = {
    'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M600'),
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}

samples['ggH_hww_700'] = {
    'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M700'),
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}

samples['ggH_hww_800'] = {
    'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M800'),
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}

samples['ggH_hww_900'] = {
    'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M900'),
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}

samples['ggH_hww_1000'] = {
    'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M1000'),
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}

# samples['ggH_hww_1500'] = {
#     'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M1500'),
#     'weight': mcCommonWeight,
#     'FilesPerJob': 1,
# }

# samples['ggH_hww_2000'] = {
#     'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M2000'),
#     'weight': mcCommonWeight,
#     'FilesPerJob': 1,
# }

# samples['ggH_hww_2500'] = {
#     'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M2500'),
#     'weight': mcCommonWeight,
#     'FilesPerJob': 1,
# }

# samples['ggH_hww_3000'] = {
#     'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M3000'),
#     'weight': mcCommonWeight,
#     'FilesPerJob': 1,
# }


###########################################################################
### mcSMHiggsWeight

samples['ggH_hww_125_SMH'] = {
    'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M125'),
    'weight': mcSMHiggsWeight,
    'FilesPerJob': 1,
}


samples['ggH_hww_200_SMH'] = {
    'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M200'),
    'weight': mcSMHiggsWeight,
    'FilesPerJob': 1,
}

samples['ggH_hww_300_SMH'] = {
    'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M300'),
    'weight': mcSMHiggsWeight,
    'FilesPerJob': 1,
}

samples['ggH_hww_500_SMH'] = {
    'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M500'),
    'weight': mcSMHiggsWeight,
    'FilesPerJob': 1,
}

samples['ggH_hww_600_SMH'] = {
    'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M600'),
    'weight': mcSMHiggsWeight,
    'FilesPerJob': 1,
}

samples['ggH_hww_700_SMH'] = {
    'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M700'),
    'weight': mcSMHiggsWeight,
    'FilesPerJob': 1,
}

samples['ggH_hww_800_SMH'] = {
    'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M800'),
    'weight': mcSMHiggsWeight,
    'FilesPerJob': 1,
}

samples['ggH_hww_900_SMH'] = {
    'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M900'),
    'weight': mcSMHiggsWeight,
    'FilesPerJob': 1,
}

samples['ggH_hww_1000_SMH'] = {
    'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M1000'),
    'weight': mcSMHiggsWeight,
    'FilesPerJob': 1,
}

# samples['ggH_hww_1500_SMH'] = {
#     'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M1500'),
#     'weight': mcSMHiggsWeight,
#     'FilesPerJob': 1,
# }

# samples['ggH_hww_2000_SMH'] = {
#     'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M2000'),
#     'weight': mcSMHiggsWeight,
#     'FilesPerJob': 1,
# }

# samples['ggH_hww_2500_SMH'] = {
#     'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M2500'),
#     'weight': mcSMHiggsWeight,
#     'FilesPerJob': 1,
# }

# samples['ggH_hww_3000_SMH'] = {
#     'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M3000'),
#     'weight': mcSMHiggsWeight,
#     'FilesPerJob': 1,
# }


###########################################################################
### mcSMHiggsPropWeight

samples['ggH_hww_125_SMHProp'] = {
    'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M125'),
    'weight': mcSMHiggsPropWeight,
    'FilesPerJob': 1,
}


samples['ggH_hww_200_SMHProp'] = {
    'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M200'),
    'weight': mcSMHiggsPropWeight,
    'FilesPerJob': 1,
}

samples['ggH_hww_300_SMHProp'] = {
    'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M300'),
    'weight': mcSMHiggsPropWeight,
    'FilesPerJob': 1,
}

samples['ggH_hww_500_SMHProp'] = {
    'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M500'),
    'weight': mcSMHiggsPropWeight,
    'FilesPerJob': 1,
}

samples['ggH_hww_600_SMHProp'] = {
    'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M600'),
    'weight': mcSMHiggsPropWeight,
    'FilesPerJob': 1,
}

samples['ggH_hww_700_SMHProp'] = {
    'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M700'),
    'weight': mcSMHiggsPropWeight,
    'FilesPerJob': 1,
}

samples['ggH_hww_800_SMHProp'] = {
    'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M800'),
    'weight': mcSMHiggsPropWeight,
    'FilesPerJob': 1,
}

samples['ggH_hww_900_SMHProp'] = {
    'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M900'),
    'weight': mcSMHiggsPropWeight,
    'FilesPerJob': 1,
}

samples['ggH_hww_1000_SMHProp'] = {
    'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M1000'),
    'weight': mcSMHiggsPropWeight,
    'FilesPerJob': 1,
}

# samples['ggH_hww_1500_SMHProp'] = {
#     'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M1500'),
#     'weight': mcSMHiggsPropWeight,
#     'FilesPerJob': 1,
# }

# samples['ggH_hww_2000_SMHProp'] = {
#     'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M2000'),
#     'weight': mcSMHiggsPropWeight,
#     'FilesPerJob': 1,
# }

# samples['ggH_hww_2500_SMHProp'] = {
#     'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M2500'),
#     'weight': mcSMHiggsPropWeight,
#     'FilesPerJob': 1,
# }

# samples['ggH_hww_3000_SMHProp'] = {
#     'name': nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M3000'),
#     'weight': mcSMHiggsPropWeight,
#     'FilesPerJob': 1,
# }

##################################################################
### ensure have all weighted signals appended

signals.append('ggH_hww_125')
signals.append('ggH_hww_200')
signals.append('ggH_hww_300')
signals.append('ggH_hww_500')
signals.append('ggH_hww_600')
signals.append('ggH_hww_700')
signals.append('ggH_hww_800')
signals.append('ggH_hww_900')
signals.append('ggH_hww_1000')
# signals.append('ggH_hww_1500')
# signals.append('ggH_hww_2000')
# signals.append('ggH_hww_2500')
# signals.append('ggH_hww_3000')

#
signals.append('ggH_hww_125_SMH')
signals.append('ggH_hww_200_SMH')
signals.append('ggH_hww_300_SMH')
signals.append('ggH_hww_500_SMH')
signals.append('ggH_hww_600_SMH')
signals.append('ggH_hww_700_SMH')
signals.append('ggH_hww_800_SMH')
signals.append('ggH_hww_900_SMH')
signals.append('ggH_hww_1000_SMH')
# signals.append('ggH_hww_1500_SMH')
# signals.append('ggH_hww_2000_SMH')
# signals.append('ggH_hww_2500_SMH')
# signals.append('ggH_hww_3000_SMH')

#
signals.append('ggH_hww_125_SMHProp')
signals.append('ggH_hww_200_SMHProp')
signals.append('ggH_hww_300_SMHProp')
signals.append('ggH_hww_500_SMHProp')
signals.append('ggH_hww_600_SMHProp')
signals.append('ggH_hww_700_SMHProp')
signals.append('ggH_hww_800_SMHProp')
signals.append('ggH_hww_900_SMHProp')
signals.append('ggH_hww_1000_SMHProp')
# signals.append('ggH_hww_1500_SMHProp')
# signals.append('ggH_hww_2000_SMHProp')
# signals.append('ggH_hww_2500_SMHProp')
# signals.append('ggH_hww_3000_SMHProp')
