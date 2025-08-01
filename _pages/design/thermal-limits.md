---
title: 1.1 Granice prijenosa
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

$$
\begin{equation}
\begin{aligned}
    Q_{produces} = {V^2 \over X_C} \\
    Q_{uses} = I^2 X_L
\end{aligned}
\end{equation}
$$

- Ako je vod opterećen ispod prirodne snage voda, najviši napon je negdje oko
sredine dalekovoda
- Ako je vod opterećen iznad prirodne snage voda, najniži napon je negdje oko
sredine dalekovoda
- Ako je vod opterećen na prirodnu snagu, profil napona je konstantan duž voda

<hr>

### Osnovne jednadžbe prijenosa

<figure>
    <img src="{{ site.baseurl }}/assets/gitbook/images/two-bus-sys.svg" alt="Jednostavni sustav s dvije sabirnice">
</figure>

- Razmatramo jednostavni prijenosni krug, od generatora do potrošača, kako je prikazano na slici gore. Generator je 
izvor napona $$E$$ pod kutem 0° koji napaja udaljenog potrošača preko prijenosnog voda modeliranog serijskom reaktancijom $X$. 
Napon na strani potrošača iznosi $V\angle\delta$. 

- Jednadžbama ispod se opisuje radna i jalova snaga na strani potrošača:

\begin{equation}
    \sin\delta = {I X \cos\varphi \over E}
\end{equation}

\begin{equation}
    I \cos\varphi = {E \over X} \sin\delta
\end{equation}

\begin{equation}
    P = V I \cos\varphi = V {E \over X} \sin\delta
\end{equation}


\begin{equation}
    P = - {E V \over X} \sin\delta
\end{equation}

\begin{equation}
    Q = {E V\over X} \cos\delta - {V^2 \over X}
\end{equation}


Eliminacijom $\delta$ dobivamo:

\begin{equation}
    \textcolor{red}{(Q+ {V^2 \over X})^2 + P^2 = ({E V \over X})^2}
\end{equation}

