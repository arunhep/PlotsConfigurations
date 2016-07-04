# samples

#samples = {}

samples['DY']  = {    'name': [
                            'latino_DYJetsToLL_M-10to50.root',
                            'latino_DYJetsToLL_M-10to50ext3.root',
                            #
                            'latino_DYJetsToLL_M-50_0000__part0.root',
                            'latino_DYJetsToLL_M-50_0000__part1.root',
                            'latino_DYJetsToLL_M-50_0000__part2.root',
                            'latino_DYJetsToLL_M-50_0000__part3.root',
                            'latino_DYJetsToLL_M-50_0000__part4.root',
                            'latino_DYJetsToLL_M-50_0001__part0.root',
                            'latino_DYJetsToLL_M-50_0001__part1.root',
                            'latino_DYJetsToLL_M-50_0001__part2.root',
                            'latino_DYJetsToLL_M-50_0001__part3.root',
                            'latino_DYJetsToLL_M-50_0001__part4.root',
                            'latino_DYJetsToLL_M-50_0002__part0.root'
                            #
                            ],    
                      'weight' : 'metFilter*(0.95 - 0.1*TMath::Erf((gen_ptll-14)/8.8))*puW*bPogSF*effTrigW*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]*std_vector_lepton_genmatched[0]*std_vector_lepton_genmatched[1]*GEN_weight_SM/abs(GEN_weight_SM)',              #   weight/cut 
                      #'isData': ['0', '0'],      
                      'weights': [  '0.238112'
                                  , '0.238112'
                                  , '0.317273040011'
                                  , '0.317273040011'
                                  , '0.317273040011'
                                  , '0.317273040011'
                                  , '0.317273040011'
                                  , '0.317273040011'
                                  , '0.317273040011'
                                  , '0.317273040011'
                                  , '0.317273040011'
                                  , '0.317273040011'
                                  , '0.317273040011'
                                  ] ,           
                  }




#samples['DY'] = { 'name' : [
                            #'latino_DYJetsToLL_M-50-LO__part0.root',
                            #'latino_DYJetsToLL_M-50-LO__part1.root',
                            ##
                            #'latino_DYJetsToLL_M-50_HT-100to200_MLM.root',
                            #'latino_DYJetsToLL_M-50_HT-200to400_MLM.root',
                            #'latino_DYJetsToLL_M-50_HT-400to600_MLM.root',
                            #'latino_DYJetsToLL_M-50_HT-600toInf_MLM.root',
                            #],
                   #'weight' : 'baseW*metFilter*puW*bPogSF*effTrigW*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]*std_vector_lepton_genmatched[0]*std_vector_lepton_genmatched[1]*((8.61313e-01+ptll*4.46807e-03-1.52324e-05*ptll*ptll)*(1.08683 * (0.95 - 0.0657370*TMath::Erf((ptll-11.)/5.51582)))*(ptll<140)+1.141996*(ptll>=140))',              #   weight/cut 
                   #'weights': [  'std_vector_LHEparton_pt[0]*(std_vector_LHEparton_pt[0]>0)+std_vector_LHEparton_pt[1]*(std_vector_LHEparton_pt[1]>0)+std_vector_LHEparton_pt[2]*(std_vector_LHEparton_pt[2]>0) < 100'
                               #, 'std_vector_LHEparton_pt[0]*(std_vector_LHEparton_pt[0]>0)+std_vector_LHEparton_pt[1]*(std_vector_LHEparton_pt[1]>0)+std_vector_LHEparton_pt[2]*(std_vector_LHEparton_pt[2]>0) < 100'
                               ##
                               #, '1'
                               #, '1'
                               #, '1'
                               #, '1'
                               #] ,

                #}
                   
                   
                   


