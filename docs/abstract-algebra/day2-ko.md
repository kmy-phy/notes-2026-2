---
title: "2일차 — 이차 상호 법칙 (11월 26일)"
---

<div class="lang-switch"><a href="../day2/">English</a><a class="on">한국어</a></div>

<div class="running-head"><span>현대대수 특강</span><span>2일차 · 이차 상호 법칙</span></div>

# 2일차 — 이차 상호 법칙 { .part-title #day-2-quadratic-reciprocity }

<p class="source-note">특강, 2026년 11월 26일 · Serre 1장 · <a class="pdf-link" href="notes.pdf" download="현대대수-특강-2일차.pdf">이 날을 PDF로 보기</a></p>

**이 날에는.** 가우스 합에 관한 두 번째 보조정리와 이차 상호 법칙의 증명, 이 법칙으로 르장드르 기호를 계산하는 방법, 그리고 부록으로 가우스 보조정리와 $\sin mx$의 곱 공식을 이용한 아이젠슈타인의 증명을 다룬다. 이 날 함께 다룬 정리 5 iii)의 증명은 1일차 §3.2에 있다. 이 날의 두 번째 강의인 피타고라스 세 쌍은 다음 부분에 있다.

!!! quote "이 날에 쓰는 규약."
    - $\ell$과 $p$는 $2$가 아닌 서로 다른 두 소수이다.
    - $\Omega$는 $\mathbb F_p$의 대수적 폐포이고, $w \in \Omega$는 1의 원시 $\ell$제곱근이다.
    - $y = \sum_{x \in \mathbb F_\ell}\left(\frac{x}{\ell}\right)w^x \in \Omega$는 가우스 합이다.
    - 홀수 $n$에 대해 1일차처럼 $\varepsilon(n) \equiv \frac{n-1}{2} \pmod 2$이다.

---

## 3 이차 상호 법칙 (계속) { #3-quadratic-reciprocity-law-continued }

### 3.3 이차 상호 법칙 (계속) { #33-quadratic-reciprocity-law-continued }

상호 법칙에 대한 가우스의 증명을 이어 간다.

!!! abstract "정리 6 (가우스, 이차 상호 법칙)"
    $\ell$과 $p$가 $2$가 아닌 서로 다른 두 소수이면

    $$
    \left(\frac{\ell}{p}\right) = \left(\frac{p}{\ell}\right)(-1)^{\varepsilon(\ell)\varepsilon(p)}
    $$

    이다.

1일차는 가우스 합에 관한 첫 번째 보조정리 $y^2 = (-1)^{\varepsilon(\ell)}\ell$(보조정리 1)에서 끝났다. 두 번째 보조정리는 다음과 같다.

!!! abstract "보조정리 2"
    $y^{p-1} = \left(\dfrac{p}{\ell}\right)$이다.

!!! success "증명"
    먼저 임의의 $a \in \mathbb F_\ell^*$에 대해

    $$
    1 = \left(\frac{1}{\ell}\right) = \left(\frac{a\,a^{-1}}{\ell}\right) = \left(\frac{a}{\ell}\right)\left(\frac{a^{-1}}{\ell}\right)
    $$

    이므로 $\left(\frac{a}{\ell}\right)$과 $\left(\frac{a^{-1}}{\ell}\right)$은 같은 값을 가진다. 둘 다 $1$이거나 둘 다 $-1$이다.

    $\Omega$의 표수가 $p$이므로 프로베니우스 사상 $x \mapsto x^p$는 덧셈을 보존한다. 계수 $\left(\frac{x}{\ell}\right) \in \{0, \pm 1\}$은 $p$가 홀수이므로 $\left(\frac{x}{\ell}\right)^p = \left(\frac{x}{\ell}\right)$를 만족한다. 따라서 $z = xp$로 놓으면($p$는 법 $\ell$로 가역이므로 $x$가 $\mathbb F_\ell$ 전체를 지날 때 $z$도 그렇다)

    $$
    y^p = \sum_{x \in \mathbb F_\ell}\left(\frac{x}{\ell}\right)w^{xp}
    = \sum_{z \in \mathbb F_\ell}\left(\frac{zp^{-1}}{\ell}\right)w^{z}
    = \left(\frac{p^{-1}}{\ell}\right)\sum_{z \in \mathbb F_\ell}\left(\frac{z}{\ell}\right)w^{z}
    = \left(\frac{p}{\ell}\right)y
    $$

    이다. 보조정리 1에 의해 $\ell \neq p$이므로 $\mathbb F_p$에서 $y^2 = \pm\ell \neq 0$이다. 따라서 $y \neq 0$이고, $y$로 나누면 $y^{p-1} = \left(\frac{p}{\ell}\right)$이다. $\square$

