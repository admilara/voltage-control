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
**Što se događa s rezidencijalnim i industrijskim teretima**?
- S padom napona dolazi i do pada radnog i jalovog tereta kućanstava.
- Često korišten statički model radnog i jalovog tereta izražava se kao eksponencijalna formula. 
- Takav model može uključivati i dio koji bi označavao frekvencijsku ovisnost tereta (jednadžba \eqref{frekv_ovisna}.
    
\begin{equation}
    P(V) = P_{0}\cdot \left({V \over V_{0}}\right)^\alpha
    \label{eq:static_radna}
\end{equation}
    
\begin{equation}
    Q(V) = Q_{0}\cdot \left({V \over V_{0}}\right)^\beta
    \label{eq:static_jalova}
\end{equation}
    
- u gore navedenim jednadžbama, $P_{0}$ i $Q_{0}$ te $V_{0}$ označavaju početne vrijednosti radne snage, jalove snage i napona u nekom čvorištu.
- $\alpha$ i $\beta$ su koeficijenti koji određuju tip tereta.

- Ako su eksponenti $\alpha = 0, \beta = 0$, tada se radi o **teretu konstantne snage**, neovisne o naponu (motori).
- Ako su eksponenti $\alpha = 1, \beta = 1$, tada se radi o **teretu konstantne struje**.
- Ako su eksponenti $\alpha = 2, \beta = 2$, tada se radi o **teretu konstantne impedancije**, čisti omski otpori.

- Radna snaga koji vuče neki potrošač, kad se uzme u obzir i frekvencijski ovisan dio glasi:
    
\begin{equation}
    P = P_{0} \cdot [p_1 V^2 + p_2 V + p_3] \cdot [1+k_p f \Delta f]
    \label{eq:frekv_ovisna}
\end{equation}

- Ako koristimo eksponencijalni model tereta, eksponenti $$\alpha$$ i $$\beta$$ za neke karakteristične terete su \ref{[1]}:

| Tip tereta    | $$\alpha$$ | $$\beta$$ |
| :-------- | :-------: | :-------: |
| Žarulje sa žarnom niti | 1,54    | 0 |
| Sobni klima uređaji | 0,50     | 2,5 |
| Ventilokonvektori    | 0,08    | 1,6 |
| Baterijski punjači | 2,59 | 4,06 |
| Fluo rasvjeta | 2,07 | 3,21 | 
    
    
- Kad neki poremećaj prouzrokuje pad napona, može doći do "aktivacije" nekoliko mehanizama.
- - Prvo, s padom napona dolazi i do pada aktivnog i reaktivnog tereta kućanstava.
- - Industrijski tereti (aktivni i reaktivni), uglavnom se sastoje od indukcijskih motora, i neće se puno promijeniti.
- - Ali, kondenzatori, kojih u industriji sigurno ima značajna količina, davat će manje reaktivne kapacitivne snage, što će povećati (neto) iznos
reaktivnog tereta u mreži.
- - U isto vrijeme, pad rezidencijalnog tereta će smanjiti zauzeti kapacitet prijenosnih vodova i reaktivne gubitke u mreži.


\label{[1]} Joe H. Chow; Juan J. Sanchez-Gasca, "Load and Induction Motor Models," in Power System Modeling, Computation, and Control , IEEE, 2020, pp.295-325, doi: 10.1002/9781119546924.ch11.
keywords: {Load modeling;Mathematical model;Induction motors;Atmospheric modeling;Analytical models;Computational modeling;Reactive power}

