#!/usr/bin/env python3

from myhdl import *
from lfsr import lfsr

tst = [1, 3, 7, 14, 28, 25, 18, 4, 8, 17, 2, 5, 10, 21, 11, 23, 15, 30, 29, 27, 22, 13, 26, 20, 9 , 19, 6, 12, 24, 16, 0]

def test_lfsr():

    @always(delay(5))
    def clkgen():
        clk.next = not clk

    @instance
    def stimulus():
        yield delay(2)

        for d in tst:
            assert bits == d
            yield clk.negedge


    bits = Signal(modbv(0)[5:])
    clk = Signal(bool(0))
    rst = ResetSignal(0, active=1, isasync=True)
    dut = lfsr(bits, clk, rst)
    sim = Simulation(dut, [stimulus, clkgen])
    sim.run(200)
