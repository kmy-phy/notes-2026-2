---
title: Differential Geometry
---

<div class="running-head"><span>Differential Geometry</span><span>Fall 2026</span></div>

# Lecture Notes in Differential Geometry { .book-title }

<p class="subject-line">Curves · Surfaces · Curvature</p>

<p class="course-info">Lectures: <em>Differential Geometry</em> — Claudio Arezzo<br>Main text: M. P. do Carmo, <em>Differential Geometry of Curves and Surfaces</em></p>

<p class="pdf-links"><a href="all-lectures.pdf" download="Differential-Geometry-Notes.pdf">Download all chapters as one PDF</a></p>

## The subject

Differential geometry uses calculus to study shape. Its basic move is local: near each point a smooth curve or surface is approximated by its derivatives, and the geometry is read off from quantities that do not depend on how the object is parametrized or on where it sits in space. Such quantities are the invariants of the subject.

For a curve in $\mathbb{R}^3$ the invariants are the curvature and the torsion, which measure how fast the curve bends and how fast it twists out of a plane. Together they determine the curve up to a rigid motion. For a surface the analogous information is carried by two quadratic forms on its tangent planes, the first and second fundamental forms, and their combinations give the Gaussian and mean curvatures.

Two questions run through the theory. The first is which properties are *intrinsic*, visible to someone who can only measure lengths and angles on the surface itself, and which depend on how the surface is placed in space. Gauss's *Theorema Egregium* says that Gaussian curvature, although defined through the embedding, is intrinsic. The second is how local information constrains global shape, as in the Gauss–Bonnet theorem, which ties the total curvature of a closed surface to its topology.

## About these notes

These are typeset versions of my notes for the lecture course *Differential Geometry* by Claudio Arezzo. The course follows do Carmo's *Differential Geometry of Curves and Surfaces*, so the notes are arranged by do Carmo's chapters and sections rather than by lecture: each chapter is one page, and its sections carry do Carmo's numbers and titles. A small tag under each section says which lecture it comes from. A section that the lectures skipped keeps its heading, with a note that it was not covered.

The handwritten notes are linked at the top of each chapter, every figure has been redrawn, and each chapter opens with the notation and sign conventions it uses. The typeset version sometimes says more than the lecture: a step that was skipped, a direction of a proof that was left out, or a comment on why a step works. Every chapter can be downloaded as a PDF.

## How these notes are organised

Numbered items are counted within each section of do Carmo, so **Theorem 1.5.3** is the third numbered item of §1.5. Figures are numbered through each chapter.

Five kinds of set-off text carry the weight.

!!! note "Definition"
    A new term, with the term itself in **bold**.

!!! abstract "Theorem"
    A boxed key result, worth remembering — the ones that get used again in later chapters.

!!! example "Example"
    A worked computation that applies the definitions to a concrete curve or surface.

!!! info "Remark"
    Explains why a step is taken, or what a result means.

!!! warning "Caution"
    Marked by a heavy rule down the left margin, it flags a convention trap: a place where another standard book makes the opposite choice, so a formula copied across would come out with the wrong sign.

A proof begins with *Proof.* and ends with $\square$.

## Contents { .contents-heading }

<div class="contents" markdown>

<p class="contents-part"><a href="chapter1/">Chapter 1 — Curves</a></p>

- [<span>Introduction</span><span class="n">1.1</span>](chapter1.md#11-introduction)
- [<span>Parametrized Curves</span><span class="n">1.2</span>](chapter1.md#12-parametrized-curves)
- [<span>Regular Curves; Arc Length</span><span class="n">1.3</span>](chapter1.md#13-regular-curves-arc-length)
- [<span>The Vector Product in $\mathbb{R}^3$</span><span class="n">1.4</span>](chapter1.md#14-the-vector-product)
- [<span>The Local Theory of Curves Parametrized by Arc Length</span><span class="n">1.5</span>](chapter1.md#15-the-local-theory-of-curves-parametrized-by-arc-length)
- [<span>The Local Canonical Form <em class="not-covered">(not covered)</em></span><span class="n">1.6</span>](chapter1.md#16-the-local-canonical-form)
- [<span>Global Properties of Plane Curves</span><span class="n">1.7</span>](chapter1.md#17-global-properties-of-plane-curves)

</div>
