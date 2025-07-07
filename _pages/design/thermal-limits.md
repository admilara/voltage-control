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

<figure>
    <img src="{{ site.baseurl }}/assets/gitbook/images/two-bus-sys.svg" width="400" alt="Jednostavni sustav s dvije sabirnice">
</figure>

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

Rješavanjem po $V^2$ dobivamo formulu ispod [[1]](https://link.springer.com/book/10.1007/978-3-642-13669-6)

\begin{equation}
    \textcolor{blue}{V^2 = {E^2 \over 2}-Q\cdot X \pm \sqrt{ {E^4 \over 4X^2} - P^2 - Q\cdot {E^2 \over X} }}
\end{equation}

- Jednadžbu napona u tom obliku znamo kao **P-V krivulju** ili **nosnu krivulju**.
Ovako definirana krivulja nije definirana na cijelom skupu racionalnih brojeva i nije bijekcija.
Uz trigonometrijski identitet $tg\varphi = Q/P$, možemo definirati tu funkciju u obliku P(V):

\begin{equation}
    P = {V^2 \over X}\cdot \left({-tg\varphi + \sqrt{tg^2\varphi -(1 - {E^2 \over V^2})} \over 1+tg^2\varphi}\right)
\end{equation}

- Ovu funkciju vizualno predstavljamo P-V krivuljom, čiji je primjer dan na slici ispod za različite iznose cos$\varphi$:

<figure>
    <img src="{{ site.baseurl }}/assets/gitbook/images/pv-curve-multiple-cos.svg" width="400" alt="PV krivulja za sustav s dvije sabirnice za razlicite iznose cosphi">
</figure>

- Maksimum ove funkcije dostiže se za (ceteris paribus) cos$\varphi$ = 1, gdje je **$P=P_{max}$** i to je maksimalna 
snaga koju je moguće prenijeti nekim sustavom.
    * Tada se radi o čisto djelatnom trošilu koje ne utječe na jalovu snagu sustava.
    * Za niže cos$\varphi$, recimo 0.9 induktivno, dolazi do smanjenja djelatne snage koja se može prenijeti sustavom i snižavanje kritičnog napona sustava. 

- Za radnu snagu veću od $P_{max}$, jednadžbe tokova snaga **neće imati rješenja** tako da su tokovi snaga za
$P = P_{max}$ poznati i kao **točka kolapsa**. 

- Za radne snage manje od $P_{max}$, postoje dva rješenja po naponu, ali samo je "gornje" rješenje fizički moguće.

- PV krivulje na slici dobivene su uz pretpostavku da slack sabirnica može dati bilokoji iznos P i Q, što ograničenje
stavlja na maksimalnu prenosivu radnu snagu u sustavu.
- Ukoliko postoji ograničenje na maksimalnu jalovinu koju može dati generator 1, točka kolapsa može biti definirana i 
jalovinom koju generator maksimalno može dati.

<figure>
    <img src="{{ site.baseurl }}/assets/gitbook/images/pv-curve-multiple-cos.svg" alt="PV krivulja za sustav s dvije sabirnice, limit Q">
</figure>




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




Lista referenci:

\[1\]: Federico Milano, [Power System Modelling and Scripting](https://link.springer.com/book/10.1007/978-3-642-13669-6) 
Springer, 2010, doi: 10.1007/978-3-642-13669-6