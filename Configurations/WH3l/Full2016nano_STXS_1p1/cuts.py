# cuts

Anacat={}
cuts={}

supercut = 'MinIf$( WH3l_mOSll[], WH3l_mOSll[Iteration$] > 0) > 12 \
            && Alt$(Lepton_pt[0],0)>25 \
            && Alt$(Lepton_pt[1],0)>15 \
            && Alt$(Lepton_pt[2],0)>10 \
            && Alt$(Lepton_pt[3],0)<10 \
            && (nLepton==3 && Alt$(Lepton_pt[3],0)<10) \
            && Alt$(Lepton_eta[0],0)<2.5 \
            && Alt$(Lepton_eta[1],0)<2.5 \
            && Alt$(Lepton_eta[2],0)<2.5 \
            && Alt$(Lepton_eta[3],0)<2.5 \
            && abs(WH3l_chlll) == 1 \
           '

#Reco level
HTSXReco = {
    'FWDH' : '1==1',
    'PTV_0_75' : 'WlepPt_wh3l[0]>0 && WlepPt_wh3l[0] <= 75',
    'PTV_75_150' : 'WlepPt_wh3l[0] > 75 && WlepPt_wh3l[0] <= 150',
    'PTV_150_250_0J' : 'WlepPt_wh3l[0] > 150 && WlepPt_wh3l[0] <= 250 && zeroJet',
    'PTV_150_250_GE1J' : 'WlepPt_wh3l[0] > 150 && WlepPt_wh3l[0] <= 250 && oneJetOrMore',
    'PTV_GT250' : 'WlepPt_wh3l[0] > 250',
    }

Anacat['wh3l_13TeV_sssf']  = 'WH3l_njet == 0 \
                       && Alt$( CleanJet_pt[0], 0) < 30 \
                       && Sum$( CleanJet_pt > 20. && abs(CleanJet_eta)<2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) == 0\
                       && WH3l_dphilllmet > 2.5 \
                       && MinIf$(WH3l_mOSll[], WH3l_mOSll[Iteration$] > 0) < 100\
                       && WH3l_flagOSSF == 0\
                       '

Anacat['wh3l_13TeV_ossf']  = 'WH3l_njet == 0 \
                       && Alt$( CleanJet_pt[0], 0) < 30 \
                       && Sum$( CleanJet_pt[] < 20 || Jet_btagDeepB[CleanJet_jetIdx[]] < 0.1522 ) == nCleanJet  \
                       && WH3l_dphilllmet > 2.2 \
                       && MET_pt > 50\
                       && WH3l_ZVeto > 25\
                       && MinIf$(WH3l_mOSll[], WH3l_mOSll[Iteration$] > 0) < 100\
                       && WH3l_flagOSSF == 1\
                       && WH3l_ptlll > 20\
                       '

for key,value in Anacat.iteritems():
    for cat,val in HTSXReco.iteritems():
        cuts['%s_%s' %(key,cat)] = '%s && %s' %(value,val)

#cuts['wh3l_wz_13TeV'] = 'WH3l_njet == 0 && Sum$(CleanJet_pt > 20. && abs(CleanJet_eta)<2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) == 0 && MET_pt > 45 && WH3l_ZVeto < 20 && WH3l_mlll > 100'
#cuts['wh3l_zg_13TeV'] = 'WH3l_njet == 0 && Sum$(CleanJet_pt > 20. && abs(CleanJet_eta)<2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) == 0 && MET_pt < 40 && WH3l_mlll > 80 && WH3l_mlll < 100'

cuts['wh3l_wz_13TeV_0j'] = 'WH3l_njet == 0\
                         && Sum$(CleanJet_pt > 20. && abs(CleanJet_eta)<2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) == 0\
                         && MET_pt > 45\
                         && WH3l_ZVeto < 20\
                         && WH3l_mlll > 100\
                         && zeroJet \
                        '

cuts['wh3l_wz_13TeV_1j'] = 'WH3l_njet == 0\
                         && Sum$(CleanJet_pt > 20. && abs(CleanJet_eta)<2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) == 0\
                         && MET_pt > 45\
                         && WH3l_ZVeto < 20\
                         && WH3l_mlll > 100\
                         && oneJetOrMore \
                         '

cuts['wh3l_zg_13TeV_0j'] = 'WH3l_njet == 0\
                         && Sum$(CleanJet_pt > 20. && abs(CleanJet_eta)<2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) == 0\
                         && MET_pt < 40\
                         && WH3l_mlll > 80\
                         && WH3l_mlll < 100\
                         && zeroJet \
                        '

cuts['wh3l_zg_13TeV_1j'] = 'WH3l_njet == 0\
                         && Sum$(CleanJet_pt > 20. && abs(CleanJet_eta)<2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) == 0\
                         && MET_pt < 40\
                         && WH3l_mlll > 80\
                         && WH3l_mlll < 100\
                         && oneJetOrMore\
                         '


# 11 = e
# 13 = mu
# 15 = tau
