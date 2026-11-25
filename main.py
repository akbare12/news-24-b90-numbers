import os, textwrap
from PIL import Image, ImageDraw, ImageFont
W,H=1024,1024; BG=(247,241,222); INK=(17,17,17); RED=(176,30,36); NAVY=(22,50,79); TEAL=(18,110,105); GOLD=(176,124,24); GREEN=(27,110,52); BLUE=(27,84,150); GREY=(90,90,90); LAND=(196,210,150); SEA=(214,231,240)
def F(p,s):
    try: return ImageFont.truetype(p,s)
    except Exception: return ImageFont.load_default()
SERIF="/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"; SANS="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"; SANSB="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
def fb(s): return F(SANSB,s)
def fs(s): return F(SANS,s)
def fser(s): return F(SERIF,s)
def wrap(d,t,font,mw):
    words=t.split(); lines=[]; cur=""
    for w in words:
        x=(cur+" "+w).strip()
        if d.textlength(x,font=font)<=mw: cur=x
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines
def para(d,x,y,t,font,mw,lh,fill=INK):
    ls=wrap(d,t,font,mw)
    for i,l in enumerate(ls): d.text((x,y+i*lh),l,font=font,fill=fill)
    return y+len(ls)*lh
def chip(d,x,y,label,fill):
    f=fb(8); w=d.textlength(label,font=f)+10; d.rounded_rectangle([x,y,x+w,y+13],radius=3,fill=fill); d.text((x+5,y+2),label,font=f,fill=(255,255,255)); return x+w+4
def scene(d,x,y,w,h,kind):
    d.rectangle([x,y,x+w,y+h],fill=NAVY if kind in (1,4) else (TEAL if kind in (2,5,9) else (128,40,40) if kind==3 else (70,90,110) if kind in (6,11,12) else (40,70,110) if kind==7 else (90,70,40) if kind==8 else (60,90,60) if kind==10 else (120,60,90)))
    if kind==1:
        d.rectangle([x+18,y+30,x+52,y+h],fill=(30,35,60)); d.rectangle([x+60,y+8,x+92,y+h],fill=(45,55,90)); d.polygon([(x+60,y+8),(x+76,y-2),(x+92,y+8)],fill=(45,55,90)); d.rectangle([x+100,y+42,x+128,y+h],fill=(30,35,60))
        for yy in range(y+16,y+h-6,10):
            for xx in (x+66,x+78):
                d.rectangle([xx,yy,xx+5,yy+5],fill=(255,210,90))
        d.ellipse([x+150,y+12,x+190,y+42],fill=(200,200,200)); d.ellipse([x+170,y+28,x+215,y+58],fill=(170,170,170))
    elif kind==2:
        d.rectangle([x+10,y+55,x+w-10,y+h],fill=(140,30,30)); d.rectangle([x+30,y+30,x+70,y+55],fill=(160,40,40)); d.polygon([(x+22,y+32),(x+50,y+12),(x+78,y+32)],fill=(200,60,50)); d.rectangle([x+120,y+40,x+180,y+h-8],fill=(255,255,255)); d.rectangle([x+128,y+48,x+172,y+56],fill=RED); d.rectangle([x+128,y+62,x+172,y+68],fill=(120,120,120)); d.rectangle([x+128,y+74,x+160,y+80],fill=(120,120,120))
    elif kind==3:
        d.rectangle([x+10,y+45,x+w-10,y+h],fill=(220,220,210))
        for cx in (x+28,x+62,x+96,x+130):
            d.rectangle([cx,y+45,cx+10,y+h],fill=(180,180,170))
        d.rectangle([x+8,y+38,x+150,y+48],fill=(150,150,140)); d.ellipse([x+255,y+10,x+295,y+40],fill=(200,170,60))
    elif kind==7:
        d.rectangle([x+10,y+28,x+w-10,y+h-6],fill=(255,255,255))
        for i,px in enumerate((x+22,x+52,x+82,x+112,x+142)):
            d.line([(px,y+h-14),(px,y+70-i*8)],fill=NAVY,width=3)
        d.line([(x+10,y+40),(x+60,y+52),(x+110,y+30),(x+160,y+18)],fill=RED,width=3); d.ellipse([x+150,y+10,x+165,y+25],fill=RED)
    elif kind==13:
        d.rectangle([x+60,y+30,x+72,y+h-10],fill=(230,230,230)); d.polygon([(x+54,y+32),(x+66,y+8),(x+78,y+32)],fill=(220,60,50)); d.ellipse([x+150,y+18,x+210,y+78],fill=(140,180,220)); d.ellipse([x+165,y+32,x+195,y+62],fill=(60,90,140)); d.rectangle([x+120,y+70,x+150,y+78],fill=(200,200,200))
    else:
        d.rectangle([x+12,y+14,x+w-12,y+h-10],fill=(255,255,255)); d.rectangle([x+18,y+20,x+w-18,y+26],fill=RED); d.rectangle([x+18,y+32,x+90,y+38],fill=(90,90,90)); d.rectangle([x+18,y+44,x+120,y+50],fill=(150,150,150))
