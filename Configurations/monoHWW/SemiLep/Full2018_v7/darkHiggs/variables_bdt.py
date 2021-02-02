variables['Puppimet']  = {
                        'name': 'PuppiMET_pt',
                        'range' : (25,0,300),
                        'xaxis' : 'p_{T} puppiMET [GeV]',
                        'fold'  : 3
                        }
variables['pt_ljj']  = {
                        'name': 'MHlnjj_pt_ljj',
                        'range' : (25,0,300),
                        'xaxis' : 'p_{T}^{ljj} [GeV]',
                        'fold'  : 3
                        }
variables['frac_PTljj_D_PTmet']  = {
    'name': 'MHlnjj_PTljj_D_PTmet',
    'range' : (25,0,3),
    'xaxis' : 'p_{T}^{ljj} / p_{T}^{met}',
    'fold'  : 3
}

variables['frac_PTljj_D_Mlmetjj']  = {
    'name': 'MHlnjj_PTljj_D_Mlmetjj',
    'range' : (25,0,1),
    'xaxis' : 'p_{T}^{ljj} / m_{lmetjj}',
    'fold'  : 3
}

variables['frac_MINPTlj_D_PTmet']  = {
    'name': 'MHlnjj_MINPTlj_D_PTmet',
    'range' : (30,0,0.8),
    'xaxis' : 'min(p_{T}^{l}, p_{T}^{j2}) / p_{T}^{met}',
    'fold'  : 3
}

variables['frac_MINPTlj_D_Mlmetjj']  = {
    'name': 'MHlnjj_MINPTlj_D_Mlmetjj',
    'range' : (30,0,0.2),
    'xaxis' : 'min(p_{T}^{l}, p_{T}^{j2}) / m_{lmetjj}',
    'fold'  : 3
}

variables['frac_MAXPTlj_D_PTmet']  = {
    'name': 'MHlnjj_MAXPTlj_D_PTmet',
    'range' : (30,0,0.8),
    'xaxis' : 'max(p_{T}^{l}, p_{T}^{j1}) / p_{T}^{met}',
    'fold'  : 3
}

variables['frac_MAXPTlj_D_Mlmetjj']  = {
    'name': 'MHlnjj_MAXPTlj_D_Mlmetjj',
    'range' : (30,0,0.4),
    'xaxis' : 'max(p_{T}^{l}, p_{T}^{j1}) / m_{lmetjj}',
    'fold'  : 3
}


variables['mt_lmet']  = {
                       #'name': 'MHlnjj_mt_lmet',
                       'name': 'mtw1',
                       'range' : (25,0,200),
                       #'range' : ([50,75,100,125,181,300],),
                       'xaxis' : 'm_{T}^{lmet} [GeV]',
                       'fold'  : 3
                       }

variables['frac_MTljj_D_PTmet']  = {
    'name': 'MHlnjj_MTljj_D_PTmet',
    'range' : (25,0,3),
    'xaxis' : 'm_{T}^{ljj} / p_{T}^{met}',
    'fold'  : 3
}

variables['frac_MTljj_D_Mlmetjj']  = {
    'name': 'MHlnjj_MTljj_D_Mlmetjj',
    'range' : (25,0,1),
    'xaxis' : 'm_{T}^{ljj} / m_{lmetjj}',
    'fold'  : 3
}

variables['dphi_ljj_met']  = {
                        'name': 'MHlnjj_dphi_ljjVmet',
                        'range' : (25,0,3.14),
                        'xaxis' : '#Delta#phi(ljj,met)',
                        'fold'  : 3,
                        }
variables['deta_ljj_met']  = {
                        'name': 'MHlnjj_deta_ljjVmet',
                        'range' : (25,-5,5),   
                        'xaxis' : '#Delta#eta(ljj,met)',
                        'fold'  : 3,
                        }
variables['dphi_l_jj']  = {
                        'name': 'MHlnjj_dphi_jjVl',
                        'range' : (25,0,3.14),
                        'xaxis' : '#Delta#phi(l,jj)',
                        'fold'  : 3
                        }
variables['deta_l_jj']  = {
                        'name': 'MHlnjj_deta_jjVl',
                        'range' : (25,-5,5),   
                        'xaxis' : '#Delta#eta(l,jj)',
                        'fold'  : 3
                        }
variables['dphi_l_met']  = {
                        'name': 'MHlnjj_dphi_lVmet',
                        'range' : (25,0,3.14),
                        'xaxis' : '#Delta#phi(l,met)',
                        'fold'  : 3
                        }
variables['deta_l_met']  = {
                        'name': 'MHlnjj_deta_lVmet',
                        'range' : (25,-5,5),   
                        'xaxis' : '#Delta#eta(l,met)',
                        'fold'  : 3
                        }
variables['dphi_j_j']  = {
                        'name': 'MHlnjj_dphi_jVj',
                        'range' : (25,0,3.14),
                        'xaxis' : '#Delta#phi(j,j)',
                        'fold'  : 3
                        }
variables['deta_j_j']  = {
                        'name': 'MHlnjj_deta_jVj',
                        'range' : (25,-5,5),   
                        'xaxis' : '#Delta#eta(j,j)',
                        'fold'  : 3
                        }
variables['m_ljj']  = {
    'name': 'MHlnjj_m_ljj',
    'range' : (30,0,400),
    'xaxis' : 'm_{ljj} [GeV]',
    'fold'  : 3
}

variables['m_lmetjj']  = {
    'name': 'MHlnjj_m_lmetjj',
    'range' : (30,0,1000),
    'xaxis' : 'm_{lmetjj} [GeV]',
    'fold'  : 3
}
variables['m_jj']  = {  'name': 'MHlnjj_m_jj',     
                        'range' : (25,0,250),   
                        'xaxis' : 'm^{j,j}',
                        'fold'  : 3                         
                        }


