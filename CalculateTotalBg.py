import AddInQuad

channels = ["EEEE", "EEMM", "MMMM", "LLLL"]

# central stat_up, stat_down, sys
dd_bg_est = {
        "Seven" : {
            "ZZ" : {
                "EEEE" : [ 0.33, 0.63, 0.54, 0.06],
                "MMMM" : [ 0, 0.68, 0.76, 0.15]
                "EEMM" : [ 0.53 ,1.16,0.77,0.25],
                "LLLL" : [ 0.15,1.26,1.08,0.35],
                },
            "ZZs" :  {
                [  3.45, 1.61, 1.55m 0.19 ],
                [  -1.33, 1.21, 1.12, 0.27],
                [  8.15, 2.88, 2.31, 0.55], 
                [  10.26, 3.19, 2.81m 0.63]
                }
            }
        }

# central stat frac_syst
ired_bg_est = {
        "Seven" : {
            "ZZ" : {
                "EEEE" : [ 0.09, 0.02, 0.077],
                "MMMM" : [ 0.14, 0.02, 0.030],
                "EEMM" : [ 0.20, 0.03, 0.042],
                "LLLL" : [ 0.43, 0.04, 0.039],
                },
            "ZZs" :  {
                "EEEE" : [  0.25, 0.03, 0.083],
                "MMMM" : [  0.34, 0.04, 0.031],
                "EEMM" : [  0.58, 0.05, 0.043], 
                "LLLL" : [  1.17, 0.07, 0.040]
                }
            }
        }

for analysis in dd_bg_est.keys():

    for selection in dd_bg_est[analysis].keys():

        for channel in dd_bg_est[analysis][selection].keys():

            dd_est = dd_bg_est[analysis][selection][channel]
            ired_est = ired_bg_est[analysis][selection][channel]

            central = dd_est[0] + ired_est[0]
            stat_up = AddInQuad.AddInQuad([dd_est[1], ired_est[1]])
            stat_down = AddInQuad.AddInQuad([dd_est[2], ired_est[1]])
            syst = AddInQuad.AddInQuad([dd_est[3], ired_est[0] * ired_est[2]])

            ired_central = ired_est[0]
            ired_stat = ired_est[1]
            ired_syst = ired_est[0] *  ired_est[2]

            print "ZZ%sTeVTotalBgEst%s%s{%.1f}" % (analysis, selection, channel, round(central,1))
            print "ZZ%sTeVTotalBgEstStat%s%s{\errAsym{%.1f}{%.1f}}" % (analysis, selection, channel, round(stat_up,1), round(stat_down,1))
            print "ZZ%sTeVTotalBgEstSyst%s%s{\errSym{%.1f}}" % (analysis, selection, channel, round(syst,1))

            print "ZZ%sTeVBgEstIred%s%s{\ZZ%sTeVBgEstIredCentral%s%s\;\ZZ%sTeVBgEstIredSyst%s%s\;\ZZ%sTeVBgEstIredStat%s%s}" % (analysis, selection, channel, analysis, selection, channel,analysis, selection, channel)
            print "ZZ%sTeVBgEstIredCentral%s%s{%.1f}" % (analysis, selection, channel, round(ired_central,1))
            print "ZZ%sTeVBgEstIredSyst%s%s{\errSym{%.1f}}" % (analysis, selection, channel, round(ired_stat,1))
            print "ZZ%sTeVBgEstIredStat%s%s{\errSym{%.1f}}" % (analysis, selection, channel, round(ired_stat,1))

