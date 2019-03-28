from subprocess import call

call(["gcc", "-O3", "-fopenmp",  "-msse4", "conv-harness-1.c"])
call(["./a.out", "16", "16", "3", "64", "64"])
call(["./a.out", "64", "64", "3", "128", "32"])
call(["./a.out", "128", "64", "7", "32", "256"])
