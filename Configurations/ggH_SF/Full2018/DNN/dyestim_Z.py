
#RAndKff  = {}

RAndKff['DYmva0p8'] = {
                      'RFile'   : 'rootFile/plots_BG_DY_NOHR_MVA080_Zpeak.root' ,
                      'KffFile' : 'rootFile/plots_BG_DY_NOHR_MVA080_Zpeak.root' ,             
                      'Regions' : { '0jee' : { 
                                               'kNum' : '0j_ee_in/events/histo_DY' ,
                                               'kDen' : '0j_uu_in/events/histo_DY' ,
                                               'RNum' : '0j_ee_out/events/histo_DY' , 
                                               'RDen' : '0j_ee_in/events/histo_DY' , 
                                             } ,
                                    '0jmm' : { 
                                               'kNum' : '0j_uu_in/events/histo_DY' ,
                                               'kDen' : '0j_ee_in/events/histo_DY' ,
                                               'RNum' : '0j_uu_out/events/histo_DY' , 
                                               'RDen' : '0j_uu_in/events/histo_DY' , 
                                             } ,
                                    '1jee' : { 
                                               'kNum' : '1j_ee_in/events/histo_DY' ,
                                               'kDen' : '1j_uu_in/events/histo_DY' ,
                                               'RNum' : '1j_ee_out/events/histo_DY' , 
                                               'RDen' : '1j_ee_in/events/histo_DY' , 
                                             } ,
                                    '1jmm' : { 
                                               'kNum' : '1j_uu_in/events/histo_DY' ,
                                               'kDen' : '1j_ee_in/events/histo_DY' ,
                                               'RNum' : '1j_uu_out/events/histo_DY' , 
                                               'RDen' : '1j_uu_in/events/histo_DY' , 
                                             } ,
                                    '2jee' : {
                                               'kNum' : '2j_ggH_ee_in/events/histo_DY' ,
                                               'kDen' : '2j_ggH_uu_in/events/histo_DY' ,
                                               'RNum' : '2j_ggH_ee_out/events/histo_DY' ,
                                               'RDen' : '2j_ggH_ee_in/events/histo_DY' ,
                                             } ,
                                    '2jmm' : {
                                               'kNum' : '2j_ggH_uu_in/events/histo_DY' ,
                                               'kDen' : '2j_ggH_ee_in/events/histo_DY' ,
                                               'RNum' : '2j_ggH_uu_out/events/histo_DY' ,
                                               'RDen' : '2j_ggH_uu_in/events/histo_DY' ,
                                             } ,
                                 '2jVBFee' : {
                                               'kNum' : '2j_VBF_ee_in/events/histo_DY' ,
                                               'kDen' : '2j_VBF_uu_in/events/histo_DY' ,
                                               'RNum' : '2j_VBF_ee_out/events/histo_DY' ,
                                               'RDen' : '2j_VBF_ee_in/events/histo_DY' ,
                                             } ,
                                 '2jVBFmm' : {
                                               'kNum' : '2j_VBF_uu_in/events/histo_DY' ,
                                               'kDen' : '2j_VBF_ee_in/events/histo_DY' ,
                                               'RNum' : '2j_VBF_uu_out/events/histo_DY' ,
                                               'RDen' : '2j_VBF_uu_in/events/histo_DY' ,
                                             } ,
                                   } , 
                     }
 
#DYestim = {}


DYestim['hww2l2v_13TeV_2016_0jee'] = {
                                 'rinout'  : 'DYmva0p8' ,
                                 'rsyst'   : 0.02 , 
                                 'ksyst'   : 0.01 , 
                                 'njet'    : '0j' , 
                                 'flavour' : 'ee' ,
                                 'DYProc'  : 'DY' ,
                                 'SFin'    : 'hww2l2v_13TeV_2016_DYin_0jee' ,
                                 'SFinDa'  : 'DATA',
                                 'SFinMC'  : ['VZ','Vg','VgS'],
                                 'DFin'    : 'hww2l2v_13TeV_2016_DYin_0jdf' ,
                                 'DFinDa'  : 'DATA' ,
                                 'DFinMC'  : ['VZ','Vg','VgS'],
                                 'NPname'  : 'DYeenorm0j' , 
                                 'AccNum'  : 'hww2l2v_13TeV_2016_0jee_HAccNum/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_2016_0jee_AccDen/events/histo_DY',
                                 'asyst'   : 0.03 , 
                                } 

