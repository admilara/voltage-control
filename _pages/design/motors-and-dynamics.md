---
title: Motori i dinamika
author: admilara
date: 2025-04-23
category: Motori i dinamika
layout: post
mermaid: true
---

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
    
- Standardni ZIP model za modeliranje tereta definiran je kao:

\begin{equation}
    P = P_0 \left \alpha_1 V^2 + \alpha_2 V + \alpha_3\right
    \tag{1}\label{P_static}
\end{equation}

\begin{equation}
    Q = Q_0 \left \beta_1V^2 + \beta_2 V + \beta_3 \right
    \tag{2}\label{Q_static}
\end{equation}

- Takav model tereta nema vremensku komponentu i ne može oslikati dinamičko
ponašanje, već samo konačni iznos u koji će se stacionirati P i Q. 

- **ERL** (exponential recovery load) modeliranje ima vremensku komponentu može
realnije oslikati ponašanje tereta, naravno ako su vremenske konstantne dobro odabrane. Takav model možemo
opisati sljedećim jednadžbama:

\begin{equation}
    P(t) = P_{stac}\leftV(t)\right + \left P_0 - P_{stac}\left V(t)\right \cdot \exp^{-t \over T_p}
\end{equation}


