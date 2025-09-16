---
title: 1.2 Izvori i ponori jalove snage
author: admilara
date: 2025-07-09
category: 1.2. Izvori i ponori jalove snage
layout: post
mermaid: true
---

### Izvori i ponori jalove snage

S obzirom da smo razmatrali jednostavni sustav s dvije sabirnice s jednim izvorom i jednim ponorom, iz prethodnog
poglavlja vidljiva je jaka ovisnost napona na strani tereta o apsorpciji ili injekciji jalove snage tereta.

<span style="color:blue"><b> Upravljanje naponom je usko vezano uz upravljanje jalovom snagom. </b></span>

<span style="color:blue"><b> Injekcija jalove snage u čvoru koji nije direktno naponski reguliran općenito će povećati napon tog čvorišta i mreže oko njega. </b></span>


Najvažniji izvori i ponori jalove snage u elektroenergetskom sustavu su:

#### Osnovni elementi prijenosnog sustava

- **Nadzemni vodovi** 
    - Pod malim opterećenjem, vod generira jalovu snagu.
    - Proizvodnja jalove snage voda od paralelnih kapaciteta je veća od gubitaka jalove snage na serijskoj impedanciji.
    - Pod velikim opterećenjem voda, vod apsorbira više jalove snage nego što je proizvodi.
    
- **Kabeli**
    - Kabeli gotovo uvijek proizvode jalovu snagu budući da gubici jalove snage nikad ne prelaze proizvodnju zbog velikog
    paralelnog kapaciteta kabela.

- **Transformatori** 
    - Uvijek apsorbiraju jalovu snagu zbog jalovih gubitaka.
    - Ukoliko trafo ima promjenjiv prijenosni omjer, može mijenjati tok jalove snage između primara i sekundara.

#### Uređaji za kompenzaciju

Kako je već rečeno, oblik P-V krivulje nekompenziranog sustava ovisi o faktoru snage
tereta te impedanciji voda i naponu na kraju prijenosnog sustava.

1. **Paralelni kondenzatori**
    - djeluju dodavanjem kapacitivne admitancije teretu, čime se može podesiti faktor
    snage tereta koji se vidi sa strane prijenosnog sustava
    - Iznos jalove snage koju kondenzator pruža je kvadratno ovisan o naponu tako da 
    **pri nižim naponima kondenzator daje manju potporu sustavu**
    - Ovaj tip kompenzacije povećava praktičnu granicu prijenosa, ali i povećava i kritični napon 
    te smanjuje krutost sustava. 
    - Slično tome, proizvodnja jalove snage kabelima i nadzemnim vodovima kvadratno je ovisna o naponu
    i ima štetan utjecan na krutost sustava.

Na slici ispod vidljiva je PV krivulja nekompenziranog sustava i sustava u kojem je korištena 
metoda kompenzacije paralelni kompenzator, prigušnica ili injekcija fiksnog iznosa Q.
    
<figure>
    <img src="{{ site.baseurl }}/assets/gitbook/images/shunts-pv-curves.svg" alt="Onion surface">
</figure>


1. **Generatori**
    - Generatorima se može upravljati na način da oni reguliraju napon sabirnica te generiraju/apsorbiraju
    jalovu snagu ovisno o potrebama mreže.
    - Normalni način rada generatora je u režimu regulacije napona u kojem ARN (AVR) djeluje na uzbudu 
    sinkronog stroja. Unutar granica normalnog rada generatora, može se regulirati napon sabirnica na koje
    je generator spojen, 
    - Iznos jalove snage koju je potrebno proizvesti da bi regulirao napon ovisi o opterećenju i strukturi
    okolnog sustava. 

3. **OLTC**
    - On load tap changeri - transformatori s regulacijom pod opterećenjem mogu **pomicati P-V krivulju po v-osi** 
    i na taj način povećati praktirčnu granicu prijenosa bez da pomiču teorijsku granicu prijenosa
    - Transformatori opremljeni preklopkom za regulaciju mogu prebacivati jalovu snagu između primara i sekundara i 
    tako regulirati napon na niženaponskoj strani. 
    - Reguliranjem niskonaponske strane utječe se i na višenaponsku stranu - ovaj utjecaj je u normalnim 
    uvjetima zaneativ, ali može biti značajan faktor u incidentnim stanjima naponske nestabilnosti. 
    - Povećanjem prijenosnog omjera trafoa žrtvuje se krutost sustava i praktična granica se pomiče bliže teorijskoj granici prijenosa.


Na slici ispod prikazane su PV krivulja nekompenziranog sustava te sustava u kojem je korištena 
metoda kompenzacije povećanje početnog napona $E$, serijski kondenzatori te upotreba tap changera.  
    
<figure>
    <img src="{{ site.baseurl }}/assets/gitbook/images/oltc-pv-curves.svg" alt="Onion surface">
</figure>















Lista referenci:

\[1\]: Larsson, M. (2001). [Coordinated Voltage Control in Electric Power Systems](https://portal.research.lu.se/en/publications/coordinated-voltage-control-in-electric-power-systems). 
Doctoral Thesis (compilation), Division for Industrial Electrical Engineering and Automation. Mats Larsson, IEA, LTH, Box 118, S-221 00 Lund, Sweden,.

