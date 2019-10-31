 # cuts

_tmp = [ 
     'mll>20.',
     'Lepton_pt[0]>25.',
     'Lepton_pt[1]>20.',
     '(nLepton>=2 && Alt$(Lepton_pt[2],0)<10.)',
     'abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5',
     ]

supercut = ' && '.join(_tmp)

def addcut(name, exprs):
    cuts[name] = ' && '.join(exprs)

#Inclusive
_tmp = [
    '1'
     ]

addcut('Control_inclusive_ll', _tmp)

#Top control region
_tmp = [
     'Sum$(abs(CleanJet_eta)>2.5) == 0',
     'Alt$(CleanJet_pt[0],0)>30.',
     'Alt$(CleanJet_pt[1],0)>30.',
     'PuppiMET_pt > 50.',
     '(mll < 76. || mll > 106.)',
     ]

addcut('Control_Top_ll', _tmp)

_tmp = [
    'Sum$(abs(CleanJet_eta)>2.5) == 0',
    'Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11',
    'Alt$(CleanJet_pt[0],0)>30.',
    'Alt$(CleanJet_pt[1],0)>30.',
    'PuppiMET_pt > 50.',
    '(mll < 76. || mll > 106.)',
     ]

addcut('Control_Top_ee', _tmp)

_tmp = [
     'Sum$(abs(CleanJet_eta)>2.5) == 0',
     'Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13',
     'Alt$(CleanJet_pt[0],0)>30.',
     'Alt$(CleanJet_pt[1],0)>30.',
     'PuppiMET_pt > 50.',
     '(mll < 76. || mll > 106.)',
     ]

addcut('Control_Top_mm', _tmp)

# Currently blinded
_tmp = [
     'Sum$(abs(CleanJet_eta)>2.5) == 0',
     'Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13',
     'Alt$(CleanJet_pt[0],0)>30.',
     'Alt$(CleanJet_pt[1],0)>30.',
     'PuppiMET_pt > 50.',
     '(mll < 76. || mll > 106.)',
    ]

addcut('Control_Top_df', _tmp)
