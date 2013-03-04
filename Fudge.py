def Fudge(czz, f):
    czz_4e = czz[0] * f
    czz_4mu = czz[1] * f
    czz_2e2mu = czz[2]
    czz_4l = (czz_4e + czz_4e + 2* czz_2e2mu)/4
    print czz_4e, czz_4mu, czz_2e2mu, czz_4l
