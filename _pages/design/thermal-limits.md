---
title: 1.1 Termalne granice prijenosa
author: admilara
date: 2025-04-28
category: 1.1. Granice prijenosa
layout: post
mermaid: true
---

### Prijenos radne i jalove snage




Gubitci jalove snage u prijenosnom sustavu direktno su vezani za naponske razine
u sustavu. Što se veća radna snaga prenosi, to su veći i jalovi gubitci u sustavu, 
kao i pad napona. 

U slučaju velikog opterećenja sustava, potrebna je dodatna potpora u vidu izvora
jalove snage kako bi se održala naponska stabilnost sustava.

Najpovoljniji slučaj prijenosa snage s jednog kraja dalekovoda na drugi je kad
se dalekovodom prenosi **prirodna snaga voda**, tj. kada su napon i struja duž
dalekovoda po iznosu konstantni i jedan s drugim u fazi. 

Taj dalekovod tada ne treba potporu sustava u vidu dodatne jalove snage jer svu 
jalovinu koja je potrebna za prijenos radne snage, vod samostalno proizvodi i troši. 

\begin{equation}
    Q_{produces} = {V^2 \over X_C}
\end{equation}

\begin{equation}
    Q_{uses} = I^2 \cdot X_L
\end{equation}

- Ako je vod opterećen ispod prirodne snage voda, najviši napon je negdje oko
sredine dalekovoda
- Ako je vod opterećen iznad prirodne snage voda, najniži napon je negdje oko
sredine dalekovoda
- Ako je vod opterećen na prirodnu snagu, profil napona je konstantan duž voda

### Prijenos radne i jalove snagež

<div>
    <img src="{{ site.baseurl }}/assets/gitbook/images/two-bus-sys.svg" width="400" alt="Jednostavni sustav s dvije sabirnice">
</div>

- Razmatramo jednostavni prijenosni krug, od generatora do potrošača, kako je prikazano na slici gore. Generator je 
izvor napona $$E$$ pod kutem 0° koji napaja udaljenog potrošača preko prijenosnog voda modeliranog serijskom reaktancijom $X$. 
Napon na strani potrošača iznosi $V\angle\delta$. 

- Jednadžbama ispod se opisuje radna i jalova snaga na strani potrošača:

\begin{equation}
    sin\delta = {I\cdot X\cdot cos\varphi \over E}
\end{equation}

\begin{equation}
    I\cdot cos\varphi = {E \over X}\cdot sin\delta
\end{equation}

\begin{equation}
    P = V \cdot I \cdot cos\varphi = V\cdot {E \over X}\cdot sin\delta
\end{equation}

\begin{equation}
    P = - {E\cdot V \over X}\cdot sin\delta
\end{equation}

\begin{equation}
    Q = {E\cdot V\over X}\cdot cos\delta - {V^2 \over X}
\end{equation}

Eliminacijom $\delta$ dobivamo:

\begin{equation}
    \textcolor{red}{(Q+ {V^2 \over X})^2 + P^2 = ({E\cdot V \over X})^2}
\end{equation}

Rješavanjem po $V^2$ dobivamo formulu ispod:

\begin{equation}
    \textcolor{green}{V^2 = {E^2 \over 2}-Q\cdotX \pm \sqrt{ {E^4 \over 4X^2} - P^2 - Q\cdot {E^2 \over X} }}
\end{equation}


Najbolja ilustracija ovisnosti napona i snage koja se prenosi dalekovodom je u
obliku **P-V krivulja**. 
- PV krivulja prikazuje kako se s povećanjem snage koja se prenosi nekim dalekovodom, 
smanjuje iznos napona u čvorištu koje prima tu istu snagu, što se događa zbog povećanja
gubitaka jalove snage. 
- Ako se radna snaga kontinuirano povećava, napon će u jednom trenutku prijeći 
maksimalnu snagu voda, nakon čega su iscrpljene rezerve jalove snage koja je potrebna
za održavanje napona te dolazi do naglog propada napona.

- Za jednostavni sustav sa dvije sabirnice (kao na slici ispod) navodimo 
jednadžbu koja pokazuje ovisnost napona o radnoj snazi i kutu opterećenja

<div>
    <img src="{{ site.baseurl }}/assets/gitbook/images/two-bus-sys.svg" width="400" alt="Jednostavni sustav s dvije sabirnice">
</div>


\begin{equation}
    V_2 = {\sqrt{ -a \pm \sqrt{1+1}}}
\end{equation}

