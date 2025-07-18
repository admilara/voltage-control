---
title: Voltage Control
author: admilara
date: 2025-03-25
category: Jekyll
layout: post
mermaid: true
---

Nestabilnost napona može se pojaviti u jako opterećenim sustavima ili sustavima s dugim vodovima (ili s oboje), kada 
se ispuni jedan od dva uvjeta:

* Reaktivna snaga dostupna iz kondenzatora, vodova, generatora i statičkih var sustava (SVS) padne ispod gubitaka 
reaktivne snage u sustavu i opterećenja, ili

* Izvori reaktivne snage ne premašuju značajno reaktivne gubitke i opterećenja, a dopušta se pad napona.

Obično se ti uvjeti javljaju nakon ispada vodova ili generatora, ili kombinacije ispada opreme. Međutim, neuobičajeno 
visoki vrh opterećenja ili manji poremećaji također mogu uzrokovati pad napona. Ako nije dostupna dovoljna količina 
eaktivne snage kada napon počne padati, rezerve reaktivne snage brzo se iscrpe, a napon dodatno pada, moguće i do 
potpunog kolapsa.

#### Osnovni pojmovi

- Nestabilnost napona – Pojava gubitka ravnotežnog stanja napona u elektroenergetskom sustavu. 
Karakterizira je nekontrolirani pad napona koji u konačnici vodi do kolapsa napona. Dogodi se kada opskrba reaktivnom 
snagom nije dovoljna za pokrivanje reaktivnih gubitaka povezanih s potrošačkim opterećenjima, vodovima i transformatorima.

- Kolaps napona – Nagli i strmoglavi pad napona koji se obično događa nekoliko minuta nakon što je izgubljeno 
ravnotežno stanje zbog nestabilnosti napona. Kolaps napona karakterizira zastoj indukcijskih motora kada napon 
padne do točke u kojoj zakretni moment motora više ne premašuje mehanički moment opterećenja. 
Tijekom procesa kolapsa motori ispadaju iz sustava, a može doći i do isključenja vodova, a potom i do lančanih ispada 
čime na širokom području dolazi do gubitka napajanja. 

- Sistemsko stanje niskog napona – Stanje niskog napona koje utječe na široko područje elektroenergetskog 
sustava kroz više razina napona.

- Sporo dinamičko ponašanje – Aktivnosti operatera, uređaja za promjenu prijenosnog omjera pod opterećenjem (LTC), 
zaštitnih uređaja generatora, potrošačkih opterećenja i drugih sustavskih kontrola tijekom pojave nestabilnosti napona.

- Nestabilnost u stacionarnom stanju – Kutna razdioba (razdvajanje)[link na stranicu o kutnoj razdiobi] koja se događa kada prijenos snage premaši 
mogućnost sinkronizacije u stacionarnom stanju, a to može biti uzrokovano padom napona povezanog s nestabilnošću napona.

#### Spora dinamika

Kad neki poremećaj prouzrokuje pad napona, može doći do "aktivacije" nekoliko mehanizama.

#### Rezidencijalni tereti
> ##### Što se događa s rezidencijalnim teretom?
> S padom napona dolazi i do pada radnog i jalovog tereta kućanstava.
{: .block-tip }


##### Eksponencijalni model tereta
- Često korišten statički model radnog i jalovog tereta izražava se kao **eksponencijalna** formula. 
    
\begin{equation}
    P(V) = P_{0}\cdot \left({V \over V_{0}}\right)^\alpha
    \tag{1}\label{static_radna}
\end{equation}
    
\begin{equation}
    Q(V) = Q_{0}\cdot \left({V \over V_{0}}\right)^\beta
    \tag{2}\label{static_jalova}
\end{equation}
    
- u gore navedenim jednadžbama, $P_{0}$ i $Q_{0}$ te $V_{0}$ označavaju početne vrijednosti radne snage, jalove snage i napona u nekom čvorištu.
- $\alpha$ i $\beta$ su koeficijenti koji određuju tip tereta.

- Ako su eksponenti $\alpha = 0, \beta = 0$, tada se radi o **teretu konstantne snage**, neovisne o naponu (motori).
- Ako su eksponenti $\alpha = 1, \beta = 1$, tada se radi o **teretu konstantne struje**.
- Ako su eksponenti $\alpha = 2, \beta = 2$, tada se radi o **teretu konstantne impedancije**, čisti omski otpori.