!!! success "정리 6의 증명"
    보조정리 1, $y^2 = (-1)^{\varepsilon(\ell)}\ell$과 보조정리 2, $y^{p-1} = \left(\frac{p}{\ell}\right)$을 떠올리자. $\mathbb F_p$에서 법 $p$에 대한 르장드르 기호의 정의와 정리 5 ii)를 쓰면

    $$
    \left(\frac{p}{\ell}\right) = y^{p-1} = (y^2)^{\frac{p-1}{2}} = \big((-1)^{\varepsilon(\ell)}\ell\big)^{\frac{p-1}{2}}
    = \left(\frac{(-1)^{\varepsilon(\ell)}\ell}{p}\right)
    = \left(\frac{-1}{p}\right)^{\varepsilon(\ell)}\left(\frac{\ell}{p}\right)
    = (-1)^{\varepsilon(\ell)\varepsilon(p)}\left(\frac{\ell}{p}\right)
    $$

    이다. 양변은 $\pm 1$이고 $p \neq 2$이므로 $\mathbb F_p$에서 $1 \neq -1$이다. 따라서 이 등식은 정수로서도 성립한다. 양변에 $(-1)^{\varepsilon(\ell)\varepsilon(p)}$를 곱하면 정리 6을 얻는다. $\square$

이차 상호 법칙을 말로 옮기면 다음과 같다.

!!! info "비고"
    $\ell$이 법 $p$로 제곱수이면(**이차 잉여**) $\ell\,R\,p$, 아니면 $\ell\,N\,p$로 쓰자. 정리 6은 다음을 뜻한다.

    - $p$나 $\ell$이 법 $4$로 $1$과 합동이면, $\ell\,R\,p$일 필요충분조건은 $p\,R\,\ell$이다.
    - $p$와 $\ell$이 모두 법 $4$로 $-1$과 합동이면, $\ell\,R\,p$일 필요충분조건은 $p\,N\,\ell$이다.

    같은 말로

    $$
    \left(\frac{\ell}{p}\right)\left(\frac{p}{\ell}\right) = (-1)^{(p-1)(\ell-1)/4}
    $$

    이다.

정리 6을 쓰면 르장드르 기호를 차례로 줄여 가며 계산할 수 있다.

!!! example "예제 (차례로 줄이기)"
    $$
    \left(\frac{29}{43}\right) = \left(\frac{43}{29}\right) = \left(\frac{14}{29}\right) = \left(\frac{2}{29}\right)\left(\frac{7}{29}\right) = -\left(\frac{7}{29}\right) = -\left(\frac{29}{7}\right) = -\left(\frac{1}{7}\right) = -1 .
    $$

    첫째와 다섯째 단계는 $29 \equiv 1 \pmod 4$이므로 정리 6을 쓴 것이다. 둘째와 여섯째 단계는 위의 수를 줄인 것이다($43 \equiv 14 \pmod{29}$, $29 \equiv 1 \pmod 7$). 넷째 단계는 $29 \equiv 5 \pmod 8$이므로 정리 5 iii)을 쓴 것이다.

---

## 부록 — 이차 상호 법칙에 대한 아이젠슈타인의 증명 { #appendix-eisensteins-proof }

