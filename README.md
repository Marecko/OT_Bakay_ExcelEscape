# OT_Bakay_ExcelEscape
Projekt ku skúške z OT

**Autor**: Marek Bakay

**Vybraná téma**: Color as a gameplay feature - farba ako herná mechanika.

---
## **1. Úvod**
Navrhnutá hrá slúži ako projekt ku skúške z predmetu Objektové technológie. Vztvorená hra spĺňa požiadavky pre tému :Color as a gameplay feature - farba ako herná mechanika. V hre hráč ovláda postavičku ktorá 
interaguje s prostredím podla farby ktorú má. Úlohou je pozbierať všetky hviezdičky a dostať sa k cielu


### **1.1 Inšpirácia**
<ins>**PewDuckPie - On the Run**</ins>
PewDuckPie - On the Run je fanmade hra pre PewDiePie-ia ktorá má za úlohu nahnevať hráča. Sú v nej ukryté rôzne nástrahy a preto hráč nevie nikdy čo očakávať. Princíp hry je jednoduchý: Preskákať prekážky a dostať sa na koniec levelu čo však nieje také priamočiare vďaka spomínaným skrytým nástrahám.


<p align="center">
  <img src="https://github.com/Marecko/OT_Bakay_ExcelEscape/blob/main/assets/New%20folder/pewdiepie_rage.png" alt=PewDuckPie - On the Run">
  <br>
  <em>Obrázok 1 Ukážka hry - PewDuckPie - On the Run</em>
</p>

<ins>**Fireboy And Watergirl**</ins>

Fireboy And Watergirl je hra pre dvoch hráčov (FireBoy a WaterGirl) kde postavičky ovládané hráčom musia presť rôzne hlavolamy aby sa dostali k cielu. A podla ich farby (Červená(Fire) a Modrá(Water)) majú rôzne úlohy v každom leveli

<p align="center">
  <img src="https://github.com/Marecko/OT_Bakay_ExcelEscape/blob/main/assets/New%20folder/fireboyandwatergirl.jpg" alt="Fireboy And Watergirl">
  <br>
  <em>Obrázok 2 Ukážka hry Fireboy And Watergirl</em>
</p>

### **1.2 Herný zážitok**
Cieľom hry je aby hráč pozbieral v kaďom levli všetky hviezdičky a dostal sa k cielu(dvere). Na to však musí využiť rôzne farby svojej postavy ayb vedel navigovať level. 


### **1.3 Vývojový softvér**
- **Pygame-CE**: zvolený programovací jazyk.
- **PyCharm 2024.1**: vybrané IDE.
- **Excel**: program na prácu s tabuľkami a dátami.
- **Pislekapp.com**: nástroj na vytváranie vlastných spritov.
- **Youtube mp3 convertor**: prekladač youtube videí do mp3 formátu (len zvuk).

---
## **2. Koncept**

### **2.1 Prehľad hry**
Hráč ovláda svoju postavu a snaží sa pozbierať hviezdičky a dostat sa na koniec. Môže zbierať checkpointy aby pri jeho smrti nemusel opakovať celý level od začiatku ale iba určitú časť.
Hráč použiva schonosť meniť farby svojej postavičky aby neumrel/prešiel cez/Išiel po rôzne zafarbených plaformách.


### **2.2 Interpretácia témy (Color as a gameplay feature)**
**Color as a gameplay feature** - hráč využíva rôzne farby ktoré spolu interagujú rôznymi spôsobmi. 



### **2.3 Základné mechaniky**
- **Políčka**: V hre sú rôzno-farebné políčka po čiernych môže vždy chodit a farebné (Červená, Zelená, Modrá) ktoré majú iné vlatnosti podla farby hráča
- **False Políčka**: Políča ktoré takmer nieje rozoznať od obyčajných a hráč s nimi nijak nedokáže interagovať.
- **Menenie farby hráča**: Hráč môže mať 3 farby (Červená, Zelená, Modrá) a podla farby políčka sa udejú rôzne udalosti.
  <p align="center">
  <img src="https://github.com/Marecko/OT_Bakay_ExcelEscape/blob/main/assets/New%20folder/Interakcie.png" alt="ExcelInteractions">
  <br>
  <em>Obrázok 3 Tabulka Interakcií</em>
  </p>                  
- **Hviezdičky**: hráč zbiera počas precchádzania levelu hviezdičky a keď nazbiera všetky v určitom levli tak sa mu otvoria "dvere" od ďalšieho levelu
- **Pichliače**: ak sa hráč dotkne pichliaču automaticky umiera a vracia sa buď na začiatok levlu alebo na posledných checkpoint


### **2.4 Návrh tried**
- **Game**: trieda, v ktorej sa bude nachádzať hlavná herná logika (úvodná obrazovka, herná slučka, vyhodnotenie hry, ...).
- **Player**: trieda reprezentujúca hráča, ovládanie hráča, vykreslenie postavy a schopnosti.


---
## **3. Grafika**

### **3.1 Interpretácia témy (Swarms - príklad témy)**
Pre dobrý zážitok z mechaniky menenia farieb je potrebné aby farby boli lahko rozlíšitelne preto boli použité 3 základne farby (RGB) aj pre postavičku aj pre políčka

<p align="center">
  <img src="https://github.com/Marecko/OT_Bakay_ExcelEscape/blob/main/assets/panacik/panacikred_0.png" alt="RED">
  
  <img src="https://github.com/Marecko/OT_Bakay_ExcelEscape/blob/main/assets/panacik/panacikgreen_0.png" alt="GREEN">
  
  <img src="https://github.com/Marecko/OT_Bakay_ExcelEscape/blob/main/assets/panacik/panacikblue_0.png" alt="BLUE">
  <br>
  <em>Obrázok 4 Ukážka sprite-ov hráča</em>
</p>

### **3.2 Dizajn**
V hre boli použité vytvorené assety na stránke Piskel (https://www.piskelapp.com/p/create/sprite) 
Levely boli dizajnované pomocou Excelu s použitím Modulov a Makier(Priložené v repozitári)

<p align="center">
  <img src="https://github.com/Marecko/OT_Bakay_ExcelEscape/blob/main/assets/New%20folder/level_excel.png" alt="Level Excel">
  <br>
  <em>Obrázok 5 Ukážka dizajnu levelu</em>
</p>

---
## **4. Zvuk**

### **4.1 Hudba**
Výber hudby bol jasný: 8-bit. Využil som video od Rymdreglage (https://www.youtube.com/watch?v=0sNxRji1STg) ktorý vytvorili takmer nespočetné množstvo hudieb.


---
## **5. Herný zážitok**

### **5.1 Používateľské rozhranie**
Používatelské rozhranie hráča informuje o jeho úmrtiach, Počtu nazbieraných hviezdičiek a ukazuje mu pomocnú schému farieb

### **5.2 Ovládanie**
<ins>**Klávesnica**</ins>
- **Šípky**: pohyb hráča po mape.
- **Klávesy 1 2 3**: Zmena farieb.

