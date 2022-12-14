"""The Utility for xfstests logfile

xfstests-results-viewer needs input (xfstests results directory)
This support some operation to prepare environment.
"""

import os
from xfstests_results_viewer.testcase import PassedClass, SkippedClass, FailedClass

def create_timefile(basepath, l, t):
    """Create check.time for test

    xfstests records the execution time(sec) to check.time.
    This method prepare this file.

    Args:
        basepath (str): basepath in result directory
        l (list[src]): test name list
        t (list[int]): execution time list
    """
    with open('%s/check.time' % (basepath), mode='x') as f:
        for (x, y) in zip(l, t):
            f.write('%s %d\n' % (x, y))

def create_logfile(basepath, passed, skipped, failed):
    """Create check.log for test

    xfstests records the test report to check.log.
    This method prepare this file.

    Args:
        basepath (str): basepath in result directory
        passed (list[src]): passed test name list
        skipped (list[src]): skipped test name list
        failed (list[src]): failed test name list
    """
    with open('%s/check.log' % (basepath), mode='x') as f:
        f.write('Thu Jan  1 00:00:00 UTC 1970\n')
        write_testline(f, 'Ran: ', passed + skipped + failed)
        write_testline(f, 'Not run: ', skipped)
        write_testline(f, 'Failures: ', failed)
        f.write('Failed %d of %d tests\n' %
                (len(failed), len(passed + skipped + failed)))

def create_notrun(basepath, skipped):
    """Create ${testname}.notrun for test

    xfstests records the summary to ${testname}.notrun if test is skipped.
    This method prepare this file.

    Args:
        basepath (str): basepath in result directory
        skipped (list[src]): skipped test name list

    Note:
        ${testname}.notrun will record testname
    """
    for i in skipped:
        paths = i.rsplit('/', 1)
        os.makedirs('%s/%s' % (basepath, paths[0]), exist_ok=True)
        with open('%s/%s.notrun' % (basepath, i), mode='x') as f:
            f.write(i)

def write_testline(f, msg, l):
    """Helper for xreate_notrun

    Args:
        f (io): io object for result directory
        msg (src): prefix message
        l (list[src]): test name list
    """
    f.write(msg)
    for i in l:
        f.write('%s ' % (i))
    f.write('\n')
