"""Ref: https://blog.csdn.net/T_T233333333/article/details/120876783"""
from queue import Queue
from collections import deque
import sys, os


def d(msg):
    if os.getenv('UVA_DEBUG'):
        print(">>>>>>> " + msg, file=sys.stderr)  # stderr buffered


def exec_cmd(c, p, pid) -> int:
    cmd = p.pop(0)
    d("{}: {}".format(pid, cmd))
    if cmd[2] == "=":
        ch, _, val = cmd.split()
        c.var[ch] = int(val)
        return c.cost[0]
    elif cmd.startswith("print"):
        _, val = cmd.split()
        print("{}: {}".format(pid + 1, c.var[val]))
        return c.cost[1]
    elif cmd == "lock":
        if c.lock:
            p.insert(0, cmd)  # must, consume when unlock
            c.qblock.put(pid)
            return -1
        else:
            c.lock = True
            return c.cost[2]
    elif cmd == "unlock":
        if not c.qblock.empty():
            c.qwait.append(c.qblock.get())  # front of wait queue
        c.lock = False
        # d("block: {} wait: {}".format(list(c.qblock.queue), list(c.qwait)))
        return c.cost[3]
    else:
        return c.cost[4]


def exec_prog(ctx, prog, prog_id):
    time = ctx.quant
    while time > 0:
        ret = exec_cmd(ctx, prog[prog_id], prog_id)
        if ret == -1:
            # lock
            return False
        if len(prog[prog_id]) == 0:
            # end of program
            return False
        time -= ret
    return True


class Context:
    def __init__(self, prog_num, t_asgn, t_print, t_lock, t_unlock, t_end, quant):
        self.var = {chr(97 + i): 0 for i in range(26)}  # counters for alphabet
        self.lock = False
        self.qblock = Queue()
        self.qwait = deque()
        # enqueue program ids as [prog_num-1, ..., 0]
        self.qwait.extendleft(range(prog_num))
        self.prog_num = prog_num
        self.cost = (
            t_asgn,
            t_print,
            t_lock,
            t_unlock,
            t_end,
        )
        self.quant = quant

def testcase():
    # load context
    init_vars = [int(i) for i in input().split()]
    context = Context(*init_vars)
    # load programs
    programs = []
    for i in range(context.prog_num):
        lines = []
        while True:  # test data may exceed 25 instructions
            line = input()
            lines.append(line)
            if line == "end":
                break
        programs.insert(i, lines)
    return (context, programs)

T = int(input())
for t in range(T, 0, -1):
    input()  # blank per tc
    context, programs = testcase()
    while len(context.qwait) > 0:
        program_id = context.qwait.pop()
        if exec_prog(context, programs, program_id):
            context.qwait.appendleft(program_id)
    if t != 1:
        print()