DYestim['hww2l2v_13TeV_2016_0jmm'] = {
                                 'rinout'  : 'DYmva0p8' ,
                                 'rsyst'   : 0.05 , 
                                 'ksyst'   : 0.03 , 
                                 'njet'    : '0j'    ,
                                 'flavour' : 'mm' ,
                                 'DYProc'  : 'DY' ,
                                 'SFin'    : 'hww2l2v_13TeV_2016_DYin_0jmm' ,
                                 'SFinDa'  : 'DATA' ,
                                 'SFinMC'  : ['VZ','Vg','VgS'],
                                 'DFin'    : 'hww2l2v_13TeV_2016_DYin_0jdf' ,
                                 'DFinDa'  : 'DATA' ,
                                 'DFinMC'  : ['VZ','Vg','VgS'],
                                 'NPname'  : 'DYmmnorm0j' ,
                                 'AccNum'  : 'hww2l2v_13TeV_2016_0jmm_HAccNum/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_2016_0jmm_AccDen/events/histo_DY',
                                 'asyst'   : 0.01 , 
                                } 

DYestim['hww2l2v_13TeV_2016_1jee'] = {
                                 'rinout'  : 'DYmva0p8' ,
                                 'rsyst'   : 0.03 , 
                                 'ksyst'   : 0.02 , 
                                 'njet'    : '1j'    ,
                                 'flavour' : 'ee' ,
                                 'DYProc'  : 'DY' ,
                                 'SFin'    : 'hww2l2v_13TeV_2016_DYin_1jee' ,
                                 'SFinDa'  : 'DATA' ,
                                 'SFinMC'  : ['VZ','Vg','VgS'],
                                 'DFin'    : 'hww2l2v_13TeV_2016_DYin_1jdf' ,
                                 'DFinDa'  : 'DATA' ,
                                 'DFinMC'  : ['VZ','Vg','VgS'],
                                 'NPname'  : 'DYeenorm1j' ,
                                 'AccNum'  : 'hww2l2v_13TeV_2016_1jee_HAccNum/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_2016_1jee_AccDen/events/histo_DY',
                                 'asyst'   : 0.02 , 
                                } 

DYestim['hww2l2v_13TeV_2016_1jmm'] = {
                                 'rinout'  : 'DYmva0p8' ,
                                 'rsyst'   : 0.06 , 
                                 'ksyst'   : 0.05 , 
                                 'njet'    : '1j'    ,
                                 'flavour' : 'mm' ,
                                 'DYProc'  : 'DY' ,
                                 'SFin'    : 'hww2l2v_13TeV_2016_DYin_1jmm' ,
                                 'SFinDa'  : 'DATA' ,
                                 'SFinMC'  : ['VZ','Vg','VgS'],
                                 'DFin'    : 'hww2l2v_13TeV_2016_DYin_1jdf' ,
                                 'DFinDa'  : 'DATA' ,
                                 'DFinMC'  : ['VZ','Vg','VgS'],
                                 'NPname'  : 'DYmmnorm1j' ,
                                 'AccNum'  : 'hww2l2v_13TeV_2016_1jmm_HAccNum/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_2016_1jmm_AccDen/events/histo_DY',
                                 'asyst'   : 0.01 , 
                                } 

