# Prints the map of INDIA

string = 's-}=o3}=m8}=j>}=i@}=n>2!}=p@\'-}=t<$1}=tT}=wP}=vQ}=tR}=qV}=pS}=qR}=rJ}=rK}=rJ}=rJ}=rL}=vL}=xK}=yJ}=' \
      '~:""}=Y=F9}=X=F:}=zB}=zB}=zC}=yC}=zH}=vN}=tT}=sU}=s[}=rZz=B!}=n\\p=B!\'%}=m\\p=B1}=l\\q=B1}=' \
      'i_m=B3}=i_i=BA}=f`i=BD}=dbg=BD}=bhb=BD}=`o~E}=Q!)s_"8M}=P"${]!8H}=NK=_W!<@}=LS=_O$<?}=JW=_L$><}=If=_?%7>}=' \
      'Ig=_?]}=Oj=_6^}=Os=_,!!X}=Nr=r\'Q}=Np=p/K}=Op=p/J}=So=o-H}=Tq=q(K}=Tq=q>4}=U~=_F0}=V{=_F0}=Wy=_E2}=O!$k=n>6}=' \
      '@{={8/}=<~=~62}=>{={8$#(}=>|=|8#$\'}=?|=|8!$\'}=@{={9 %$}=A(#{=n?%}=D!&{=n@#}=Lw=w@#}=Gy=yA"}=D{={}=B;$g=n}=' \
      'E8!j=n}=G7"^=n}=H6#Z=n}=J2$U=n}=K.&T=n}=M&.S=n}=R 0S=n}=ed=_}=dc=_}=cc=_}=c`=_}=c^=_}=cY=_}=cT=_}=cS=_}=dP=_}=' \
      'cO=_}=dM=_}=dK=_}=dI=_}=eG=_}=fC=_}=fA=_}=g>=_}=g|}=gy}=hr}=hu}=ht}=hs}=ii}=jg}=jg}=l^}=k^}=l[}=lZ}=oW}=pW}' \
      '=qW}=''qV}=sT}=tT}=tT}=tU}=sU}=tT}=uT}=vR}=vQ}=wP}=wM}=yJ}={H}=|G}=zG}=~F}=~F}=W=FE}=W=FE}=X=FC}=Y=F>}=Z=F<}' \
      '=[=F9}=''\\=F6}=\\=F6}=\\=F8}=]=F/}=^=F,}=^=F,}=_=F*}=a=F\'}'

x = 1
# character used to print
while True:
    c = input('Enter the character which you want to use for printing the map:\n')
    if len(c) == 0:
        print('Please enter a character')
        continue
    elif len(c) > 1:
        print('Only {} will be used'.format(c[0]))
        c = c[0]
        break
    else:
        break


for e in string:
    if e == "}":
        print()
        x += 1
    elif e == "=":
        x += 1
        continue
    else:
        if x % 2 == 0:
            for i in range(ord(e)-30):
                print(c, end='')
            i = 0
            x += 1
        else:
            for i in range(ord(e)-30):
                print(" ", end='')
            i = 0
            x += 1
