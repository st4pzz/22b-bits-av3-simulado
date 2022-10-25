#!/usr/bin/env python3

from myhdl import *


@block
def lfsr(bits, clk, rst):

    @always_comb
    def comb():
        pass

    return instances()


@block
def dff(q, d, clear, presset, clk, rst):
    @always_seq(clk.posedge, reset=rst)
    def logic():
        if clear:
            q.next = 0
        elif presset:
            q.next = 1
        else:
            q.next = d

    return instances()
