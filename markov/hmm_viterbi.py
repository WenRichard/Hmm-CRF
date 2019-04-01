# -*- coding: utf-8 -*-
# @Time    : 2019/3/31 11:26
# @Author  : Alan
# @Email   : xiezhengwen2013@163.com
# @File    : hmm_viterbi.py
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


def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}
    for y in states:    #建立t_0时刻各状态概率
        V[0][y] = start_p[y] * emit_p[y][obs[0]]
        path[y] = [y]
    print(path)
    for t in range(1, len(obs)):    #沿着时间（1，...t）进行计算
        V.append({})
        newpath = {}

        # 根据t-1时刻状态概率、观测概率矩阵和状态转移概率
        # 计算t时刻最大概率的状态，记录路径
        for y in states:
            (prob, state) = max([(V[t-1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0) for y0 in states])
            V[t][y] = prob
            newpath[y] = path[state] + [y]
        path = newpath
    (prob, state) = max([(V[len(obs) - 1][y], y) for y in states])
    return (prob, path[state])


print(viterbi(observations, states, start_probability, transition_probability, emission_probability))