def main():
    im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im); d.rectangle([0,0,W,6],fill=RED)
    d.text((12,10),"THE WORLD ON ONE PAGE",font=fb(11),fill=RED)
    r=d.textlength("38 STORIES · 6 REGIONS · 13 FIELDS",font=fb(11)); d.text((W-12-r,10),"38 STORIES · 6 REGIONS · 13 FIELDS",font=fb(11),fill=INK)
    d.text((12,26),"Tuesday 24 November 2026",font=fser(33),fill=INK); d.line([(12,62),(W-12,62)],fill=RED,width=2)
    d.text((12,66),"Riyadh tower hit again  ·  Shanghai party chief probed  ·  Huawei guilty on 10 of 12 counts.",font=fb(12),fill=RED)
    regs=[("Europe",9,(22,50,79)),("Middle East",8,(176,30,36)),("Asia",8,(18,110,105)),("Africa",2,(176,124,24)),("Americas",7,(90,60,140)),("World/Space",4,(70,90,110))]; x=12; tot=38
    for name,n,col in regs:
        w=int(1000*n/tot); d.rectangle([x,86,x+w-2,104],fill=col); d.text((x+4,89),f"{name} {n}",font=fb(9),fill=(255,255,255)); x+=w
    nums=[("11","hurt in Riyadh"),("9","killed in Ukraine"),("50,018","Dow, first close"),("+8.99%","Taiex record"),("25","killed in Yemen"),("26","Cikande toll"),("10/12","Huawei guilty"),("96","drones at Ukraine")]
    d.text((12,110),"THE DAY IN NUMBERS",font=fb(10),fill=RED)
    for i,(n,lab) in enumerate(nums):
        cx=12+i*125; d.text((cx,122),n,font=fb(21),fill=NAVY); d.text((cx,145),lab,font=fs(8),fill=GREY)
    d.line([(12,160),(W-12,160)],fill=(180,170,150),width=1); d.text((12,164),"THE DAY IN UTC  —  00:30 Zelensky urges talks  ·  08:16 Hanoi blast  ·  10:42 Saudi strikes Yemen  ·  14:27 Riyadh tower hit  ·  16:51 Houthis 60 km from Aden  ·  18:58 Hormuz ship attack  ·  20:41 Huawei guilty.",font=fs(9),fill=INK)
    heroes=[
        (1,"1 RIYADH · MIDDLE EAST","CONFIRMED",GREEN,"Houthi drone hits Riyadh's tallest tower again, 11 hurt","A Houthi drone struck the PIF tower, Riyadh's tallest, for the second time in a week. At least 11 were hurt: 2 Saudis, 2 Indians, 3 Nepalis and 4 Egyptians.","(Saudi officials · wires)","11",46),
        (2,"2 SHANGHAI · ASIA","OFFICIAL",BLUE,"China probes Shanghai party chief Chen Jining","Chen Jining, 62, is probed for serious violations. He is the fourth Politburo member to fall in a probe this year, a shock at the top of the Party.","(CCDI · wires)","62",46),
        (3,"3 NEW YORK · AMERICAS","CONFIRMED",GREEN,"Huawei guilty on 10 of 12 counts","A US federal jury found Huawei guilty on 10 of 12 counts, including trade-secret theft and bank fraud. It was cleared of racketeering, with sentencing in Sep 2027.","(US court · wires)","10/12",32)]
    for kind,kick,chiplbl,chipcol,head,deck,src,giant,gs in heroes:
        hx=12+(kind-1)*338; scene(d,hx,182,326,96,kind); d.rectangle([hx,182,hx+326,182+96],outline=INK,width=1)
        gx=hx+205 if kind!=3 else hx+185; d.text((gx,200),giant,font=fb(gs),fill=(255,255,255),stroke_width=2,stroke_fill=INK)
        d.text((hx,284),kick,font=fb(10),fill=RED); chip(d,hx+225,284,chiplbl,chipcol); para(d,hx,300,head,fb(13),326,15); para(d,hx,332,deck,fs(10),326,13); d.text((hx,372),src,font=fs(8),fill=GREY)
    cards=[
        (4,"4 ZAPORIZHZHIA","REPORTED",GREY,"Russian attacks kill 9 across Ukraine in a day","Russian attacks killed 9 and wounded 81 in Ukraine. Kyiv said 96 drones were launched and 73 were downed.","(Ukraine officials · wires)"),
        (5,"5 CAS · SENEGAL","OFFICIAL",BLUE,"CAS hands Senegal back the AFCON title","CAS restored the Africa Cup title to Senegal after Morocco forfeited 3-0, turning the final into a 1-0 win.","(CAS · wires)"),
        (6,"6 HORMUZ","REPORTED",GREY,"IRGC attacks container ship in Hormuz","An IRGC attack hit a container ship in the Strait of Hormuz at 18:58 UTC, disabling its navigation near Khasab.","(UKMTO · wires)"),
        (7,"7 NEW YORK","CONFIRMED",GREEN,"Dow closes above 50,000 for the first time","The Dow closed at 50,018, its first close above 50,000. Taiwan's Taiex jumped a record 8.99% on the day.","(Market close · wires)"),
        (8,"8 REDMOND","REPORTED",GREY,"Microsoft declares 'Code Red' after historic outage","After a 24-hour outage, the worst in Exchange Online history, Microsoft declared Code Red.","(Reuters · wires)"),
        (9,"9 ESKISEHIR","REPORTED",GREY,"Turkish military helicopter crash kills 5","A Turkish military AS-532 helicopter crashed in Eskisehir, killing all 5 people on board.","(Turkish officials · wires)"),
        (10,"10 CARTAGENA","REPORTED",GREY,"Supermarket hostages: 25 held in Cartagena","Gunmen held 25 hostages in a Cartagena supermarket, releasing 5 elderly women, as landings paused 45 minutes.","(Colombia officials · wires)"),
        (11,"11 ADEN","REPORTED",GREY,"Houthis advance within 60 km of Aden","Houthi forces advanced to within 60 km of Aden, Yemen, in the latest push south toward the port city.","(Wires · officials)"),
        (12,"12 LAHJ","REPORTED",GREY,"Saudi strikes kill 25, wound 6 in Yemen","Saudi strikes on a bus and truck in Wadi Maabaq, Lahj, killed or left missing 25 people and wounded 6 others.","(Yemen officials · wires)"),
        (13,"13 JIUQUAN","OFFICIAL",BLUE,"China names first foreign astronaut for Tiangong","China named the Shenzhou-24 crew, including Muhammad Zeeshan Ali of Pakistan, the first foreign astronaut.","(CMSA · wires)")]
    for i,(n,kick,chiplbl,chipcol,head,deck,src) in enumerate(cards):
        cx=12+(i%5)*201; cy=396+(i//5)*138; scene(d,cx,cy,196,46,n); d.rectangle([cx,cy,cx+196,cy+46],outline=INK,width=1)
        d.text((cx,cy+52),kick,font=fb(8),fill=RED); chip(d,cx+128,cy+52,chiplbl,chipcol)
        para(d,cx,cy+68,head,fb(10),196,12); para(d,cx,cy+94,deck,fs(9),196,11); d.text((cx,cy+130),src,font=fs(7),fill=GREY)
    d.text((12,674),"THE WORLD · 13 STORIES PINNED",font=fb(11),fill=RED); d.text((714,674),"MAP KEY — 1 TO 13",font=fb(11),fill=RED)
    MX,MY,MW,MH=12,690,690,140
    d.rectangle([MX,MY,MX+MW,MY+MH],fill=SEA,outline=INK)
    def XY(lon,lat): return (MX+(lon+180)/360*MW, MY+(85-lat)/140*MH)
    conts=[[(-168,66),(-140,70),(-120,72),(-95,80),(-80,73),(-75,62),(-65,60),(-55,52),(-60,45),(-75,35),(-80,32),(-85,30),(-90,21),(-97,26),(-105,20),(-110,23),(-120,34),(-125,40),(-125,49),(-135,58),(-155,60)],[(-80,10),(-75,5),(-60,0),(-50,-5),(-35,-8),(-40,-20),(-48,-28),(-58,-35),(-65,-45),(-70,-52),(-73,-40),(-75,-20),(-80,-5)],[(-17,15),(-10,30),(0,35),(10,37),(20,32),(32,31),(35,28),(43,12),(51,11),(48,0),(40,-10),(35,-20),(32,-28),(20,-35),(15,-30),(12,-18),(8,4),(-8,5)],[(30,70),(50,70),(70,72),(90,75),(110,76),(130,72),(150,70),(170,66),(162,60),(158,52),(142,50),(140,40),(130,35),(127,33),(122,30),(120,25),(110,20),(105,10),(100,8),(95,15),(90,22),(85,20),(80,8),(75,8),(70,22),(60,25),(55,26),(50,29),(48,30),(40,35),(35,36),(30,36),(30,42)],[(-10,36),(-9,43),(-2,48),(0,50),(5,53),(8,57),(10,59),(18,56),(21,55),(24,58),(28,60),(30,62),(30,70),(20,70),(15,68),(12,65),(5,60),(0,55),(-5,50)],[(113,-22),(114,-30),(115,-35),(124,-33),(130,-32),(137,-35),(142,-38),(147,-39),(150,-37),(153,-32),(153,-27),(146,-19),(142,-11),(136,-12),(132,-12),(126,-14),(122,-17),(118,-20)]]
    for poly in conts: d.polygon([XY(lo,la) for lo,la in poly],fill=LAND,outline=(120,140,90))
    pins=[(1,24.7,46.7),(2,31.2,121.5),(3,40.7,-74.0),(4,47.8,35.2),(5,14.7,-17.4),(6,26.5,56.3),(7,40.9,-73.9),(8,47.7,-122.1),(9,39.8,30.5),(10,10.4,-75.5),(11,12.8,45.0),(12,13.1,44.9),(13,39.7,98.5)]
    off={7:(12,0),12:(12,-6),11:(-12,4)}
    for n,la,lo in pins:
        px,py=XY(lo,la); dx,dy=off.get(n,(0,0)); d.line([(px,py),(px+dx,py+dy)],fill=RED,width=1); d.ellipse([px+dx-8,py+dy-8,px+dx+8,py+dy+8],fill=RED,outline=(255,255,255)); d.text((px+dx-3,py+dy-6),str(n),font=fb(8),fill=(255,255,255))
    keys=["1 Riyadh · PIF tower","2 Shanghai · Chen probe","3 New York · Huawei","4 Zaporizhzhia · 9 killed","5 Dakar · AFCON title","6 Hormuz · ship attack","7 New York · Dow 50,018","8 Redmond · Code Red","9 Eskisehir · crash, 5 dead","10 Cartagena · 25 held","11 Aden · Houthis 60 km","12 Lahj · 25 killed","13 Jiuquan · Tiangong crew"]
    for i,k in enumerate(keys): d.text((714,690+i*10),k,font=fs(9),fill=INK)
    d.text((12,836),"ALSO ON TUESDAY 24 NOVEMBER — 25 MORE STORIES",font=fb(11),fill=RED)
    also=["14 Ankara: Haftar visits Turkey first time.","15 London: UK sanctions Houthis + 4 officials. OFFICIAL","16 Villavicencio: Car bomb injures 23.","17 Gaza: Israel kills Hamas security chief.","18 Baghdad: Iraq orders control of Kurdish oil. OFFICIAL","19 Gaza: Meningitis alert, 272 cases in Oct. OFFICIAL","20 DR Congo: Missing Cessna 208, rebels claim hit.","21 Hanoi: Hot-pot blast kills at least 6.","22 Gulf of Finland: Ukraine hits ship Sparta II.","23 Kuala Lumpur: Malaysia to return migrants. OFFICIAL","24 Ulleungdo: S. Korea shelter order, jets in ADIZ. OFFICIAL","25 Dhaka: Hasina plans return on 16 Dec.","26 The Hague: 14 nations back ICJ Myanmar ruling.","27 Jakarta: Indonesia nominates 2 VP candidates. OFFICIAL","28 Beijing: China sentences official Ma to death. OFFICIAL","29 Brussels: NATO vows defence vs space threat. OFFICIAL","30 Mexico City: US drone aided El Chapo capture; Mexico to try him (arrested Fri 20 Nov).","31 San Salvador: Bukele names 3 soldiers killed in Haiti. OFFICIAL","32 Ottawa: Pentagon rebukes Canada — only 41.9% of air fleet ready.","33 Washington: US adds Megaspeed to blacklist. OFFICIAL","34 Kyiv: Zelensky urges Ukraine-Russia-US-EU talks.","35 Ras Al Khaimah: Bus-truck crash kills 13.","36 London: England record 5,258 heat deaths. OFFICIAL","37 Kourou: Ariane 6 lofts 36 Amazon satellites. OFFICIAL","38 Cikande: Factory-fire toll rises to 26."]
    for i,a in enumerate(also):
        ax=12+(i//9)*338; ay=852+(i%9)*11; d.text((ax,ay),a,font=fs(8),fill=INK)
    d.rectangle([12,956,1012,992],fill=(255,235,235),outline=RED); d.text((18,959),"DATE CHECK — All stories above happened or were first reported Tue 24 Nov 2026. LEFT OUT (not 24 Nov): Hormuz mines (23 Nov) · Huang returns (23 Nov) · EU sanctions (23 Nov) · COP31 (22 Nov).",font=fs(9),fill=INK); d.text((18,974),"El Chapo arrested Fri 20 Nov · Cikande fire started Sat 21 Nov · Merkury sunk Sat 22 Nov. NOT YET: Shenzhou-24 launch Wed 25 Nov · Huawei sentencing Sep 2027 · MPR VP vote 11 Dec.",font=fs(9),fill=INK)
    d.text((12,998),"Sources: Saudi officials · CCDI · US court · CAS · UKMTO · CMSA · Reuters · AP · wires. CONFIRMED = 2+ outlets · OFFICIAL = on record · REPORTED = one outlet · CLAIM = one side only.",font=fs(8),fill=GREY); d.text((12,1010),"Scenes are drawn in code, not photographs. Wires read up to 23:00 UTC.",font=fs(8),fill=GREY)
    out=os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR","out"),"entry.png"); os.makedirs(os.path.dirname(out),exist_ok=True); im.save(out,optimize=True)
if __name__=="__main__": main()
