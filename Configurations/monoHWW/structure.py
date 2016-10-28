# structure configuration for datacard

#structure = {}

# keys here must match keys in samples.py    
#                    
structure['DY']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }


structure['Wjets']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['Fake']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['ttbar'] = {   
                  'isSignal' : 0,
                  'isData'   : 0 
                  }


structure['singletop'] = {   
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['top'] = {   
                  'isSignal' : 0,
                  'isData'   : 0 
                  }


structure['WW']  = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['ggWW']  = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['ggWW_Int']  = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['Wg']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['Vg']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['VgS'] = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['Zg']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['VZ']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['WZ']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }


structure['VVV']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['ZZ']  = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }


structure['ggH'] = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['ggH_hww'] = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['qqH_hww'] = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['qqH_hww'] = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['WH_hww'] = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['ZH_hww'] = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['ggZH_hww'] = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['H_htt'] = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['H_hww'] = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

# Signals
ZpMasses={"600","800","1000","1200","1400","1700","2000","2500"}
A0Masses={"400","500","600","700","800"}

for mZp in ZpMasses:
    for mA0 in A0Masses :
        if ((mZp == "600" and mA0 == "400") or ((mZp == "800" and (mA0 == "400" or mA0 == "500" or mA0 == "600"))) or (mZp != "600" and mZp != "800")) :
            structure['monoH_' + mZp + '_' + mA0] = {
                'isSignal' : 1,
                'isData'   : 0    
                }
            
# structure['monoH_800'] = {
#                   'isSignal' : 1,
#                   'isData'   : 0    
#                   }

# structure['monoH_1000'] = {
#                   'isSignal' : 1,
#                   'isData'   : 0    
#                   }

# structure['monoH_1200'] = {
#                   'isSignal' : 1,
#                   'isData'   : 0    
#                   }

# structure['monoH_1400'] = {
#                   'isSignal' : 1,
#                   'isData'   : 0    
#                   }

# structure['monoH_1700'] = {
#                   'isSignal' : 1,
#                   'isData'   : 0    
#                   }

# structure['monoH_2000'] = {
#                   'isSignal' : 1,
#                   'isData'   : 0    
#                   }

# structure['monoH_2500'] = {
#                   'isSignal' : 1,
#                   'isData'   : 0    
#                   }


# data


structure['DATA']  = { 
                  'isSignal' : 0,
                  'isData'   : 1 
              }




