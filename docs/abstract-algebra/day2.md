---
title: "Day 2 — Quadratic Reciprocity (26 November)"
---

<div class="lang-switch"><a class="on">English</a><a href="../day2-ko/">한국어</a></div>

<div class="running-head"><span>Abstract Algebra</span><span>Day 2 · Quadratic Reciprocity</span></div>

# Day 2 — Quadratic Reciprocity { .part-title #day-2-quadratic-reciprocity }

<p class="source-note">Special lecture, 26 November 2026 · Serre, Chapter I · <a class="pdf-link" href="notes.pdf" download="Abstract-Algebra-Day-2.pdf">This day as PDF</a></p>

**In this day.** The second lemma on the Gauss sum and the proof of the quadratic reciprocity law; how the law is used to compute Legendre symbols; and, in an appendix, Eisenstein's proof of the law through Gauss's lemma and a product formula for $\sin mx$. The proof of Theorem 5 iii), also given on this day, is in Day 1, §3.2. The second lecture of the day, on Pythagorean triples, is the next part.

!!! quote "Conventions used in this day."
    - $\ell$ and $p$ are two distinct primes different from $2$.
    - $\Omega$ is an algebraic closure of $\mathbb F_p$, and $w \in \Omega$ is a primitive $\ell$th root of unity.
    - $y = \sum_{x \in \mathbb F_\ell}\left(\frac{x}{\ell}\right)w^x \in \Omega$ is the Gauss sum.
    - For an odd integer $n$, $\varepsilon(n) \equiv \frac{n-1}{2} \pmod 2$, as in Day 1.

---

## 3 Quadratic Reciprocity Law (continued) { #3-quadratic-reciprocity-law-continued }

### 3.3 Quadratic reciprocity law (continued) { #33-quadratic-reciprocity-law-continued }

We continue Gauss's proof of the reciprocity law.

!!! abstract "Theorem 6 (Gauss, quadratic reciprocity law)"
    Let $\ell$ and $p$ be two distinct primes different from $2$. Then

    $$
    \left(\frac{\ell}{p}\right) = \left(\frac{p}{\ell}\right)(-1)^{\varepsilon(\ell)\varepsilon(p)}.
    $$

Day 1 ended with the first lemma on the Gauss sum, $y^2 = (-1)^{\varepsilon(\ell)}\ell$ (Lemma 1). The second one is the following.

!!! abstract "Lemma 2"
    $y^{p-1} = \left(\dfrac{p}{\ell}\right)$.

!!! success "Proof"
    First, for any $a \in \mathbb F_\ell^*$,

    $$
    1 = \left(\frac{1}{\ell}\right) = \left(\frac{a\,a^{-1}}{\ell}\right) = \left(\frac{a}{\ell}\right)\left(\frac{a^{-1}}{\ell}\right),
    $$

    so $\left(\frac{a}{\ell}\right)$ and $\left(\frac{a^{-1}}{\ell}\right)$ have the same value: both $1$ or both $-1$.

    Since $\Omega$ has characteristic $p$, the Frobenius map $x \mapsto x^p$ is additive. The coefficients $\left(\frac{x}{\ell}\right) \in \{0, \pm 1\}$ satisfy $\left(\frac{x}{\ell}\right)^p = \left(\frac{x}{\ell}\right)$ because $p$ is odd. Hence, putting $z = xp$ (as $x$ runs over $\mathbb F_\ell$, so does $z$, since $p$ is invertible modulo $\ell$),

    $$
    y^p = \sum_{x \in \mathbb F_\ell}\left(\frac{x}{\ell}\right)w^{xp}
    = \sum_{z \in \mathbb F_\ell}\left(\frac{zp^{-1}}{\ell}\right)w^{z}
    = \left(\frac{p^{-1}}{\ell}\right)\sum_{z \in \mathbb F_\ell}\left(\frac{z}{\ell}\right)w^{z}
    = \left(\frac{p}{\ell}\right)y .
    $$

    By Lemma 1, $y^2 = \pm\ell \neq 0$ in $\mathbb F_p$, because $\ell \neq p$. So $y \neq 0$, and dividing by $y$ gives $y^{p-1} = \left(\frac{p}{\ell}\right)$. $\square$

!!! success "Proof of Theorem 6"
    Recall Lemma 1, $y^2 = (-1)^{\varepsilon(\ell)}\ell$, and Lemma 2, $y^{p-1} = \left(\frac{p}{\ell}\right)$. In $\mathbb F_p$, using the definition of the Legendre symbol modulo $p$ and Theorem 5 ii),

    $$
    \left(\frac{p}{\ell}\right) = y^{p-1} = (y^2)^{\frac{p-1}{2}} = \big((-1)^{\varepsilon(\ell)}\ell\big)^{\frac{p-1}{2}}
    = \left(\frac{(-1)^{\varepsilon(\ell)}\ell}{p}\right)
    = \left(\frac{-1}{p}\right)^{\varepsilon(\ell)}\left(\frac{\ell}{p}\right)
    = (-1)^{\varepsilon(\ell)\varepsilon(p)}\left(\frac{\ell}{p}\right).
    $$

    Both sides are $\pm 1$, and $1 \neq -1$ in $\mathbb F_p$ because $p \neq 2$, so the equality also holds between integers. Multiplying by $(-1)^{\varepsilon(\ell)\varepsilon(p)}$ gives Theorem 6. $\square$

