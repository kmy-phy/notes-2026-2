---
title: "Day 1 — Finite Fields (25 November)"
---

<div class="lang-switch"><a class="on">English</a><a href="../day1-ko/">한국어</a></div>

<div class="running-head"><span>Abstract Algebra</span><span>Day 1 · Finite Fields</span></div>

# Day 1 — Finite Fields { .part-title }

<p class="source-note">Special lecture, 25 November 2026 · Serre, Chapter I · <a class="pdf-link" href="notes.pdf" download="Abstract-Algebra-Day-1.pdf">This day as PDF</a></p>

**In this day.** Finite fields: the Frobenius map, the existence and uniqueness of the field $\mathbb F_q$, and the cyclicity of its multiplicative group. Then squares in $\mathbb F_q$, the Legendre symbol, and the start of Gauss's proof of quadratic reciprocity, up to the first lemma on the Gauss sum. The lecture skipped §2 (equations over a finite field); its headings are kept so that the numbering matches Serre.

!!! quote "Conventions used in this day."
    - All fields are commutative.
    - For a field $K$, the map $\mathbb Z \to K$ sending $1 \mapsto 1$ has as image an integral domain, hence isomorphic to $\mathbb Z$ or to $\mathbb Z/p\mathbb Z$ for some prime $p$. Its field of fractions is isomorphic to $\mathbb Q$ or to $\mathbb Z/p\mathbb Z = \mathbb F_p$. In the first case we say $\operatorname{char} K = 0$; in the second, $\operatorname{char} K = p$.
    - If $\operatorname{char} K = p \neq 0$, then $p$ is the smallest integer $n > 0$ such that $n \cdot 1 = 0$.
    - $K^*$ is the multiplicative group of nonzero elements of $K$.
    - $p$ always denotes a prime and $q = p^f$ a power of it.

---

## 1 Finite Fields

### 1.1 Finite fields

!!! abstract "Lemma (Frobenius map)"
    If $\operatorname{char} K = p$, then $\sigma\colon K \to K$, $x \mapsto x^p$, is an injective homomorphism with image $K^p = \{x^p \mid x \in K\}$.

!!! success "Proof"
    Since $K$ is commutative, $\sigma(xy) = (xy)^p = x^p y^p = \sigma(x)\sigma(y)$. By the binomial theorem,

    $$
    \sigma(x + y) = (x + y)^p = x^p + \binom{p}{1}x^{p-1}y + \cdots + \binom{p}{p-1}xy^{p-1} + y^p = x^p + y^p = \sigma(x) + \sigma(y),
    $$

    because $p \mid \binom{p}{k}$ for $0 < k < p$. Finally, if $\sigma(x) = 0$ then $x^p = 0$; if $x \neq 0$ we could multiply by $(x^{-1})^p$ and get $1 = 0$, so $x = 0$. Hence $\ker\sigma = \{0\}$ and $\sigma$ is injective. $\square$

!!! info "Remark"
    If $K$ is finite or algebraically closed, then $\sigma$ is an automorphism of $K$. For $K$ finite, an injective map $K \to K$ is surjective. For $K$ algebraically closed, take any $y \in K$: the equation $X^p - y = 0$ has a root $z \in K$, so $z^p = y$ and $y$ lies in the image.

!!! abstract "Theorem 1"
    i) If $K$ is a finite field, then $\operatorname{char} K = p \neq 0$ and $|K| = p^f$, where $f = [K : \mathbb F_p]$.

    ii) Let $p$ be prime, $q = p^f$, and $\Omega$ an algebraically closed field of characteristic $p$. There is a unique subfield $\mathbb F_q$ of $\Omega$ with $q$ elements, namely $\mathbb F_q = \{x \in \Omega \mid x^q - x = 0\}$.

    iii) All finite fields with $q = p^f$ elements are isomorphic to $\mathbb F_q$.

