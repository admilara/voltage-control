---
title: Tipovi tereta
author: admilara
date: 2025-04-23
category: Tipovi tereta
layout: post
mermaid: true
---

### Statički modeli tereta

Statički model predstavlja radnu i jalovu snagu pomoću vremenski invarijantnih algebarskih izraza.
Oni su funkcije napona $$U$$ i frekvencije $$f$$ na nekoj sabirnici.

\begin{equation}
    P_i = f_P (U_i, f_i)
    \tag{1}\label{static_radna}
\end{equation}
    
\begin{equation}
    Q_i = f_Q (U_i, f_i)
    \tag{2}\label{static_jalova}
\end{equation}

> S obzirom na ovisnost o naponu, modele dijelimo na
>    1. Model konstantne snage
>    2. Model konstantne struje
>    3. Model konstantne impedancije
{: .block-tip }

##### Eksponencijalni model tereta
- Često korišten statički model radnog i jalovog opterećenja izražava se kao **eksponencijalna** formula.

\begin{equation}
    P(V) = P_{0}\cdot \left({V \over V_{0}}\right)^\{k_pu} \left({f \over f_0}\right)^{k_pf}
    \tag{3}\label{full_exp_radna}
\end{equation}
    
\begin{equation}
    Q(V) = Q_{0}\cdot \left({V \over V_{0}}\right)^\{k_qu} \left({f \over f_0}\right)^{k_qf}
    \tag{4}\label{full_exp_jalova}
\end{equation}

- Dio jednadžbe koji se odnosi na varijacije frekvencije se često izostavlja s obzirom da su odstupanja
frekvencije puno uža nego odstupanja napona, pa se gore navedene formule svedu na

\begin{equation}
    P(V) = P_{0}\cdot \left({V \over V_{0}}\right)^\alpha 
    \tag{5}\label{lim_exp_radna}
\end{equation}
    
\begin{equation}
    Q(V) = Q_{0}\cdot \left({V \over V_{0}}\right)^\beta
    \tag{6}\label{lim_exp_jalova}
\end{equation}

- Faktore $$k_{pu}$$ i $$k_{qu}$$ zamijenili smo faktorima $$\alpha$$ i $$\beta$$ radi jednostavnijeg označavanja.
    
- u gore navedenim jednadžbama, $P_{0}$ i $Q_{0}$ te $V_{0}$ označavaju početne vrijednosti radne snage, jalove snage i napona u nekom čvorištu.
- $\alpha$ i $\beta$ su koeficijenti koji određuju tip tereta, što je slikovito prikazano na grafu ispod.

- Ako su eksponenti $\alpha = 0, \beta = 0$, tada se radi o **teretu konstantne snage**, neovisne o naponu (motori).
- Ako su eksponenti $\alpha = 1, \beta = 1$, tada se radi o **teretu konstantne struje**.
- Ako su eksponenti $\alpha = 2, \beta = 2$, tada se radi o **teretu konstantne impedancije**, čisti omski otpori.


<figure>
    <img src="{{ site.baseurl }}/assets/gitbook/images/ZIP-karakteristike.svg" width="600" alt="Karakteristike tereta - model konstantne snage, konstantne struje i konstantne impedancije">
</figure>


- Ako koristimo eksponencijalni model tereta, eksponenti $$\alpha$$ i $$\beta$$ za neke karakteristične terete su [[1]](https://ieeexplore.ieee.org/document/8958809):

| Tip tereta                | $$\alpha$$    | $$\beta$$ |
| :--------                 | :-------:     | :-------: |
| Žarulje sa žarnom niti    | 1,54          | 0         |
| Sobni klima uređaji       | 0,50          | 2,5       |
| Ventilokonvektori         | 0,08          | 1,6       |
| Baterijski punjači        | 2,59          | 4,06      |
| Fluo rasvjeta             | 2,07          | 3,21      | 


##### Polinomni model tereta 
- Model tereta može uključivati i dio koji bi označavao frekvencijsku ovisnost tereta (jednadžba [\ref{frekv_ovisna}]).
- Radna snaga koji vuče neki potrošač, kad se uzme u obzir i frekvencijski ovisan dio glasi:
    
\begin{equation}
    P = P_{0} \cdot [p_1 V^2 + p_2 V + p_3] \cdot [1+k_p f \Delta f]
    \tag{3}\label{frekv_ovisna}
\end{equation}



##### Industrijski teret
- Industrijski (radni i jalovi) tereti uglavnom se sastoje od indukcijskih motora i njihovi iznosi se ne mijenjaju previše.
- Ako se od asinkronog motora očekuje neka određena (konstantna) snaga (moment), u slučaju da dođe do pada mrežnog napona, doći će do 
malog pada brzine i pada EMS motora, ali će se zato povećati struja koju motor povlači, što bi trebalo osigurati relativno 
konstantnu snagu motora.

- Graf na slici ispod prikazuje odnos momenta i brzine motora za različite iznose mrežnog napona za **konstantni teret** napajan motorom.

<figure>
    <img src="{{ site.baseurl }}/assets/gitbook/images/torque-voltage-clean.svg" width="600" alt="Moment vs. brzina vrtnje za različite napone">
</figure>

Za ilustraciju su korištene vrijednosti iz [[2]](https://www.researchgate.net/publication/313773111_Fuzzy_Gain_Scheduling_of_PID_FGS-PID_for_Speed_Control_Three_Phase_Induction_Motor_Based_on_Indirect_Field_Oriented_Control_IFOC).

| Napon | Brzina rotora (o/min) | Klizanje (%)  | Struja (A)    |
| 60%   | 1363,365              | 9,1           | 26,442        |
| 70%   | 1408,410              | 6,1           | 21,515        |
| 80%   | 1432,434              | 4,5           | 18,504        |
| 90%   | 1447,449              | 3,5           | 16,386        |
| 100%  | 1459,461              | 2,7           | 14,175        |















Lista referenci:

\[1\]: Joe H. Chow; Juan J. Sanchez-Gasca, [Load and Induction Motor Models](https://ieeexplore.ieee.org/document/8958809) in 
Power System Modeling, Computation, and Control , IEEE, 2020, pp.295-325, doi: 10.1002/9781119546924.ch11

\[2\]: Ferdiansyah, Indra & Era, Purwanto & Windarko, Novie Ayub. (2016). 
[Fuzzy Gain Scheduling of PID (FGS-PID) for Speed Control 3PH Induction Motor](https://www.researchgate.net/publication/313773111_Fuzzy_Gain_Scheduling_of_PID_FGS-PID_for_Speed_Control_Three_Phase_Induction_Motor_Based_on_Indirect_Field_Oriented_Control_IFOC). 
EMITTER International Journal of Engineering Technology. 4. 10.24003/emitter.v4i2.147. 