- Ako koristimo eksponencijalni model tereta, eksponenti $$\alpha$$ i $$\beta$$ za neke karakteristične terete su [[1]](https://ieeexplore.ieee.org/document/8958809):

| Tip tereta                | $$\alpha$$ | $$\beta$$ |
| :--------                 | :-------:  | :-------: |
| Žarulje sa žarnom niti    | 1,54      | 0 |
| Sobni klima uređaji       | 0,50      | 2,5 |
| Ventilokonvektori         | 0,08      | 1,6 |
| Baterijski punjači        | 2,59      | 4,06 |
| Fluo rasvjeta             | 2,07      | 3,21 | 

##### Polinomni model tereta 
- Model tereta može uključivati i dio koji bi označavao frekvencijsku ovisnost tereta (jednadžba [\ref{frekv_ovisna}]).
- Radna snaga koji vuče neki potrošač, kad se uzme u obzir i frekvencijski ovisan dio glasi:
    
\begin{equation}
    P = P_{0} \cdot [p_1 V^2 + p_2 V + p_3] \cdot [1+k_p f \Delta f]
    \tag{3}\label{frekv_ovisna}
\end{equation}

#### Industrijski teret

> ##### Što se događa s industrijskim teretom?
> Industrijski (radni i jalovi) tereti uglavnom se sastoje od indukcijskih motora i njihovi iznosi se ne mijenjaju previše, barem kad se radi o **steady state** ponašanju.
{: .block-tip }

- Ako se od asinkronog motora očekuje neka određena (konstantna) snaga (moment), u slučaju da dođe do pada mrežnog napona, doći će do 
malog pada brzine i pada EMS motora, ali će se zato povećati struja koju motor povlači, što bi trebalo osigurati relativno 
konstantnu snagu motora.

- Graf na slici ispod prikazuje odnos momenta i brzine motora za različite iznose mrežnog napona za **konstantni teret** napajan motorom.
To su primjerice dizalice, tekuće trake i slično.  

<figure>
  <img src="{{ site.baseurl }}/assets/gitbook/images/torque-voltage-clean.svg" alt="Moment vs. brzina vrtnje za različite napone">
</figure>

Za ilustraciju su korištene vrijednosti iz [[2]](https://www.researchgate.net/publication/313773111_Fuzzy_Gain_Scheduling_of_PID_FGS-PID_for_Speed_Control_Three_Phase_Induction_Motor_Based_on_Indirect_Field_Oriented_Control_IFOC).

| Napon | Brzina rotora (o/min) | Klizanje (%)  | Struja (A)    |
| 60%   | 1363,365              | 9,1           | 26,442        |
| 70%   | 1408,410              | 6,1           | 21,515        |
| 80%   | 1432,434              | 4,5           | 18,504        |
| 90%   | 1447,449              | 3,5           | 16,386        |
| 100%  | 1459,461              | 2,7           | 14,175        |


> Ako se radi o teretu koji ima nelinearnu karakteristiku, kao što su pumpe ili ventilatori, graf izgleda kao na slici ispod.
> Funkcija tereta je izmišljena radi jednostavnog prikaza i funkcija glasi $$ 0.5\cdot (n_r \over n_s)^2$$
> U steady state proračunima, motori se najčešće aproksimiraju kao tereti konstantne snage.
{: .block-tip }

<figure>
  <img src="{{ site.baseurl }}/assets/gitbook/images/torque-voltage-pump.svg" alt="Moment vs. brzina vrtnje za različite napone za pumpe">
</figure>

| Napon | Brzina rotora (o/min) | Klizanje (%)  | Struja (A)    | Moment (p.u.) | 
| 60%   | 1198,199              | 20,1          | 49,821        |  0,319        |
| 70%   | 1285,287              | 36,6          | 45,042        |  0,366        |
| 80%   | 1339,341              | 10,7          | 40,549        |  0,397        |
| 90%   | 1375,377              | 8,3           | 36,57         |  0,416        |
| 100%  | 1399,401              | 6,7           | 33,50         |  0,433        |


> Za **dinamičke proračune**, motori se najčešće modeliraju kao **exponential recovery dinamički tereti (ERL)**. []
> Više o takvom modeliranju tereta navedeno je na [Motori u dinamici](admilara.github.io/voltage-control/pages/design/motors-and-dynamics/)    
{: .block-warning }







  
    
- Kad neki poremećaj prouzrokuje pad napona, može doći do "aktivacije" nekoliko mehanizama.
- - Prvo, s padom napona dolazi i do pada aktivnog i reaktivnog tereta kućanstava.
- - Industrijski tereti (aktivni i reaktivni), uglavnom se sastoje od indukcijskih motora, i neće se puno promijeniti.
- - Ali, kondenzatori, kojih u industriji sigurno ima značajna količina, davat će manje reaktivne kapacitivne snage, što će povećati (neto) iznos
reaktivnog tereta u mreži.
- - U isto vrijeme, pad rezidencijalnog tereta će smanjiti zauzeti kapacitet prijenosnih vodova i reaktivne gubitke u mreži.


Lista referenci:

\[1\]: Joe H. Chow; Juan J. Sanchez-Gasca, [Load and Induction Motor Models](https://ieeexplore.ieee.org/document/8958809) in 
Power System Modeling, Computation, and Control , IEEE, 2020, pp.295-325, doi: 10.1002/9781119546924.ch11

\[2\]: Ferdiansyah, Indra & Era, Purwanto & Windarko, Novie Ayub. (2016). 
[Fuzzy Gain Scheduling of PID (FGS-PID) for Speed Control 3PH Induction Motor](https://www.researchgate.net/publication/313773111_Fuzzy_Gain_Scheduling_of_PID_FGS-PID_for_Speed_Control_Three_Phase_Induction_Motor_Based_on_Indirect_Field_Oriented_Control_IFOC). 
EMITTER International Journal of Engineering Technology. 4. 10.24003/emitter.v4i2.147. 