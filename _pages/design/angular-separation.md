---
title: Razlike kuteva
author: admilara
date: 2025-03-19
category: Kutno razdvajanje
layout: post
mermaid: true
---

Kut je jedna od ključnih veličina koja određuje različite aspekte stabilnosti i upravljanja elektroenergetskim sustavom.
Različite vrste definiranih kuteva pružaju bitne informacije o faktoru snage, smjeru toka snage, opterećenju sustava i 
njegovoj stabilnosti, kao i stabilnosti proizvodnih postrojenja. 

Tri su važna kuta za znati:
- Fazni kut (engl. __phase angle__), $\Theta$
- Kut opterećenja (engl. __load angle__), $\delta$
- Kut snage (engl. __power angle__), $\delta$

#### Fazni kut 

Fazni kut u nekom trenutku i mjestu u sustavu je razlika kuteva (razlika u fazi) između sinusa napona i struje. 
U induktivnom sustavu, fazni kut je pozitivan i struja kasni za naponom. Ako napon kasni za strujom, kao što je slučaj
u kapacitivnom sustavu, fazni kut je negativan. 

<figure><img src="assets/gitbook/images/phase_angle.PNG" alt="Fazni kut"></figure>
![]({{ site.baseurl }}/assets/gitbook/images/torque-voltage.png)



#### Kut opterećenja 

Kut opterećenja važan je faktor u određivanju aktivne snage koju isporučuje sinkroni generator ili aktivne snage
koju troši sinkroni motor.

Magnetsko polje koje stvara uzbudni namot dovodi se u vrtnju mehaničkom rotacijom čitavog rotora. Struje statora koje
teku kad je stroj pod opterećenjem stvaraju okretno polje koje ima jednaku brzinu kao i polje rotora tj. sam rotor. 
Kut opterećenja sinkronog električnog struja definira se kao kutna razlika između **rotora i okretnog magnetskog polja statora**.

<figure><img src="assets/gitbook/images/torque_angle.PNG" alt="Kut opterećenja"></figure>

**Kut opterećenja i napon**
Iznos napona generatora ovisi o struji uzbude koja dolazi na rotor. Unutarnji napon generatora $E_{0}$ ovisi o primarnom
protjecanju tj. o struji uzbude - veća struja uzbude znači viši napon generatora. Razlika kuteva između dva okretna
magnetska polja može se promatrati i kao razlika kuteva njihovih induciranih napona.

<figure>
    <img src="assets/gitbook/images/torque_angle_and_voltage.PNG" alt="Kut opterećenja i napon">
</figure>

#### Kut snage
__Power angle__ u engleskoj literaturi, je kutna razlika između faza napona na dvije lokacije u elektroenergetskom 
sustavu. 

<figure><img src="assets/gitbook/images/power_angle.PNG" alt="Kut snage"></figure>
