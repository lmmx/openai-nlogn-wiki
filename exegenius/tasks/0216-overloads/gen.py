import json
same = {1,5,7-7,13,14,16,18,19,21,22,23,24,31,32,33,36,37,38,39,40,41,42,43,53,56,61,74,89,105,125,126,127,128,129,137,143,146,153,154,155,156,157,158,161,167,170,171,175,177,179,180,
        15,34,176,27,29}
same.discard(0)
# candidates 5 and 7: 5 same; 7 different
same.discard(7)
diff = {}
def d(nums, note, change=None):
    for n in nums:
        diff[n] = (note, change)

d([2], "Say on the radix-digit page that q is the number of digits of each input (the convolution length there is S), or use another letter; do not carry over q as the sequence length of the convolution page.")
d([3,4], "Keep q as the sequence length on the DFT/convolution page; on the stream-ops page say that q is the radix of a digit and not a sequence length, or rename it.")
d([6,7], "The page already says its q is a prime and not a sequence length; keep that remark (or use another letter for the prime base).")
d([8,12,112,113,114,149,150,151,152], "Use another letter for this quantity, or say on this page that b is not the lowest bit of the output index (butterfly page / meaning given in the binding).")
d([9,107,108,109,110,111,138,139,140,141,142,96,97,98,99], "Use another letter, or say on this page that B means something else here than on the other page.")
d([10], "Use another letter for the number of fields per group, or say that m is not an output index here.")
d([11], "Say that a is the rank of the matrix A here and not the offset added to a field, or use another letter.")
d([17,20], "Say that k here is a single coefficient or coordinate index, not an output index tuple, or use another letter.")
d([25,50,86,87,88,51], "Use another letter, or say that h here is not the other page's meaning of h.")
d([26], "Use another letter for the setup exponent, or say that g is not the second operand of the bilinear map.")
d([28,121,122,123,134,135,136,72], "Use another letter, or say that L here is not the other page's L.")
d([30], "The page already says u is the scaled digit array and not the integer; keep that remark or use another letter for the array.")
d([35], "The page already says c is a new meaning; keep the remark or rename the chunk-width exponent.")
d([44,45], "Say that F here is the time per unit volume, not a label space, or use another letter.")
d([46,62,60], "Use another letter, or say that j here is not the other page's j.")
d([47,67,68,173,174], "Use another letter, or say that u here is not an input sequence of the DFT.")
d([48,178], "Use another letter, or say that V here is a volume and not a label.")
d([49], "Use another letter, or say that p here is a prefix of an address, not the number of fractional bits.")
d([52,13+0] if False else [52], "Use another letter, or say that d is the second address chunk here, not the axis count.")
d([54,55,57-57+54,56-56+55] if False else [54,55], "Say that q is the digit radix here, not a sequence length, or use another letter.")
d([57], "Use another letter, or say that k here counts recursion levels, not the depth of a value.")
d([58,75], "Use another letter, or say that M here is the vertex matrix, not an address count.")
d([59], "Use another letter, or say that x is a stream row number here, not a vector of F.")
d([63], "The page already says v is not the triple count; keep the remark or use another letter.")
d([64,94,95], "Say that E here is not the first tensor factor, or use another letter.")
d([65], "The page already says k changes meaning; keep that remark or use another letter.")
d([66,191], "Say that c is not the other meaning of c, or use another letter.")
d([69,168,169], "Use another letter, or say that w is not the wire index/second integer meaning of the other page.")
d([70,71,160,162,163], "Say that R is not the scalar ring (or row count) here, or use another letter.")
d([73,103,104,147,148], "Use another letter, or say that K here is not the later tensor line / segment spacing.")
d([76], "Use another letter, or say that rho here is an offset, not a role map.")
d([77], "Use another letter, or say that g here is the gap, not a guard value.")
d([78,79,80,81,82], "Say that q is an address here, not a radix/sequence length, or use another letter.")
d([83,101,102], "Use another letter, or say that D here is not the other page's D.")
d([84,124,164,165,166], "Say that z is not the other page's z here, or use another letter.")
d([85], "Say that e here counts selected axes of a group (e = mf), not radix-q digits of a chunk, or use another letter.")
d([90], "Use another letter, or say that G is a matrix here, not the second tensor factor.")
d([91,92,93,182,183,184,185], "Use another letter, or say that A here is not the other page's A.")
d([100], "Use another letter, or say that nu here is an exponent of m, not a digit count.")
d([106,144], "Use another letter, or say that ell here is the log of the length, not the depth of a value.")
d([115,116,117,118,119,120], "Say that q is a number of whole chunks here, not the other page's q, or use another letter.")
d([145], "Use another letter, or say that eta here is a truncation error bound, not a relative deficit.")
d([159], "Use another letter, or say that gamma here is an exponent of a scale, not the initial central values.")
d([181], "Use another letter, or say that g_i is a margin, not a guard value.")
d([186,187,188], "Use another letter, or say that C here is a setup exponent, not the other page's C.")
d([189,190,192], "The page already says c is not the machine constant; keep that remark or rename.")
d([130], "Say on the subspace-labels page that T is a triple (a three-element subset) and not the padded size used on other pages, or use another letter for a triple.", "subspace-labels")
d([131,132,133], "Use another letter, or say that P here is the pointwise product, not a prefix count or subspace.")
d([12], "Say that b is the coefficient (1-i)/2 here, not a bit index, or use another letter.")
d([172], "Say that u here is the array from applying Phi to the digits, not the integer; the page already does, keep it.")
d([29] if False else [], "")

out=[]
for n in range(1,193):
    if n in diff:
        note,ch = diff[n]
        v = {"candidate":n,"same":False,"note":note}
        if ch: v["change"]=ch
    else:
        v = {"candidate":n,"same":True,"note":""}
        assert n in same, n
    out.append(v)
# sanity: same set vs computed
for n in same:
    assert n not in diff, n
json.dump({"verdicts":out}, open("/home/user/e2e-run/exegenius/tasks/0216-overloads.answer.json","w"), indent=1)
print(sum(1 for v in out if v["same"]))