# data driven
samples['Fake']  = {    'name': [
                       #'../../../../../../../eos/user/a/amassiro/HWW2015/04MarchFake/22Jan_Run2015C_16Dec2015/latino_DD_Run2015C_16Dec2015_DoubleEG.root',
                       #'../../../../../../../eos/user/a/amassiro/HWW2015/04MarchFake/22Jan_Run2015C_16Dec2015/latino_DD_Run2015C_16Dec2015_DoubleMuon.root',
                       #'../../../../../../../eos/user/a/amassiro/HWW2015/04MarchFake/22Jan_Run2015C_16Dec2015/latino_DD_Run2015C_16Dec2015_MuonEG.root',
                       #'../../../../../../../eos/user/a/amassiro/HWW2015/04MarchFake/22Jan_Run2015C_16Dec2015/latino_DD_Run2015C_16Dec2015_SingleElectron.root',
                       #'../../../../../../../eos/user/a/amassiro/HWW2015/04MarchFake/22Jan_Run2015C_16Dec2015/latino_DD_Run2015C_16Dec2015_SingleMuon.root',
                       #'../../../../../../../eos/user/a/amassiro/HWW2015/04MarchFake/22Jan_Run2015D_16Dec2015/latino_DD_Run2015D_16Dec2015_DoubleEG.root',
                       #'../../../../../../../eos/user/a/amassiro/HWW2015/04MarchFake/22Jan_Run2015D_16Dec2015/latino_DD_Run2015D_16Dec2015_DoubleMuon.root',
                       #'../../../../../../../eos/user/a/amassiro/HWW2015/04MarchFake/22Jan_Run2015D_16Dec2015/latino_DD_Run2015D_16Dec2015_MuonEG.root',
                       #'../../../../../../../eos/user/a/amassiro/HWW2015/04MarchFake/22Jan_Run2015D_16Dec2015/latino_DD_Run2015D_16Dec2015_SingleElectron.root',
                       #'../../../../../../../eos/user/a/amassiro/HWW2015/04MarchFake/22Jan_Run2015D_16Dec2015/latino_DD_Run2015D_16Dec2015_SingleMuon.root'
                       # 
                       '../../../../../../user/r/rebeca/HWW2015/03Mar_Run2015C_16Dec2015/l2loose__hadd__EpTCorr__fakeW/latino_DD_Run2015C_16Dec2015_DoubleEG.root',
                       '../../../../../../user/r/rebeca/HWW2015/03Mar_Run2015C_16Dec2015/l2loose__hadd__EpTCorr__fakeW/latino_DD_Run2015C_16Dec2015_DoubleMuon.root',
                       '../../../../../../user/r/rebeca/HWW2015/03Mar_Run2015C_16Dec2015/l2loose__hadd__EpTCorr__fakeW/latino_DD_Run2015C_16Dec2015_MuonEG.root',
                       '../../../../../../user/r/rebeca/HWW2015/03Mar_Run2015C_16Dec2015/l2loose__hadd__EpTCorr__fakeW/latino_DD_Run2015C_16Dec2015_SingleElectron.root',
                       '../../../../../../user/r/rebeca/HWW2015/03Mar_Run2015C_16Dec2015/l2loose__hadd__EpTCorr__fakeW/latino_DD_Run2015C_16Dec2015_SingleMuon.root',
                       '../../../../../../user/r/rebeca/HWW2015/03Mar_Run2015D_16Dec2015/l2loose__hadd__EpTCorr__fakeW/latino_DD_Run2015D_16Dec2015_DoubleEG.root',
                       '../../../../../../user/r/rebeca/HWW2015/03Mar_Run2015D_16Dec2015/l2loose__hadd__EpTCorr__fakeW/latino_DD_Run2015D_16Dec2015_DoubleMuon.root',
                       '../../../../../../user/r/rebeca/HWW2015/03Mar_Run2015D_16Dec2015/l2loose__hadd__EpTCorr__fakeW/latino_DD_Run2015D_16Dec2015_MuonEG.root',
                       '../../../../../../user/r/rebeca/HWW2015/03Mar_Run2015D_16Dec2015/l2loose__hadd__EpTCorr__fakeW/latino_DD_Run2015D_16Dec2015_SingleElectron.root',
                       '../../../../../../user/r/rebeca/HWW2015/03Mar_Run2015D_16Dec2015/l2loose__hadd__EpTCorr__fakeW/latino_DD_Run2015D_16Dec2015_SingleMuon.root'
                       #
                                 ],     
                      #'weight' : 'metFilter*trigger*(fakeW2l0j*(njet==0)+fakeW2l1j*(njet==1)+fakeW2l2j*(njet>=2))',              #   weight/cut 
                      'weight' : '0.8*metFilter*trigger*(fakeW2l0j*(njet==0)+fakeW2l1j*(njet==1)+fakeW2l2j*(njet>=2))',              #   weight/cut 
                      'isData': ['all'],                             
                  }

             

samples['top'] = {   'name': [
                          'latino_TTTo2L2Nu.root', 
                          'latino_ST_tW_antitop.root',
                          'latino_ST_tW_top.root'
                          ],          
                       'weight' : 'metFilter*puW*baseW*bPogSF*effTrigW*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]*std_vector_lepton_genmatched[0]*std_vector_lepton_genmatched[1]',                
                   }


samples['WW']  = {    'name': [
                                  'latino_WWTo2L2Nu.root'
                                ],      
                      'weight' : 'metFilter*nllW*puW*baseW*bPogSF*effTrigW*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]*std_vector_lepton_genmatched[0]*std_vector_lepton_genmatched[1]',          
                      #'weights': ['abs(nllW)'] ,           
                  }


