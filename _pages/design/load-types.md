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

<div class="custom-block tip">
  <p>S obzirom na ovisnost o naponu, modele dijelimo na:</p>
  <ol>1. Model konstantne snage</ol>
  <ol>2. Model konstantne struje</ol>
  <ol>3. Model konstantne impedancije</ol>
</div>

#### Eksponencijalni model tereta

- Često korišten statički model radnog i jalovog opterećenja izražava se kao **eksponencijalna** formula.

\begin{equation}
    P(V) = P_{0}\cdot \left({V \over V_{0}}\right)^\{k_{pu}} \left({f \over f_0}\right)^{k_{pf}}
    \tag{3}\label{full_exp_radna}
\end{equation}
    
\begin{equation}
    Q(V) = Q_{0}\cdot \left({V \over V_{0}}\right)^\{k_{qu}} \left({f \over f_0}\right)^{k_{qf}}
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

