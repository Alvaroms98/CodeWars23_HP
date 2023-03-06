f = float(input())
c = float(input())
vr = float(input()) * 1000/3600
vs = float(input()) * 1000/3600

def doppler_freq(f:int, c: int, vr: int, vs: int) -> float:
    return f * (c + vr) / (c + vs)

result = round(doppler_freq(f,c,vr,vs),2)
print("{:.2f} Hz".format(result))