samples['WWewk']  = {    'name': [
                                  'latino_WpWmJJ_EWK_QCD_noTop.root',
                                  'latino_WpWmJJ_QCD_noTop.root'
                                ],      
                      'weight' : 'metFilter*puW*baseW*bPogSF*effTrigW*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]*std_vector_lepton_genmatched[0]*std_vector_lepton_genmatched[1]',          
                      'weights': [
                          '1',
                          '-1'
                          ] ,           
                  }



samples['ggWW']  = {    'name': ['latino_GluGluWWTo2L2Nu_MCFM.root'],      
                      'weight' : 'metFilter*puW*baseW*bPogSF*effTrigW*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]*std_vector_lepton_genmatched[0]*std_vector_lepton_genmatched[1]',          
                      'weights': ['1.000'] ,           
                      'isData': ['0'],                            
                  }

#samples['ggWW_Int']  = {    'name': ['latino_GluGluWWTo2L2Nu_MCFM.root', 'latino_GluGluWWTo2L2NuHiggs_MCFM.root'],      
                      #'weight' : '1.87*puW*baseW*bPogSF*effTrigW*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]*std_vector_lepton_genmatched[0]*std_vector_lepton_genmatched[1]',          
                      #'weights': ['-1./1.4', '1/1.4'] ,           
                  #}

# during tree production: 1.4 k-factor has been applied to both samples
# ggWW sample: k = 1.4 +/- 15%
# ggWW interference: k = 1.87 +/- 25%



#samples['Vg']  = {    'name': ['latino_Wg_AMCNLOFXFX.root'],      
                      #'weight' : 'metFilter*puW*baseW*bPogSF*effTrigW*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]*GEN_weight_SM/abs(GEN_weight_SM)\
                                  #* !(Gen_ZGstar_mass > 0 && Gen_ZGstar_MomId == 22 )',
                                 ##*(!(Gen_ZGstar_MomStatus==44 && Gen_ZGstar_MomId==22))',
                      #'weights': ['1'] ,           
                      ##'isData': ['0'],                            
                  #}

#samples['Vg']  = {    'name': ['latino_Wg_MADGRAPHMLM.root'],      
                      #'weight' : 'metFilter*puW*baseW*bPogSF*effTrigW*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]*GEN_weight_SM/abs(GEN_weight_SM)\
                                  #* !(Gen_ZGstar_mass > 0 && Gen_ZGstar_MomId == 22 )',    ----> missing variable for this sample!!
                                 ##*(!(Gen_ZGstar_MomStatus==44 && Gen_ZGstar_MomId==22))',
                      #'weights': ['1'] ,           
                      ##'isData': ['0'],                            
                  #}



samples['VgS']  = {    'name': ['latino_WgStarLNuEE.root', 'latino_WgStarLNuMuMu.root'],      
                      'weight' : 'metFilter*2.0*puW*baseW*bPogSF*effTrigW*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]*std_vector_lepton_genmatched[0]*std_vector_lepton_genmatched[1]*GEN_weight_SM/abs(GEN_weight_SM)',
                      'weights': ['1','1'] ,           
                  }

# 
# Wg* scale factor is
#
# 1.98 +/- 0.54    in mumumu
# 2.0  +/- 0.5     in emumu
#
#


samples['VZ']  = {    'name': [
                          'latino_WZTo3LNu.root', 
                          #'latino_ZZ.root',  ---> replaced by inclusive samples
                          'latino_ZZTo2L2Nu.root', #  ---->  NEEDED FIXME
                          #'latino_ZZTo2L2Q.root'
                          'latino_ZZTo4L.root'
                         ], 
                      'weight' : 'metFilter*puW*baseW*bPogSF*effTrigW*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]*std_vector_lepton_genmatched[0]*std_vector_lepton_genmatched[1]',          
                      #'weights': ['1'] ,           
                      #'isData': ['0'],                            
                  }


samples['VVV'] = {    'name': [
                          'latino_WZZ.root', 
                          #'latino_ZZZ.root'
                          #'latino_WWW.root'
                          #'latino_WWZ.root'
                          ],      
                      'weight' : 'metFilter*puW*baseW*bPogSF*effTrigW*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]*std_vector_lepton_genmatched[0]*std_vector_lepton_genmatched[1]*GEN_weight_SM/abs(GEN_weight_SM)',          
                      #'isData': ['0'],                            
                  }


# Htautau
samples['H_htt']  = {      'name': ['latino_GluGluHToTauTau_M125.root',
                                    'latino_VBFHToTauTau_M125.root',
                                    'latino_HWminusJ_HToTauTau_M125.root',
                                    'latino_HWplusJ_HToTauTau_M125.root',
                                    'latino_HZJ_HToTauTau_M125.root'
                                    ],      
                           'weight' : 'metFilter*puW*baseW*bPogSF*effTrigW*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]*std_vector_lepton_genmatched[0]*std_vector_lepton_genmatched[1]',         
                           'weights': ['1', '1', 'GEN_weight_SM/abs(GEN_weight_SM)', 'GEN_weight_SM/abs(GEN_weight_SM)', 'GEN_weight_SM/abs(GEN_weight_SM)' ]            
                  }



