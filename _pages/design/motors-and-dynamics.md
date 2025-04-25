---
title: Motori i dinamika
author: admilara
date: 2025-04-23
category: Motori i dinamika
layout: post
mermaid: true
---

- Modeli tereta mogu se klasificirati u statičke i dinamičke. 

- Statički modeli predstavljaju teret s vremenski invarijantnim funkcijama napona 
i frekvencije. Često korišteni statički modeli su eksponencijalni i polinomni model tereta.

- Dinamički modeli tereta koriste trenutne i prošle vrijednosti napona i frekvencije
kako bi se što bolje prikazao teret. 
- Dinamika tereta trebala bi uključivati i dinamiku
asinkronih motora, **utjecaj tap-changer transformatora** i ponašanje tereta koji imaju 
sposobnost samo-restauracije (kao što su termostatski kontrolirani tereti).

- Dinamika motora posebno je bitna te se predlaže detaljno modeliranje većih motora.
- Dinamika asinkronih motora ovisi o njihovoj veličini (snazi) te mehaničkom teretu koji napajaju.
- Mali motori su skloniji preopterećenju i zastoju tijekom padova napona od srednjih i velikih motora. 

- Za potrebe dinamičkih proračuna, često se ide na najintuitivniji, a i najjednostavniji model 
**kompozitni model tereta**, koji u sebi sadrži statički dio (predstavljen polinomom) i 
dinamički dio (predstavljen nekim udjelom motora) 


### ERL - Exponential recovery load

- Kako je već rečeno, u proračunima stacionarnih stanja, motori se modeliraju kao
tereti konstantne snage. 
- U studijama naponske stabilnosti ne možemo na taj način modelirati motore.
    - Asinkroni motori imaju dinamičku interakciju sa sustavom u slučaju promjena napona
    - U slučaju pada napona asinkroni motor usporava jer gubi kinetičku energiju.
    - Kako bi povratio svoju brzinu, mora proizvesti veći moment, što znači da treba veću snagu.
    - S ozbirom da je napon pao, snagu može dobiti s većom strujom. 
    
- Karakter struje koju vuče motor u tom slučaju je kombinirani, struja ima i radnu i 
jalovu komponentu. 
    - Ako se gleda manja vremenska skala, karakter je pretežno reaktivan, što u trenutku 
    propada napona, dodatno povećava zahtjeve na jalovinu u sustavu te imamo pozitivnu povratnu vezu.
    - Ako je potpora sustavu, u vidu kondenzatora i generatora, nedovoljna, sustav se ne može 
    oporaviti i dolazi do propada napona. 
    
<div class="custom-block tip">
  <p class="custom-block-title">ZIP model</p>
  
  <p>Standardni ZIP model za modeliranje tereta definiran je kao polinom koji se sastoji od tri
  dijela - teret konstantne snage, teret konstantne struje i teret konstantne impedancije.</p>
</div>

\begin{equation}
    P = P_0 \left( \alpha_1 V^2 + \alpha_2 V + \alpha_3 \right)
    \tag{1}\label{P_static}
\end{equation}

\begin{equation}
    Q = Q_0 \left( \beta_1V^2 + \beta_2 V + \beta_3 \right)
    \tag{2}\label{Q_static}
\end{equation}

- Takav model tereta nema vremensku komponentu i ne može oslikati dinamičko
ponašanje, već samo konačni iznos u koji će se stacionirati P i Q. 

<div class="custom-block tip">
  <p class="custom-block-title">ERL (exponential recovery load)</p>
  
  <p>ERL modeliranje ima vremensku komponentu možerealnije oslikati ponašanje tereta, naravno ako su vremenske konstantne dobro odabrane.
  Takav model možemo opisati sljedećim jednadžbama.</p>
</div>


\begin{equation}
    P(t) = P_{stac}\left(V(t)\right) + \left(P_0 - P_{stac}\left(V(t)\right)\right) \cdot \exp^{-t \over T_p}
\end{equation}

\begin{equation}
    Q(t) = Q_{stac}\left(V(t)\right) + \left(Q_0 - Q_{stac}\left(V(t)\right)\right) \cdot \exp^{-t \over T_q}
\end{equation}

gdje su:
- $$P_0, Q_0$$ - iznosi radne i jalove snage prije poremećaja,
- $$P_{stac}, Q_{stac}$$ - statičke funkcije ovisne o naponu vezu (dakle, ZIP modeli),
- $$T_p, T_q$$ - vremenske konstante 

