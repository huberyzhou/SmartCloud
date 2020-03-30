# -*- coding: utf-8 -*-
# @Time    : 2020-02-10 14:38
# @Author  : Dingzh.tobest
# 文件描述  ：用于计算相关指数相关指标

# 计算指数市盈率(PE)
# df中包含所有股票的pe_ttm信息
# 计算方法：对所有个股的pe_ttm数据取倒数，剔除掉小于0的数据，通过总和除以所有的股票数，再取倒数，形成指数pe_ttm
# 通过取倒数的形式，大大减小了超高PE的股票对指数PE的影响
def calc_index_pe_ttm(df):
    df['r_pe_ttm'] = 1 / df['pe_ratio']
    df2 = df[df['r_pe_ttm'] > 0]
    r_index_pe = df2['r_pe_ttm'].sum() / len(df)
    index_pe = 1 / r_index_pe
    return index_pe

# 计算指数市净率(PB)
# df中包含所有股票的pb_ttm信息
# 计算方法：对所有个股的pb_ttm数据取倒数，剔除掉小于0的数据，通过总和除以所有的股票数，再取倒数，形成指数pb_ttm
# 通过取倒数的形式，大大减小了超高PB的股票对指数PB的影响
def calc_index_pb_ttm(df):
    df['r_pb_ttm'] = 1 / df['pb_ratio']
    df2 = df[df['r_pb_ttm'] > 0]
    r_index_pb = df2['r_pb_ttm'].sum() / len(df)
    index_pb = 1 / r_index_pb
    return index_pb

# 计算指数市净率(PB)
# df中包含所有股票的pb_ttm信息
# 计算方法：对所有个股的pb_ttm数据取倒数，剔除掉小于0的数据，通过总和除以所有的股票数，再取倒数，形成指数pb_ttm
# 通过取倒数的形式，大大减小了超高PB的股票对指数PB的影响
def calc_index_ps_ttm(df):
    df['r_ps_ttm'] = 1 / df['ps_ratio']
    df2 = df[df['r_ps_ttm'] > 0]
    r_index_ps = df2['r_ps_ttm'].sum() / len(df)
    index_ps = 1 / r_index_ps
    return index_ps