!!! success "Proof of i)"
    A finite field cannot contain $\mathbb Q$, so its characteristic is a prime $p$ and it contains $\mathbb F_p$. As a vector space over $\mathbb F_p$ of dimension $f = [K : \mathbb F_p]$, it has $|K| = p^f$ elements. $\square$

!!! success "Proof of ii)"
    Let $\Omega$ be algebraically closed with $\operatorname{char}\Omega = p$, and $q = p^f$. Put

    $$
    \mathbb F_q = \{x \in \Omega \mid x^q - x = 0\}.
    $$

    The polynomial $X^q - X$ has derivative $qX^{q-1} - 1 = -1 \neq 0$, so it has no repeated roots, and since $\Omega$ is algebraically closed it has exactly $q$ roots: $|\mathbb F_q| = q$. The map $\sigma\colon \Omega \to \Omega$, $x \mapsto x^q$, is an automorphism (a power of the Frobenius map), and $\mathbb F_q$ is the set of its fixed points, hence a subfield.

    For uniqueness, let $K$ be a subfield of $\Omega$ with $q$ elements. Then $K^*$ is a group with $q - 1$ elements, so $x^{q-1} = 1$ for all $x \in K^*$, and therefore $x^q = x$ for all $x \in K$. Thus $K \subseteq \mathbb F_q$, and since both have $q$ elements, $K = \mathbb F_q$. $\square$

*Proof of iii).* Omitted in the lecture.

!!! info "Remark"
    The uniqueness in ii) is inside a fixed algebraically closed field $\Omega$. The uniqueness in iii) is up to isomorphism.

### 1.2 The multiplicative group of a finite field

!!! abstract "Theorem 2"
    For a prime $p$ and $q = p^f$, the multiplicative group $\mathbb F_q^*$ of $\mathbb F_q$ is cyclic of order $q - 1$.

It rests on the following group-theoretic lemma.

!!! abstract "Lemma 2"
    Let $H$ be a finite group of order $n$. Suppose that, for every divisor $d$ of $n$, the set $\{x \in H \mid x^d = 1\}$ has at most $d$ elements. Then $H$ is cyclic.

!!! success "Proof of Theorem 2"
    Take $H = \mathbb F_q^*$ and $n = q - 1$. For each divisor $d$ of $n$, the equation $x^d = 1$ is a polynomial equation of degree $d$ in the field $\mathbb F_q$, so it has at most $d$ solutions. By Lemma 2, $H$ is cyclic. $\square$

!!! info "Remark"
    The proof shows that every finite subgroup of the multiplicative group of a field is cyclic.

To prove Lemma 2 we need the following lemma.

!!! abstract "Lemma 1"
    For an integer $n \geq 1$, $n = \sum_{d \mid n} \phi(d)$, where $\phi$ is the Euler $\phi$ function.

!!! success "Proof of Lemma 1"
    For each $d \mid n$, let $C_d$ be the unique subgroup of $\mathbb Z/n\mathbb Z$ of order $d$, and let $\Phi_d$ be the set of generators of $C_d$. Then $|\Phi_d| = \phi(d)$. Every element of $\mathbb Z/n\mathbb Z$ generates exactly one of the $C_d$, namely the subgroup it generates, so

    $$
    \mathbb Z/n\mathbb Z = \bigsqcup_{d \mid n} \Phi_d,
    \qquad
    n = |\mathbb Z/n\mathbb Z| = \Big|\bigsqcup_{d \mid n}\Phi_d\Big| = \sum_{d \mid n}\phi(d). \qquad \square
    $$

!!! example "Example ($n = 12$)"
    In $\mathbb Z/12\mathbb Z$:

    | $d$ | $C_d$ | $\Phi_d$ | $\phi(d)$ |
    |---|---|---|---|
    | 1 | $\{0\}$ | $\{0\}$ | 1 |
    | 2 | $\{0, 6\}$ | $\{6\}$ | 1 |
    | 3 | $\{0, 4, 8\}$ | $\{4, 8\}$ | 2 |
    | 4 | $\{0, 3, 6, 9\}$ | $\{3, 9\}$ | 2 |
    | 6 | $\{0, 2, 4, 6, 8, 10\}$ | $\{2, 10\}$ | 2 |
    | 12 | $\mathbb Z/12\mathbb Z$ | $\{1, 5, 7, 11\}$ | 4 |

    and indeed $1 + 1 + 2 + 2 + 2 + 4 = 12$.