DYestim['hww2l2v_13TeV_2016_2jee'] = {
                                 'rinout'  : 'DYmva0p8' ,
                                 'rsyst'   : 0.05 ,
                                 'ksyst'   : 0.01 ,
                                 'njet'    : '2j'    ,
                                 'flavour' : 'ee' ,
                                 'DYProc'  : 'DY' ,
                                 'SFin'    : 'hww2l2v_13TeV_2016_DYin_2jee' ,
                                 'SFinDa'  : 'DATA' ,
                                 'SFinMC'  : ['VZ','Vg','VgS'],
                                 'DFin'    : 'hww2l2v_13TeV_2016_DYin_2jdf' ,
                                 'DFinDa'  : 'DATA' ,
                                 'DFinMC'  : ['VZ','Vg','VgS'],
                                 'NPname'  : 'DYeenorm2j' ,
                                 'AccNum'  : 'hww2l2v_13TeV_2016_2jee_HAccNum/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_2016_2jee_AccDen/events/histo_DY',
                                 'asyst'   : 0.01 ,
                                }

DYestim['hww2l2v_13TeV_2016_2jmm'] = {
                                 'rinout'  : 'DYmva0p8' ,
                                 'rsyst'   : 0.02 ,
                                 'ksyst'   : 0.03 ,
                                 'njet'    : '2j'    ,
                                 'flavour' : 'mm' ,
                                 'DYProc'  : 'DY' ,
                                 'SFin'    : 'hww2l2v_13TeV_2016_DYin_2jmm' ,
                                 'SFinDa'  : 'DATA' ,
                                 'SFinMC'  : ['VZ','Vg','VgS'],
                                 'DFin'    : 'hww2l2v_13TeV_2016_DYin_2jdf' ,
                                 'DFinDa'  : 'DATA' ,
                                 'DFinMC'  : ['VZ','Vg','VgS'],
                                 'NPname'  : 'DYmmnorm2j' ,
                                 'AccNum'  : 'hww2l2v_13TeV_2016_2jmm_HAccNum/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_2016_2jmm_AccDen/events/histo_DY',
                                 'asyst'   : 0.01 ,
                                }

DYestim['hww2l2v_13TeV_2016_2jee_vbf'] = {
                                 'rinout'  : 'DYmva0p8' ,
                                 'rsyst'   : 0.08 ,
                                 'ksyst'   : 0.01 ,
                                 'njet'    : '2jVBF'    ,
                                 'flavour' : 'ee' ,
                                 'DYProc'  : 'DY' ,
                                 'SFin'    : 'hww2l2v_13TeV_2016_DYin_2jee_vbf' ,
                                 'SFinDa'  : 'DATA' ,
                                 'SFinMC'  : ['VZ','Vg','VgS'],
                                 'DFin'    : 'hww2l2v_13TeV_2016_DYin_2jdf_vbf' ,
                                 'DFinDa'  : 'DATA' ,
                                 'DFinMC'  : ['VZ','Vg','VgS'],
                                 'NPname'  : 'DYeenorm2jVBF' ,
                                 'AccNum'  : 'hww2l2v_13TeV_2016_2jee_vbf_HAccNum/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_2016_2jee_vbf_AccDen/events/histo_DY',
                                 'asyst'   : 0.02 ,
                                }

DYestim['hww2l2v_13TeV_2016_2jmm_vbf'] = {
                                 'rinout'  : 'DYmva0p8' ,
                                 'rsyst'   : 0.02 ,
                                 'ksyst'   : 0.03 ,
                                 'njet'    : '2jVBF'    ,
                                 'flavour' : 'mm' ,
                                 'DYProc'  : 'DY' ,
                                 'SFin'    : 'hww2l2v_13TeV_2016_DYin_2jmm_vbf' ,
                                 'SFinDa'  : 'DATA' ,
                                 'SFinMC'  : ['VZ','Vg','VgS'],
                                 'DFin'    : 'hww2l2v_13TeV_2016_DYin_2jdf_vbf' ,
                                 'DFinDa'  : 'DATA' ,
                                 'DFinMC'  : ['VZ','Vg','VgS'],
                                 'NPname'  : 'DYmmnorm2jVBF' ,
                                 'AccNum'  : 'hww2l2v_13TeV_2016_2jmm_vbf_HAccNum/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_2016_2jmm_vbf_AccDen/events/histo_DY',
                                 'asyst'   : 0.03 ,
                                }