Here is a translation of the quadratic reciprocity law.

!!! info "Remark"
    Write $\ell\,R\,p$ if $\ell$ is a square modulo $p$ (a **quadratic residue**), and $\ell\,N\,p$ otherwise. Theorem 6 means that

    - $\ell\,R\,p$ if and only if $p\,R\,\ell$, when $p$ or $\ell$ is congruent to $1$ modulo $4$;
    - $\ell\,R\,p$ if and only if $p\,N\,\ell$, when both $p$ and $\ell$ are congruent to $-1$ modulo $4$.

    Equivalently,

    $$
    \left(\frac{\ell}{p}\right)\left(\frac{p}{\ell}\right) = (-1)^{(p-1)(\ell-1)/4}.
    $$

By Theorem 6, Legendre symbols can be computed by successive reductions.

!!! example "Example (successive reductions)"
    $$
    \left(\frac{29}{43}\right) = \left(\frac{43}{29}\right) = \left(\frac{14}{29}\right) = \left(\frac{2}{29}\right)\left(\frac{7}{29}\right) = -\left(\frac{7}{29}\right) = -\left(\frac{29}{7}\right) = -\left(\frac{1}{7}\right) = -1 .
    $$

    The first and fifth steps use Theorem 6 with $29 \equiv 1 \pmod 4$; the second and sixth reduce the top number ($43 \equiv 14 \pmod{29}$, $29 \equiv 1 \pmod 7$); the fourth uses Theorem 5 iii) with $29 \equiv 5 \pmod 8$.

---

## Appendix — Eisenstein's Proof of the Quadratic Reciprocity Law { #appendix-eisensteins-proof }

Let $p \neq 2$ be prime, and let $S$ be a subset of $\mathbb F_p^*$ with $\mathbb F_p^* = S \sqcup -S$ (for example $S = \{1, 2, \dots, \frac{p-1}{2}\}$). For $s \in S$ and $a \in \mathbb F_p^*$, exactly one of $as$ and $-as$ lies in $S$, so we can write

$$
as = e_s(a)\,s_a, \qquad e_s(a) = \pm 1,\quad s_a \in S .
$$

!!! abstract "Lemma (Gauss)"
    $\left(\dfrac{a}{p}\right) = \displaystyle\prod_{s \in S}e_s(a)$.

!!! success "Proof"
    First observe that $s \mapsto s_a$ is a bijection of $S$ for fixed $a$. If $s, s'$ are two elements of $S$ with $s_a = s'_a$, then $as = \pm as'$, so $s = \pm s'$; since $S \cap -S = \varnothing$, $s = s'$. An injective map of a finite set to itself is a bijection.

    Since $S$ has $\frac{p-1}{2}$ elements,

    $$
    \left(\frac{a}{p}\right)\prod_{s \in S}s = a^{\frac{p-1}{2}}\prod_{s \in S}s = \prod_{s \in S}(as) = \prod_{s \in S}e_s(a)\,s_a = \prod_{s \in S}e_s(a)\prod_{s \in S}s_a = \prod_{s \in S}e_s(a)\prod_{s \in S}s .
    $$

    The product $\prod_{s \in S}s$ is nonzero, so $\left(\frac{a}{p}\right) = \prod_{s \in S}e_s(a)$. $\square$

!!! example "Example"
    For an odd prime $p$, take $a = 2$ and $S = \{1, \dots, \frac{p-1}{2}\}$. Then

    $$
    e_s(2) = \begin{cases} 1 & \text{if } 2s \le \frac{p-1}{2},\\ -1 & \text{otherwise.}\end{cases}
    $$

    From this we get $\left(\frac{2}{p}\right) = (-1)^{n(p)}$, where $n(p) = \big|\{x \in \mathbb Z \mid \frac{p-1}{4} < x \le \frac{p-1}{2}\}\big|$. Note that $n(p) = k$ if $p = 4k + 1$ or $p = 4k - 1$. Thus

    $$
    \left(\frac{2}{p}\right) = \begin{cases} 1 & \text{if } p \equiv \pm 1 \pmod 8,\\ -1 & \text{if } p \equiv \pm 5 \pmod 8.\end{cases}
    $$

    Compare Theorem 5 iii).

