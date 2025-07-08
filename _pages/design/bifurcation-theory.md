---
title: 1.2. Teorija bifurkacije
author: admilara
date: 2025-07-07
category: 1.2. Teorija bifurkacije
layout: post
mermaid: true
---

### Teorija bifurkacija i elektroenergetski sustav

#### Uvod


Nestanci struje (blackouti) su postali sve češći problem u mnogim zemljama svijeta. Iz različitih razloga
mnogi su sustavi prisiljeni razditi blizu svojh granica stabilnosti te su ranjivi na poremećaje radne točke.
Kad se granice prekorače, može doći do nemogućnosti zadržavanja stabilnog profila napona napona, što u najgorem 
slučaju dovodi do sloma napona. Čimbenici koji mogu utjecati na to su:
- povećanje potrošnje koje doseže granice mreže ili proizvodnog kapaciteta
- djelovanje loše podešenih regulatora
- ispadanje vodova i generatora i slični ispadi.

Elektroenergeski sustav je jedan od najsložnijih sustava za modeliranje, gdje je prvi problem veličina sustava, 
a drugi složena priroda tog sustava. Neke od razlika koje otkrivaju složenost sustava i modela su:
- fizičke varijable s različitim periodima djelovanja (električne veličine koje su brže od mehaničkih stanja), 
- uređaji modelirani kontinuiranom dinamikom (generatori, tereti)
- diskretni događaji koji utječu na sustav (kvarovi, djelovanje regulatora i OLTC-a)
- algebarska ograničenja sustava (ograničenja mreže, radni uvjeti i sl.)  

Najčešći pristup modeliranju elektroenergetskog sustava je korištenje diferencijalno-algebarskih jednadžbi u obliku:

\begin{eqnarray}
    \dot x = f(x, y; \mu)
    0 = g(x, y; \mu)
    \tag{1}\label{DAE}
\end{eqnarray}

gdje su:
- f: $\mathbb{R}^n$ x $\mathbb{R}^m$ x $\mathbb{R}^p$ $\rightarrow$ $\mathbb{R}^n$
- g: $\mathbb{R}^n$ x $\mathbb{R}^m$ x $\mathbb{R}^p$ $\rightarrow$ $\mathbb{R}^m$
- $x \in \mathbb{R}^n$ - dinamičke varijable stanja (mehanička stanja generatora, električna stanja rotora, sustava 
uzbude, turbinske regulacije i sl.)
- $y \in \mathbb{R}^m$ - algebarske variable stanja (stanja određena prijenosnom mrežom i algebarskim stanjima 
statora generatora i opterećenja, proizlaze iz zanemarivanja dinamike vodova i drugih uređaja.)
- $\mu \in \mathbb{R}^p$ - vektor parametara 

Koristeći ovakve jednadžbe, na primjeru sustava s 9 sabirnica i 3 generatora, dolazimo do sustava 45 jednadžbi - 21 
diferencijalna i 24 algebarske, što je ogromna složenost. Nadalje, taj broj može i rasti ovisno o detaljnosti 
modeliranja svih komponenti sustava. 

Elektroenergetski sustavi su izrazito nelinearni, a njihovo dinamičko ponašanje može se kvalitativno promijeniti 
promjenom parametara. Na primjer, nakon povećanja opterećenja, stabilna radna točka može postati nestabilna i mogu se 
pojaviti oscilacije. Ovo ponašanje može se lokalno povezati s Hopfovom bifurkacijom, a općenito teorija bifurkacija 
se može primijeniti kako bi se razumjeli mehanizmi koji vode do nelinearnih pojava u ovakvim sustavima. 


### Bifurkacijska analiza

Osnovna ideja bifurkacijske analize jest proučavanje kvalitativnih promjena u dinamici sustava (npr. gubitak stabilnosti, 
pojava ili nestanak oscilacija) pri sporim promjenama karakterističnih parametara sustava.

Bavit ćemo se najjednostavnijom klasom problema u nelinearnoj dinamici - ponašanjima koja se mogu u potpunosti opisati 
lokalno, tj. u nekoj okolini radne točke sustava.
Lokalni bifurkacijski fenomeni su važni elementi nestabilnosti napona. Dvije najjednostavnije među njima su:
- sedlasta čvorna bifurkacija ( __saddle node bifurcation__)
- Hopfova bifurkacija

