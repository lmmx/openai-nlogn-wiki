import json, re, sys
base='exegenius/tasks/0016-write-rank-saving-recurrence'
t=open(base+'.answer.md').read()
def find(start, end):
    i=t.index(start); j=t.index(end,i)+len(end)
    return t[i:j]
def sent(start, end):
    s=find(start,end)
    assert '<cite' not in s, s
    return s
q_e=sent("The parameter $e$ counts","Euler's number here).")
q_mk=sent("Each level cuts","the number of levels.")
q_VW=sent("Let $V$ be","(linear-network.md).")
q_s=sent("The network takes its frames from","below $Wm$")
q_F=sent("For the address interchange everything else","obeys")
q_a=sent("Unrolling with $a=s/W$","otherwise.")
q_eta=sent("Let $\\eta=","$s/W=m(1-\\eta)$.")
q_N=sent("The label counts give","each data bank.")
q_tau=sent("Let $\\tau<1$","<m^\\tau$.")
q_sigma=sent("Take $\\tau=\\sigma","complex recurrence.")
q_frames=sent("By [frames on wire arrays]","that edge's stream.")
q_streams=sent("A call deals whole rows","costing $O(V)$.")
d1=sent("Take $\\tau=\\sigma","<1$.")
ans={
 "symbols":[
  {"symbol":"e","name":"procedure parameter","meaning":"The number of digits in each of the two address chunks being swapped, or the number of selected address bits in a butterfly layer.","relation":"count","quote":q_e},
  {"symbol":"m","name":"level split factor","meaning":"The number of equal pieces, 10^6, into which one level of recursion cuts the parameter.","relation":"count","quote":q_mk},
  {"symbol":"k","name":"recursion depth","meaning":"The number of recursion levels, with e = m^k.","relation":"count","quote":q_mk},
  {"symbol":"V","name":"logical volume","meaning":"The logical volume of the array a call works on.","relation":"direct","quote":q_VW},
  {"symbol":"W","name":"network width","meaning":"The number of wires of the fixed linear exchange network, which is also the number of role streams.","relation":"count","quote":q_VW},
  {"symbol":"s","name":"total edge rank","meaning":"The total number of smaller recursive calls made over all edges of the network at one level.","relation":"count","quote":q_s},
  {"symbol":"F_k","name":"cost per volume","meaning":"An upper bound on running time divided by logical volume at parameter m^k.","relation":"direct","quote":q_F},
  {"symbol":"a","name":"per-level factor","meaning":"The ratio s/W by which each level multiplies the cost per volume.","relation":"direct","quote":q_a},
  {"symbol":"\\eta","name":"relative rank deficit","meaning":"The fraction (Wm - s)/(Wm) by which the number of smaller calls falls short of Wm.","relation":"direct","quote":q_eta},
  {"symbol":"N","name":"data bank size","meaning":"The number of wires in each of the two data banks of the network.","relation":"count","quote":q_N},
  {"symbol":"\\tau","name":"interchange exponent","meaning":"An exponent below one with s/W < m^tau, which becomes the exponent of the cost; the page fixes it as 1 - 2^{-50}.","relation":"direct","quote":q_tau},
  {"symbol":"\\sigma","name":"complex exponent","meaning":"The exponent 1 - 2^{-50} bounding the complex-network (butterfly layer) recurrence.","relation":"direct","quote":q_sigma},
 ],
 "relations":[
  {"prerequisite":"subset-intersection-labels","predicate":"takes its frames from","quote":q_s},
  {"prerequisite":"common-frame-principle","predicate":"cancels intermediate frames by","quote":q_frames},
  {"prerequisite":"elementary-stream-ops","predicate":"deals rows into role streams by","quote":q_streams},
 ],
 "derivations":[
  {"step":"S4.4","quote":d1},
 ]
}
json.dump(ans,open(base+'.answer.json','w'),indent=1,ensure_ascii=False)
print("ok")
