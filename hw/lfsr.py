#!/usr/bin/env python3

from myhdl import *


@block
def lfsr(bits, clk, rst):

    s1, s2, s3, s4, s5 = [Signal(bool(0)) for i in range(5)]
    sxor = Signal(bool(0))
    b1 = dff(s1, sxor, 0, 0, clk, rst)
    b2 = dff(s2, s1, 0, 0, clk, rst)
    b3 = dff(s3, s2, 0, 0, clk, rst)
    b4 = dff(s4, s3, 0, 0, clk, rst)
    b5 = dff(s5, s4, 0, 0, clk, rst)


    @always_comb
    def comb():
        sxor.next = not (s5 ^ s3)
        bits.next = ConcatSignal(s5, s4, s3, s2, s1)

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
