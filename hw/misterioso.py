#!/usr/bin/env python3
from myhdl import *

@block
def misterioso(q0, q1, clk, rst):

    q0s = Signal(bool(0))
    q1s = Signal(bool(0))

    @always_seq(clk.posedge, reset=rst)
    def seq():
        q0s.next = not q1s
        q1s.next = q0s

    @always_comb
    def comb():
        q0.next = q0s
        q1.next = q1s

    return instances()


def test_misterioso():
    q0, q1, clk = [Signal(bool(0)) for i in range(3)]
    rst = ResetSignal(0, active=1, isasync=True)
    dut = misterioso(q0, q1, clk, rst)

    @always(delay(10))
    def clkgen():
        clk.next = not clk

    @instance
    def stimulus():

        # (a)
        assert q0 == 0
        assert q1 == 0
        yield clk.negedge

        # (b)
        assert q0 == 1 # mude aqui
        assert q1 == 0 # mude aqui
        yield clk.negedge

        ## (c)
        assert q0 == 1 # mude aqui
        assert q1 == 1 # mude aqui
        yield clk.negedge

        ## (d)
        assert q0 == 0 # mude aqui
        assert q1 == 1 # mude aqui
        yield clk.negedge

    sim = Simulation(dut, [stimulus, clkgen])
    sim.run(500)
    sim.quit()