!!! abstract "Lemma"
    For a positive odd integer $m$,

    $$
    \sin mx = (-4)^{(m-1)/2}\sin x\prod_{j=1}^{(m-1)/2}\left(\sin^2 x - \sin^2\frac{2\pi j}{m}\right).
    $$

!!! success "Proof"
    Put $z = e^{ix}$. Then

    $$
    \frac{\sin mx}{\sin x} = \frac{z^m - z^{-m}}{z - z^{-1}} = z^{m-1} + z^{m-3} + \dots + z^{-(m-1)} = 1 + 2\sum_{k=1}^{(m-1)/2}\cos 2kx ,
    $$

    since $m$ is odd. Each $\cos 2kx$ is a polynomial of degree $k$ in $\cos 2x = 1 - 2\sin^2 x$, so $\frac{\sin mx}{\sin x}$ is a polynomial $f$ of degree $\frac{m-1}{2}$ in $\sin^2 x$.

    Its leading coefficient: $\sin^2 x = -\frac14 z^2 + \frac12 - \frac14 z^{-2}$, so the power $z^{m-1}$ comes only from the top term $c\,(\sin^2 x)^{(m-1)/2}$ of $f$, with coefficient $c\left(-\frac14\right)^{(m-1)/2}$. This must equal $1$, so $c = (-4)^{(m-1)/2}$.

    Its roots: for $j = 1, \dots, \frac{m-1}{2}$, $x = \frac{2\pi j}{m}$ gives $\sin mx = 0$ and $\sin x \neq 0$, so $\xi_j = \sin^2\frac{2\pi j}{m}$ is a root of $f$. These are distinct numbers: the angles $\frac{2\pi j}{m}$ lie in $(0, \pi)$, and $\sin^2\theta = \sin^2\theta'$ there only if $\theta' = \theta$ or $\theta' = \pi - \theta$; the latter would give $2(j + j') = m$, impossible since $m$ is odd. A polynomial of degree $\frac{m-1}{2}$ with these $\frac{m-1}{2}$ distinct roots and leading coefficient $c$ is $c\prod_j(X - \xi_j)$. Multiplying by $\sin x$ gives the lemma. $\square$

!!! info "Remark"
    $\dfrac{\sin(2n+1)x}{\sin x} = W_n(\cos 2x) = W_n(1 - 2\sin^2 x)$, where $W_n$ is the **Chebyshev polynomial of the fourth kind**: $W_0(z) = 1$, $W_1(z) = 2z + 1$, and $W_{n+1}(z) = 2zW_n(z) - W_{n-1}(z)$ for $n \ge 1$.

!!! success "Proof of Theorem 6 (Eisenstein)"
    Let $\ell$ and $p$ be two distinct odd primes, and $S = \{1, 2, \dots, \frac{p-1}{2}\}$. For $s \in S$ we have $\ell s \equiv e_s(\ell)\,s_\ell \pmod p$. Since $\sin$ is an odd function of period $2\pi$,

    $$
    \sin\frac{2\pi\ell s}{p} = e_s(\ell)\,\sin\frac{2\pi s_\ell}{p} .
    $$

    By Gauss's lemma, and since $s \mapsto s_\ell$ is a bijection of $S$ (the numbers $\sin\frac{2\pi s}{p}$, $s \in S$, are nonzero),

    $$
    \left(\frac{\ell}{p}\right) = \prod_{s=1}^{(p-1)/2}e_s(\ell) = \prod_{s=1}^{(p-1)/2}\frac{\sin(2\pi\ell s/p)}{\sin(2\pi s/p)} .
    $$

    The lemma with $m = \ell$ and $x = \frac{2\pi s}{p}$ turns this into

    $$
    \left(\frac{\ell}{p}\right) = (-4)^{(\ell-1)(p-1)/4}\prod_{s=1}^{(p-1)/2}\prod_{t=1}^{(\ell-1)/2}\left(\sin^2\frac{2\pi s}{p} - \sin^2\frac{2\pi t}{\ell}\right).
    $$

    Exchanging the roles of $\ell$ and $p$,

    $$
    \left(\frac{p}{\ell}\right) = (-4)^{(\ell-1)(p-1)/4}\prod_{t=1}^{(\ell-1)/2}\prod_{s=1}^{(p-1)/2}\left(\sin^2\frac{2\pi t}{\ell} - \sin^2\frac{2\pi s}{p}\right).
    $$

    The two double products have the same $\frac{(p-1)(\ell-1)}{4}$ factors with opposite signs. Hence

    $$
    \left(\frac{\ell}{p}\right) = (-1)^{\frac{p-1}{2}\cdot\frac{\ell-1}{2}}\left(\frac{p}{\ell}\right) = (-1)^{\varepsilon(\ell)\varepsilon(p)}\left(\frac{p}{\ell}\right). \qquad \square
    $$