<div class="custom-block warning">
  <p>Iz ova dva seta jednadžbi očito je da se ZIP model automatski odaziva na promjenu napona, dok se u 
  ovom jednostavnom ERL modelu ipak opisuje nekakvo dinamičko ponašanje tereta prilikom promjene napona. 
  Koristeći ERL model moguće je i modelirati promjenu napona u vremenu.</p>
</div>
    
Na slici ispod dana je pojednostavljena vizualizacija odziva tereta na promjenu napona. 
Simuliran je pad napona sa 1 p.u. na 0.7 p.u. Iscrtkano su prikazan ZIP odziv za radnu i jalovu snagu, dok
je punom linijom prikazan ERL model (prema gore navedenim jednadžbama).

<figure>
  <img src="{{ site.baseurl }}/assets/gitbook/images/ERL-vs-ZIP.svg" width="800" alt="Odziv jednostavnog ERL i ZIP modela tereta">
</figure>
    
<hr>  
    
Gore navedene jednadžbe ne uzimaju u obzir jednu karakteristiku odziva motora, 
a to je instant promjena snage i potom oporavak do neke stacionarne vrijednosti.
Kao što je vidljivo na slici iznad, ovakav model pretpostavlja monotonu promjenu
do nove stacionarne vrijednosti, što u stvarnosti nije tako. 

U stvarnosti postoji početni propad $$\Delta P_0$$ uzrokovan nemogućnošću promjene
klizanja motora u trenutku pojave stepa napona. Detaljniji model naveden je u članku na linku [[1]](https://ieeexplore.ieee.org/document/221270).

Prema tom članku, mjerenjima je potvrđeno da se teret na step promjenu u naponu odaziva kao prema slici ispod (preuzeto iz članka).
Isti oblik odziva se može očekivati i od jalove snage. 

<figure>
    <img src="{{ site.baseurl }}/assets/gitbook/images/load-response-to-v-step.svg" width="500" alt="Odziv tereta na step promjenu napona">
</figure>    
    
Intuitivno to znači sljedeće - tijekom stepa, klizanje motora se ne može promijeniti,
pa teret izgleda statično - tako step napona uzrokuje step u snazi. Navodimo jednadžbe koje 
uzimaju u obzir tranzijentno ponašanje tereta.

\begin{equation}
    T_p {dP_d \over dt} + P_d = P_S(V) + k_p(V)
\end{equation}

gdje je:
- $$P_S(V)$$ - ZIP funkcija radne snage u stacionarnom stanju
- $$k_p(V)$$ - tranzijentni propad
- $$T_p$$ - vremenska konstanta oporavka
- $$P_d(t)$$ - stvarna radna snaga koju vuče teret

\begin{equation}
    k_p(V) = \lambda_p(V^2 - 1)
\end{equation}

\begin{equation}
    T_q {dQ_d \over dt} + Q_d = Q_S(V) + k_q(V)
\end{equation}

gdje je:
- $$Q_S(V)$$ - ZIP funkcija jalove snage u stacionarnom stanju
- $$k_q(V)$$ - tranzijentni propad
- $$T_q$$ - vremenska konstanta oporavka
- $$Q_d(t)$$ - stvarna jalova snaga koju vuče teret

\begin{equation}
    k_q(V) = \lambda_q(\\V^2 - 1)
\end{equation}

- Gore navedene jednadžbe su pojednostavljene da ne uključuju ovisnost o promjeni napona.
Takav oblik je dovoljan kako bi se prikazala dinamika tereta vidljiva u većini mjerenja.
- Problem je što za uhvatiti brze dinamičke promjene, kakve su kod indukcijski motora (klizanje i magnetski tok se jako brzo mijenjaju), 
ali takav model zahtjeva parametriranje prema stvarnim podatcima. 

\begin{equation}
    T_p {dP_d \over dt} + P_d = P_S(V) + k_p(V) + k_{pv}(V)\cdot {dV \over dt}
\end{equation}




\[1\]: D. J. Hill, ["Nonlinear dynamic load models with recovery for voltage stability studies"](https://ieeexplore.ieee.org/document/221270) 
in IEEE Transactions on Power Systems, vol. 8, no. 1, pp. 166-176, Feb. 1993, doi: 10.1109/59.221270.

   
    
    
    
    
    
    
    
    