!!! success "Proof of Lemma 2"
    Let $d \mid n$. If $H$ contains an element $z$ of order $d$, then $\langle z\rangle = \{1, z, \dots, z^{d-1}\}$ is cyclic of order $d$, and $\langle z\rangle \subseteq \{x \in H \mid x^d = 1\}$. By hypothesis the right-hand side has at most $d$ elements, so the two sets are equal: every $y \in H$ with $y^d = 1$ lies in $\langle z\rangle$. In particular every element of order $d$ is a generator of $\langle z\rangle$, and there are exactly $\phi(d)$ of those.

    Thus the number of elements of order $d$ in $H$ is either $0$ or $\phi(d)$. Every element of $H$ has some order $d \mid n$, so these numbers add up to $n$. If one of them were zero, the sum would be less than $\sum_{d\mid n}\phi(d) = n$ (Lemma 1), a contradiction. Hence, for every $d \mid n$, $H$ has exactly $\phi(d)$ elements of order $d$. In particular it has $\phi(n) \geq 1$ elements of order $n$, so $H$ is cyclic. $\square$

---

## 2 Equations over a Finite Field

### 2.1 Power sums

<div class="admonition skipped" markdown>
This section was not covered in the lecture and is skipped in these notes. It shows that $\sum_{x \in K} x^u$ is $-1$ when $u \geq 1$ is divisible by $q - 1$ and $0$ otherwise; nothing later on Day 1 depends on it.
</div>

### 2.2 Chevalley's theorem

<div class="admonition skipped" markdown>
This section was not covered in the lecture and is skipped in these notes. It contains the Chevalley–Warning theorem (the number of common zeros of polynomials with $\sum \deg f_\alpha < n$ is divisible by $p$) and its corollaries on quadratic forms; nothing later on Day 1 depends on it.
</div>

---

## 3 Quadratic Reciprocity Law

### 3.1 Squares in finite fields

Let $q = p^f$. Recall that $\mathbb F_q^*$ is cyclic of order $q - 1$, so $x^{q-1} = 1$ for all $x \in \mathbb F_q^*$.

!!! abstract "Theorem 4"
    (a) If $p = 2$, then every element of $\mathbb F_q$ is a square.

    (b) If $p \neq 2$, then the squares $\mathbb F_q^{*2} = \{x^2 \mid x \in \mathbb F_q^*\}$ form a subgroup of index $2$ in $\mathbb F_q^*$, which is the kernel of the homomorphism $x \mapsto x^{(q-1)/2}$ with values in $\{\pm 1\}$. In short, the sequence

    $$
    1 \longrightarrow \mathbb F_q^{*2} \longrightarrow \mathbb F_q^* \longrightarrow \{\pm 1\} \longrightarrow 1
    $$

    is exact, that is, at each place the kernel of the outgoing map equals the image of the incoming one.

!!! success "Proof of (a)"
    For $p = 2$, the map $x \mapsto x^2$ is the Frobenius map, which is an automorphism of the finite field $\mathbb F_q$; in particular it is surjective. $\square$

