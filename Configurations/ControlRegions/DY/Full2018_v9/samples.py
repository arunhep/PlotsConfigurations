import os
import inspect

# /afs/cern.ch/user/n/ntrevisa/work/latinos/unblinding/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/ControlRegions/DY/Full2018_v9

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # Full2018_v9
configurations = os.path.dirname(configurations) # DY
configurations = os.path.dirname(configurations) # ControlRegions
configurations = os.path.dirname(configurations) # Configurations

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

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

# MC:   /eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9/
# DATA: /eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2018_UL2018_nAODv9_Full2018v9/DATAl1loose2018v9__l2loose__l2tightOR2018v9/

mcProduction = 'Summer20UL18_106x_nAODv9_Full2018v9'

dataReco = 'Run2018_UL2018_nAODv9_Full2018v9'

# embedReco = 'Embedding2016_102X_nAODv7_Full2016v7'

mcSteps = 'MCl1loose2018v9__MCCorr2018v9'

# fakeSteps = 'DATAl1loose2016v7__l2loose__fakeW'

dataSteps = 'DATAl1loose2018v9__l2loose__l2tightOR2018v9'

# embedSteps = 'DATAl1loose2016v7__l2loose__l2tightOR2016v7__Embedding'

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
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))

mcDirectory = makeMCDirectory()
# fakeDirectory = os.path.join(treeBaseDir, dataReco, fakeSteps)
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)
# embedDirectory = os.path.join(treeBaseDir, embedReco, embedSteps)

################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
    ['A','Run2018A-UL2018-v1'],
    ['B','Run2018B-UL2018-v1'],
    ['C','Run2018C-UL2018-v1'],
    ['D','Run2018D-UL2018-v1'],
]

DataSets = ['MuonEG','SingleMuon','EGamma','DoubleMuon']

DataTrig = {
    'MuonEG'         : 'Trigger_ElMu' ,
    'DoubleMuon'     : '!Trigger_ElMu && Trigger_dblMu' ,
    'SingleMuon'     : '!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu' ,
    'EGamma'         : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && (Trigger_sngEl || Trigger_dblEl)' ,
}

#########################################
############ MC COMMON ##################
#########################################

# SFweight does not include btag weights
mcCommonWeightNoMatch = 'XSWeight*METFilter_MC*SFweight'
mcCommonWeight = 'XSWeight*METFilter_MC*PromptGenLepMatch2l*SFweight'

###########################################
#############  BACKGROUNDS  ###############
###########################################

###### DY #######

useEmbeddedDY = False
embed_tautauveto = ''

files = nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO')

samples['DY'] = {
    'name': files,
    'weight': mcCommonWeight + '*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0))',
    'FilesPerJob': 2,
}
# addSampleWeight(samples,'DY','DYJetsToLL_M-50',       'DY_NLO_pTllrw')
# addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO','DY_LO_pTllrw')


# ##### Top #######

# files = nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') + \
#         nanoGetSampleFiles(mcDirectory, 'ST_s-channel') + \
#         nanoGetSampleFiles(mcDirectory, 'ST_t-channel_top') + \
#         nanoGetSampleFiles(mcDirectory, 'ST_t-channel_antitop') + \
#         nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop') + \
#         nanoGetSampleFiles(mcDirectory, 'ST_tW_top')

# samples['top'] = {
#     'name': files,
#     'weight': mcCommonWeight,
#     'FilesPerJob': 1,
# }

# addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw')

# ###### WW ########

# samples['WW'] = {
#     'name': nanoGetSampleFiles(mcDirectory, 'WWTo2L2Nu'),
#     'weight': mcCommonWeight + '*nllW', # temporary - nllW module not run on PS and UE variation samples
#     'FilesPerJob': 1
# }

# # Do we have WWewk samples??
# # samples['WWewk'] = {
# #     'name': nanoGetSampleFiles(mcDirectory, 'WpWmJJ_EWK_noTop'),
# #     'weight': mcCommonWeight+embed_tautauveto + '*(Sum$(abs(GenPart_pdgId)==6 || GenPart_pdgId==25)==0)*(lhe_mW1[0] > 60. && lhe_mW1[0] < 100. && lhe_mW2[0] > 60. && lhe_mW2[0] < 100.)', # Filter tops and Higgs, limit w mass
# #     'FilesPerJob': 4
# # }

