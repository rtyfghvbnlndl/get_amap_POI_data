import re
import math
def iflen(bpo):
    apo='119.281123, 26.056889'

    ax=float(re.findall(r'\d*\.\d*',apo)[0])
    ay=float(re.findall(r'\d*\.\d*',apo)[1])
    bx=float(re.findall(r'\d*\.\d*',bpo)[0])
    by=float(re.findall(r'\d*\.\d*',bpo)[1])
    lenth=math.sqrt(abs(ax-bx)**2+abs(ay-by)**2)
    print(lenth)
    lenmax=0.00499292189003869*2
    if lenth<=lenmax:
        return lenth
    else :return ''
