---
title: 미분기하학
---

<div class="lang-switch"><a href="../">English</a><a class="on">한국어</a></div>

<div class="running-head"><span>미분기하학</span><span>2026 가을</span></div>

# 미분기하학 강의 노트 { .book-title #lecture-notes-in-differential-geometry }

<p class="subject-line">곡선 · 곡면 · 곡률</p>

<p class="course-info">강의: <em>Differential Geometry</em> — Claudio Arezzo<br>주교재: M. P. do Carmo, <em>Differential Geometry of Curves and Surfaces</em></p>

<p class="pdf-links"><a href="../all-lectures-ko.pdf" download="미분기하학-노트.pdf">모든 장을 하나의 PDF로 보기</a></p>

## 이 과목에 대하여 { #the-subject }

미분기하학은 미적분을 써서 모양을 연구한다. 기본 방법은 국소적이다. 매끄러운 곡선이나 곡면을 각 점 근처에서 도함수로 근사하고, 대상을 어떻게 매개화했는지나 공간의 어디에 놓였는지에 따라 달라지지 않는 양에서 기하를 읽어 낸다. 이런 양을 이 분야의 불변량이라 한다.

$\mathbb{R}^3$의 곡선에서 불변량은 곡률과 열률(비틀림률)이다. 곡률은 곡선이 얼마나 빨리 휘는지, 열률은 평면에서 얼마나 빨리 비틀려 벗어나는지를 잰다. 이 둘이 합쳐지면 곡선을 강체 운동을 제외하고 결정한다. 곡면에서는 같은 정보를 접평면 위의 두 이차형식, 제1기본형식과 제2기본형식이 담고 있으며, 이들을 조합하면 가우스 곡률과 평균 곡률을 얻는다.

이론 전체를 두 질문이 관통한다. 첫째는 어떤 성질이 *내재적*인지, 즉 곡면 위에서 길이와 각도만 잴 수 있는 사람도 알아볼 수 있는지, 그리고 어떤 성질이 곡면이 공간에 놓인 방식에 의존하는지이다. 가우스의 *빼어난 정리(Theorema Egregium)*는 가우스 곡률이 매장을 통해 정의되었는데도 내재적이라고 말한다. 둘째는 국소적 정보가 전체 모양을 어떻게 제약하는지이며, 닫힌곡면의 전체 곡률을 위상과 연결하는 가우스–보네 정리가 그 예이다.

## 이 노트에 대하여 { #about-these-notes }

Claudio Arezzo의 강의 *Differential Geometry*를 들으며 쓴 필기를 조판한 것이다. 강의는 do Carmo의 *Differential Geometry of Curves and Surfaces*를 따르므로, 노트도 강의 순서가 아니라 do Carmo의 장과 절에 따라 배열했다. 장 하나가 한 페이지이고, 각 절에는 do Carmo의 번호와 제목을 붙였다. 각 절 아래의 작은 표시는 그 내용이 몇 번째 강의에서 나왔는지 알려 준다. 강의에서 건너뛴 절도 목차와 본문에 제목은 남겨 두고, 다루지 않았다는 메모를 달았다.

손필기 원본은 각 장 맨 위에 링크되어 있고, 그림은 모두 새로 그렸으며, 각 장은 그 장에서 쓰는 기호와 부호 규약으로 시작한다. 조판본은 강의보다 조금 더 말할 때가 있다. 건너뛴 단계, 생략된 증명의 한쪽 방향, 왜 그 단계가 성립하는지에 대한 설명 같은 것들이다. 모든 장은 PDF로 내려받을 수 있다.

## 노트의 구성 { #how-these-notes-are-organised }

번호는 do Carmo의 각 절 안에서 센다. 그래서 **정리 1.5.3**은 §1.5의 세 번째 번호 붙은 항목이다. 그림 번호는 장 전체에 걸쳐 이어진다.

본문은 다섯 종류의 상자로 구분된다.

!!! note "정의"
    새로운 용어. 용어 자체는 **굵게** 쓴다.

!!! abstract "정리"
    상자로 둘러싼 핵심 결과. 기억해 둘 만한 것, 즉 뒤의 장에서 다시 쓰이는 것들이다.

!!! example "예제"
    정의를 구체적인 곡선이나 곡면에 적용한 계산.

!!! info "참고"
    왜 그 단계를 밟는지, 또는 결과가 무엇을 뜻하는지 설명한다.

!!! warning "주의"
    왼쪽의 굵은 세로줄로 표시하며, 규약의 함정을 알려 준다. 다른 표준 교재가 반대 선택을 해서, 공식을 그대로 옮겨 오면 부호가 틀리게 되는 곳이다.

증명은 *증명.*으로 시작하고 $\square$로 끝난다.

## 목차 { .contents-heading #contents }

<div class="contents" markdown>

<p class="contents-part"><a href="../chapter1-ko/">1장 — 곡선</a></p>

- [<span>도입</span><span class="n">1.1</span>](chapter1-ko.md#11-introduction)
- [<span>매개곡선</span><span class="n">1.2</span>](chapter1-ko.md#12-parametrized-curves)
- [<span>정칙곡선; 호의 길이</span><span class="n">1.3</span>](chapter1-ko.md#13-regular-curves-arc-length)
- [<span>$\mathbb{R}^3$의 벡터곱 <em class="not-covered">(다루지 않음)</em></span><span class="n">1.4</span>](chapter1-ko.md#14-the-vector-product)
- [<span>호의 길이로 매개화된 곡선의 국소 이론</span><span class="n">1.5</span>](chapter1-ko.md#15-the-local-theory-of-curves-parametrized-by-arc-length)
- [<span>국소 표준형 <em class="not-covered">(다루지 않음)</em></span><span class="n">1.6</span>](chapter1-ko.md#16-the-local-canonical-form)
- [<span>평면곡선의 대역적 성질</span><span class="n">1.7</span>](chapter1-ko.md#17-global-properties-of-plane-curves)

</div>
