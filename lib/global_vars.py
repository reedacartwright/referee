# This file holds some global variables for some of the input options.
# Global variables are exclusively read only -- they are not modified anywhere else in the code except when reading the input options.

import timeit, lib.refcore as RC

def init():
    globs = {
        'version' : '1.1',
        'releasedate' : 'August 31, 2019',
        'doi' : 'https://doi.org/10.1093/gbe/evz088',
        'http' : 'https://gwct.github.io/referee/',
        'github' : 'https://github.com/gwct/referee/issues',
        'starttime' : timeit.default_timer(),
        'startdatetime' : RC.getOutTime(),
        'infile' : "",
        'intype' : "",
        'out' : "",
        'outdir' : "",
        'reffile' : "",
        'ref' : "",
        'num-procs' : 1,
        'fastq' : False,
        'fastq-len' : 100,
        'bed' : False,
        'beddir' : False,
        'correct-opt' : False,
        'raw-opt' : False,
        'log-v' : 1,
        'mapped' : False,
        'stats' : True,
        'allcalc' : False,
        'pileup' : False,
        'haploid' : False,
        'mapq' : False,
        'progstarttime' : 0,
        'stepstarttime' : 0,
        'pids' : "",
        'method' : 1,
        'genotypes' : ["AA", "AC", "AG", "AT", "CC", "CG", "CT", "GG", "GT", "TT"],
        'haploid-gt' : ["A","T","C","G"],
        'psutil' : "",
        'probs' : "",
        'debug' : False,
        'nolog' : False
    }

    globs['logfilename'] = "referee-" + globs['startdatetime'] + ".log";
    globs['tmpdir'] = "referee-tmpdir-" + globs['startdatetime'] + "-" + RC.getRandStr();

    return globs;