# files = nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENEN') + \
#         nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENMN') + \
#         nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENTN') + \
#         nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNEN') + \
#         nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNMN') + \
#         nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNTN') + \
#         nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNEN') + \
#         nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNMN') + \
#         nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNTN')

# samples['ggWW'] = {
#     'name': files,
#     'weight': mcCommonWeight+embed_tautauveto + '*1.53/1.4', # updating k-factor <-- do we still need the k-factor?
#     'FilesPerJob': 4
# }

# ######## Vg ########

# files = nanoGetSampleFiles(mcDirectory, 'WGToLNuG') + \
#         nanoGetSampleFiles(mcDirectory, 'ZGToLLG')

# samples['Vg'] = {
#     'name': files,
#     'weight': mcCommonWeightNoMatch+embed_tautauveto + '*(!(Gen_ZGstar_mass > 0))',
#     'FilesPerJob': 4
# }

# ######## VgS ########

# files = nanoGetSampleFiles(mcDirectory, 'WGToLNuG') + \
#         nanoGetSampleFiles(mcDirectory, 'ZGToLLG') + \
#         nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin4p0') # WZTo3LNu_mllmin01_ext1

# samples['VgS'] = {
#     'name': files,
#     'weight': mcCommonWeight+embed_tautauveto + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
#     'FilesPerJob': 4,
#     'subsamples': {
#       'L': 'gstarLow',
#       'H': 'gstarHigh'
#     }
# }
# addSampleWeight(samples, 'VgS', 'WGToLNuG', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass <= 4.0)')
# addSampleWeight(samples, 'VgS', 'ZGToLLG', '(Gen_ZGstar_mass > 0)')
# addSampleWeight(samples, 'VgS', 'WZTo3LNu_mllmin4p0', '(Gen_ZGstar_mass > 4.0)')

# ############ VZ ############

# files = nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Nu') + \
#         nanoGetSampleFiles(mcDirectory, 'ZZTo2Q2L_mllmin4p0') + \
#         nanoGetSampleFiles(mcDirectory, 'WZTo2Q2L_mllmin4p0') # 'WZTo2L2Q')

# samples['VZ'] = {
#     'name': files,
#     'weight': mcCommonWeight+embed_tautauveto + '*1.11',
#     'FilesPerJob': 4
# }

# ########## VVV #########

# files = nanoGetSampleFiles(mcDirectory, 'ZZZ') + \
#         nanoGetSampleFiles(mcDirectory, 'WZZ') + \
#         nanoGetSampleFiles(mcDirectory, 'WWZ') + \
#         nanoGetSampleFiles(mcDirectory, 'WWW')
# #+ nanoGetSampleFiles(mcDirectory, 'WWG'), #should this be included? or is it already taken into account in the WW sample?

# samples['VVV'] = {
#     'name': files,
#     'weight': mcCommonWeight,
#     'FilesPerJob': 4
# }

# # ###########################################
# # ################## FAKE ###################
# # ###########################################

# # samples['Fake'] = {
# #   'name': [],
# #   'weight': 'METFilter_DATA*fakeW',
# #   'weights': [],
# #   'isData': ['all'],
# #   'FilesPerJob': 50
# # }

# # for _, sd in DataRun:
# #   for pd in DataSets:
# #     files = nanoGetSampleFiles(fakeDirectory, pd + '_' + sd)

# #     samples['Fake']['name'].extend(files)
# #     samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))

###########################################
################## DATA ###################
###########################################

samples['DATA'] = {
  'name': [],
  'weight': 'LepWPCut*METFilter_DATA',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 50
}

for _, sd in DataRun:
  for pd in DataSets:
    tag = pd + '_' + sd

    if (   ('DoubleMuon' in pd and 'Run2018B' in sd)
        or ('DoubleMuon' in pd and 'Run2018D' in sd)
        or ('DoubleMuon' in pd and 'Run2018D' in sd)
        or ('SingleMuon' in pd and 'Run2018A' in sd)
        or ('SingleMuon' in pd and 'Run2018B' in sd)
        or ('SingleMuon' in pd and 'Run2018C' in sd)):
        print("sd      = {}".format(sd))
        print("pd      = {}".format(pd))
        print("Old tag = {}".format(tag))
        tag = tag.replace('v1','v2')
        print("New tag = {}".format(tag))

    files = nanoGetSampleFiles(dataDirectory, tag)

    samples['DATA']['name'].extend(files)
    samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))