Rješavanjem po $V^2$ dobivamo formulu ispod [[1]](https://link.springer.com/book/10.1007/978-3-642-13669-6)

\begin{equation}
    \textcolor{blue}{V^2 = {E^2 \over 2}-Q X \pm \sqrt{ {E^4 \over 4X^2} - P^2 - Q {E^2 \over X} }}
    \tag{1}\label{PV-napon}
\end{equation}

<hr>

Problem opisan jednadžbom \ref{PV-napon} ima realno pozitivno rješenje ako je:

\begin{equation}
    P^2 + Q{E^2 \over X} \leq {E^4 \over {4X^2}}
\end{equation}

Ova nejednakost pokazuje kombinaciju radne i jalove snage koju vod može prenijeti potrošaču. Uvrštenjem kratkospojne
snage na početku voda, koja je jednaka $S_{sc} = E^2 \over X$ imamo sljedeći izraz:

\begin{equation}
    P^2 + QS_{sc} \leq \left(S_{sc} \over 2 \right)^2 
\end{equation}

>Što nam to znači fizikalno?
> - **Maksimalna djelatna snaga prijenosa** postiže se za $Q = 0$ i iznosi $P = S_{sc}/2$
> - **Maksimalna jalova snaga prijenosa** postiže se $P = 0$ i iznosi $Q = S_{sc}/4$
> - Injekcija jalove snage na kraju voda, odnosno $Q \leq 0$ povećava granicu prijenosa djelatne snage
> - Ograničenje prijenosa proporcionalno je admitanciji voda $X$ i kvadratu napona napajanja $E$
{: .block-tip }

Ukoliko pretpostavimo da teret koji se napaja ima admitancijsku karakteristiku, tj. da se radi o čistom omskom otporu 
tada vrijedi (pogledati i link [Tereti])(https://admilara.github.io/voltage-control/pages/design/load-types/):

\begin{equation}
    Z = const. \rightarrow G=const.
\end{equation}

\begin{equation}
    S = P + jQ = P \left(1+\tan\varphi \right) = VI\left(1+\tan\varphi \right)\\ 
    = {V^2 \over Z} \left(1+\tan\varphi \right) = V^2 G \left(1+\tan\varphi \right)
\end{equation}

- Trošilo proizvodi jalovu snagu za $\tan\varphi \lt 0 $
- Trošilo troši jalovu snagu za $\tan\varphi \gt 0$

<hr>

#### P-V krivulje

- Jednadžbu napona u tom obliku znamo kao **P-V krivulju** ili **nosnu krivulju**.
Ovako definirana krivulja nije definirana na cijelom skupu racionalnih brojeva i nije bijekcija.
Uz trigonometrijski identitet $tg\varphi = Q/P$, možemo definirati tu funkciju u obliku P(V):

\begin{equation}
    P = {V^2 \over X} \left({-tg\varphi + \sqrt{tg^2\varphi -(1 - {E^2 \over V^2})} \over 1+tg^2\varphi}\right)
\end{equation}

- Ovu funkciju vizualno predstavljamo P-V krivuljom, čiji je primjer dan na slici ispod za različite iznose cos$\varphi$:

<figure>
    <img src="{{ site.baseurl }}/assets/gitbook/images/pv-curve-multiple-cos-v2.svg" alt="PV krivulja za sustav s dvije sabirnice za razlicite iznose cosphi">
</figure>

- Maksimum ove funkcije dostiže se za (ceteris paribus) cos$\varphi$ = 1, gdje je **$P=P_{max}$** i to je maksimalna 
snaga koju je moguće prenijeti nekim sustavom. 
    * Tada se radi o čisto djelatnom trošilu koje ne utječe na jalovu snagu sustava.
    * Za niže cos$\varphi$, recimo 0.9 induktivno, dolazi do smanjenja djelatne snage koja se može prenijeti sustavom i snižavanje kritičnog napona sustava. 
    * Kad razmatramo slučaj gdje je cos$\varphi$ = 1 tj. imamo trošilo koje je isključivo djelatno, ono što održava napon je sam sustav - generiranjem induktivne i 
    kapacitivne jalove snage (npr. kabel, dalekovod, generator, trafo) - do sloma napona dolazi kad se iscrpe rezerve jalove snage koje 
    su potrebne za održavanje napona. 
    * Vidljivo je da porastom prijenosa radne snage (injektiranjem snage u čvorište), napon tog čvorišta opada.

- Za radnu snagu veću od $P_{max}$, jednadžbe tokova snaga **neće imati rješenja** tako da su tokovi snaga za
$P = P_{max}$ poznati i kao **točka kolapsa**. 
    * Za velika opterećenja, velike su i struje. Velike struje za sobom povlače i velike gubitke. Jalovi gubitci
    su također proporcionalni kvadratu struje, a oni stvaraju padove napona.
    * Još jedan problem kod P-V krivulja je sljedeći - analiza naponske stabilnosti bazirana na sporom porastu
    opterećenja bazira se na tokovima snaga, što znači rješavanje nelinearnih jednadžbi Newton-Raphson metodom.
    * Osnovni problem te metode je Jakobijan koji u točki koljena P-V krivulje postaje singularan, tj. divergira

- Za radne snage manje od $P_{max}$, postoje dva rješenja po naponu, ali samo je "gornje" rješenje fizički moguće.

- PV krivulje na slici dobivene su uz pretpostavku da slack sabirnica može dati bilokoji iznos P i Q, što ograničenje
stavlja na maksimalnu prenosivu radnu snagu u sustavu.
- Ukoliko postoji ograničenje na maksimalnu jalovinu koju može dati generator 1, točka kolapsa može biti definirana i 
jalovinom koju generator maksimalno može dati.

<figure>
    <img src="{{ site.baseurl }}/assets/gitbook/images/pv-curve-q-limit.svg" alt="PV krivulja za sustav s dvije sabirnice, limit Q">
</figure>

<hr>

#### Q-V krivulje

Osim P-V krivulja, u proučavanju naponske stabilnosti koriste se i Q-V krivulje, koje se izrađuju za sabirnice koje se 
smatra kritičnima tj. najpodložnijima naponskoj nestabilnosti pa i slomu [. 
Svaka Q-V krivulja prikazuje koliko je u čvor potrebno injektirati Mvar kako bi se napon u tom čvoru održao unutar
propisanih granica pri **konstantnoj injekciji radne snage**. 

<figure>
    <img src="{{ site.baseurl }}/assets/gitbook/images/qv-curve-multiple-cos-v2.svg" alt="QV krivulja za sustav s dvije sabirnice, dQ/dV">
</figure>


<hr>

Čisto za vizualizaciju, na slici ispod se nalazi tzv. 'onion' površina koja pokazuje u 3D prostoru odnose između
radne snage, jalove snage i napona. 

<figure>
    <img src="{{ site.baseurl }}/assets/gitbook/images/onion-surface-pv.svg" alt="Onion surface">
</figure>

Projekcijom na P-V ili Q-V ravnine, dobiju se gore opisane P-V i Q-V krivulje.

- Prema uvjetu maksimalne prenosive radne snage na vodu, čisto aktivno trošilo teoretski može primiti polovicu 
kratkospojne snage na svojim sabirnicama, uz uvjet da ne prima nikakvu jalovu snagu. Naravno, takav iznos snage 
postiže se za naponske razine koje su daleko od dopuštenih u normalnom prijenosnom sustavu. 
- Granice za 110 kV napon u hrvatskom prijenosnom sustavu su $\pm$ 10%.
- Na slici ispod vidljivo je kako to izgleda na P-V krivuljama, gdje je sivo osjenčana regija dopuštenog napona (op.a.
slika je preuzeta iz \[6\] te su na njoj granice $\pm$ 5%)
- Prema tome, **praktična granica prijenosa** je još niža od teorijske za čisti radni teret.

<figure>
    <img src="{{ site.baseurl }}/assets/gitbook/images/pv-practical-limits.svg" alt="Onion surface">
</figure>

- Na kraj prijenosnog voda se često dodaju **kondenzatorske baterije** kako bi se povećao krajnji napon na vodu
i time i povećala praktična granica prijenosne moći.
- Na taj način se jalova snaga proizvodi lokalno umjesto da se prijenosni kapacitet voda zagušuje prijenosom jalovine.
- Iz perspektive prijenosnog sustava, povećava se i faktor snage tereta - što je prema P-V krivuljama jednako pomicanju
na drugu krivulju koja ima povoljniji $\tan\varphi$ (tj. $\cos\varphi$).
- Prelaskom u kapacitivni režim (negativni $\tan\varphi$) moguće je prenijeti i više od $S_{sc} \over 2$ radne snage pri
naponima blizu 1 p.u, **ALI**
    - <font color="red"> vidljiva je osjetljivost rada u takvom prekompenziranom sustavu - za malu promjenu tereta možemo očekivati velike promjene napona </font>
    - <font color="red"> kritični napon (točka u kojoj dolazi do sloma) je veoma blizu nominalnom </font>



Lista referenci:

\[1\]: Federico Milano, [Power System Modelling and Scripting](https://link.springer.com/book/10.1007/978-3-642-13669-6) 
Springer, 2010, doi: 10.1007/978-3-642-13669-6

\[2\]: Electric Power Research Institute, [Power System Dynamics Tutorial](https://www.epri.com/research/products/000000000001016042), Final Report, 2009.

\[3\]: Institut za elektroprivredu, Uloga NE Krško u regulaciji napona slovenskog i hrvatskog EES-a, Zagreb, 2006.

\[4\]: Stipe Ćurlin, HEP OPS d.o.o. [Naponska stabilnost elektroenergetskog sustava](https://www.scribd.com/doc/211829732/Stabilnost-Ees-A)

\[5\]: N. Valentin et al. [Voltage Stability Analysis Based on PV and QV curves in transmission lines using SVC with the Power Factory Program](https://iopscience.iop.org/article/10.1088/1742-6596/1993/1/012015/pdf), Journal of Physics: Conference Series 2021

\[6\]: Larsson, M. (2001). [Coordinated Voltage Control in Electric Power Systems](https://portal.research.lu.se/en/publications/coordinated-voltage-control-in-electric-power-systems). 
Doctoral Thesis (compilation), Division for Industrial Electrical Engineering and Automation. Mats Larsson, IEA, LTH, Box 118, S-221 00 Lund, Sweden,.