!!! success "Proof of (b)"
    Let $p \neq 2$ and let $\Omega$ be an algebraic closure of $\mathbb F_q$. For $x \in \mathbb F_q^*$, choose $y \in \Omega$ with $y^2 = x$. Then

    $$
    y^{q-1} = x^{(q-1)/2} = \pm 1, \qquad \text{since } \big(x^{(q-1)/2}\big)^2 = x^{q-1} = 1 .
    $$

    Hence $x$ is a square in $\mathbb F_q$ if and only if $y \in \mathbb F_q^*$, if and only if $y^{q-1} = 1$ (by Theorem 1 ii), $\mathbb F_q^*$ is exactly the set of $y \in \Omega$ with $y^{q-1} = 1$). Thus $\mathbb F_q^{*2}$ is the kernel of the map $x \mapsto x^{(q-1)/2}$ with values in $\{\pm 1\}$.

    The squaring map $\mathbb F_q^* \to \mathbb F_q^*$ has kernel $\{\pm 1\}$, which has two elements because $p \neq 2$; so its image $\mathbb F_q^{*2}$ has $(q-1)/2$ elements and index $2$. In particular the map $x \mapsto x^{(q-1)/2}$ is onto $\{\pm 1\}$. $\square$

### 3.2 Legendre symbol

!!! note "Definition (Legendre symbol)"
    For a prime $p \neq 2$ and $x \in \mathbb F_p^*$, the **Legendre symbol** is

    $$
    \left(\frac{x}{p}\right) = x^{(p-1)/2} \in \{\pm 1\}.
    $$

!!! info "Remark"
    - As a convention, the symbol is extended to all of $\mathbb F_p$ by putting $\left(\frac{0}{p}\right) = 0$.
    - If $x \in \mathbb Z$ has image $x' \in \mathbb F_p$, we define $\left(\frac{x}{p}\right) = \left(\frac{x'}{p}\right)$, so that $\left(\frac{x}{p}\right)\left(\frac{y}{p}\right) = \left(\frac{xy}{p}\right)$ holds.
    - $\left(\frac{x}{p}\right) = 1$ is equivalent to $x \in \mathbb F_p^{*2}$ (Theorem 4).
    - If $x \in \mathbb F_p^*$ and $y \in \Omega$ is a square root of $x$, then $\left(\frac{x}{p}\right) = y^{p-1}$.

    Altogether,

    $$
    \left(\frac{x}{p}\right) =
    \begin{cases}
    0 & x \equiv 0 \pmod p,\\
    1 & x \equiv y^2 \pmod p \text{ for some } y \not\equiv 0,\\
    -1 & \text{otherwise.}
    \end{cases}
    $$

If $n$ is an odd integer, let $\varepsilon(n)$ and $\omega(n)$ be the elements of $\mathbb Z/2\mathbb Z$ defined by

$$
\varepsilon(n) \equiv \frac{n-1}{2} \pmod 2 =
\begin{cases} 0 & n \equiv 1 \pmod 4,\\ 1 & n \equiv -1 \pmod 4,\end{cases}
\qquad
\omega(n) \equiv \frac{n^2-1}{8} \pmod 2 =
\begin{cases} 0 & n \equiv \pm 1 \pmod 8,\\ 1 & n \equiv \pm 5 \pmod 8.\end{cases}
$$

Note that $\varepsilon\colon (\mathbb Z/4\mathbb Z)^* \to \mathbb Z/2\mathbb Z$ and $\omega\colon (\mathbb Z/8\mathbb Z)^* \to \mathbb Z/2\mathbb Z$ are homomorphisms.

!!! abstract "Theorem 5"
    i) $\left(\frac{1}{p}\right) = 1$.

    ii) $\left(\frac{-1}{p}\right) = (-1)^{\varepsilon(p)}$.

    iii) $\left(\frac{2}{p}\right) = (-1)^{\omega(p)}$.

!!! info "Remark"
    Theorem 5 can be expressed as follows:

    - $-1$ is a square modulo $p$ if and only if $p \equiv 1 \pmod 4$;
    - $2$ is a square modulo $p$ if and only if $p \equiv \pm 1 \pmod 8$.

<div class="admonition skipped" markdown>
The proof of iii) was not covered in the lecture and is skipped in these notes. (Parts i) and ii) follow at once from the definition: $1^{(p-1)/2} = 1$ and $(-1)^{(p-1)/2} = (-1)^{\varepsilon(p)}$.)
</div>

