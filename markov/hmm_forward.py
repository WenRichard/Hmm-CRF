# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 17:26
# @Author  : Alan
# @Email   : xiezhengwen2013@163.com
# @File    : hmm_forward.py
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


def forward(obs):
    fwd = [{}]
    # 初始化 （t = 0）
    for y in states:
        fwd[0][y] = start_probability[y] * emission_probability[y][obs[0]]
    # 前向算法（t>0）
    for t in range(1, len(obs)):
        fwd.append({})
        for y in states:
            fwd[t][y] = sum((fwd[t-1][y0] * transition_probability[y0][y] *
                             emission_probability[y][obs[t]]) for y0 in states)
    prob = sum((fwd[len(obs) - 1][s]) for s in states)
    return prob


def observation_prob_foward(obs_seq):
    return forward(obs_seq)


print(observation_prob_foward(observations))