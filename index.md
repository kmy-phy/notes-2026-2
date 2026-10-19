# Differential Geometry

<small>2026 Fall · Lecture notes</small>

**Curves and surfaces in $\mathbb{R}^3$** — arc length · curvature and torsion · the Frenet frame · …

---

## Conventions

!!! abstract "Conventions used throughout these notes"
    - **Curves.** A curve is a smooth map $\alpha : I \to \mathbb{R}^3$ on an open interval $I$. A prime means a derivative with respect to the curve's parameter: $\alpha'(t) = \frac{d\alpha}{dt}$, or $\frac{d\alpha}{ds}$ once the curve is parametrized by arc length.
    - **Inner product, norm, cross product.** $\langle u, v\rangle$ is the Euclidean inner product, $|u| = \langle u, u\rangle^{1/2}$, and $u \wedge v$ is the cross product in $\mathbb{R}^3$.
    - **Vectors.** Fixed (constant) vectors are written in bold: $\mathbf{v}, \mathbf{v}_0, \mathbf{c}$.
    - **Arc length.** "p.a.l." means *parametrized by arc length*, i.e. $|\alpha'| \equiv 1$. The arc-length parameter is $s$.
    - **Frenet frame.** $T = \alpha'$, $\;N = T'/k$, $\;B = T \wedge N$, with curvature $k = |T'|$ and torsion $\tau$ defined by $B' = \tau N$. With these signs,

        $$
        T' = kN, \qquad N' = -kT - \tau B, \qquad B' = \tau N .
        $$

    Notation and sign conventions follow do Carmo, *Differential Geometry of Curves and Surfaces*.

## About these notes

These are typeset versions of my handwritten notes for the course, one page per lecture. They follow the order of the lectures, so each page can be read side by side with the original. The handwritten PDF is linked at the top of every lecture page.

Wherever the typeset version says more than the handwriting, for example a step the lecture skipped, a direction of a proof that was left out, or a comment on why a step works, the box is marked **(added)**. Everything not marked that way is what was written in class.

## How these notes are organised

Numbering restarts with each lecture and runs through definitions, theorems and examples together, so **Theorem 2.8** is the eighth numbered item of Lecture 2. Section numbers follow the same pattern: §2.5 is the fifth section of Lecture 2.

Five kinds of boxes carry the weight:

!!! note "Definition"
    A new term, with the term itself in **bold**.

!!! abstract "Theorem"
    A result worth remembering — the ones that get used again in later lectures.

!!! example "Example"
    A worked computation that applies the definitions to a concrete curve.

!!! info "Remark"
    Explains why a step is taken, or what a result means. Remarks marked *(added)* are not in the handwritten notes.

!!! warning "Caution"
    A convention trap: a place where another standard book makes the opposite choice, so a formula copied across would come out with the wrong sign.

Proofs sit in green boxes under their theorem and can be folded away by clicking their title.

## Contents

### [Lecture 2 — Arc Length and the Frenet Frame](lec02.md)

- [2.1 The arc-length function](lec02.md#21-the-arc-length-function)
- [2.2 Examples of arc length](lec02.md#22-examples-of-arc-length)
- [2.3 Curvature and the Frenet trihedron](lec02.md#23-curvature-and-the-frenet-trihedron)
- [2.4 Torsion](lec02.md#24-torsion)
- [2.5 The Frenet formulas](lec02.md#25-the-frenet-formulas)
- [2.6 Examples of the Frenet frame](lec02.md#26-examples-of-the-frenet-frame)
- [2.7 Lines and plane curves](lec02.md#27-lines-and-plane-curves)