$p \neq 2$를 소수라 하고, $S$를 $\mathbb F_p^* = S \sqcup -S$인 $\mathbb F_p^*$의 부분집합이라 하자(예를 들어 $S = \{1, 2, \dots, \frac{p-1}{2}\}$). $s \in S$, $a \in \mathbb F_p^*$이면 $as$와 $-as$ 중 정확히 하나가 $S$에 들어 있으므로

$$
as = e_s(a)\,s_a, \qquad e_s(a) = \pm 1,\quad s_a \in S
$$

로 쓸 수 있다.

!!! abstract "보조정리 (가우스)"
    $\left(\dfrac{a}{p}\right) = \displaystyle\prod_{s \in S}e_s(a)$이다.

!!! success "증명"
    먼저 $a$를 고정하면 $s \mapsto s_a$는 $S$의 전단사 사상이다. $s, s'$이 $S$의 두 원소이고 $s_a = s'_a$이면 $as = \pm as'$이므로 $s = \pm s'$이고, $S \cap -S = \varnothing$이므로 $s = s'$이다. 유한집합에서 자기 자신으로 가는 단사 사상은 전단사이다.

    $S$의 원소는 $\frac{p-1}{2}$개이므로

    $$
    \left(\frac{a}{p}\right)\prod_{s \in S}s = a^{\frac{p-1}{2}}\prod_{s \in S}s = \prod_{s \in S}(as) = \prod_{s \in S}e_s(a)\,s_a = \prod_{s \in S}e_s(a)\prod_{s \in S}s_a = \prod_{s \in S}e_s(a)\prod_{s \in S}s
    $$

    이다. 곱 $\prod_{s \in S}s$는 0이 아니므로 $\left(\frac{a}{p}\right) = \prod_{s \in S}e_s(a)$이다. $\square$

!!! example "예제"
    홀수 소수 $p$에 대해 $a = 2$, $S = \{1, \dots, \frac{p-1}{2}\}$로 두면

    $$
    e_s(2) = \begin{cases} 1 & 2s \le \frac{p-1}{2}\text{이면},\\ -1 & \text{그 밖의 경우}\end{cases}
    $$

    이다. 여기서 $\left(\frac{2}{p}\right) = (-1)^{n(p)}$를 얻는다. 단 $n(p) = \big|\{x \in \mathbb Z \mid \frac{p-1}{4} < x \le \frac{p-1}{2}\}\big|$이다. $p = 4k + 1$이거나 $p = 4k - 1$이면 $n(p) = k$이다. 따라서

    $$
    \left(\frac{2}{p}\right) = \begin{cases} 1 & p \equiv \pm 1 \pmod 8\text{이면},\\ -1 & p \equiv \pm 5 \pmod 8\text{이면}\end{cases}
    $$

    이다. 정리 5 iii)과 비교하라.

!!! abstract "보조정리"
    양의 홀수 $m$에 대해

    $$
    \sin mx = (-4)^{(m-1)/2}\sin x\prod_{j=1}^{(m-1)/2}\left(\sin^2 x - \sin^2\frac{2\pi j}{m}\right)
    $$

    이다.

