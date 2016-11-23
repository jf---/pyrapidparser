#this file is an automatic traslation of rapid code
import sys
sys.path.append('..')
import pyrapid
from collections import OrderedDict
import copy
import sys
# Line test/wobj_issue.prg:1
################### Start module ODC ####################
pyrapid.Symbols().PushScope('ODC', None)
##################################################################
############################# start declaration
# Line test/wobj_issue.prg:2
pyrapid.Symbols().AddGlobalSym('hotwirez', pyrapid.Symbol.CreatePers(pyrapid.Symbols().GetSymbol(symbolname='tooldata', modulename='ODC', functionname=None).data([True, [[0.0, 0.0, 733.0], [1.0, 0.0, 0.0, 0.0]], [10.0, [0.04, 0.0, 733.0], [1, 0, 0, 0], 0, 0, 0]])))
# end declaration
############################# start declaration
# Line test/wobj_issue.prg:3
pyrapid.Symbols().AddGlobalSym('Pos_Offset', pyrapid.Symbol.CreatePers(pyrapid.Symbols().GetSymbol(symbolname='pos', modulename='ODC', functionname=None).data([0, 0, 0])))
# end declaration
############################# start declaration
# Line test/wobj_issue.prg:4
pyrapid.Symbols().AddGlobalSym('cur_vel', pyrapid.Symbol.CreatePers(pyrapid.Symbols().GetSymbol(symbolname='speeddata', modulename='ODC', functionname=None).data([200.0, 200.0, 1000.0, 1000.0])))
# end declaration
############################# start declaration
# Line test/wobj_issue.prg:5
pyrapid.Symbols().AddGlobalSym('cur_zone', pyrapid.Symbol.CreatePers(pyrapid.Symbols().GetSymbol(symbolname='zonedata', modulename='ODC', functionname=None).data([False, 1, 1, 50, 0.1, 50, 0.1])))
# end declaration
# Line test/wobj_issue.prg:6
# ## COMMENT:PERS wobjdata cur_wobj := [ FALSE, TRUE, "", [ [ -0.000, -0.000, -1400.000 ], [ 1.000000000, 0.000000000, 0.000000000, 0.000000000 ] ], [ [0, 0, 0], [1, 0, 0 ,0] ] ]; ##
############################# start declaration
# Line test/wobj_issue.prg:8
pyrapid.Symbols().AddGlobalSym('cnstNoStepIn', pyrapid.Symbol.CreatePers(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='ODC', functionname=None).data('ohno')))
# end declaration
# Line test/wobj_issue.prg:10
# ## COMMENT: shell name: shell_000 ##
############################# start routine declaration
# Line test/wobj_issue.prg:11
# Start Procedure Definition
def error_rapid_proc_shell_000 (local_exception):
    return 0
def undo_rapid_proc_shell_000 ():
    pass
def rapid_proc_shell_000 (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='ODC', functionname='shell_000', invalue=local_args_scope):
        pass
        # data definitions
        # Line test/wobj_issue.prg:12
        # ## COMMENT: <<< group name: grouped_faces_000 >>> ##
        # Line test/wobj_issue.prg:13
        # ## COMMENT: ruled surface 001 ##
        # stantments
        #StatementAST shell_000
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure MoveL
# end routine declaration
##################################################################
pyrapid.Symbols().PopScope()
################### End module ODC ####################
