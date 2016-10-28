#cuts

#cuts = {}

supercut = 'std_vector_lepton_pt[0]>25 && std_vector_lepton_pt[1]>20 \
            && std_vector_lepton_pt[2]<10 \
            && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] < 0) \
            && mll>12  \
            && metPfType1 > 20 \
            && mpmet > 20 \
            && ptll > 30 \
            && mth > 60 \
            && mll < 100 \
            && drll < 1.5 \
            && mtw2 > 100 \
            && mth > 200 \
            && ((abs(std_vector_lepton_flavour[0])!=abs(std_vector_lepton_flavour[0])) || (abs(mll-91)>15)) \
            && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.715 ) \
            && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.715 ) \
            && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.715 ) \
            && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.715 ) \
            && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.715 ) \
            && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.715 ) \
            && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.715 ) \
            && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.715 ) \
            && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.715 ) \
            && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.715 ) \
'

cuts['monoH_Alberto_ll'] = 'njet >= 0 \
            && metTtrk > 100 \
            && dphilmet1 > 2.6 \
            && dphilmet2 > 2.6 \
            && drll < 0.8 \
            && mtw1 > 160 \
            && metTtrk > 100 \
'

# cuts['monoH_Alberto_em'] = 'njet >= 0 \
#             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*13) \
#             && mpmet > 100 \
#             && dphilmet1 > 2.6 \
#             && dphilmet2 > 2.6 \
#             && drll < 0.8 \
#             && mtw1 > 160 \
#             && metTtrk > 100 \
# '


# 11 = e
# 13 = mu
# 15 = tau

