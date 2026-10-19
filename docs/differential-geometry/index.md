---
title: Differential Geometry
---

<div class="running-head"><span>Differential Geometry</span><span>Fall 2026</span></div>

# Lecture Notes in Differential Geometry { .book-title }

<p class="subject-line">Curves · Surfaces · Curvature</p>

<p class="pdf-links"><a href="all-lectures.pdf" download="Differential-Geometry-Notes.pdf">Download all lectures as one PDF</a></p>

## The subject

Differential geometry uses calculus to study shape. Its basic move is local: near each point a smooth curve or surface is approximated by its derivatives, and the geometry is read off from quantities that do not depend on how the object is parametrized or on where it sits in space. Such quantities are the invariants of the subject.

For a curve in $\mathbb{R}^3$ the invariants are the curvature and the torsion, which measure how fast the curve bends and how fast it twists out of a plane. Together they determine the curve up to a rigid motion. For a surface the analogous information is carried by two quadratic forms on its tangent planes, the first and second fundamental forms, and their combinations give the Gaussian and mean curvatures.

Two questions run through the theory. The first is which properties are *intrinsic*, visible to someone who can only measure lengths and angles on the surface itself, and which depend on how the surface is placed in space. Gauss's *Theorema Egregium* says that Gaussian curvature, although defined through the embedding, is intrinsic. The second is how local information constrains global shape, as in the Gauss–Bonnet theorem, which ties the total curvature of a closed surface to its topology.

## About these notes

These are typeset versions of my handwritten notes for the course, one page per lecture. They follow the order of the lectures, so each page can be read side by side with the original. The handwritten PDF is linked at the top of every lecture page, every figure has been redrawn, and each lecture opens with the notation and sign conventions it uses. Every lecture can also be downloaded as a PDF.

Wherever the typeset version says more than the handwriting, for example a step the lecture skipped, a direction of a proof that was left out, or a comment on why a step works, the remark is marked *(added)*. Everything not marked that way is what was written in class.

## How these notes are organised

Numbering restarts with each lecture and runs through definitions, theorems, examples and figures together within their kinds, so **Theorem 2.8** is the eighth numbered item of Lecture 2 and §2.5 is its fifth section.

Five kinds of set-off text carry the weight.

!!! note "Definition"
    A new term, with the term itself in **bold**.

!!! abstract "Theorem"
    A boxed key result, worth remembering — the ones that get used again in later lectures.

!!! example "Example"
    A worked computation that applies the definitions to a concrete curve or surface.

!!! info "Remark"
    Explains why a step is taken, or what a result means. Remarks marked *(added)* are not in the handwritten notes.

!!! warning "Caution"
    Marked by a heavy rule down the left margin, it flags a convention trap: a place where another standard book makes the opposite choice, so a formula copied across would come out with the wrong sign.

A proof begins with *Proof.* and ends with $\square$.

## Contents { .contents-heading }

<div class="contents" markdown>

<p class="contents-part"><a href="lec01/">Lecture 1 — Curves and Their Length</a></p>

- [<span>Parametrized curves</span><span class="n">1.1</span>](lec01.md#11-parametrized-curves)
- [<span>What a smooth curve can look like</span><span class="n">1.2</span>](lec01.md#12-what-a-smooth-curve-can-look-like)
- [<span>Examples</span><span class="n">1.3</span>](lec01.md#13-examples)
- [<span>Length</span><span class="n">1.4</span>](lec01.md#14-length)
- [<span>Invariance under isometries</span><span class="n">1.5</span>](lec01.md#15-invariance-under-isometries)
- [<span>Lines as minima</span><span class="n">1.6</span>](lec01.md#16-lines-as-minima)
- [<span>Reparametrization</span><span class="n">1.7</span>](lec01.md#17-reparametrization)

<p class="contents-part"><a href="lec02/">Lecture 2 — Arc Length and the Frenet Frame</a></p>

- [<span>The arc-length function</span><span class="n">2.1</span>](lec02.md#21-the-arc-length-function)
- [<span>Examples of arc length</span><span class="n">2.2</span>](lec02.md#22-examples-of-arc-length)
- [<span>Curvature and the Frenet trihedron</span><span class="n">2.3</span>](lec02.md#23-curvature-and-the-frenet-trihedron)
- [<span>Torsion</span><span class="n">2.4</span>](lec02.md#24-torsion)
- [<span>The Frenet formulas</span><span class="n">2.5</span>](lec02.md#25-the-frenet-formulas)
- [<span>Examples of the Frenet frame</span><span class="n">2.6</span>](lec02.md#26-examples-of-the-frenet-frame)
- [<span>Lines and plane curves</span><span class="n">2.7</span>](lec02.md#27-lines-and-plane-curves)

</div>