# HWW 

samples['ggH_hww']  = {    'name': [
                               'latino_GluGluHToWWTo2L2NuPowheg_M125.root'
                               #'latino_GluGluHToWWTo2L2Nu_M125.root'
                               #'latino_GluGluHToWWTo2L2Nu_alternative_M125.root' # --> 500k events
                               ],      
                           'weight' : 'metFilter*puW*baseW*bPogSF*effTrigW*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]*std_vector_lepton_genmatched[0]*std_vector_lepton_genmatched[1]',          
                  }

samples['qqH_hww']  = {    'name': [
                               'latino_VBFHToWWTo2L2Nu_M125.root'
                               #'latino_VBFHToWWTo2L2Nu_alternative_M125.root'
                               ],      
                           'weight' : 'metFilter*puW*baseW*bPogSF*effTrigW*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]*std_vector_lepton_genmatched[0]*std_vector_lepton_genmatched[1]',          
                  }

samples['ggZH_hww']  = {    'name': [
                               'latino_ggZH_HToWW_M125.root',
                               ],      
                           'weight' : 'metFilter*puW*baseW*bPogSF*effTrigW*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]*std_vector_lepton_genmatched[0]*std_vector_lepton_genmatched[1]',          
                  }


samples['WH_hww']  = {    'name': ['latino_HWminusJ_HToWW_M125.root', 'latino_HWplusJ_HToWW_M125.root'],      
                           'weight' : 'metFilter*puW*baseW*bPogSF*effTrigW*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]*std_vector_lepton_genmatched[0]*std_vector_lepton_genmatched[1]*GEN_weight_SM/abs(GEN_weight_SM)',          
                  }

samples['ZH_hww']  = {    'name': ['latino_HZJ_HToWW_M125.root'],      
                           'weight' : 'metFilter*puW*baseW*bPogSF*effTrigW*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]*std_vector_lepton_genmatched[0]*std_vector_lepton_genmatched[1]*GEN_weight_SM/abs(GEN_weight_SM)',          
                  }



###########################################
###########################################
###########################################

samples['DATA']  = {   'name': [
                                '../../../../../r/rebeca/HWW2015/03Mar_Run2015C_16Dec2015/l2loose__hadd__EpTCorr__l2tight__wwSel/latino_Run2015C_16Dec2015_DoubleEG.root',
                                '../../../../../r/rebeca/HWW2015/03Mar_Run2015C_16Dec2015/l2loose__hadd__EpTCorr__l2tight__wwSel/latino_Run2015C_16Dec2015_DoubleMuon.root',
                                '../../../../../r/rebeca/HWW2015/03Mar_Run2015C_16Dec2015/l2loose__hadd__EpTCorr__l2tight__wwSel/latino_Run2015C_16Dec2015_MuonEG.root',
                                '../../../../../r/rebeca/HWW2015/03Mar_Run2015C_16Dec2015/l2loose__hadd__EpTCorr__l2tight__wwSel/latino_Run2015C_16Dec2015_SingleElectron.root',
                                '../../../../../r/rebeca/HWW2015/03Mar_Run2015C_16Dec2015/l2loose__hadd__EpTCorr__l2tight__wwSel/latino_Run2015C_16Dec2015_SingleMuon.root',
                                '../../../../../r/rebeca/HWW2015/03Mar_Run2015D_16Dec2015/l2loose__hadd__EpTCorr__l2tight__wwSel/latino_Run2015D_16Dec2015_DoubleEG.root',
                                '../../../../../r/rebeca/HWW2015/03Mar_Run2015D_16Dec2015/l2loose__hadd__EpTCorr__l2tight__wwSel/latino_Run2015D_16Dec2015_DoubleMuon.root',
                                '../../../../../r/rebeca/HWW2015/03Mar_Run2015D_16Dec2015/l2loose__hadd__EpTCorr__l2tight__wwSel/latino_Run2015D_16Dec2015_MuonEG.root',
                                '../../../../../r/rebeca/HWW2015/03Mar_Run2015D_16Dec2015/l2loose__hadd__EpTCorr__l2tight__wwSel/latino_Run2015D_16Dec2015_SingleElectron.root',
                                '../../../../../r/rebeca/HWW2015/03Mar_Run2015D_16Dec2015/l2loose__hadd__EpTCorr__l2tight__wwSel/latino_Run2015D_16Dec2015_SingleMuon.root',
                                ] ,     
                       'weight' : 'trigger*metFilter',
                       'isData': ['all'],                            
                  }




