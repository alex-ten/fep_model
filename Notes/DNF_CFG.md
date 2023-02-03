# Context-free, disjunctive normal form (DNF) grammar

- $(\text{S1}) \qquad S \rightarrow \forall x~l(x) \Leftrightarrow (D)$ 
  - For all objects $x$, label $x$ as $1$ if and only if the definition $D$ us true
- $(\text{D1}) \qquad D \rightarrow (C)~\lor~D$
- $(\text{D2}) \qquad D \rightarrow False$
  - Definition $D$ is a disjunction (`or`) of $C$-terms.
  - Each $C$-term is a ***sense*** of a definition -- one of potentially many *sufficient* conditions for a definition to apply (at least one needs to apply).
- $(\text{C1}) \qquad C \rightarrow P~\land~C$
- $(\text{C2}) \qquad C \rightarrow True$
  - Each $C$-term is a conjunction of $P$-terms. ***predicates***
  - Eacg $P$-term is a ***predicate*** -- one of potentially many *necessary* conditions that satisfy a sense of a definition (all need to apply).
---
- $(\text{P1}) \qquad P \rightarrow F_1$

$\qquad \vdots$

- $(\text{PN}) \qquad P \rightarrow F_N$
  - Each of the $N$ predicates $\text{P}$ depends on its corresponding feature $F$. ($F_i$ terms are called ***feature predicates***)
---
- $(\text{F}_11) \qquad F_1 \rightarrow f_1(x) = 1$
- $(\text{F}_12) \qquad F_1 \rightarrow f_1(x) = 0$

$\qquad \vdots$

- $(\text{F}_N1) \qquad  F_N \rightarrow f_N(x) = 1$
- $(\text{F}_N2) \qquad  F_N \rightarrow f_N(x) = 0$
  - Each feature $F_i$ is either present or absent in a given object $x$. ($f_i(x) = 1$ equations are called ***assertions***)
---