!!! success "증명"
    $z = e^{ix}$로 놓으면 $m$이 홀수이므로

    $$
    \frac{\sin mx}{\sin x} = \frac{z^m - z^{-m}}{z - z^{-1}} = z^{m-1} + z^{m-3} + \dots + z^{-(m-1)} = 1 + 2\sum_{k=1}^{(m-1)/2}\cos 2kx
    $$

    이다. 각 $\cos 2kx$는 $\cos 2x = 1 - 2\sin^2 x$의 $k$차 다항식이므로, $\frac{\sin mx}{\sin x}$는 $\sin^2 x$의 $\frac{m-1}{2}$차 다항식 $f$이다.

    최고차 계수: $\sin^2 x = -\frac14 z^2 + \frac12 - \frac14 z^{-2}$이므로 $z^{m-1}$은 $f$의 최고차항 $c\,(\sin^2 x)^{(m-1)/2}$에서만 나오고 그 계수는 $c\left(-\frac14\right)^{(m-1)/2}$이다. 이것이 $1$이어야 하므로 $c = (-4)^{(m-1)/2}$이다.

    근: $j = 1, \dots, \frac{m-1}{2}$에 대해 $x = \frac{2\pi j}{m}$이면 $\sin mx = 0$, $\sin x \neq 0$이므로 $\xi_j = \sin^2\frac{2\pi j}{m}$은 $f$의 근이다. 이 수들은 서로 다르다. 각 $\frac{2\pi j}{m}$은 $(0, \pi)$에 있고, 거기서 $\sin^2\theta = \sin^2\theta'$이면 $\theta' = \theta$이거나 $\theta' = \pi - \theta$이다. 뒤의 경우는 $2(j + j') = m$을 뜻하므로 $m$이 홀수라서 불가능하다. 최고차 계수가 $c$이고 서로 다른 근 $\frac{m-1}{2}$개를 갖는 $\frac{m-1}{2}$차 다항식은 $c\prod_j(X - \xi_j)$이다. 양변에 $\sin x$를 곱하면 보조정리를 얻는다. $\square$

!!! info "비고"
    $\dfrac{\sin(2n+1)x}{\sin x} = W_n(\cos 2x) = W_n(1 - 2\sin^2 x)$이다. 여기서 $W_n$은 **제4종 체비쇼프 다항식**으로, $W_0(z) = 1$, $W_1(z) = 2z + 1$이고 $n \ge 1$에 대해 $W_{n+1}(z) = 2zW_n(z) - W_{n-1}(z)$이다.

!!! success "정리 6의 증명 (아이젠슈타인)"
    $\ell$과 $p$를 서로 다른 두 홀수 소수, $S = \{1, 2, \dots, \frac{p-1}{2}\}$라 하자. $s \in S$에 대해 $\ell s \equiv e_s(\ell)\,s_\ell \pmod p$이다. $\sin$은 주기가 $2\pi$인 홀함수이므로

    $$
    \sin\frac{2\pi\ell s}{p} = e_s(\ell)\,\sin\frac{2\pi s_\ell}{p}
    $$

    이다. 가우스 보조정리와, $s \mapsto s_\ell$이 $S$의 전단사 사상이라는 사실에 의해($s \in S$에 대해 $\sin\frac{2\pi s}{p} \neq 0$이다)

    $$
    \left(\frac{\ell}{p}\right) = \prod_{s=1}^{(p-1)/2}e_s(\ell) = \prod_{s=1}^{(p-1)/2}\frac{\sin(2\pi\ell s/p)}{\sin(2\pi s/p)}
    $$

    이다. 위 보조정리에 $m = \ell$, $x = \frac{2\pi s}{p}$를 넣으면

    $$
    \left(\frac{\ell}{p}\right) = (-4)^{(\ell-1)(p-1)/4}\prod_{s=1}^{(p-1)/2}\prod_{t=1}^{(\ell-1)/2}\left(\sin^2\frac{2\pi s}{p} - \sin^2\frac{2\pi t}{\ell}\right)
    $$

    이다. $\ell$과 $p$의 역할을 바꾸면

    $$
    \left(\frac{p}{\ell}\right) = (-4)^{(\ell-1)(p-1)/4}\prod_{t=1}^{(\ell-1)/2}\prod_{s=1}^{(p-1)/2}\left(\sin^2\frac{2\pi t}{\ell} - \sin^2\frac{2\pi s}{p}\right)
    $$

    이다. 두 이중곱은 같은 $\frac{(p-1)(\ell-1)}{4}$개의 인수를 부호만 반대로 가진다. 따라서

    $$
    \left(\frac{\ell}{p}\right) = (-1)^{\frac{p-1}{2}\cdot\frac{\ell-1}{2}}\left(\frac{p}{\ell}\right) = (-1)^{\varepsilon(\ell)\varepsilon(p)}\left(\frac{p}{\ell}\right). \qquad \square
    $$
