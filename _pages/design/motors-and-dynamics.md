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
    
> ##### **ZIP** model
> Standardni ZIP model za modeliranje tereta definiran je kao polinom koji se sastoji od tri
> dijela - teret konstantne snage, teret konstantne struje i teret konstantne impedancije
{: .block-tip }

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

> ##### **ERL** (exponential recovery load)
> modeliranje ima vremensku komponentu možerealnije oslikati ponašanje tereta, naravno ako su vremenske konstantne dobro odabrane.
> Takav model možemo opisati sljedećim jednadžbama
{: .block-tip }

\begin{equation}
    P(t) = P_{stac}\left(V(t)\right) + \left(P_0 - P_{stac}\left(V(t)\right)\right) \cdot \exp^{-t \over T_p}
\end{equation}

\begin{equation}
    Q(t) = Q_{stac}\left(V(t)\right) + \left(Q_0 - Q_{stac}\left(V(t)\right)\right) \cdot \exp^{-t \over T_q}
\end{equation}

gdje su:
    - $$P_0, Q_0$$ - iznosi radne i jalove snage prije poremećaja
    - $$P_{stac}, Q_{stac}$$ - statičke funkcije ovisne o naponu vezu (dakle, ZIP modeli)
    - $$T_p, T_q$$ - vremenske konstante 
    
> Iz ova dva seta jednadžbi očito je da se ZIP model automatski odaziva na promjenu napona, dok se u 
> ovom jednostavnom ERL modelu ipak opisuje nekakvo dinamičko ponašanje tereta prilikom promjene napona. 
> Koristeći ERL model moguće je i modelirati promjenu napona u vremenu.
{: .block-warning }
    
Na slici ispod dana je pojednostavljena vizualizacija odziva tereta na promjenu napona. 
Simuliran je pad napona sa 1 p.u. na 0.7 p.u. Iscrtkano su prikazan ZIP odziv za radnu i jalovu snagu, dok
je punom linijom prikazan ERL model (prema gore navedenim jednadžbama).

<figure>
  <img src="{{ site.baseurl }}/assets/gitbook/images/graphs/ERL-vs-ZIP.jpg" alt="Odziv jednostavnog ERL i ZIP modela tereta">
</figure>
    
Gore navedene jednadžbe ne uzimaju u obzir jednu karakteristiku odziva motora, 
a to je instant promjena snage i potom oporavak do neke stacionarne vrijednosti.
Kao što je vidljivo na slici iznad, ovakav model pretpostavlja monotonu promjenu
do nove stacionarne vrijednosti, što u stvarnosti nije tako. 

U stvarnosti postoji početni propad $$\Delta P_0$$ uzrokovan nemogućnošću promjene
klizanja motora u trenutku pojave stepa napona. Detaljniji model naveden je u članku na linku [[1]](https://ieeexplore.ieee.org/document/221270).

Prema tom članku, mjerenjima je potvrđeno da se teret na step promjenu u naponu odaziva kao prema slici ispod (preuzeto iz članka).
Isti oblik odziva se može očekivati i od jalove snage. 

<figure>
  <img src="{{ site.baseurl }}/assets/gitbook/images/graphs/load-response-to-v-step.PNG" alt="Odziv tereta na step promjenu napona">
</figure>    
    
Intuitivno to znači sljedeće - tijekom stepa, klizanje motora se ne može promijeniti,
pa teret izgleda statično - tako step napona uzrokuje step u snazi. 



\[1\]: D. J. Hill, ["Nonlinear dynamic load models with recovery for voltage stability studies"](https://ieeexplore.ieee.org/document/221270) 
in IEEE Transactions on Power Systems, vol. 8, no. 1, pp. 166-176, Feb. 1993, doi: 10.1109/59.221270.

   
    
    
    
    
    
    
    
    