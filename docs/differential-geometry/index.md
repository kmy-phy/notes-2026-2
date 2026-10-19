---
title: Differential Geometry
---

<div class="running-head"><span>Differential Geometry</span><span>Fall 2026</span></div>

# Lecture Notes in Differential Geometry { .book-title }

<p class="subject-line">Arc length · Curvature and torsion · The Frenet frame</p>

## Conventions

!!! quote "Conventions used throughout these notes."
    - *Curves.* A curve is a smooth map $\alpha : I \to \mathbb{R}^3$ on an open interval $I$. A prime means a derivative with respect to the curve's parameter: $\alpha'(t) = d\alpha/dt$, or $d\alpha/ds$ once the curve is parametrized by arc length.
    - *Inner product, norm, cross product.* $\langle u, v\rangle$ is the Euclidean inner product, $|u| = \langle u, u\rangle^{1/2}$, and $u \wedge v$ is the cross product in $\mathbb{R}^3$.
    - *Vectors.* Fixed (constant) vectors are written in bold: $\mathbf{v}, \mathbf{v}_0, \mathbf{c}$.
    - *Arc length.* "p.a.l." means *parametrized by arc length*, i.e. $|\alpha'| \equiv 1$. The arc-length parameter is $s$.
    - *Frenet frame.* $T = \alpha'$, $\;N = T'/k$, $\;B = T \wedge N$, with curvature $k = |T'|$ and torsion $\tau$ defined by $B' = \tau N$. With these signs,

        $$
        T' = kN, \qquad N' = -kT - \tau B, \qquad B' = \tau N .
        $$

    Notation and sign conventions follow do Carmo, *Differential Geometry of Curves and Surfaces*.

## About these notes

These are typeset versions of my handwritten notes for the course, one page per lecture. They follow the order of the lectures, so each page can be read side by side with the original. The handwritten PDF is linked at the top of every lecture page, and every figure has been redrawn.

Wherever the typeset version says more than the handwriting, for example a step the lecture skipped, a direction of a proof that was left out, or a comment on why a step works, the remark is marked *(added)*. Everything not marked that way is what was written in class.

## How these notes are organised

Numbering restarts with each lecture and runs through definitions, theorems, examples and figures together within their kinds, so **Theorem 2.8** is the eighth numbered item of Lecture 2 and §2.5 is its fifth section.

Five kinds of set-off text carry the weight.

!!! note "Definition"
    A new term, with the term itself in **bold**.

!!! abstract "Theorem"
    A boxed key result, worth remembering — the ones that get used again in later lectures.

!!! example "Example"
    A worked computation that applies the definitions to a concrete curve.

!!! info "Remark"
    Explains why a step is taken, or what a result means. Remarks marked *(added)* are not in the handwritten notes.

!!! warning "Caution"
    Marked by a heavy rule down the left margin, it flags a convention trap: a place where another standard book makes the opposite choice, so a formula copied across would come out with the wrong sign.

A proof begins with *Proof.* and ends with $\square$.

## Contents { .contents-heading }

<div class="contents" markdown>

<p class="contents-part"><a href="lec02/">Lecture 2 — Arc Length and the Frenet Frame</a></p>

- [<span>The arc-length function</span><span class="n">2.1</span>](lec02.md#21-the-arc-length-function)
- [<span>Examples of arc length</span><span class="n">2.2</span>](lec02.md#22-examples-of-arc-length)
- [<span>Curvature and the Frenet trihedron</span><span class="n">2.3</span>](lec02.md#23-curvature-and-the-frenet-trihedron)
- [<span>Torsion</span><span class="n">2.4</span>](lec02.md#24-torsion)
- [<span>The Frenet formulas</span><span class="n">2.5</span>](lec02.md#25-the-frenet-formulas)
- [<span>Examples of the Frenet frame</span><span class="n">2.6</span>](lec02.md#26-examples-of-the-frenet-frame)
- [<span>Lines and plane curves</span><span class="n">2.7</span>](lec02.md#27-lines-and-plane-curves)

</div>
