# 라그랑주 역학

## 라그랑지안

계의 운동에너지를 $T$, 퍼텐셜 에너지를 $V$라 하면 라그랑지안은

$$
L(q, \dot q, t) = T - V
$$

## 오일러–라그랑주 방정식

작용 $S = \int_{t_1}^{t_2} L \, dt$ 가 극값을 갖는 경로는 다음을 만족한다.

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot q_i}\right) - \frac{\partial L}{\partial q_i} = 0
\label{eq:el}
$$

## 예시: 단진자

길이 $\ell$, 질량 $m$인 단진자에서 일반화 좌표를 $\theta$로 잡으면

$$
T = \frac{1}{2} m \ell^2 \dot\theta^2, \qquad V = -m g \ell \cos\theta
$$

식 $\eqref{eq:el}$에 대입하면

$$
\ddot\theta + \frac{g}{\ell}\sin\theta = 0
$$

!!! note "작은 각 근사"
    $\theta \ll 1$ 이면 $\sin\theta \approx \theta$ 이므로 각진동수 $\omega = \sqrt{g/\ell}$ 인 단조화 운동이 된다.