Elektroenergetski sustav promatrat ćemo kako je prethodno opisano \ref{DAE}- kao sustav diferencijalnih i algebarskih jednadžbi 
te razmotriti statičko i dinamičko ponašanje takvih sustava kao funkcije parametara.

Prema tom sustavu jednadžbi, klasični model koji se sastoji od $n_g$ generatora, $n_{PV}$ čvorišta te 
$n_{PQ}$ čvorišta se može opisati sljedećim setom jednadžbi:

\begin{eqnarray}
    \dot \delta = \omega
    M \dot \omega + D\omega +f_g(\delta, \Phi, V, \mu) = 0
    f_l(\delta, \Phi, V, \mu) = 0
    \tag{2}\label{classic_model}
\end{eqnarray}

Ravnotežna stanja sustava zadovoljavaju algebarske jednadžbe:

\begin{eqnarray}
    0 = f(x, y; \mu)
    0 = g(x, y; \mu)
    \tag{3}\label{equi}
\end{eqnarray}

> Ove jednadžbe (\ref{equi}) nazivamo **jednadžbama tokova snaga**. 
{: .block-tip }

Dvije ključne značajke modela \ref{DAE} su:
- <span style="color:blue">eksplicitna ovisnost o parametrima</span>
- <span style="color:blue">diferencijalno-algebarska struktura</span>

**Što to znači za naš model?**
- Diferencijalno-algebarska struktura može generirati ponašanja koja nisu prisutna u sustavima isključivo diferencijalnih
jednadžbi.
- Na primjer, ako klasični sustav sadrži samo opterećenja konstantne admitancije (Z=const.), bez opterećenja konstantne snage, 
tada je ekvivalentan sustavu opisanom isključivo diferencijalnim jednadžbama.
- U tom slučaju postoje parametrima inducirane nestabilnosti, ali one su vezane uz stacionarna stanja ili kutne nestabilnosti.
- **Kolaps napona u uobičajenom smislu se ne događa.**

#### Mnogostrukost prostora

Razmotrimo jednostavnu mrežu s tri sabirnice sa slike dolje. 

<figure>
    <img src="{{ site.baseurl }}/assets/gitbook/images/three-bus-sys.svg" alt="Jednostavni sustav s dvije sabirnice">
</figure>

- Pretpostavimo da su $P_1$, $P_1$ i $P_1$ radne snage u svakom od čvorišta. 
- Ravnotežno rješenje postoji samo ako vrijedi $P_1 + P_2 + P_3 = 0$
- Radi jednostavnosti fiksiramo neke od parametara:
    * $V_0 = 1$
    * $X = 0$
    * $M_1 = 1$, $M_2 = 1$ - moment generatora
    * $\Phi = \delta_2 - \delta_1$
    * $\phi = \delta_3 - \delta_1$
    * $\Delta P = P_2 - P_1$
    
Jednadžbe gibanja su tad:

\begin{eqnarray}
    \ddot \Phi = -V sin(\Phi - \phi) - V sin \phi + \Delta P
    0 = V (sin \phi + sin(\phi - \Phi)) - P_3
    0 = -V (cos\phi + cos(\phi - \Phi) + (2-B)V^2 - Q_3)
\end{eqnarray}

- Bilokoje gibanje opisano prvom jednadžbom iz seta ograničeno je drugim dvjema (algebarskim) jednadžbama.





Literatura:
\[1\]: G. Revel, D.M. Alonso, J.L. Moiola, [Biifurcation theory applied to the analysis of power systems](http://ref.scielo.org/csx5fd),
Revista de la Unión Matemática Argentina, 2008.

\[2\]: H.G. Kwatny, R.F. Fischl, [Local Bifurcation in Power Systems: Theory, Computation and Application](https://ieeexplore.ieee.org/document/481630/), 
Proceedings of the IEEE 83(11):1456 - 1483, doi: 10.1109/5.481630, 1995.

\[3\]: Federico Milano, [Power System Modelling and Scripting](https://link.springer.com/book/10.1007/978-3-642-13669-6) 
Springer, 2010, doi: 10.1007/978-3-642-13669-6