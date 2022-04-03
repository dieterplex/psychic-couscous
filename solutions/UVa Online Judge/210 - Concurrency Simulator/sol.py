from queue import Queue
from collections import deque
import sys  # debug print
def d(msg):
    print(">>>>>>> " + msg, file=sys.stderr)

def init():
    global programs, var, lock, qblock, qwait, QUANT
    global t_asgn, t_print, t_lock, t_unlock, t_end
    # load context
    (pcount, t_asgn, t_print, t_lock, t_unlock, t_end, QUANT) = [
        int(i) for i in input().split()
    ]
    # load programs
    programs = list()
    for i in range(pcount):
        lines = []
        while True:
            line = input()
            lines.append(line)
            if line == "end":
                break
        programs.insert(i, lines)
    # import pprint; pprint.pprint(programs)

    # internal state
    var = {chr(97 + i): 0 for i in range(26)}
    lock = False
    qblock = Queue()
    qwait = deque()
    qwait.extendleft(range(pcount))
    # enqueue program id. [pcount-1, ..., 0]


def exec_cmd(p, pid) -> int:
    global var
    global lock
    global qblock
    global qwait
    excute = p.pop(0)
    cmd = excute.split()
    d("{}: {}".format(pid, excute))
    if len(cmd) > 1 and cmd[1] == "=":
        var[cmd[0]] = int(cmd[2])
        return t_asgn
    elif cmd[0] == "print":
        print("{}: {}".format(pid+1, var[cmd[1]]))
        return t_print
    elif cmd[0] == "lock":
        if lock:
            # must, to resume as lock instruction
            p.insert(0, excute)
            qblock.put(pid)
            return -1
        else:
            lock = True
            return t_lock
    elif cmd[0] == "unlock":
        if not qblock.empty():
            qwait.append(qblock.get())
        lock = False
        return t_unlock
    else:  # end
        return t_end


def exec_prog(prog, prog_id, quant):
    time = quant
    while time > 0:
        ret = exec_cmd(prog[prog_id], prog_id)
        if ret == -1:
            # lock
            return False
        if len(prog[prog_id]) == 0:
            # end of program
            return False
        time -= ret
    return True


T = int(input())
for t in range(T):
    input()
    init()
    while len(qwait) > 0:
        id = qwait.pop()
        if exec_prog(programs, id, QUANT):
            qwait.appendleft(id)
    if t != T - 1:
        print()
