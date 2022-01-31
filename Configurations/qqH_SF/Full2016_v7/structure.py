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

structure['Fake_ee']  = {  
    'isSignal' : 0,
    'isData'   : 0,
    'removeFromCuts' : [ k for k in cuts if 'ee' not in k],
}

structure['Fake_mm']  = {  
    'isSignal' : 0,
    'isData'   : 0,
    'removeFromCuts' : [ k for k in cuts if 'mm' not in k],
}

structure['Fake_df']  = {
    'isSignal' : 0,
    'isData'   : 0,
    'removeFromCuts' : [ k for k in cuts if 'df' not in k],
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

structure['WWewk']  = {
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

structure['VgS_L'] = {
    'isSignal' : 0,
    'isData'   : 0
}

structure['VgS_H'] = {
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
    'isSignal' : 1,
    'isData'   : 0    
}

structure['ggH_hww'] = {
    'isSignal' : 1,
    'isData'   : 0,
    'scaleSampleForDatacard' : {cut : 1.03364 for cut in cuts.keys()}, # XSECxBR correction for mH = 125.38
}

structure['WH_hww'] = {
    'isSignal' : 1,
    'isData'   : 0,
    'scaleSampleForDatacard' : {cut : 1.01724 for cut in cuts.keys()}, # XSECxBR correction for mH = 125.38 
}

structure['ZH_hww'] = {
    'isSignal' : 1,
    'isData'   : 0,
    'scaleSampleForDatacard' : {cut : 1.01994 for cut in cuts.keys()}, # XSECxBR correction for mH = 125.38
}

structure['ggZH_hww'] = {
    'isSignal' : 1,
    'isData'   : 0,
    'scaleSampleForDatacard' : {cut : 1.02494 for cut in cuts.keys()}, # XSECxBR correction for mH = 125.38
}

import pickle
with open('vbfDipoleScale.pkl', 'rb') as handle:
    vbfDipoleScale = pickle.load(handle)

# XSECxBR correction for mH = 125.38
for key, val in vbfDipoleScale.items():
    vbfDipoleScale[key] = val * 1.03621

structure['qqH_hww'] = {
  'isSignal' : 1,
  'isData'   : 0,
  'scaleSampleForDatacard' : vbfDipoleScale,
}

# structure['ggH_hww'] = {
#     'isSignal' : 1,
#     'isData'   : 0    
# }

# structure['WH_hww'] = {
#     'isSignal' : 1,
#     'isData'   : 0    
# }

# structure['ZH_hww'] = {
#     'isSignal' : 1,
#     'isData'   : 0    
# }

# structure['ggZH_hww'] = {
#     'isSignal' : 1,
#     'isData'   : 0    
# }

structure['H_hww'] = {
    'isSignal' : 1,
    'isData'   : 0    
}

structure['bbH_hww'] = {
    'isSignal' : 1,
    'isData'   : 0
}

structure['ttH_hww'] = {
    'isSignal' : 1,
    'isData'   : 0
}

structure['ggH_htt'] = {
    'isSignal' : 1,
    'isData'   : 0,
}

structure['qqH_htt'] = {
    'isSignal' : 1,
    'isData'   : 0,
}

structure['WH_htt'] = {
    'isSignal' : 1,
    'isData'   : 0,
}

structure['ZH_htt'] = {
    'isSignal' : 1,
    'isData'   : 0,
}

structure['H_htt'] = {
    'isSignal' : 1,
    'isData'   : 0    
}


# data


structure['DATA']  = { 
                  'isSignal' : 0,
                  'isData'   : 1 
              }

print "INSTRUCTURE"
print cuts
#print nuisances['WWresum0j']
print "OK"

for nuis in nuisances.itervalues():
  if 'cutspost' in nuis:
    nuis['cuts'] = nuis['cutspost'](nuis, cuts)

    print nuis
