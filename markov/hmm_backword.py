# -*- coding: utf-8 -*-
# @Time    : 2019/3/31 10:50
# @Author  : Alan
# @Email   : xiezhengwen2013@163.com
# @File    : hmm_backword.py
# @Software: PyCharm


states = ('健康', '感冒')
observations = ('正常', '发冷', '发烧')
start_probability = {'健康':0.6, '感冒':0.4}

transition_probability = {
    '健康': {'健康': 0.7, '感冒': 0.3},
    '感冒': {'健康': 0.4, '感冒': 0.6},
}

emission_probability = {
    '健康':{'正常':0.5, '发冷': 0.4, '发烧':0.1},
    '感冒':{'正常':0.1, '发冷': 0.3, '发烧':0.6},
}


def backward(obs):
    bwk = [{} for t in range(len(obs))]
    T = len(obs)
    # 初始化 （t = T）
    for y in states:
        bwk[T-1][y] = 1
    print(bwk)
    for t in reversed(range(T-1)):
        for y in states:
            print(y)
            # 核心部分：sum（后向概率*状态转移矩阵*观测概率）
            bwk[t][y] = sum((bwk[t+1][y1] * transition_probability[y][y1] *
                             emission_probability[y1][obs[t+1]]) for y1 in states)
    prob = sum((start_probability[y] * emission_probability[y][obs[0]] * bwk[0][y]) for y in states)
    return prob


def observation_prob_backword(obs_seq):
    return backward(obs_seq)


print(observation_prob_backword(observations))