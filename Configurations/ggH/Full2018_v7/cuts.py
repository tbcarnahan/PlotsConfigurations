# cuts

_tmp = [ 
     'mll>0.',
       ]

supercut = ' && '.join(_tmp)

def addcut(name, exprs):
    cuts[name] = ' && '.join(exprs)


_tmp = [
    'Lepton_pt[0] > 0.',
       ]

addcut('test', _tmp)

