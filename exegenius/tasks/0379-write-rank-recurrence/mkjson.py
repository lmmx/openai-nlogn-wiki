import re,json
p='/home/user/e2e-run/exegenius/tasks/0379-write-rank-recurrence.answer.md'
t=open(p).read()
s=re.sub(r'\s*<cite[^>]*>.*?</cite>','',t,flags=re.S)
def span(start,end):
    i=s.index(start); j=s.index(end,i)+len(end)
    q=s[i:j]; assert '\n' not in q, q
    return q
def sent(start,end):
    i=t.index(start); j=t.index(end,i)+len(end); q=t[i:j]; assert '<cite' not in q and '\n' not in q; return q
d={
 "symbols":[
  {"symbol":"f","name":"call parameter","meaning":"The parameter of a recursive call: the number of digits per interchanged chunk, or the number of selected axes of a layer.","relation":"direct",
   "quote":sent("A call acts on a stream","selected axes of a layer.")},
  {"symbol":"\\mathcal C","name":"time per unit volume","meaning":"The running time of a call at a given parameter, divided by the volume of its stream.","relation":"direct",
   "quote":sent("Let $\\mathcal C(f)$","its stream's volume.")},
  {"symbol":"j","name":"recursion depth","meaning":"The number of recursion levels below the top call, indexing the terms of the unrolled sum; here not a stage number.","relation":"count",
   "quote":sent("Unrolling $\\log_m f$ levels","(s/W)^j\\big)$.")},
  {"symbol":"\\eta","name":"relative rank deficit","meaning":"The relative amount (Wm-s)/(Wm) by which the number of smaller calls falls short of Wm; here not the prime distance of the parameter-choice page.","relation":"direct",
   "quote":sent("Write $s/W=m(1-\\eta)$","(parameter-choice.md).")},
 ],
 "relations":[
  {"prerequisite":"subspace-labels","predicate":"gets the strict inequality from",
   "quote":sent("The recursion gets the strict inequality","its dimension change.")}
 ],
 "derivations":[
  {"step":"S1.0","quote":span("A call at parameter $mf$ cuts each chunk","total rank of the edge changes.")},
  {"step":"S1.4","quote":span("Later pages need an explicit rational exponent","with $0<\\tau=\\sigma<1$.")},
 ]
}
json.dump(d,open('/home/user/e2e-run/exegenius/tasks/0379-write-rank-recurrence.answer.json','w'),indent=1,ensure_ascii=False)
print(json.dumps(d["derivations"],indent=1,ensure_ascii=False))