### 3.3 Quadratic reciprocity law

!!! abstract "Theorem 6 (Gauss, quadratic reciprocity law)"
    Let $\ell$ and $p$ be two distinct primes different from $2$. Then

    $$
    \left(\frac{\ell}{p}\right) = \left(\frac{p}{\ell}\right)(-1)^{\varepsilon(\ell)\varepsilon(p)}.
    $$

Here $\left(\frac{\ell}{p}\right)$ is computed modulo $p$ and $\left(\frac{p}{\ell}\right)$ modulo $\ell$.

Let $\Omega$ be an algebraic closure of $\mathbb F_p$, and let $w \in \Omega$ be a primitive $\ell$th root of unity. For $x \in \mathbb F_\ell$, the element $w^x$ is well defined, since $w^\ell = 1$. We form the **Gauss sum**

$$
y = \sum_{x \in \mathbb F_\ell}\left(\frac{x}{\ell}\right)w^x \in \Omega .
$$

Serre proves two lemmas about this sum. Day 1 ended with the first.

!!! abstract "Lemma 1"
    $y^2 = (-1)^{\varepsilon(\ell)}\,\ell$. (By abuse of notation, $\ell$ also denotes the image of $\ell$ in the field $\mathbb F_p$.)

!!! success "Proof"
    Expanding the square and putting $u = x + z$, $t = z$,

    $$
    y^2 = \sum_{x, z \in \mathbb F_\ell}\left(\frac{xz}{\ell}\right)w^{x+z} = \sum_{u, t \in \mathbb F_\ell}\left(\frac{t(u-t)}{\ell}\right)w^u .
    $$

    The terms with $t = 0$ vanish. For $t \neq 0$, write $t(u - t) = (-1)\,t^2\,(1 - ut^{-1})$; since the symbol is multiplicative and $\left(\frac{t^2}{\ell}\right) = 1$,

    $$
    y^2 = \sum_{u \in \mathbb F_\ell,\ t \in \mathbb F_\ell^*}\left(\frac{-1}{\ell}\right)\left(\frac{t^2}{\ell}\right)\left(\frac{1 - ut^{-1}}{\ell}\right)w^u
    = (-1)^{\varepsilon(\ell)}\sum_{u \in \mathbb F_\ell,\ t \in \mathbb F_\ell^*}\left(\frac{1 - ut^{-1}}{\ell}\right)w^u ,
    $$

    using Theorem 5 ii). Hence

    $$
    (-1)^{\varepsilon(\ell)}y^2 = \sum_{u \in \mathbb F_\ell} C_u\,w^u, \qquad C_u = \sum_{t \in \mathbb F_\ell^*}\left(\frac{1 - ut^{-1}}{\ell}\right).
    $$

    For $u = 0$, every term is $\left(\frac{1}{\ell}\right) = 1$, so $C_0 = \ell - 1$. For $u \neq 0$, as $t$ runs over $\mathbb F_\ell^*$ the element $s = 1 - ut^{-1}$ runs over $\mathbb F_\ell - \{1\}$, so

    $$
    C_u = \sum_{s \in \mathbb F_\ell - \{1\}}\left(\frac{s}{\ell}\right) = \sum_{s \in \mathbb F_\ell^*}\left(\frac{s}{\ell}\right) - \left(\frac{1}{\ell}\right) = 0 - 1 = -1,
    $$

    because $\mathbb F_\ell^*$ has as many squares as non-squares (Theorem 4). Therefore

    $$
    (-1)^{\varepsilon(\ell)}y^2 = (\ell - 1) - \sum_{u \in \mathbb F_\ell^*}w^u = \ell ,
    $$

    since $w$ is a primitive $\ell$th root of unity: $\sum_{u \in \mathbb F_\ell}w^u = \frac{w^\ell - 1}{w - 1} = 0$, so $\sum_{u \in \mathbb F_\ell^*}w^u = -1$. $\square$
