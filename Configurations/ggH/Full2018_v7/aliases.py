import os
import copy
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # Full2017_v6
configurations = os.path.dirname(configurations) # ggH
configurations = os.path.dirname(configurations) # Configurations
configurations = os.path.dirname(configurations)
#aliases = {}

# imported from samples.py:
# samples, signals

mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]

aliases['gen_mVV'] = {
    'linesToAdd':['.L /afs/cern.ch/work/t/tcarnaha/HWW/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/ggH/Full2018_v7/onTheFly/getmVV.cc+'],
    'class': 'getmVV',
    'samples': mc
}

