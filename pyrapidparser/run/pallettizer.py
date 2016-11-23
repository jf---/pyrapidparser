#this file is an automatic traslation of rapid code
import sys
sys.path.append('..')
import pyrapid
from collections import OrderedDict
import copy
import sys
# Line ./default/standard.sys:1
################### Start module SYSTEMMODULE ####################
pyrapid.Symbols().PushScope('SYSTEMMODULE', None)
##################################################################
# Line ./default/standard.sys:3
# ## COMMENT: from: 3HAC16581-1_revK_en ##
# Line ./default/standard.sys:4
# ## COMMENT: ##
# Line ./default/standard.sys:6
# ## COMMENT:CJointT ##
# Line ./default/standard.sys:7
# ## COMMENT:StopMove;  ##
# Line ./default/standard.sys:8
# ## COMMENT:ClearPath ##
# Line ./default/standard.sys:9
# ## COMMENT:StartMove ##
# Line ./default/standard.sys:10
# ## COMMENT:WaitTestAndSet ##
############################# start routine declaration
# Line ./default/standard.sys:12
# Start Function Definition
def error_rapid_func_IsStopMoveAct (local_exception):
    return 0
def undo_rapid_func_IsStopMoveAct ():
    pass
def rapid_func_IsStopMoveAct (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='IsStopMoveAct', invalue=local_args_scope):
        pass
        # data definitions
        # Line ./default/standard.sys:13
        # ## COMMENT:to be implemented ##
        # Line ./default/standard.sys:14
        # ## COMMENT: ##
        # stantments
        #StatementAST IsStopMoveAct
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:15
                return ( True )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStopMoveAct', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStopMoveAct', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' IsStopMoveAct(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsStopMoveAct, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' IsStopMoveAct(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('IsStopMoveAct', pyrapid.Symbol.CreateFunction(OrderedDict([('FromMoveTask', ('switch', None, None, None, ['FromNonMoveTask'])), ('FromNonMoveTask', ('switch', None, None, None, ['FromMoveTask']))]), pyrapid.Symbols().GetSymbol('bool', 'SYSTEMMODULE', None), rapid_func_IsStopMoveAct, error_rapid_func_IsStopMoveAct, undo_rapid_func_IsStopMoveAct), 'SYSTEMMODULE')
del rapid_func_IsStopMoveAct
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:18
# Start Procedure Definition
def error_rapid_proc_SkipWarn (local_exception):
    return 0
def undo_rapid_proc_SkipWarn ():
    pass
def rapid_proc_SkipWarn (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='SkipWarn', invalue=local_args_scope):
        pass
        # data definitions
        # stantments
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('SkipWarn', pyrapid.Symbol.CreateProcedure(OrderedDict(), rapid_proc_SkipWarn, error_rapid_proc_SkipWarn, undo_rapid_proc_SkipWarn), 'SYSTEMMODULE')
del rapid_proc_SkipWarn
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:21
# Start Procedure Definition
def error_rapid_proc_ExitCycle (local_exception):
    return 0
def undo_rapid_proc_ExitCycle ():
    pass
def rapid_proc_ExitCycle (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='ExitCycle', invalue=local_args_scope):
        pass
        # data definitions
        # Line ./default/standard.sys:22
        import sys
        # Line ./default/standard.sys:23
        print "Exit for ExitCycle"
        # Line ./default/standard.sys:24
        sys.exit(0)
        # stantments
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('ExitCycle', pyrapid.Symbol.CreateProcedure(OrderedDict(), rapid_proc_ExitCycle, error_rapid_proc_ExitCycle, undo_rapid_proc_ExitCycle), 'SYSTEMMODULE')
del rapid_proc_ExitCycle
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:27
# Start Procedure Definition
def error_rapid_proc_ErrWrite (local_exception):
    return 0
def undo_rapid_proc_ErrWrite ():
    pass
def rapid_proc_ErrWrite (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='ErrWrite', invalue=local_args_scope):
        pass
        # data definitions
        # Line ./default/standard.sys:28
        Header = pyrapid.Symbols().GetSymbol("Header").data.Get()
        # Line ./default/standard.sys:29
        Reason = pyrapid.Symbols().GetSymbol("Reason").data.Get()
        # stantments
        #StatementAST ErrWrite
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:30
                if (pyrapid.Symbols().IsInScope('W')) :
                    pass
                    # Line ./default/standard.sys:31
                    print( "Warning" )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ErrWrite', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ErrWrite', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ErrWrite(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ErrWrite, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ErrWrite(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST ErrWrite
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:33
                if (pyrapid.Symbols().IsInScope('I')) :
                    pass
                    # Line ./default/standard.sys:34
                    print( "Information" )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ErrWrite', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ErrWrite', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ErrWrite(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ErrWrite, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ErrWrite(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # Line ./default/standard.sys:36
        print( "Header: %s, Reason: %s"%(Header, Reason) )
        #StatementAST ErrWrite
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:38
                if (pyrapid.Symbols().IsInScope('RL2')) :
                    pass
                    # Line ./default/standard.sys:39
                    RL2 = pyrapid.Symbols().GetSymbol("RL2").data.Get()
                    # Line ./default/standard.sys:40
                    print( RL2 )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ErrWrite', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ErrWrite', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ErrWrite(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ErrWrite, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ErrWrite(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST ErrWrite
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:43
                if (pyrapid.Symbols().IsInScope('RL3')) :
                    pass
                    # Line ./default/standard.sys:44
                    RL3 = pyrapid.Symbols().GetSymbol("RL3").data.Get()
                    # Line ./default/standard.sys:45
                    print( RL3 )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ErrWrite', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ErrWrite', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ErrWrite(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ErrWrite, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ErrWrite(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST ErrWrite
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:48
                if (pyrapid.Symbols().IsInScope('RL4')) :
                    pass
                    # Line ./default/standard.sys:49
                    RL4 = pyrapid.Symbols().GetSymbol("RL4").data.Get()
                    # Line ./default/standard.sys:50
                    print( RL4 )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ErrWrite', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ErrWrite', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ErrWrite(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ErrWrite, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ErrWrite(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('ErrWrite', pyrapid.Symbol.CreateProcedure(OrderedDict([('W', ('switch', None, None, None, ['I'])), ('I', ('switch', None, None, None, ['W'])), ('Header', ('required', 'NORMAL', 'string', 0, [])), ('Reason', ('required', 'NORMAL', 'string', 0, [])), ('RL2', ('optional', 'NORMAL', 'string', 0, [])), ('RL3', ('optional', 'NORMAL', 'string', 0, [])), ('RL4', ('optional', 'NORMAL', 'string', 0, []))]), rapid_proc_ErrWrite, error_rapid_proc_ErrWrite, undo_rapid_proc_ErrWrite), 'SYSTEMMODULE')
del rapid_proc_ErrWrite
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:56
# Start Procedure Definition
def error_rapid_proc_ClearRawBytes (local_exception):
    return 0
def undo_rapid_proc_ClearRawBytes ():
    pass
def rapid_proc_ClearRawBytes (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='ClearRawBytes', invalue=local_args_scope):
        pass
        # data definitions
        # Line ./default/standard.sys:57
        FromIndex = 1
        # stantments
        #StatementAST ClearRawBytes
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:58
                if (pyrapid.Symbols().IsInScope('FromIndex')) :
                    pass
                    # Line ./default/standard.sys:59
                    FromIndex = pyrapid.Symbols().GetSymbol("FromIndex").data.Get()
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ClearRawBytes', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ClearRawBytes', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ClearRawBytes(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ClearRawBytes, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ClearRawBytes(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # Line ./default/standard.sys:61
        FromIndex -= 1 
        # Line ./default/standard.sys:62
        RawData = pyrapid.Symbols().GetSymbol("RawData").data
        # Line ./default/standard.sys:63
        RawData.Set( RawData.Get()[:FromIndex] )
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('ClearRawBytes', pyrapid.Symbol.CreateProcedure(OrderedDict([('RawData', ('required', 'VAR', 'rawbytes', 0, [])), ('FromIndex', ('optional', 'NORMAL', 'num', 0, []))]), rapid_proc_ClearRawBytes, error_rapid_proc_ClearRawBytes, undo_rapid_proc_ClearRawBytes), 'SYSTEMMODULE')
del rapid_proc_ClearRawBytes
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:66
# Start Procedure Definition
def error_rapid_proc_CopyRawBytes (local_exception):
    return 0
def undo_rapid_proc_CopyRawBytes ():
    pass
def rapid_proc_CopyRawBytes (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='CopyRawBytes', invalue=local_args_scope):
        pass
        # data definitions
        # stantments
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('CopyRawBytes', pyrapid.Symbol.CreateProcedure(OrderedDict([('FromRawData', ('required', 'NORMAL', 'rawbytes', 0, [])), ('FromIndex', ('required', 'NORMAL', 'num', 0, [])), ('ToRawData', ('required', 'VAR', 'rawbytes', 0, [])), ('ToIndex', ('required', 'NORMAL', 'num', 0, [])), ('NoOfBytes', ('optional', 'NORMAL', 'num', 0, []))]), rapid_proc_CopyRawBytes, error_rapid_proc_CopyRawBytes, undo_rapid_proc_CopyRawBytes), 'SYSTEMMODULE')
del rapid_proc_CopyRawBytes
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:69
# Start Procedure Definition
def error_rapid_proc_PackRawBytes (local_exception):
    return 0
def undo_rapid_proc_PackRawBytes ():
    pass
def rapid_proc_PackRawBytes (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='PackRawBytes', invalue=local_args_scope):
        pass
        # data definitions
        # Line ./default/standard.sys:70
        RawData = pyrapid.Symbols().GetSymbol("RawData").data.Get()
        # Line ./default/standard.sys:71
        Value = pyrapid.Symbols().GetSymbol("Value").data
        # Line ./default/standard.sys:72
        StartIndex = pyrapid.Symbols().GetSymbol("StartIndex").data.Get()
        # Line ./default/standard.sys:73
        StartIndex -= 1
        # Line ./default/standard.sys:74
        import struct
        # Line ./default/standard.sys:75
        endian = '<'
        # Line ./default/standard.sys:76
        # ## COMMENT:\Network   -> BigEndian ##
        # stantments
        #StatementAST PackRawBytes
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:77
                if (pyrapid.Symbols().IsInScope('Network')) :
                    pass
                    # Line ./default/standard.sys:78
                    endian = '>'
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='PackRawBytes', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='PackRawBytes', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' PackRawBytes(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=PackRawBytes, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' PackRawBytes(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST PackRawBytes
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:80
                if (pyrapid.Symbols().IsInScope('Hex1')) :
                    pass
                    # Line ./default/standard.sys:81
                    if isinstance(Value, pyrapid.rapid_byte):
                    # Line ./default/standard.sys:82
                        Value = Value.Get()
                    # Line ./default/standard.sys:83
                        app=struct.pack(endian+"B", Value)
                    # Line ./default/standard.sys:84
                        RawData =RawData[:StartIndex]+app+RawData[StartIndex+len(app):]
                    # Line ./default/standard.sys:85
                    else:
                    # Line ./default/standard.sys:86
                        raise Exception('type not valid')
                # Line ./default/standard.sys:87
                elif (pyrapid.Symbols().IsInScope('IntX')) :
                    pass
                    # Line ./default/standard.sys:88
                    IntX = pyrapid.Symbols().GetSymbol("IntX").data.Get()
                    # Line ./default/standard.sys:90
                    USINT = pyrapid.Symbols().GetSymbol("USINT").data.Get()
                    # Line ./default/standard.sys:91
                    UINT = pyrapid.Symbols().GetSymbol("UINT").data.Get()
                    # Line ./default/standard.sys:92
                    UDINT = pyrapid.Symbols().GetSymbol("UDINT").data.Get()
                    # Line ./default/standard.sys:93
                    ULINT = pyrapid.Symbols().GetSymbol("ULINT").data.Get()
                    # Line ./default/standard.sys:94
                    SINT = pyrapid.Symbols().GetSymbol("SINT").data.Get()
                    # Line ./default/standard.sys:95
                    INT = pyrapid.Symbols().GetSymbol("INT").data.Get()
                    # Line ./default/standard.sys:96
                    DINT = pyrapid.Symbols().GetSymbol("DINT").data.Get()
                    # Line ./default/standard.sys:97
                    LINT = pyrapid.Symbols().GetSymbol("LINT").data.Get()
                    # Line ./default/standard.sys:99
                    Value = long( Value.Get() )
                    # Line ./default/standard.sys:101
                    if IntX==USINT:
                    # Line ./default/standard.sys:102
                        app=struct.pack(endian+"B", Value)
                    # Line ./default/standard.sys:103
                    elif IntX==UINT:
                    # Line ./default/standard.sys:104
                        app=struct.pack(endian+"H", Value)
                    # Line ./default/standard.sys:105
                    elif IntX==UDINT:
                    # Line ./default/standard.sys:106
                        app=struct.pack(endian+"I", Value)
                    # Line ./default/standard.sys:107
                    elif IntX==ULINT:
                    # Line ./default/standard.sys:108
                        app=struct.pack(endian+"Q", Value)
                    # Line ./default/standard.sys:109
                    elif IntX==SINT:
                    # Line ./default/standard.sys:110
                        app=struct.pack(endian+"b", Value)
                    # Line ./default/standard.sys:111
                    elif IntX==INT:
                    # Line ./default/standard.sys:112
                        app=struct.pack(endian+"h", Value)
                    # Line ./default/standard.sys:113
                    elif IntX==DINT:
                    # Line ./default/standard.sys:114
                        app=struct.pack(endian+"i", Value)
                    # Line ./default/standard.sys:115
                    elif IntX==LINT:
                    # Line ./default/standard.sys:116
                        app=struct.pack(endian+"q", Value)
                    # Line ./default/standard.sys:117
                    RawData =RawData[:StartIndex]+app+RawData[StartIndex+len(app):]
                # Line ./default/standard.sys:119
                elif (pyrapid.Symbols().IsInScope('Float4')) :
                    pass
                    # Line ./default/standard.sys:120
                    Value = float(Value.Get())
                    # Line ./default/standard.sys:121
                    app=struct.pack(endian+"f", Value)
                    # Line ./default/standard.sys:122
                    RawData =RawData[:StartIndex]+app+RawData[StartIndex+len(app):]
                # Line ./default/standard.sys:124
                elif (pyrapid.Symbols().IsInScope('ASCII')) :
                    pass
                    # Line ./default/standard.sys:125
                    if isinstance(Value, pyrapid.rapid_byte):
                    # Line ./default/standard.sys:126
                        Value = Value.Get()
                    # Line ./default/standard.sys:127
                        app=struct.pack(endian+"b", Value)
                    # Line ./default/standard.sys:128
                        RawData =RawData[:StartIndex]+app+RawData[StartIndex+len(app):]
                    # Line ./default/standard.sys:129
                    else:
                    # Line ./default/standard.sys:130
                        Value = Value.Get()
                    # Line ./default/standard.sys:131
                        len_Value = len(Value)
                    # Line ./default/standard.sys:132
                        app=struct.pack(endian+"%ds"%(len_Value,), Value)
                    # Line ./default/standard.sys:133
                        RawData =RawData[:StartIndex]+app+RawData[StartIndex+len(app):]
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='PackRawBytes', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='PackRawBytes', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' PackRawBytes(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=PackRawBytes, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' PackRawBytes(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # Line ./default/standard.sys:136
        pyrapid.Symbols().GetSymbol("RawData").data.Set(RawData)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('PackRawBytes', pyrapid.Symbol.CreateProcedure(OrderedDict([('Value', ('required', 'NORMAL', 'anytype', 0, [])), ('RawData', ('required', 'VAR', 'rawbytes', 0, [])), ('Network', ('switch', None, None, None, [])), ('StartIndex', ('required', 'NORMAL', 'num', 0, [])), ('Hex1', ('switch', None, None, None, ['Float4', 'ASCII', 'IntX'])), ('IntX', ('optional', 'NORMAL', 'num', 0, ['Hex1', 'Float4', 'ASCII'])), ('Float4', ('switch', None, None, None, ['Hex1', 'ASCII', 'IntX'])), ('ASCII', ('switch', None, None, None, ['Hex1', 'Float4', 'IntX']))]), rapid_proc_PackRawBytes, error_rapid_proc_PackRawBytes, undo_rapid_proc_PackRawBytes), 'SYSTEMMODULE')
del rapid_proc_PackRawBytes
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:140
# Start Procedure Definition
def error_rapid_proc_UnPackRawBytes (local_exception):
    return 0
def undo_rapid_proc_UnPackRawBytes ():
    pass
def rapid_proc_UnPackRawBytes (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='UnPackRawBytes', invalue=local_args_scope):
        pass
        # data definitions
        # Line ./default/standard.sys:141
        RawData = pyrapid.Symbols().GetSymbol("RawData").data.Get()
        # Line ./default/standard.sys:142
        StartIndex = pyrapid.Symbols().GetSymbol("StartIndex").data.Get()
        # Line ./default/standard.sys:143
        StartIndex -= 1
        # Line ./default/standard.sys:144
        import struct
        # Line ./default/standard.sys:145
        endian = '<'
        # Line ./default/standard.sys:146
        # ## COMMENT:\Network   -> BigEndian ##
        # stantments
        #StatementAST UnPackRawBytes
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:147
                if (pyrapid.Symbols().IsInScope('Network')) :
                    pass
                    # Line ./default/standard.sys:148
                    endian = '>'
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='UnPackRawBytes', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='UnPackRawBytes', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' UnPackRawBytes(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=UnPackRawBytes, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' UnPackRawBytes(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST UnPackRawBytes
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:150
                if (pyrapid.Symbols().IsInScope('Hex1')) :
                    pass
                    # Line ./default/standard.sys:151
                    if isinstance(Value, pyrapid.rapid_byte):
                    # Line ./default/standard.sys:152
                        RawData = RawData[StartIndex:StartIndex+struct.calcsize(endian+"B")]
                    # Line ./default/standard.sys:153
                        Value, = struct.unpack(endian+"B", RawData)
                    # Line ./default/standard.sys:154
                    else:
                    # Line ./default/standard.sys:155
                        raise Exception('type not valid')
                # Line ./default/standard.sys:156
                elif (pyrapid.Symbols().IsInScope('IntX')) :
                    pass
                    # Line ./default/standard.sys:157
                    IntX = pyrapid.Symbols().GetSymbol("IntX").data.Get()
                    # Line ./default/standard.sys:159
                    USINT = pyrapid.Symbols().GetSymbol("USINT").data.Get()
                    # Line ./default/standard.sys:160
                    UINT = pyrapid.Symbols().GetSymbol("UINT").data.Get()
                    # Line ./default/standard.sys:161
                    UDINT = pyrapid.Symbols().GetSymbol("UDINT").data.Get()
                    # Line ./default/standard.sys:162
                    ULINT = pyrapid.Symbols().GetSymbol("ULINT").data.Get()
                    # Line ./default/standard.sys:163
                    SINT = pyrapid.Symbols().GetSymbol("SINT").data.Get()
                    # Line ./default/standard.sys:164
                    INT = pyrapid.Symbols().GetSymbol("INT").data.Get()
                    # Line ./default/standard.sys:165
                    DINT = pyrapid.Symbols().GetSymbol("DINT").data.Get()
                    # Line ./default/standard.sys:166
                    LINT = pyrapid.Symbols().GetSymbol("LINT").data.Get()
                    # Line ./default/standard.sys:168
                    if IntX==USINT:
                    # Line ./default/standard.sys:169
                        RawData = RawData[StartIndex:StartIndex+struct.calcsize(endian+"B")]
                    # Line ./default/standard.sys:170
                        Value, = struct.unpack(endian+"B", RawData)
                    # Line ./default/standard.sys:171
                    elif IntX==UINT:
                    # Line ./default/standard.sys:172
                        RawData = RawData[StartIndex:StartIndex+struct.calcsize(endian+"H")]
                    # Line ./default/standard.sys:173
                        Value, = struct.unpack(endian+"H", RawData)
                    # Line ./default/standard.sys:174
                    elif IntX==UDINT:
                    # Line ./default/standard.sys:175
                        RawData = RawData[StartIndex:StartIndex+struct.calcsize(endian+"I")]
                    # Line ./default/standard.sys:176
                        Value, = struct.unpack_from(endian+"I", RawData)
                    # Line ./default/standard.sys:177
                    elif IntX==ULINT:
                    # Line ./default/standard.sys:178
                        RawData = RawData[StartIndex:StartIndex+struct.calcsize(endian+"Q")]
                    # Line ./default/standard.sys:179
                        Value, = struct.unpack_from(endian+"Q", RawData)
                    # Line ./default/standard.sys:180
                    elif IntX==SINT:
                    # Line ./default/standard.sys:181
                        RawData = RawData[StartIndex:StartIndex+struct.calcsize(endian+"b")]
                    # Line ./default/standard.sys:182
                        Value, = struct.unpack(endian+"b", RawData)
                    # Line ./default/standard.sys:183
                    elif IntX==INT:
                    # Line ./default/standard.sys:184
                        RawData = RawData[StartIndex:StartIndex+struct.calcsize(endian+"h")]
                    # Line ./default/standard.sys:185
                        Value, = struct.unpack(endian+"h", RawData)
                    # Line ./default/standard.sys:186
                    elif IntX==DINT:
                    # Line ./default/standard.sys:187
                        RawData = RawData[StartIndex:StartIndex+struct.calcsize(endian+"i")]
                    # Line ./default/standard.sys:188
                        Value, = struct.unpack(endian+"i", RawData)
                    # Line ./default/standard.sys:189
                    elif IntX==LINT:
                    # Line ./default/standard.sys:190
                        RawData = RawData[StartIndex:StartIndex+struct.calcsize(endian+"q")]
                    # Line ./default/standard.sys:191
                        Value, = struct.unpack(endian+"q", RawData)
                # Line ./default/standard.sys:193
                elif (pyrapid.Symbols().IsInScope('Float4')) :
                    pass
                    # Line ./default/standard.sys:194
                    RawData = RawData[StartIndex:StartIndex+struct.calcsize(endian+"f")]
                    # Line ./default/standard.sys:195
                    Value, = struct.unpack(endian+"f", RawData)
                # Line ./default/standard.sys:196
                elif (pyrapid.Symbols().IsInScope('ASCII')) :
                    pass
                    # Line ./default/standard.sys:197
                    if isinstance(pyrapid.Symbols().GetSymbol("Value").data, pyrapid.rapid_byte):
                    # Line ./default/standard.sys:198
                        RawData = RawData[StartIndex:StartIndex+struct.calcsize(endian+"b")]
                    # Line ./default/standard.sys:199
                        Value, = struct.unpack(endian+"b", RawData)
                    # Line ./default/standard.sys:200
                    else:
                    # Line ./default/standard.sys:201
                        ASCII = pyrapid.Symbols().GetSymbol("ASCII").data.Get()
                    # Line ./default/standard.sys:202
                        RawData = RawData[StartIndex:StartIndex+struct.calcsize(endian+"%ds"%(ASCII,))]
                    # Line ./default/standard.sys:203
                        Value, = struct.unpack(endian+"%ds"%(ASCII,), RawData)
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='UnPackRawBytes', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='UnPackRawBytes', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' UnPackRawBytes(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=UnPackRawBytes, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' UnPackRawBytes(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # Line ./default/standard.sys:206
        pyrapid.Symbols().GetSymbol("Value").data.Set(Value)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('UnPackRawBytes', pyrapid.Symbol.CreateProcedure(OrderedDict([('RawData', ('required', 'VAR', 'rawbytes', 0, [])), ('Network', ('switch', None, None, None, [])), ('StartIndex', ('required', 'NORMAL', 'num', 0, [])), ('Value', ('required', 'VAR', 'anytype', 0, [])), ('Hex1', ('switch', None, None, None, ['Float4', 'ASCII', 'IntX'])), ('IntX', ('optional', 'NORMAL', 'num', 0, ['Hex1', 'Float4', 'ASCII'])), ('Float4', ('switch', None, None, None, ['Hex1', 'ASCII', 'IntX'])), ('ASCII', ('optional', 'NORMAL', 'num', 0, ['Hex1', 'Float4', 'IntX']))]), rapid_proc_UnPackRawBytes, error_rapid_proc_UnPackRawBytes, undo_rapid_proc_UnPackRawBytes), 'SYSTEMMODULE')
del rapid_proc_UnPackRawBytes
# End Procedure Definition
# end routine declaration
# Line ./default/standard.sys:209
# ## COMMENT: PackDNHeader Service Path RawData ##
# Line ./default/standard.sys:210
# ## COMMENT: RawBytesLen (RawData) ##
############################# start routine declaration
# Line ./default/standard.sys:211
# Start Function Definition
def error_rapid_func_RawBytesLen (local_exception):
    return 0
def undo_rapid_func_RawBytesLen ():
    pass
def rapid_func_RawBytesLen (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='RawBytesLen', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line ./default/standard.sys:212
        pyrapid.Symbols().AddScopeSym('ret', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='SYSTEMMODULE', functionname='RawBytesLen').data(None)))
        # end declaration
        # Line ./default/standard.sys:213
        RawData = pyrapid.Symbols().GetSymbol("RawData").data.Get()
        # Line ./default/standard.sys:214
        pyrapid.Symbols().GetSymbol("ret").data.Set(len(RawData))
        # stantments
        #StatementAST RawBytesLen
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:215
                return ( pyrapid.Symbols().GetSymbol(symbolname='ret', modulename='SYSTEMMODULE', functionname='RawBytesLen').data.Get() )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='RawBytesLen', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='RawBytesLen', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' RawBytesLen(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=RawBytesLen, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' RawBytesLen(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('RawBytesLen', pyrapid.Symbol.CreateFunction(OrderedDict([('RawData', ('required', 'VAR', 'rawbytes', 0, []))]), pyrapid.Symbols().GetSymbol('num', 'SYSTEMMODULE', None), rapid_func_RawBytesLen, error_rapid_func_RawBytesLen, undo_rapid_func_RawBytesLen), 'SYSTEMMODULE')
del rapid_func_RawBytesLen
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:219
# Start Function Definition
def error_rapid_func_GetSysInfo (local_exception):
    return 0
def undo_rapid_func_GetSysInfo ():
    pass
def rapid_func_GetSysInfo (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='GetSysInfo', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line ./default/standard.sys:220
        pyrapid.Symbols().AddScopeSym('ret', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='SYSTEMMODULE', functionname='GetSysInfo').data(None)))
        # end declaration
        # stantments
        #StatementAST GetSysInfo
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:221
                if (pyrapid.Symbols().IsInScope('LanIp')) :
                    pass
                    # Line ./default/standard.sys:222
                    pyrapid.Symbols().GetSymbol("ret").data.Set("0.0.0.0")
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='GetSysInfo', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='GetSysInfo', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' GetSysInfo(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=GetSysInfo, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' GetSysInfo(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST GetSysInfo
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:224
                return ( pyrapid.Symbols().GetSymbol(symbolname='ret', modulename='SYSTEMMODULE', functionname='GetSysInfo').data.Get() )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='GetSysInfo', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='GetSysInfo', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' GetSysInfo(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=GetSysInfo, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' GetSysInfo(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('GetSysInfo', pyrapid.Symbol.CreateFunction(OrderedDict([('SerialNo', ('switch', None, None, None, ['CtrlId', 'CtrlLang', 'SWVersion', 'RobotType', 'LanIp'])), ('SWVersion', ('switch', None, None, None, ['CtrlId', 'CtrlLang', 'RobotType', 'SerialNo', 'LanIp'])), ('RobotType', ('switch', None, None, None, ['CtrlId', 'CtrlLang', 'SWVersion', 'SerialNo', 'LanIp'])), ('CtrlId', ('switch', None, None, None, ['CtrlLang', 'SWVersion', 'RobotType', 'SerialNo', 'LanIp'])), ('LanIp', ('switch', None, None, None, ['CtrlId', 'CtrlLang', 'SWVersion', 'RobotType', 'SerialNo'])), ('CtrlLang', ('switch', None, None, None, ['CtrlId', 'SWVersion', 'RobotType', 'SerialNo', 'LanIp']))]), pyrapid.Symbols().GetSymbol('string', 'SYSTEMMODULE', None), rapid_func_GetSysInfo, error_rapid_func_GetSysInfo, undo_rapid_func_GetSysInfo), 'SYSTEMMODULE')
del rapid_func_GetSysInfo
# End Function Definition
# end routine declaration
# Line ./default/standard.sys:227
# ## COMMENT:!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! SOCKET !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ##
############################# start routine declaration
# Line ./default/standard.sys:229
# Start Function Definition
def error_rapid_func_SocketGetStatus (local_exception):
    return 0
def undo_rapid_func_SocketGetStatus ():
    pass
def rapid_func_SocketGetStatus (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='SocketGetStatus', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line ./default/standard.sys:230
        pyrapid.Symbols().AddScopeSym('ret', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='socketstatus', modulename='SYSTEMMODULE', functionname='SocketGetStatus').data(None)))
        # end declaration
        # Line ./default/standard.sys:231
        import socket
        # Line ./default/standard.sys:232
        lstate, lsocket = pyrapid.Symbols().GetSymbol("Socket").data.Get()
        # Line ./default/standard.sys:233
        pyrapid.Symbols().GetSymbol("ret").data.Set(lstate)
        # stantments
        #StatementAST SocketGetStatus
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:234
                return ( pyrapid.Symbols().GetSymbol(symbolname='ret', modulename='SYSTEMMODULE', functionname='SocketGetStatus').data.Get() )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='SocketGetStatus', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='SocketGetStatus', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' SocketGetStatus(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=SocketGetStatus, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' SocketGetStatus(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('SocketGetStatus', pyrapid.Symbol.CreateFunction(OrderedDict([('Socket', ('required', 'NORMAL', 'socketdev', 0, []))]), pyrapid.Symbols().GetSymbol('socketstatus', 'SYSTEMMODULE', None), rapid_func_SocketGetStatus, error_rapid_func_SocketGetStatus, undo_rapid_func_SocketGetStatus), 'SYSTEMMODULE')
del rapid_func_SocketGetStatus
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:237
# Start Procedure Definition
def error_rapid_proc_SocketCreate (local_exception):
    return 0
def undo_rapid_proc_SocketCreate ():
    pass
def rapid_proc_SocketCreate (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='SocketCreate', invalue=local_args_scope):
        pass
        # data definitions
        # Line ./default/standard.sys:238
        import socket
        # Line ./default/standard.sys:239
        SOCKET_CREATED = pyrapid.Symbols().GetSymbol("SOCKET_CREATED").data.Get()
        # Line ./default/standard.sys:240
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Line ./default/standard.sys:241
        pyrapid.Symbols().GetSymbol("Socket").data.Set( (SOCKET_CREATED, s) )
        # stantments
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('SocketCreate', pyrapid.Symbol.CreateProcedure(OrderedDict([('Socket', ('required', 'VAR', 'socketdev', 0, []))]), rapid_proc_SocketCreate, error_rapid_proc_SocketCreate, undo_rapid_proc_SocketCreate), 'SYSTEMMODULE')
del rapid_proc_SocketCreate
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:244
# Start Procedure Definition
def error_rapid_proc_SocketClose (local_exception):
    return 0
def undo_rapid_proc_SocketClose ():
    pass
def rapid_proc_SocketClose (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='SocketClose', invalue=local_args_scope):
        pass
        # data definitions
        # Line ./default/standard.sys:245
        import socket
        # Line ./default/standard.sys:246
        SOCKET_CLOSED = pyrapid.Symbols().GetSymbol("SOCKET_CLOSED").data.Get()
        # Line ./default/standard.sys:247
        state,s = pyrapid.Symbols().GetSymbol("Socket").data.Get()
        # Line ./default/standard.sys:248
        s.close()
        # Line ./default/standard.sys:249
        pyrapid.Symbols().GetSymbol("Socket").data.Set( (SOCKET_CLOSED, None) )
        # stantments
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('SocketClose', pyrapid.Symbol.CreateProcedure(OrderedDict([('Socket', ('required', 'VAR', 'socketdev', 0, []))]), rapid_proc_SocketClose, error_rapid_proc_SocketClose, undo_rapid_proc_SocketClose), 'SYSTEMMODULE')
del rapid_proc_SocketClose
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:252
# Start Procedure Definition
def error_rapid_proc_SocketAccept (local_exception):
    return 0
def undo_rapid_proc_SocketAccept ():
    pass
def rapid_proc_SocketAccept (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='SocketAccept', invalue=local_args_scope):
        pass
        # data definitions
        # Line ./default/standard.sys:253
        # ## COMMENT:Socket ##
        # Line ./default/standard.sys:254
        # ## COMMENT:The server socket that are waiting for incoming connections. The socket must ##
        # Line ./default/standard.sys:255
        # ## COMMENT:already be created, bounded and ready for listen. ##
        # Line ./default/standard.sys:256
        # ## COMMENT:ClientSocket ##
        # Line ./default/standard.sys:257
        # ## COMMENT:The returned new client socket, that will be updated with the accepted incoming ##
        # Line ./default/standard.sys:258
        # ## COMMENT:connection request. ##
        # Line ./default/standard.sys:259
        # ## COMMENT:ClientAddress ##
        # Line ./default/standard.sys:260
        # ## COMMENT:The variable that will be updated with the IP-address of the accepted incoming ##
        # Line ./default/standard.sys:261
        # ## COMMENT:connection request. ##
        # Line ./default/standard.sys:262
        # ## COMMENT:Time ##
        # Line ./default/standard.sys:263
        # ## COMMENT:The maximum amount of time [s] that program execution waits for incoming ##
        # Line ./default/standard.sys:264
        # ## COMMENT:connections. If this time runs out before any incoming connection, the error  ##
        # Line ./default/standard.sys:265
        # ## COMMENT:handler will be called, if there is one, with the error code ERR_SOCK_TIMEOUT. ##
        # Line ./default/standard.sys:266
        # ## COMMENT:If there is no error handler, the execution will be stopped. ##
        # Line ./default/standard.sys:267
        # ## COMMENT:If parameter Time is not used, the waiting time is 60 s. ##
        # Line ./default/standard.sys:268
        # ## COMMENT: ##
        # Line ./default/standard.sys:269
        # ## COMMENT:Exception: ERR_SOCK_TIMEOUT ##
        # Line ./default/standard.sys:270
        # ## COMMENT: ##
        # Line ./default/standard.sys:271
        import socket
        # Line ./default/standard.sys:272
        Socket = pyrapid.Symbols().GetSymbol("Socket").data
        # Line ./default/standard.sys:273
        ClientSocket = pyrapid.Symbols().GetSymbol("ClientSocket").data
        # Line ./default/standard.sys:275
        s = Socket.Get()[1]
        # Line ./default/standard.sys:276
        Time = None
        # stantments
        #StatementAST SocketAccept
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:277
                if (pyrapid.Symbols().IsInScope('Time')) :
                    pass
                    #StatementAST SocketAccept
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line ./default/standard.sys:278
                            if (( pyrapid.Symbols().GetSymbol(symbolname='Time', modulename='SYSTEMMODULE', functionname='SocketAccept').data.Get() != pyrapid.Symbols().GetSymbol(symbolname='WAIT_MAX', modulename='SYSTEMMODULE', functionname='SocketAccept').data.Get() )) :
                                pass
                                # Line ./default/standard.sys:279
                                Time = pyrapid.Symbols().GetSymbol("Time").data.Get()
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='SocketAccept', modulename='SYSTEMMODULE').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='SocketAccept', modulename='SYSTEMMODULE').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' SocketAccept(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=SocketAccept, modulename='SYSTEMMODULE').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' SocketAccept(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='SocketAccept', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='SocketAccept', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' SocketAccept(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=SocketAccept, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' SocketAccept(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # Line ./default/standard.sys:282
        s.settimeout(Time)
        # Line ./default/standard.sys:284
        try:
        # Line ./default/standard.sys:285
                sc, address = s.accept()
        # Line ./default/standard.sys:286
        except socket.timeout:
        # Line ./default/standard.sys:287
                ERR_SOCK_TIMEOUT = pyrapid.Symbols().GetSymbol("ERR_SOCK_TIMEOUT").data.Get()
        # Line ./default/standard.sys:288
                raise pyrapid.RapidException(ERR_SOCK_TIMEOUT, "accept timeout: SocketAccept(%d) -"%(pyrapid.lineno(),))
        # Line ./default/standard.sys:290
        SOCKET_CONNECTED = pyrapid.Symbols().GetSymbol("SOCKET_CONNECTED").data.Get()
        # Line ./default/standard.sys:291
        ClientSocket.Set( (SOCKET_CONNECTED, sc) )
        # Line ./default/standard.sys:293
        ClientAddress = None
        #StatementAST SocketAccept
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:294
                if (pyrapid.Symbols().IsInScope('ClientAddress')) :
                    pass
                    # Line ./default/standard.sys:295
                    ClientAddress = pyrapid.Symbols().GetSymbol("ClientAddress").data
                    # Line ./default/standard.sys:296
                    ClientAddress.Set(address[0])
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='SocketAccept', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='SocketAccept', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' SocketAccept(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=SocketAccept, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' SocketAccept(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('SocketAccept', pyrapid.Symbol.CreateProcedure(OrderedDict([('Socket', ('required', 'VAR', 'socketdev', 0, [])), ('ClientSocket', ('required', 'VAR', 'socketdev', 0, [])), ('ClientAddress', ('optional', 'VAR', 'string', 0, [])), ('Time', ('optional', 'NORMAL', 'num', 0, []))]), rapid_proc_SocketAccept, error_rapid_proc_SocketAccept, undo_rapid_proc_SocketAccept), 'SYSTEMMODULE')
del rapid_proc_SocketAccept
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:301
# Start Procedure Definition
def error_rapid_proc_SocketBind (local_exception):
    return 0
def undo_rapid_proc_SocketBind ():
    pass
def rapid_proc_SocketBind (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='SocketBind', invalue=local_args_scope):
        pass
        # data definitions
        # Line ./default/standard.sys:302
        import socket
        # Line ./default/standard.sys:303
        Socket = pyrapid.Symbols().GetSymbol("Socket").data
        # Line ./default/standard.sys:304
        LocalAddress = pyrapid.Symbols().GetSymbol("LocalAddress").data.Get()
        # Line ./default/standard.sys:305
        LocalPort = pyrapid.Symbols().GetSymbol("LocalPort").data.Get()
        # Line ./default/standard.sys:306
        s = Socket.Get()[1]
        # Line ./default/standard.sys:307
        s.settimeout(None)
        # Line ./default/standard.sys:308
        s.bind( (LocalAddress, LocalPort) )
        # Line ./default/standard.sys:309
        SOCKET_BOUND = pyrapid.Symbols().GetSymbol("SOCKET_BOUND").data.Get()
        # Line ./default/standard.sys:310
        Socket.Set( (SOCKET_BOUND, s) )
        # stantments
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('SocketBind', pyrapid.Symbol.CreateProcedure(OrderedDict([('Socket', ('required', 'VAR', 'socketdev', 0, [])), ('LocalAddress', ('required', 'NORMAL', 'string', 0, [])), ('LocalPort', ('required', 'NORMAL', 'num', 0, []))]), rapid_proc_SocketBind, error_rapid_proc_SocketBind, undo_rapid_proc_SocketBind), 'SYSTEMMODULE')
del rapid_proc_SocketBind
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:313
# Start Procedure Definition
def error_rapid_proc_SocketConnect (local_exception):
    return 0
def undo_rapid_proc_SocketConnect ():
    pass
def rapid_proc_SocketConnect (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='SocketConnect', invalue=local_args_scope):
        pass
        # data definitions
        # Line ./default/standard.sys:314
        # ## COMMENT:Exception: ERR_SOCK_CLOSED  ##
        # Line ./default/standard.sys:315
        # ## COMMENT:Exception: ERR_SOCK_ISCON  ##
        # Line ./default/standard.sys:316
        # ## COMMENT:Exception: ERR_SOCK_CONNREF  ##
        # Line ./default/standard.sys:317
        # ## COMMENT:Exception: ERR_SOCK_TIMEOUT  ##
        # stantments
        #StatementAST SocketConnect
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:319
                if (( pyrapid.Symbols().GetSymbol(symbolname='SocketGetStatus', modulename='SYSTEMMODULE', functionname='SocketConnect').data( {'Socket':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='socketdev', modulename='SYSTEMMODULE', functionname='SocketConnect').data(pyrapid.Symbols().GetSymbol(symbolname='Socket', modulename='SYSTEMMODULE', functionname='SocketConnect').data.Get()))} ) == pyrapid.Symbols().GetSymbol(symbolname='SOCKET_CONNECTED', modulename='SYSTEMMODULE', functionname='SocketConnect').data.Get() )) :
                    pass
                    #StatementAST SocketConnect
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line ./default/standard.sys:320
                            raise pyrapid.RapidException(pyrapid.Symbols().GetSymbol(symbolname='ERR_SOCK_ISCON', modulename='SYSTEMMODULE', functionname='SocketConnect').data.Get(),'ERR_SOCK_ISCON')
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='SocketConnect', modulename='SYSTEMMODULE').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='SocketConnect', modulename='SYSTEMMODULE').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' SocketConnect(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=SocketConnect, modulename='SYSTEMMODULE').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' SocketConnect(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='SocketConnect', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='SocketConnect', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' SocketConnect(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=SocketConnect, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' SocketConnect(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST SocketConnect
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:322
                if (( pyrapid.Symbols().GetSymbol(symbolname='SocketGetStatus', modulename='SYSTEMMODULE', functionname='SocketConnect').data( {'Socket':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='socketdev', modulename='SYSTEMMODULE', functionname='SocketConnect').data(pyrapid.Symbols().GetSymbol(symbolname='Socket', modulename='SYSTEMMODULE', functionname='SocketConnect').data.Get()))} ) == pyrapid.Symbols().GetSymbol(symbolname='SOCKET_CLOSED', modulename='SYSTEMMODULE', functionname='SocketConnect').data.Get() )) :
                    pass
                    #StatementAST SocketConnect
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line ./default/standard.sys:323
                            raise pyrapid.RapidException(pyrapid.Symbols().GetSymbol(symbolname='ERR_SOCK_CLOSED', modulename='SYSTEMMODULE', functionname='SocketConnect').data.Get(),'ERR_SOCK_CLOSED')
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='SocketConnect', modulename='SYSTEMMODULE').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='SocketConnect', modulename='SYSTEMMODULE').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' SocketConnect(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=SocketConnect, modulename='SYSTEMMODULE').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' SocketConnect(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='SocketConnect', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='SocketConnect', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' SocketConnect(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=SocketConnect, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' SocketConnect(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # Line ./default/standard.sys:325
        import socket
        # Line ./default/standard.sys:326
        SOCKET_CONNECTED = pyrapid.Symbols().GetSymbol("SOCKET_CONNECTED").data.Get()
        # Line ./default/standard.sys:328
        Socket = pyrapid.Symbols().GetSymbol("Socket").data
        # Line ./default/standard.sys:329
        Address = pyrapid.Symbols().GetSymbol("Address").data.Get()
        # Line ./default/standard.sys:330
        Port = pyrapid.Symbols().GetSymbol("Port").data.Get()
        # Line ./default/standard.sys:331
        s = Socket.Get()[1]
        # Line ./default/standard.sys:332
        if s is None:
        # Line ./default/standard.sys:333
                ERR_SOCK_CLOSED = pyrapid.Symbols().GetSymbol("ERR_SOCK_CLOSED").data.Get()
        # Line ./default/standard.sys:334
                raise pyrapid.RapidException(ERR_SOCK_CLOSED, "strang error: SocketConnect(%d) -"%(pyrapid.lineno(),))
        # Line ./default/standard.sys:336
        Time = None
        #StatementAST SocketConnect
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:337
                if (pyrapid.Symbols().IsInScope('Time')) :
                    pass
                    #StatementAST SocketConnect
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line ./default/standard.sys:338
                            if (( pyrapid.Symbols().GetSymbol(symbolname='Time', modulename='SYSTEMMODULE', functionname='SocketConnect').data.Get() != pyrapid.Symbols().GetSymbol(symbolname='WAIT_MAX', modulename='SYSTEMMODULE', functionname='SocketConnect').data.Get() )) :
                                pass
                                # Line ./default/standard.sys:339
                                Time = pyrapid.Symbols().GetSymbol("Time").data.Get()
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='SocketConnect', modulename='SYSTEMMODULE').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='SocketConnect', modulename='SYSTEMMODULE').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' SocketConnect(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=SocketConnect, modulename='SYSTEMMODULE').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' SocketConnect(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='SocketConnect', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='SocketConnect', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' SocketConnect(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=SocketConnect, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' SocketConnect(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # Line ./default/standard.sys:342
        s.settimeout(Time)
        # Line ./default/standard.sys:344
        try:
        # Line ./default/standard.sys:345
                s.connect( (Address, Port) )
        # Line ./default/standard.sys:346
        except socket.error:
        # Line ./default/standard.sys:347
                ERR_SOCK_CONNREF = pyrapid.Symbols().GetSymbol("ERR_SOCK_CONNREF").data.Get()
        # Line ./default/standard.sys:348
                raise pyrapid.RapidException(ERR_SOCK_CONNREF, "connection refused: SocketConnect(%d) -"%(pyrapid.lineno(),))
        # Line ./default/standard.sys:349
        except socket.timeout:
        # Line ./default/standard.sys:350
                ERR_SOCK_TIMEOUT = pyrapid.Symbols().GetSymbol("ERR_SOCK_TIMEOUT").data.Get()
        # Line ./default/standard.sys:351
                raise pyrapid.RapidException(ERR_SOCK_TIMEOUT, "connection timeout: SocketConnect(%d) -"%(pyrapid.lineno(),))
        # Line ./default/standard.sys:353
        Socket.Set( (SOCKET_CONNECTED, s) )
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('SocketConnect', pyrapid.Symbol.CreateProcedure(OrderedDict([('Socket', ('required', 'VAR', 'socketdev', 0, [])), ('Address', ('required', 'NORMAL', 'string', 0, [])), ('Port', ('required', 'NORMAL', 'num', 0, [])), ('Time', ('optional', 'NORMAL', 'num', 0, []))]), rapid_proc_SocketConnect, error_rapid_proc_SocketConnect, undo_rapid_proc_SocketConnect), 'SYSTEMMODULE')
del rapid_proc_SocketConnect
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:356
# Start Procedure Definition
def error_rapid_proc_SocketListen (local_exception):
    return 0
def undo_rapid_proc_SocketListen ():
    pass
def rapid_proc_SocketListen (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='SocketListen', invalue=local_args_scope):
        pass
        # data definitions
        # Line ./default/standard.sys:357
        import socket
        # Line ./default/standard.sys:358
        Socket = pyrapid.Symbols().GetSymbol("Socket").data
        # Line ./default/standard.sys:359
        s = Socket.Get()[1]
        # Line ./default/standard.sys:360
        s.listen( 1 )
        # Line ./default/standard.sys:361
        SOCKET_LISTENING = pyrapid.Symbols().GetSymbol("SOCKET_LISTENING").data.Get()
        # Line ./default/standard.sys:362
        Socket.Set( (SOCKET_LISTENING, s) )
        # stantments
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('SocketListen', pyrapid.Symbol.CreateProcedure(OrderedDict([('Socket', ('required', 'VAR', 'socketdev', 0, []))]), rapid_proc_SocketListen, error_rapid_proc_SocketListen, undo_rapid_proc_SocketListen), 'SYSTEMMODULE')
del rapid_proc_SocketListen
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:365
# Start Procedure Definition
def error_rapid_proc_SocketReceive (local_exception):
    return 0
def undo_rapid_proc_SocketReceive ():
    pass
def rapid_proc_SocketReceive (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='SocketReceive', invalue=local_args_scope):
        pass
        # data definitions
        # Line ./default/standard.sys:366
        # ## COMMENT:Exception: ERR_SOCK_CLOSED  ##
        # Line ./default/standard.sys:367
        # ## COMMENT:Exception: ERR_SOCK_TIMEOUT  ##
        # Line ./default/standard.sys:368
        import socket
        # Line ./default/standard.sys:369
        Socket = pyrapid.Symbols().GetSymbol("Socket").data
        # Line ./default/standard.sys:370
        s = Socket.Get()[1]
        # Line ./default/standard.sys:372
        Time = None
        # stantments
        #StatementAST SocketReceive
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:373
                if (pyrapid.Symbols().IsInScope('Time')) :
                    pass
                    #StatementAST SocketReceive
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line ./default/standard.sys:374
                            if (( pyrapid.Symbols().GetSymbol(symbolname='Time', modulename='SYSTEMMODULE', functionname='SocketReceive').data.Get() != pyrapid.Symbols().GetSymbol(symbolname='WAIT_MAX', modulename='SYSTEMMODULE', functionname='SocketReceive').data.Get() )) :
                                pass
                                # Line ./default/standard.sys:375
                                Time = pyrapid.Symbols().GetSymbol("Time").data.Get()
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='SocketReceive', modulename='SYSTEMMODULE').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='SocketReceive', modulename='SYSTEMMODULE').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' SocketReceive(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=SocketReceive, modulename='SYSTEMMODULE').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' SocketReceive(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='SocketReceive', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='SocketReceive', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' SocketReceive(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=SocketReceive, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' SocketReceive(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # Line ./default/standard.sys:378
        s.settimeout(Time)
        # Line ./default/standard.sys:380
        try:
        # Line ./default/standard.sys:381
            data = s.recv(1024)
        # Line ./default/standard.sys:382
        except socket.error:
        # Line ./default/standard.sys:383
                ERR_SOCK_CLOSED = pyrapid.Symbols().GetSymbol("ERR_SOCK_CLOSED").data.Get()
        # Line ./default/standard.sys:384
                #SOCKET_CLOSED = pyrapid.Symbols().GetSymbol("SOCKET_CLOSED").data.Get()
        # Line ./default/standard.sys:385
                #Socket.Set((SOCKET_CLOSED, None))
        # Line ./default/standard.sys:386
                raise pyrapid.RapidException(ERR_SOCK_CLOSED, "socket error: SocketReceive(%d) -"%(pyrapid.lineno(),))
        # Line ./default/standard.sys:387
        except socket.timeout:
        # Line ./default/standard.sys:388
                ERR_SOCK_TIMEOUT = pyrapid.Symbols().GetSymbol("ERR_SOCK_TIMEOUT").data.Get()
        # Line ./default/standard.sys:389
                raise pyrapid.RapidException(ERR_SOCK_TIMEOUT, "socket read timeout: SocketReceive(%d) -"%(pyrapid.lineno(),))
        #StatementAST SocketReceive
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:390
                if (pyrapid.Symbols().IsInScope('Str')) :
                    pass
                    # Line ./default/standard.sys:391
                    pyrapid.Symbols().GetSymbol("Str").data.Set(data)
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='SocketReceive', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='SocketReceive', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' SocketReceive(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=SocketReceive, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' SocketReceive(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('SocketReceive', pyrapid.Symbol.CreateProcedure(OrderedDict([('Socket', ('required', 'VAR', 'socketdev', 0, [])), ('Str', ('optional', 'VAR', 'string', 0, ['Data', 'RawData'])), ('RawData', ('optional', 'VAR', 'rawbytes', 0, ['Data', 'Str'])), ('Data', ('optional', 'VAR', 'byte', 1, ['RawData', 'Str'])), ('Time', ('optional', 'NORMAL', 'num', 0, []))]), rapid_proc_SocketReceive, error_rapid_proc_SocketReceive, undo_rapid_proc_SocketReceive), 'SYSTEMMODULE')
del rapid_proc_SocketReceive
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:395
# Start Procedure Definition
def error_rapid_proc_SocketSend (local_exception):
    return 0
def undo_rapid_proc_SocketSend ():
    pass
def rapid_proc_SocketSend (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='SocketSend', invalue=local_args_scope):
        pass
        # data definitions
        # Line ./default/standard.sys:396
        # ## COMMENT:Exception: ERR_SOCK_CLOSED  ##
        # Line ./default/standard.sys:397
        # ## COMMENT:The size of the data to send is limited to 1024 bytes. ##
        # Line ./default/standard.sys:398
        import socket
        # Line ./default/standard.sys:399
        Socket = pyrapid.Symbols().GetSymbol("Socket").data
        # Line ./default/standard.sys:400
        s = Socket.Get()[1]
        # stantments
        #StatementAST SocketSend
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:401
                if (pyrapid.Symbols().IsInScope('Str')) :
                    pass
                    # Line ./default/standard.sys:402
                    data =  pyrapid.Symbols().GetSymbol("Str").data.Get()
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='SocketSend', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='SocketSend', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' SocketSend(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=SocketSend, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' SocketSend(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # Line ./default/standard.sys:404
        try:
        # Line ./default/standard.sys:405
                s.send(data)
        # Line ./default/standard.sys:406
        except socket.error:
        # Line ./default/standard.sys:407
                ERR_SOCK_CLOSED = pyrapid.Symbols().GetSymbol("ERR_SOCK_CLOSED").data.Get()
        # Line ./default/standard.sys:408
                #SOCKET_CLOSED = pyrapid.Symbols().GetSymbol("SOCKET_CLOSED").data.Get()
        # Line ./default/standard.sys:409
                #Socket.Set((SOCKET_CLOSED, None))
        # Line ./default/standard.sys:410
                raise pyrapid.RapidException(ERR_SOCK_CLOSED, "socket error: SocketSend(%d) -"%(pyrapid.lineno(),))
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('SocketSend', pyrapid.Symbol.CreateProcedure(OrderedDict([('Socket', ('required', 'VAR', 'socketdev', 0, [])), ('Str', ('optional', 'NORMAL', 'string', 0, ['Data', 'RawData'])), ('RawData', ('optional', 'VAR', 'rawbytes', 0, ['Data', 'Str'])), ('Data', ('optional', 'NORMAL', 'byte', 1, ['RawData', 'Str'])), ('NoOfBytes', ('optional', 'NORMAL', 'num', 0, []))]), rapid_proc_SocketSend, error_rapid_proc_SocketSend, undo_rapid_proc_SocketSend), 'SYSTEMMODULE')
del rapid_proc_SocketSend
# End Procedure Definition
# end routine declaration
# Line ./default/standard.sys:413
# ## COMMENT:!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ##
############################# start routine declaration
# Line ./default/standard.sys:415
# Start Procedure Definition
def error_rapid_proc_WaitTime (local_exception):
    return 0
def undo_rapid_proc_WaitTime ():
    pass
def rapid_proc_WaitTime (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='WaitTime', invalue=local_args_scope):
        pass
        # data definitions
        # Line ./default/standard.sys:416
        import time
        # Line ./default/standard.sys:417
        time.sleep(pyrapid.Symbols().GetSymbol("Time").data.Get())
        # stantments
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('WaitTime', pyrapid.Symbol.CreateProcedure(OrderedDict([('InPos', ('switch', None, None, None, [])), ('Time', ('required', 'NORMAL', 'num', 0, []))]), rapid_proc_WaitTime, error_rapid_proc_WaitTime, undo_rapid_proc_WaitTime), 'SYSTEMMODULE')
del rapid_proc_WaitTime
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:420
# Start Procedure Definition
def error_rapid_proc_TPWrite (local_exception):
    return 0
def undo_rapid_proc_TPWrite ():
    pass
def rapid_proc_TPWrite (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='TPWrite', invalue=local_args_scope):
        pass
        # data definitions
        # Line ./default/standard.sys:421
        val = pyrapid.Symbols().GetSymbol("String").data.Get()
        # stantments
        #StatementAST TPWrite
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:423
                if (pyrapid.Symbols().IsInScope('Num')) :
                    pass
                    # Line ./default/standard.sys:424
                    val = val + " Num: " + str(pyrapid.Symbols().GetSymbol("Num").data.Get())
                # Line ./default/standard.sys:425
                elif (pyrapid.Symbols().IsInScope('Bool')) :
                    pass
                    # Line ./default/standard.sys:426
                    val = val + " Bool: " + str(pyrapid.Symbols().GetSymbol("Bool").data.Get())
                # Line ./default/standard.sys:427
                elif (pyrapid.Symbols().IsInScope('Pos')) :
                    pass
                    # Line ./default/standard.sys:428
                    val = val + " Pos: " + ",".join([ str(pyrapid.Symbols().GetSymbol("Pos").data.GetElem("x").Get()), 
                    # Line ./default/standard.sys:429
                                                     str(pyrapid.Symbols().GetSymbol("Pos").data.GetElem("y").Get()), 
                    # Line ./default/standard.sys:430
                                                     str(pyrapid.Symbols().GetSymbol("Pos").data.GetElem("z").Get())])
                # Line ./default/standard.sys:431
                elif (pyrapid.Symbols().IsInScope('Orient')) :
                    pass
                    # Line ./default/standard.sys:432
                    val = val + " Orient: " + ",".join([ str(pyrapid.Symbols().GetSymbol("Orient").data.GetElem("q1").Get()), 
                    # Line ./default/standard.sys:433
                                                        str(pyrapid.Symbols().GetSymbol("Orient").data.GetElem("q2").Get()), 
                    # Line ./default/standard.sys:434
                                                        str(pyrapid.Symbols().GetSymbol("Orient").data.GetElem("q3").Get()), 
                    # Line ./default/standard.sys:435
                                                        str(pyrapid.Symbols().GetSymbol("Orient").data.GetElem("q4").Get())])
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' TPWrite(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=TPWrite, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' TPWrite(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # Line ./default/standard.sys:437
        print( "'"+val+"'" )
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('TPWrite', pyrapid.Symbol.CreateProcedure(OrderedDict([('String', ('required', 'NORMAL', 'string', 0, [])), ('Num', ('optional', 'NORMAL', 'num', 0, ['Bool', 'Pos', 'Orient'])), ('Bool', ('optional', 'NORMAL', 'bool', 0, ['Num', 'Pos', 'Orient'])), ('Pos', ('optional', 'NORMAL', 'pos', 0, ['Num', 'Bool', 'Orient'])), ('Orient', ('optional', 'NORMAL', 'orient', 0, ['Num', 'Bool', 'Pos']))]), rapid_proc_TPWrite, error_rapid_proc_TPWrite, undo_rapid_proc_TPWrite), 'SYSTEMMODULE')
del rapid_proc_TPWrite
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:440
# Start Procedure Definition
def error_rapid_proc_ClkStart (local_exception):
    return 0
def undo_rapid_proc_ClkStart ():
    pass
def rapid_proc_ClkStart (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='ClkStart', invalue=local_args_scope):
        pass
        # data definitions
        # Line ./default/standard.sys:441
        import datetime
        # Line ./default/standard.sys:442
        val = pyrapid.Symbols().GetSymbol("Clock").data.Get()
        # Line ./default/standard.sys:443
        val = (val[0], None, True)
        # Line ./default/standard.sys:444
        pyrapid.Symbols().GetSymbol("Clock").data.Set(val)
        # stantments
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('ClkStart', pyrapid.Symbol.CreateProcedure(OrderedDict([('Clock', ('required', 'INOUT', 'clock', 0, []))]), rapid_proc_ClkStart, error_rapid_proc_ClkStart, undo_rapid_proc_ClkStart), 'SYSTEMMODULE')
del rapid_proc_ClkStart
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:447
# Start Procedure Definition
def error_rapid_proc_ClkStop (local_exception):
    return 0
def undo_rapid_proc_ClkStop ():
    pass
def rapid_proc_ClkStop (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='ClkStop', invalue=local_args_scope):
        pass
        # data definitions
        # Line ./default/standard.sys:448
        import datetime
        # Line ./default/standard.sys:449
        val = pyrapid.Symbols().GetSymbol("Clock").data.Get()
        # Line ./default/standard.sys:450
        val = (val[0], datetime.datetime.now(), False)
        # Line ./default/standard.sys:451
        pyrapid.Symbols().GetSymbol("Clock").data.Set(val)
        # stantments
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('ClkStop', pyrapid.Symbol.CreateProcedure(OrderedDict([('Clock', ('required', 'INOUT', 'clock', 0, []))]), rapid_proc_ClkStop, error_rapid_proc_ClkStop, undo_rapid_proc_ClkStop), 'SYSTEMMODULE')
del rapid_proc_ClkStop
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:454
# Start Procedure Definition
def error_rapid_proc_ClkReset (local_exception):
    return 0
def undo_rapid_proc_ClkReset ():
    pass
def rapid_proc_ClkReset (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='ClkReset', invalue=local_args_scope):
        pass
        # data definitions
        # Line ./default/standard.sys:455
        import datetime
        # Line ./default/standard.sys:456
        val = (datetime.datetime.now(), None, False)
        # Line ./default/standard.sys:457
        try:
        # Line ./default/standard.sys:458
            val = pyrapid.Symbols().GetSymbol("Clock").data.Get()
        # Line ./default/standard.sys:459
        except:
        # Line ./default/standard.sys:460
            pass
        # Line ./default/standard.sys:461
        val = (datetime.datetime.now(), val[1], val[2])
        # Line ./default/standard.sys:462
        pyrapid.Symbols().GetSymbol("Clock").data.Set(val)
        # stantments
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('ClkReset', pyrapid.Symbol.CreateProcedure(OrderedDict([('Clock', ('required', 'INOUT', 'clock', 0, []))]), rapid_proc_ClkReset, error_rapid_proc_ClkReset, undo_rapid_proc_ClkReset), 'SYSTEMMODULE')
del rapid_proc_ClkReset
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:465
# Start Function Definition
def error_rapid_func_ClkRead (local_exception):
    return 0
def undo_rapid_func_ClkRead ():
    pass
def rapid_func_ClkRead (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='ClkRead', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line ./default/standard.sys:466
        pyrapid.Symbols().AddScopeSym('ret', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='SYSTEMMODULE', functionname='ClkRead').data(None)))
        # end declaration
        # Line ./default/standard.sys:467
        import datetime
        # Line ./default/standard.sys:468
        val = pyrapid.Symbols().GetSymbol("Clock").data.Get()
        # Line ./default/standard.sys:469
        starttime = datetime.datetime.now()
        # Line ./default/standard.sys:470
        stoptime = datetime.datetime.now()
        # Line ./default/standard.sys:471
        if not(val[0] is None):
        # Line ./default/standard.sys:472
            starttime = val[0]
        # Line ./default/standard.sys:473
        if not(val[1] is None):
        # Line ./default/standard.sys:474
            stoptime = val[1]
        # Line ./default/standard.sys:475
        pyrapid.Symbols().GetSymbol("ret").data.Set( (stoptime-starttime).total_seconds() )
        # stantments
        #StatementAST ClkRead
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:476
                return ( pyrapid.Symbols().GetSymbol(symbolname='ret', modulename='SYSTEMMODULE', functionname='ClkRead').data.Get() )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ClkRead', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ClkRead', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ClkRead(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ClkRead, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ClkRead(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('ClkRead', pyrapid.Symbol.CreateFunction(OrderedDict([('Clock', ('required', 'NORMAL', 'clock', 0, []))]), pyrapid.Symbols().GetSymbol('num', 'SYSTEMMODULE', None), rapid_func_ClkRead, error_rapid_func_ClkRead, undo_rapid_func_ClkRead), 'SYSTEMMODULE')
del rapid_func_ClkRead
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:479
# Start Procedure Definition
def error_rapid_proc_UnLoad (local_exception):
    return 0
def undo_rapid_proc_UnLoad ():
    pass
def rapid_proc_UnLoad (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='UnLoad', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line ./default/standard.sys:480
        pyrapid.Symbols().AddScopeSym('ret', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='bool', modulename='SYSTEMMODULE', functionname='UnLoad').data(None)))
        # end declaration
        # stantments
        #StatementAST UnLoad
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='SYSTEMMODULE', functionname='UnLoad').data('UnLoad it is unsafe'))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='SYSTEMMODULE', functionname='UnLoad').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='UnLoad', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='UnLoad', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' UnLoad(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=UnLoad, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' UnLoad(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # Line ./default/standard.sys:482
        FilePath = pyrapid.Symbols().GetSymbol("FilePath").data.Get()
        # Line ./default/standard.sys:483
        FilePath = FilePath.split('/')[-1].split('.')[0].upper()
        # Line ./default/standard.sys:484
        ret = pyrapid.Symbols().UnLoadModule(FilePath)
        # Line ./default/standard.sys:485
        pyrapid.Symbols().GetSymbol("ret").data.Set( ret )
        #StatementAST UnLoad
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:486
                if (( pyrapid.Symbols().GetSymbol(symbolname='ret', modulename='SYSTEMMODULE', functionname='UnLoad').data.Get() == False )) :
                    pass
                    #StatementAST UnLoad
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line ./default/standard.sys:487
                            raise pyrapid.RapidException(pyrapid.Symbols().GetSymbol(symbolname='ERR_UNLOAD', modulename='SYSTEMMODULE', functionname='UnLoad').data.Get(),'ERR_UNLOAD')
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='UnLoad', modulename='SYSTEMMODULE').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='UnLoad', modulename='SYSTEMMODULE').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' UnLoad(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=UnLoad, modulename='SYSTEMMODULE').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' UnLoad(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='UnLoad', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='UnLoad', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' UnLoad(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=UnLoad, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' UnLoad(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('UnLoad', pyrapid.Symbol.CreateProcedure(OrderedDict([('FilePath', ('required', 'NORMAL', 'string', 0, []))]), rapid_proc_UnLoad, error_rapid_proc_UnLoad, undo_rapid_proc_UnLoad), 'SYSTEMMODULE')
del rapid_proc_UnLoad
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:492
# Start Procedure Definition
def error_rapid_proc_Load (local_exception):
    return 0
def undo_rapid_proc_Load ():
    pass
def rapid_proc_Load (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='Load', invalue=local_args_scope):
        pass
        # data definitions
        # stantments
        #StatementAST Load
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='SYSTEMMODULE', functionname='Load').data('Load it is unsafe'))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='SYSTEMMODULE', functionname='Load').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='Load', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='Load', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' Load(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=Load, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' Load(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # Line ./default/standard.sys:494
        FilePath = pyrapid.Symbols().GetSymbol("FilePath").data.Get()
        # Line ./default/standard.sys:495
        FilePath = FilePath.split('/')[-1].split('.')[0]
        # Line ./default/standard.sys:496
        import sys
        # Line ./default/standard.sys:497
        if sys.modules.has_key(FilePath):
        # Line ./default/standard.sys:498
            reload(sys.modules[FilePath])
        # Line ./default/standard.sys:499
        else:
        # Line ./default/standard.sys:500
            __import__(FilePath)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('Load', pyrapid.Symbol.CreateProcedure(OrderedDict([('Dynamic', ('switch', None, None, None, [])), ('FilePath', ('required', 'NORMAL', 'string', 0, [])), ('File', ('optional', 'NORMAL', 'string', 0, [])), ('CheckRef', ('switch', None, None, None, []))]), rapid_proc_Load, error_rapid_proc_Load, undo_rapid_proc_Load), 'SYSTEMMODULE')
del rapid_proc_Load
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:503
# Start Function Definition
def error_rapid_func_NumToStr (local_exception):
    return 0
def undo_rapid_func_NumToStr ():
    pass
def rapid_func_NumToStr (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='NumToStr', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line ./default/standard.sys:504
        pyrapid.Symbols().AddScopeSym('ret', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='SYSTEMMODULE', functionname='NumToStr').data(None)))
        # end declaration
        # Line ./default/standard.sys:505
        val = pyrapid.Symbols().GetSymbol("Val").data.Get()
        # Line ./default/standard.sys:506
        dec = pyrapid.Symbols().GetSymbol("Dec").data.Get()
        # stantments
        #StatementAST NumToStr
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:507
                if (pyrapid.Symbols().IsInScope('Exp')) :
                    pass
                    # Line ./default/standard.sys:508
                    val=("{0:.%dE}"%(dec,)).format(val)
                else:
                    # Line ./default/standard.sys:510
                    val=("{0:.%dF}"%(dec,)).format(val)
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='NumToStr', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='NumToStr', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' NumToStr(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=NumToStr, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' NumToStr(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # Line ./default/standard.sys:512
        pyrapid.Symbols().GetSymbol("ret").data.Set( val )
        #StatementAST NumToStr
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:513
                return ( pyrapid.Symbols().GetSymbol(symbolname='ret', modulename='SYSTEMMODULE', functionname='NumToStr').data.Get() )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='NumToStr', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='NumToStr', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' NumToStr(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=NumToStr, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' NumToStr(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('NumToStr', pyrapid.Symbol.CreateFunction(OrderedDict([('Val', ('required', 'NORMAL', 'num', 0, [])), ('Dec', ('required', 'NORMAL', 'num', 0, [])), ('Exp', ('switch', None, None, None, []))]), pyrapid.Symbols().GetSymbol('string', 'SYSTEMMODULE', None), rapid_func_NumToStr, error_rapid_func_NumToStr, undo_rapid_func_NumToStr), 'SYSTEMMODULE')
del rapid_func_NumToStr
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:516
# Start Procedure Definition
def error_rapid_proc_Incr (local_exception):
    return 0
def undo_rapid_proc_Incr ():
    pass
def rapid_proc_Incr (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='Incr', invalue=local_args_scope):
        pass
        # data definitions
        # stantments
        #StatementAST Incr
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='Name', modulename='SYSTEMMODULE', functionname='Incr').data.Set( ( pyrapid.Symbols().GetSymbol(symbolname='Name', modulename='SYSTEMMODULE', functionname='Incr').data.Get() + 1 ) ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='Incr', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='Incr', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' Incr(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=Incr, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' Incr(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('Incr', pyrapid.Symbol.CreateProcedure(OrderedDict([('Name', ('required', 'INOUT', 'num', 0, []))]), rapid_proc_Incr, error_rapid_proc_Incr, undo_rapid_proc_Incr), 'SYSTEMMODULE')
del rapid_proc_Incr
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:520
# Start Procedure Definition
def error_rapid_proc_Decr (local_exception):
    return 0
def undo_rapid_proc_Decr ():
    pass
def rapid_proc_Decr (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='Decr', invalue=local_args_scope):
        pass
        # data definitions
        # stantments
        #StatementAST Decr
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='Name', modulename='SYSTEMMODULE', functionname='Decr').data.Set( ( pyrapid.Symbols().GetSymbol(symbolname='Name', modulename='SYSTEMMODULE', functionname='Decr').data.Get() - 1 ) ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='Decr', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='Decr', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' Decr(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=Decr, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' Decr(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('Decr', pyrapid.Symbol.CreateProcedure(OrderedDict([('Name', ('required', 'INOUT', 'num', 0, []))]), rapid_proc_Decr, error_rapid_proc_Decr, undo_rapid_proc_Decr), 'SYSTEMMODULE')
del rapid_proc_Decr
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:524
# Start Procedure Definition
def error_rapid_proc_Add (local_exception):
    return 0
def undo_rapid_proc_Add ():
    pass
def rapid_proc_Add (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='Add', invalue=local_args_scope):
        pass
        # data definitions
        # stantments
        #StatementAST Add
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='Name', modulename='SYSTEMMODULE', functionname='Add').data.Set( ( pyrapid.Symbols().GetSymbol(symbolname='Name', modulename='SYSTEMMODULE', functionname='Add').data.Get() + pyrapid.Symbols().GetSymbol(symbolname='AddDvalue', modulename='SYSTEMMODULE', functionname='Add').data.Get() ) ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='Add', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='Add', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' Add(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=Add, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' Add(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('Add', pyrapid.Symbol.CreateProcedure(OrderedDict([('Name', ('required', 'INOUT', 'num', 0, [])), ('AddDvalue', ('required', 'NORMAL', 'num', 0, []))]), rapid_proc_Add, error_rapid_proc_Add, undo_rapid_proc_Add), 'SYSTEMMODULE')
del rapid_proc_Add
# End Procedure Definition
# end routine declaration
# Line ./default/standard.sys:528
# ## COMMENT:PROC Incr( \INOUT num Name | INOUT num Dname ) ##
# Line ./default/standard.sys:529
# ## COMMENT:    IF Present(Name) THEN ##
# Line ./default/standard.sys:530
# ## COMMENT:        Name := Name + 1; ##
# Line ./default/standard.sys:531
# ## COMMENT:    ENDIF ##
# Line ./default/standard.sys:532
# ## COMMENT:    IF Present(Dname) THEN ##
# Line ./default/standard.sys:533
# ## COMMENT:        Dname := Dname + 1; ##
# Line ./default/standard.sys:534
# ## COMMENT:    ENDIF ##
# Line ./default/standard.sys:535
# ## COMMENT:ENDPROC ##
# Line ./default/standard.sys:537
# ## COMMENT:PROC Decr( \INOUT num Name | INOUT num Dname ) ##
# Line ./default/standard.sys:538
# ## COMMENT:    IF Present(Name) THEN ##
# Line ./default/standard.sys:539
# ## COMMENT:        Name := Name - 1; ##
# Line ./default/standard.sys:540
# ## COMMENT:    ENDIF ##
# Line ./default/standard.sys:541
# ## COMMENT:    IF Present(Dname) THEN ##
# Line ./default/standard.sys:542
# ## COMMENT:        Dname := Dname - 1; ##
# Line ./default/standard.sys:543
# ## COMMENT:    ENDIF ##
# Line ./default/standard.sys:544
# ## COMMENT:ENDPROC ##
# Line ./default/standard.sys:546
# ## COMMENT:PROC Add( \INOUT num Name | INOUT num Dname, \num AddValue, | \num AddDvalue) ##
# Line ./default/standard.sys:547
# ## COMMENT:    IF Present(Name) THEN ##
# Line ./default/standard.sys:548
# ## COMMENT:        IF Present(AddValue) THEN ##
# Line ./default/standard.sys:549
# ## COMMENT:            Name := Name + AddValue; ##
# Line ./default/standard.sys:550
# ## COMMENT:        ENDIF ##
# Line ./default/standard.sys:551
# ## COMMENT:        IF Present(AddDvalue) THEN ##
# Line ./default/standard.sys:552
# ## COMMENT:            Name := Name + AddDvalue; ##
# Line ./default/standard.sys:553
# ## COMMENT:        ENDIF ##
# Line ./default/standard.sys:554
# ## COMMENT:    ENDIF ##
# Line ./default/standard.sys:555
# ## COMMENT:    IF Present(Dname) THEN ##
# Line ./default/standard.sys:556
# ## COMMENT:        IF Present(AddDvalue) THEN ##
# Line ./default/standard.sys:557
# ## COMMENT:            Dname := Dname + AddDvalue; ##
# Line ./default/standard.sys:558
# ## COMMENT:        ENDIF ##
# Line ./default/standard.sys:559
# ## COMMENT:        IF Present(AddValue) THEN ##
# Line ./default/standard.sys:560
# ## COMMENT:            Dname := Dname + AddValue; ##
# Line ./default/standard.sys:561
# ## COMMENT:        ENDIF ##
# Line ./default/standard.sys:562
# ## COMMENT:    ENDIF ##
# Line ./default/standard.sys:563
# ## COMMENT:ENDPROC ##
############################# start routine declaration
# Line ./default/standard.sys:565
# Start Procedure Definition
def error_rapid_proc_TryInit (local_exception):
    return 0
def undo_rapid_proc_TryInit ():
    pass
def rapid_proc_TryInit (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='TryInit', invalue=local_args_scope):
        pass
        # data definitions
        # Line ./default/standard.sys:566
        # ## COMMENT:!!!!!!!!!!!!!!!!TODO ##
        # stantments
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('TryInit', pyrapid.Symbol.CreateProcedure(OrderedDict([('DataObj', ('required', 'NORMAL', 'num', 0, []))]), rapid_proc_TryInit, error_rapid_proc_TryInit, undo_rapid_proc_TryInit), 'SYSTEMMODULE')
del rapid_proc_TryInit
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:569
# Start Function Definition
def error_rapid_func_Abs (local_exception):
    return 0
def undo_rapid_func_Abs ():
    pass
def rapid_func_Abs (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='Abs', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line ./default/standard.sys:570
        pyrapid.Symbols().AddScopeSym('ret', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='SYSTEMMODULE', functionname='Abs').data(None)))
        # end declaration
        # Line ./default/standard.sys:571
        val = pyrapid.Symbols().GetSymbol("Value").data.Get()
        # Line ./default/standard.sys:572
        val = abs(val)
        # Line ./default/standard.sys:573
        pyrapid.Symbols().GetSymbol("ret").data.Set( val )
        # stantments
        #StatementAST Abs
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:574
                return ( pyrapid.Symbols().GetSymbol(symbolname='ret', modulename='SYSTEMMODULE', functionname='Abs').data.Get() )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='Abs', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='Abs', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' Abs(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=Abs, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' Abs(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('Abs', pyrapid.Symbol.CreateFunction(OrderedDict([('Value', ('required', 'NORMAL', 'num', 0, []))]), pyrapid.Symbols().GetSymbol('num', 'SYSTEMMODULE', None), rapid_func_Abs, error_rapid_func_Abs, undo_rapid_func_Abs), 'SYSTEMMODULE')
del rapid_func_Abs
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:577
# Start Function Definition
def error_rapid_func_Round (local_exception):
    return 0
def undo_rapid_func_Round ():
    pass
def rapid_func_Round (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='Round', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line ./default/standard.sys:578
        pyrapid.Symbols().AddScopeSym('ret', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='SYSTEMMODULE', functionname='Round').data(None)))
        # end declaration
        # Line ./default/standard.sys:579
        val = pyrapid.Symbols().GetSymbol("Value").data.Get()
        # Line ./default/standard.sys:580
        val = round(val)
        # Line ./default/standard.sys:581
        pyrapid.Symbols().GetSymbol("ret").data.Set( val )
        # stantments
        #StatementAST Round
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:582
                return ( pyrapid.Symbols().GetSymbol(symbolname='ret', modulename='SYSTEMMODULE', functionname='Round').data.Get() )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='Round', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='Round', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' Round(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=Round, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' Round(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('Round', pyrapid.Symbol.CreateFunction(OrderedDict([('Value', ('required', 'NORMAL', 'num', 0, []))]), pyrapid.Symbols().GetSymbol('num', 'SYSTEMMODULE', None), rapid_func_Round, error_rapid_func_Round, undo_rapid_func_Round), 'SYSTEMMODULE')
del rapid_func_Round
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:585
# Start Function Definition
def error_rapid_func_Trunc (local_exception):
    return 0
def undo_rapid_func_Trunc ():
    pass
def rapid_func_Trunc (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='Trunc', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line ./default/standard.sys:586
        pyrapid.Symbols().AddScopeSym('ret', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='SYSTEMMODULE', functionname='Trunc').data(None)))
        # end declaration
        # Line ./default/standard.sys:587
        import math
        # Line ./default/standard.sys:588
        val = pyrapid.Symbols().GetSymbol("Value").data.Get()
        # Line ./default/standard.sys:589
        val = math.floor(val)
        # Line ./default/standard.sys:590
        pyrapid.Symbols().GetSymbol("ret").data.Set( val )
        # stantments
        #StatementAST Trunc
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:591
                return ( pyrapid.Symbols().GetSymbol(symbolname='ret', modulename='SYSTEMMODULE', functionname='Trunc').data.Get() )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='Trunc', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='Trunc', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' Trunc(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=Trunc, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' Trunc(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('Trunc', pyrapid.Symbol.CreateFunction(OrderedDict([('Value', ('required', 'NORMAL', 'num', 0, []))]), pyrapid.Symbols().GetSymbol('num', 'SYSTEMMODULE', None), rapid_func_Trunc, error_rapid_func_Trunc, undo_rapid_func_Trunc), 'SYSTEMMODULE')
del rapid_func_Trunc
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:594
# Start Function Definition
def error_rapid_func_Sqrt (local_exception):
    return 0
def undo_rapid_func_Sqrt ():
    pass
def rapid_func_Sqrt (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='Sqrt', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line ./default/standard.sys:595
        pyrapid.Symbols().AddScopeSym('ret', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='SYSTEMMODULE', functionname='Sqrt').data(None)))
        # end declaration
        # Line ./default/standard.sys:596
        import math
        # Line ./default/standard.sys:597
        val = pyrapid.Symbols().GetSymbol("Value").data.Get()
        # Line ./default/standard.sys:598
        val = math.sqrt(val)
        # Line ./default/standard.sys:599
        pyrapid.Symbols().GetSymbol("ret").data.Set( val )
        # stantments
        #StatementAST Sqrt
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:600
                return ( pyrapid.Symbols().GetSymbol(symbolname='ret', modulename='SYSTEMMODULE', functionname='Sqrt').data.Get() )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='Sqrt', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='Sqrt', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' Sqrt(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=Sqrt, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' Sqrt(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('Sqrt', pyrapid.Symbol.CreateFunction(OrderedDict([('Value', ('required', 'NORMAL', 'num', 0, []))]), pyrapid.Symbols().GetSymbol('num', 'SYSTEMMODULE', None), rapid_func_Sqrt, error_rapid_func_Sqrt, undo_rapid_func_Sqrt), 'SYSTEMMODULE')
del rapid_func_Sqrt
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:603
# Start Function Definition
def error_rapid_func_Exp (local_exception):
    return 0
def undo_rapid_func_Exp ():
    pass
def rapid_func_Exp (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='Exp', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line ./default/standard.sys:604
        pyrapid.Symbols().AddScopeSym('ret', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='SYSTEMMODULE', functionname='Exp').data(None)))
        # end declaration
        # Line ./default/standard.sys:605
        import math
        # Line ./default/standard.sys:606
        val = pyrapid.Symbols().GetSymbol("Value").data.Get()
        # Line ./default/standard.sys:607
        val = math.exp(val)
        # Line ./default/standard.sys:608
        pyrapid.Symbols().GetSymbol("ret").data.Set( val )
        # stantments
        #StatementAST Exp
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:609
                return ( pyrapid.Symbols().GetSymbol(symbolname='ret', modulename='SYSTEMMODULE', functionname='Exp').data.Get() )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='Exp', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='Exp', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' Exp(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=Exp, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' Exp(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('Exp', pyrapid.Symbol.CreateFunction(OrderedDict([('Value', ('required', 'NORMAL', 'num', 0, []))]), pyrapid.Symbols().GetSymbol('num', 'SYSTEMMODULE', None), rapid_func_Exp, error_rapid_func_Exp, undo_rapid_func_Exp), 'SYSTEMMODULE')
del rapid_func_Exp
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:612
# Start Function Definition
def error_rapid_func_Pow (local_exception):
    return 0
def undo_rapid_func_Pow ():
    pass
def rapid_func_Pow (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='Pow', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line ./default/standard.sys:613
        pyrapid.Symbols().AddScopeSym('ret', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='SYSTEMMODULE', functionname='Pow').data(None)))
        # end declaration
        # Line ./default/standard.sys:614
        # ## COMMENT:TODO non gestito errore ##
        # Line ./default/standard.sys:615
        import math
        # Line ./default/standard.sys:616
        base = pyrapid.Symbols().GetSymbol("Base").data.Get()
        # Line ./default/standard.sys:617
        exponent = pyrapid.Symbols().GetSymbol("Exponent").data.Get()
        # Line ./default/standard.sys:618
        val = math.pow(base, exponent)
        # Line ./default/standard.sys:619
        pyrapid.Symbols().GetSymbol("ret").data.Set( val )
        # stantments
        #StatementAST Pow
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:620
                return ( pyrapid.Symbols().GetSymbol(symbolname='ret', modulename='SYSTEMMODULE', functionname='Pow').data.Get() )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='Pow', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='Pow', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' Pow(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=Pow, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' Pow(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('Pow', pyrapid.Symbol.CreateFunction(OrderedDict([('Base', ('required', 'NORMAL', 'num', 0, [])), ('Exponent', ('required', 'NORMAL', 'num', 0, []))]), pyrapid.Symbols().GetSymbol('num', 'SYSTEMMODULE', None), rapid_func_Pow, error_rapid_func_Pow, undo_rapid_func_Pow), 'SYSTEMMODULE')
del rapid_func_Pow
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:623
# Start Function Definition
def error_rapid_func_StrMatch (local_exception):
    return 0
def undo_rapid_func_StrMatch ():
    pass
def rapid_func_StrMatch (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='StrMatch', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line ./default/standard.sys:624
        pyrapid.Symbols().AddScopeSym('ret', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='SYSTEMMODULE', functionname='StrMatch').data(None)))
        # end declaration
        # Line ./default/standard.sys:625
        Str = pyrapid.Symbols().GetSymbol("Str").data.Get()
        # Line ./default/standard.sys:626
        ChPos = pyrapid.Symbols().GetSymbol("ChPos").data.Get() - 1
        # Line ./default/standard.sys:627
        Pattern = pyrapid.Symbols().GetSymbol("Pattern").data.Get()
        # Line ./default/standard.sys:628
        ret = Str.find(Pattern, ChPos)
        # Line ./default/standard.sys:629
        if ret<0:
        # Line ./default/standard.sys:630
                ret = len(Str)
        # Line ./default/standard.sys:631
        ret += 1
        # Line ./default/standard.sys:632
        pyrapid.Symbols().GetSymbol("ret").data.Set( ret )
        # stantments
        #StatementAST StrMatch
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:633
                return ( pyrapid.Symbols().GetSymbol(symbolname='ret', modulename='SYSTEMMODULE', functionname='StrMatch').data.Get() )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='StrMatch', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='StrMatch', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' StrMatch(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=StrMatch, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' StrMatch(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('StrMatch', pyrapid.Symbol.CreateFunction(OrderedDict([('Str', ('required', 'NORMAL', 'string', 0, [])), ('ChPos', ('required', 'NORMAL', 'num', 0, [])), ('Pattern', ('required', 'NORMAL', 'string', 0, []))]), pyrapid.Symbols().GetSymbol('num', 'SYSTEMMODULE', None), rapid_func_StrMatch, error_rapid_func_StrMatch, undo_rapid_func_StrMatch), 'SYSTEMMODULE')
del rapid_func_StrMatch
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:636
# Start Function Definition
def error_rapid_func_StrLen (local_exception):
    return 0
def undo_rapid_func_StrLen ():
    pass
def rapid_func_StrLen (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='StrLen', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line ./default/standard.sys:637
        pyrapid.Symbols().AddScopeSym('ret', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='SYSTEMMODULE', functionname='StrLen').data(None)))
        # end declaration
        # Line ./default/standard.sys:638
        Str = pyrapid.Symbols().GetSymbol("Str").data.Get()
        # Line ./default/standard.sys:639
        pyrapid.Symbols().GetSymbol("ret").data.Set( len(Str) )
        # stantments
        #StatementAST StrLen
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:640
                return ( pyrapid.Symbols().GetSymbol(symbolname='ret', modulename='SYSTEMMODULE', functionname='StrLen').data.Get() )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='StrLen', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='StrLen', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' StrLen(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=StrLen, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' StrLen(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('StrLen', pyrapid.Symbol.CreateFunction(OrderedDict([('Str', ('required', 'NORMAL', 'string', 0, []))]), pyrapid.Symbols().GetSymbol('num', 'SYSTEMMODULE', None), rapid_func_StrLen, error_rapid_func_StrLen, undo_rapid_func_StrLen), 'SYSTEMMODULE')
del rapid_func_StrLen
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:643
# Start Function Definition
def error_rapid_func_StrFind (local_exception):
    return 0
def undo_rapid_func_StrFind ():
    pass
def rapid_func_StrFind (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='StrFind', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line ./default/standard.sys:644
        pyrapid.Symbols().AddScopeSym('ret', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='SYSTEMMODULE', functionname='StrFind').data(None)))
        # end declaration
        # Line ./default/standard.sys:645
        Str = pyrapid.Symbols().GetSymbol("Str").data.Get()
        # Line ./default/standard.sys:646
        ChPos = pyrapid.Symbols().GetSymbol("ChPos").data.Get()
        # Line ./default/standard.sys:647
        Set = pyrapid.Symbols().GetSymbol("Set").data.Get()
        # stantments
        #StatementAST StrFind
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:648
                if (pyrapid.Symbols().IsInScope('NotInSet')) :
                    pass
                    # Line ./default/standard.sys:649
                    NotInSet=True
                else:
                    # Line ./default/standard.sys:651
                    NotInSet=False
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='StrFind', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='StrFind', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' StrFind(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=StrFind, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' StrFind(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # Line ./default/standard.sys:653
        ret = len(Str)+1
        # Line ./default/standard.sys:654
        for i in range(int(ChPos)-1,len(Str)):
        # Line ./default/standard.sys:655
            if (Str[i] in Set) ^ NotInSet:
        # Line ./default/standard.sys:656
                ret = i+1
        # Line ./default/standard.sys:657
                break
        # Line ./default/standard.sys:658
        pyrapid.Symbols().GetSymbol("ret").data.Set( ret )
        #StatementAST StrFind
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:659
                return ( pyrapid.Symbols().GetSymbol(symbolname='ret', modulename='SYSTEMMODULE', functionname='StrFind').data.Get() )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='StrFind', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='StrFind', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' StrFind(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=StrFind, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' StrFind(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('StrFind', pyrapid.Symbol.CreateFunction(OrderedDict([('Str', ('required', 'NORMAL', 'string', 0, [])), ('ChPos', ('required', 'NORMAL', 'num', 0, [])), ('Set', ('required', 'NORMAL', 'string', 0, [])), ('NotInSet', ('switch', None, None, None, []))]), pyrapid.Symbols().GetSymbol('num', 'SYSTEMMODULE', None), rapid_func_StrFind, error_rapid_func_StrFind, undo_rapid_func_StrFind), 'SYSTEMMODULE')
del rapid_func_StrFind
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:662
# Start Function Definition
def error_rapid_func_StrPart (local_exception):
    return 0
def undo_rapid_func_StrPart ():
    pass
def rapid_func_StrPart (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='StrPart', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line ./default/standard.sys:663
        pyrapid.Symbols().AddScopeSym('ret', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='SYSTEMMODULE', functionname='StrPart').data(None)))
        # end declaration
        # Line ./default/standard.sys:664
        Str = pyrapid.Symbols().GetSymbol("Str").data.Get()
        # Line ./default/standard.sys:665
        ChPos = pyrapid.Symbols().GetSymbol("ChPos").data.Get()
        # Line ./default/standard.sys:666
        Len = pyrapid.Symbols().GetSymbol("Len").data.Get()
        # Line ./default/standard.sys:667
        ret = Str[(ChPos-1):(ChPos-1+Len)]
        # Line ./default/standard.sys:668
        pyrapid.Symbols().GetSymbol("ret").data.Set( ret )
        # stantments
        #StatementAST StrPart
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:669
                return ( pyrapid.Symbols().GetSymbol(symbolname='ret', modulename='SYSTEMMODULE', functionname='StrPart').data.Get() )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='StrPart', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='StrPart', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' StrPart(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=StrPart, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' StrPart(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('StrPart', pyrapid.Symbol.CreateFunction(OrderedDict([('Str', ('required', 'NORMAL', 'string', 0, [])), ('ChPos', ('required', 'NORMAL', 'num', 0, [])), ('Len', ('required', 'NORMAL', 'num', 0, []))]), pyrapid.Symbols().GetSymbol('string', 'SYSTEMMODULE', None), rapid_func_StrPart, error_rapid_func_StrPart, undo_rapid_func_StrPart), 'SYSTEMMODULE')
del rapid_func_StrPart
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:672
# Start Function Definition
def error_rapid_func_ValToStr (local_exception):
    return 0
def undo_rapid_func_ValToStr ():
    pass
def rapid_func_ValToStr (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='ValToStr', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line ./default/standard.sys:673
        pyrapid.Symbols().AddScopeSym('ret', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='SYSTEMMODULE', functionname='ValToStr').data(None)))
        # end declaration
        # Line ./default/standard.sys:674
        Val = pyrapid.Symbols().GetSymbol("Val").data.Get()
        # Line ./default/standard.sys:675
        pyrapid.Symbols().GetSymbol("ret").data.Set( str(Val) )
        # stantments
        #StatementAST ValToStr
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:676
                return ( pyrapid.Symbols().GetSymbol(symbolname='ret', modulename='SYSTEMMODULE', functionname='ValToStr').data.Get() )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ValToStr', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ValToStr', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ValToStr(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ValToStr, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ValToStr(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('ValToStr', pyrapid.Symbol.CreateFunction(OrderedDict([('Val', ('required', 'NORMAL', 'anytype', 0, []))]), pyrapid.Symbols().GetSymbol('string', 'SYSTEMMODULE', None), rapid_func_ValToStr, error_rapid_func_ValToStr, undo_rapid_func_ValToStr), 'SYSTEMMODULE')
del rapid_func_ValToStr
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line ./default/standard.sys:679
# Start Function Definition
def error_rapid_func_StrToVal (local_exception):
    return 0
def undo_rapid_func_StrToVal ():
    pass
def rapid_func_StrToVal (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SYSTEMMODULE', functionname='StrToVal', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line ./default/standard.sys:680
        pyrapid.Symbols().AddScopeSym('ret', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='bool', modulename='SYSTEMMODULE', functionname='StrToVal').data(None)))
        # end declaration
        # Line ./default/standard.sys:681
        from browse_rapid_ast import EvaluateRapidExpression
        # Line ./default/standard.sys:682
        import rapid_parser
        # Line ./default/standard.sys:683
        Str = pyrapid.Symbols().GetSymbol("Str").data.Get()
        # Line ./default/standard.sys:684
        try:
        # Line ./default/standard.sys:685
            Val = pyrapid.Symbols().GetSymbol("Val").data.Get()
        # Line ./default/standard.sys:686
        except:
        # Line ./default/standard.sys:687
            Val = None
        # Line ./default/standard.sys:688
        try:
        # Line ./default/standard.sys:689
            parser = rapid_parser.RAPIDParser(lex_optimize=True, yacc_debug=False, yacc_optimize=False, start_from='constant_expression')
        # Line ./default/standard.sys:690
            parser_ast = parser.parse(Str, "tmp", debuglevel=0)
        # Line ./default/standard.sys:691
            compute = EvaluateRapidExpression("sys", "sys")
        # Line ./default/standard.sys:692
            compute.visit(parser_ast)
        # Line ./default/standard.sys:693
            Val = compute.return_value
        # Line ./default/standard.sys:694
            ret = True
        # Line ./default/standard.sys:695
            pyrapid.Symbols().GetSymbol("Val").data.Set( Val )
        # Line ./default/standard.sys:696
        except:
        # Line ./default/standard.sys:697
            #import traceback
        # Line ./default/standard.sys:698
            #print traceback.format_exc()
        # Line ./default/standard.sys:699
            ret = False
        # Line ./default/standard.sys:700
        pyrapid.Symbols().GetSymbol("ret").data.Set( ret )
        # stantments
        #StatementAST StrToVal
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line ./default/standard.sys:701
                return ( pyrapid.Symbols().GetSymbol(symbolname='ret', modulename='SYSTEMMODULE', functionname='StrToVal').data.Get() )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='StrToVal', modulename='SYSTEMMODULE').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='StrToVal', modulename='SYSTEMMODULE').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' StrToVal(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=StrToVal, modulename='SYSTEMMODULE').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' StrToVal(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('StrToVal', pyrapid.Symbol.CreateFunction(OrderedDict([('Str', ('required', 'NORMAL', 'string', 0, [])), ('Val', ('required', 'INOUT', 'anytype', 0, []))]), pyrapid.Symbols().GetSymbol('bool', 'SYSTEMMODULE', None), rapid_func_StrToVal, error_rapid_func_StrToVal, undo_rapid_func_StrToVal), 'SYSTEMMODULE')
del rapid_func_StrToVal
# End Function Definition
# end routine declaration
##################################################################
pyrapid.Symbols().PopScope()
################### End module SYSTEMMODULE ####################
# Line Palletizer/settings.mod:1
################### Start module SETTINGS ####################
pyrapid.Symbols().PushScope('SETTINGS', None)
##################################################################
############################# start type definition
# Line Palletizer/settings.mod:2

class rapid_prodtype (pyrapid.rapid_struct):
    def __init__(self, val=None):
        pyrapid.rapid_struct.__init__(self, [ 'X','Y','Z','Weight','Type' ], [ pyrapid.Symbols().GetSymbol(symbolname='num', modulename='SETTINGS',functionname=None).data,pyrapid.Symbols().GetSymbol(symbolname='num', modulename='SETTINGS',functionname=None).data,pyrapid.Symbols().GetSymbol(symbolname='num', modulename='SETTINGS',functionname=None).data,pyrapid.Symbols().GetSymbol(symbolname='num', modulename='SETTINGS',functionname=None).data,pyrapid.Symbols().GetSymbol(symbolname='num', modulename='SETTINGS',functionname=None).data ])
        if not(val  is None):
            self.Set( val )
            
    def Set(self, val):
        if isinstance(val, type(self)):
            self.val = val.val
        else:
            pyrapid.rapid_struct.Set(self, val)

pyrapid.Symbols().AddGlobalSym('prodtype', pyrapid.Symbol.CreateDataType(rapid_prodtype))
del rapid_prodtype
# end type definition
############################# start declaration
# Line Palletizer/settings.mod:10
pyrapid.Symbols().AddGlobalSym('nQueueForSchema', pyrapid.Symbol.CreateConst(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='SETTINGS', functionname=None).data(2)))
# end declaration
############################# start declaration
# Line Palletizer/settings.mod:11
pyrapid.Symbols().AddGlobalSym('MAIN_QUEUE', pyrapid.Symbol.CreateConst(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='SETTINGS', functionname=None).data(2)))
# end declaration
############################# start declaration
# Line Palletizer/settings.mod:12
pyrapid.Symbols().AddGlobalSym('ORDER_QUEUE', pyrapid.Symbol.CreateConst(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='SETTINGS', functionname=None).data(1)))
# end declaration
############################# start declaration
# Line Palletizer/settings.mod:13
pyrapid.Symbols().AddGlobalSym('MAX_STEP', pyrapid.Symbol.CreateConst(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='SETTINGS', functionname=None).data(500)))
# end declaration
############################# start declaration
# Line Palletizer/settings.mod:17
pyrapid.Symbols().AddGlobalSym('nPROD_PICKLINE', pyrapid.Symbol.CreateConst(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='SETTINGS', functionname=None).data(2)))
# end declaration
# Line Palletizer/settings.mod:17
# ## COMMENT: number of product picking points ##
############################# start declaration
# Line Palletizer/settings.mod:18
pyrapid.Symbols().AddGlobalSym('nPLACELINE', pyrapid.Symbol.CreateConst(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='SETTINGS', functionname=None).data(2)))
# end declaration
# Line Palletizer/settings.mod:18
# ## COMMENT: number of place points ##
############################# start declaration
# Line Palletizer/settings.mod:20
pyrapid.Symbols().AddGlobalSym('nSHEET_PICKLINE', pyrapid.Symbol.CreateConst(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='SETTINGS', functionname=None).data(1)))
# end declaration
# Line Palletizer/settings.mod:20
# ## COMMENT: number of poit from piking sheets ##
############################# start declaration
# Line Palletizer/settings.mod:21
pyrapid.Symbols().AddGlobalSym('nPALLET_PICKLINE', pyrapid.Symbol.CreateConst(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='SETTINGS', functionname=None).data(0)))
# end declaration
# Line Palletizer/settings.mod:21
# ## COMMENT: number of poit from piking pallets ##
# Line Palletizer/settings.mod:24
# ## COMMENT:!! SCHEMAS ##
# Line Palletizer/settings.mod:26
# ## COMMENT: actionType Elements ##
# Line Palletizer/settings.mod:27
# ## COMMENT:VAR string r_ActionType_Name{nPLACELINE, nQueueForSchema, MAX_STEP}; ##
# Line Palletizer/settings.mod:30
# ## COMMENT: schemaType Elements ##
# Line Palletizer/settings.mod:31
# ## COMMENT:VAR bool r_SchemaType_Valid{nPLACELINE}; ##
# Line Palletizer/settings.mod:32
# ## COMMENT:VAR num r_SchemaType_NSteps{nPLACELINE, nQueueForSchema}; ##
# Line Palletizer/settings.mod:33
# ## COMMENT:VAR num r_SchemaType_RunSteps{nPLACELINE, nQueueForSchema}; ##
# Line Palletizer/settings.mod:34
# ## COMMENT:VAR prodtype r_ProductType{nPLACELINE}; ##
# Line Palletizer/settings.mod:35
# ## COMMENT:VAR prodtype r_PalletType{nPLACELINE}; ##
# Line Palletizer/settings.mod:36
# ## COMMENT:VAR prodtype r_SheetType{nPLACELINE}; ##
# Line Palletizer/settings.mod:37
# ## COMMENT:VAR num r_GripperType{nPLACELINE}; ##
# Line Palletizer/settings.mod:38
# ## COMMENT:VAR num r_TakeLine{nPLACELINE}; ##
# Line Palletizer/settings.mod:39
# ## COMMENT: ##
# Line Palletizer/settings.mod:40
# ## COMMENT:VAR bool r_QueuePaused{nPLACELINE, nQueueForSchema}; ##
# Line Palletizer/settings.mod:41
# ## COMMENT: ##
# Line Palletizer/settings.mod:42
# ## COMMENT: ##
# Line Palletizer/settings.mod:43
# ## COMMENT:VAR bool r_PalletExiting{nPLACELINE}; ##
##################################################################
pyrapid.Symbols().PopScope()
################### End module SETTINGS ####################
# Line Palletizer/gloadschema.mod:1
################### Start module GLOADSCHEMA ####################
pyrapid.Symbols().PushScope('GLOADSCHEMA', None)
##################################################################
# Line Palletizer/gloadschema.mod:3
# ## COMMENT: actionType Elements ##
############################# start declaration
# Line Palletizer/gloadschema.mod:4
pyrapid.Symbols().AddGlobalSym('ActionType_Name', pyrapid.Symbol.CreateVar( pyrapid.rapid_array([2, 500], pyrapid.Symbols().GetSymbol(symbolname='string', modulename='GLOADSCHEMA', functionname=None).data, None) ))
# end declaration
# Line Palletizer/gloadschema.mod:7
# ## COMMENT: schemaType Elements ##
############################# start declaration
# Line Palletizer/gloadschema.mod:8
pyrapid.Symbols().AddGlobalSym('SchemaType_Valid', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='bool', modulename='GLOADSCHEMA', functionname=None).data(None)))
# end declaration
# Line Palletizer/gloadschema.mod:8
# ## COMMENT: True if The Schema is valid ##
############################# start declaration
# Line Palletizer/gloadschema.mod:9
pyrapid.Symbols().AddGlobalSym('SchemaType_NSteps', pyrapid.Symbol.CreateVar( pyrapid.rapid_array([2], pyrapid.Symbols().GetSymbol(symbolname='num', modulename='GLOADSCHEMA', functionname=None).data, None) ))
# end declaration
# Line Palletizer/gloadschema.mod:9
# ## COMMENT: Number of Step for cicle ##
############################# start declaration
# Line Palletizer/gloadschema.mod:10
pyrapid.Symbols().AddGlobalSym('SchemaType_RunSteps', pyrapid.Symbol.CreateVar( pyrapid.rapid_array([2], pyrapid.Symbols().GetSymbol(symbolname='num', modulename='GLOADSCHEMA', functionname=None).data, None) ))
# end declaration
# Line Palletizer/gloadschema.mod:10
# ## COMMENT: if >0 Step from Start  ##
############################# start declaration
# Line Palletizer/gloadschema.mod:12
pyrapid.Symbols().AddGlobalSym('TakeLine', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='GLOADSCHEMA', functionname=None).data(None)))
# end declaration
############################# start declaration
# Line Palletizer/gloadschema.mod:13
pyrapid.Symbols().AddGlobalSym('ProductType', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='prodtype', modulename='GLOADSCHEMA', functionname=None).data(None)))
# end declaration
############################# start declaration
# Line Palletizer/gloadschema.mod:14
pyrapid.Symbols().AddGlobalSym('PalletType', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='prodtype', modulename='GLOADSCHEMA', functionname=None).data(None)))
# end declaration
############################# start declaration
# Line Palletizer/gloadschema.mod:15
pyrapid.Symbols().AddGlobalSym('SheetType', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='prodtype', modulename='GLOADSCHEMA', functionname=None).data(None)))
# end declaration
############################# start declaration
# Line Palletizer/gloadschema.mod:16
pyrapid.Symbols().AddGlobalSym('GripperType', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='GLOADSCHEMA', functionname=None).data(None)))
# end declaration
##################################################################
pyrapid.Symbols().PopScope()
################### End module GLOADSCHEMA ####################
# Line Palletizer/schema.mod:1
################### Start module SCHEMA ####################
pyrapid.Symbols().PushScope('SCHEMA', None)
##################################################################
############################# start routine declaration
# Line Palletizer/schema.mod:2
# Start Procedure Definition
def error_rapid_proc_INIT_SCHEMA (local_exception):
    return 0
def undo_rapid_proc_INIT_SCHEMA ():
    pass
def rapid_proc_INIT_SCHEMA (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='SCHEMA', functionname='INIT_SCHEMA', invalue=local_args_scope):
        pass
        # data definitions
        # stantments
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='SchemaType_Valid', modulename='SCHEMA', functionname='INIT_SCHEMA').data.Set( True ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='ProductType', modulename='SCHEMA', functionname='INIT_SCHEMA').data.GetElem('X').Set( 100 ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='ProductType', modulename='SCHEMA', functionname='INIT_SCHEMA').data.GetElem('Y').Set( 100 ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='ProductType', modulename='SCHEMA', functionname='INIT_SCHEMA').data.GetElem('Z').Set( 100 ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='ProductType', modulename='SCHEMA', functionname='INIT_SCHEMA').data.GetElem('Weight').Set( 1000 ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='ProductType', modulename='SCHEMA', functionname='INIT_SCHEMA').data.GetElem('Type').Set( 1 ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='PalletType', modulename='SCHEMA', functionname='INIT_SCHEMA').data.GetElem('X').Set( 1200 ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='PalletType', modulename='SCHEMA', functionname='INIT_SCHEMA').data.GetElem('Y').Set( 800 ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='PalletType', modulename='SCHEMA', functionname='INIT_SCHEMA').data.GetElem('Z').Set( 150 ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='PalletType', modulename='SCHEMA', functionname='INIT_SCHEMA').data.GetElem('Weight').Set( 3000 ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='PalletType', modulename='SCHEMA', functionname='INIT_SCHEMA').data.GetElem('Type').Set( 1 ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='SheetType', modulename='SCHEMA', functionname='INIT_SCHEMA').data.GetElem('X').Set( 1200 ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='SheetType', modulename='SCHEMA', functionname='INIT_SCHEMA').data.GetElem('Y').Set( 800 ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='SheetType', modulename='SCHEMA', functionname='INIT_SCHEMA').data.GetElem('Z').Set( 3 ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='SheetType', modulename='SCHEMA', functionname='INIT_SCHEMA').data.GetElem('Weight').Set( 100 ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='SheetType', modulename='SCHEMA', functionname='INIT_SCHEMA').data.GetElem('Type').Set( 1 ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='GripperType', modulename='SCHEMA', functionname='INIT_SCHEMA').data.Set( 1 ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='TakeLine', modulename='SCHEMA', functionname='INIT_SCHEMA').data.Set( 1 ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='SchemaType_NSteps', modulename='SCHEMA', functionname='INIT_SCHEMA').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='ORDER_QUEUE', modulename='SCHEMA', functionname='INIT_SCHEMA')] ).Set( 2 ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='SchemaType_NSteps', modulename='SCHEMA', functionname='INIT_SCHEMA').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='MAIN_QUEUE', modulename='SCHEMA', functionname='INIT_SCHEMA')] ).Set( 9 ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='SchemaType_RunSteps', modulename='SCHEMA', functionname='INIT_SCHEMA').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='ORDER_QUEUE', modulename='SCHEMA', functionname='INIT_SCHEMA')] ).Set( 1 ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='SchemaType_RunSteps', modulename='SCHEMA', functionname='INIT_SCHEMA').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='MAIN_QUEUE', modulename='SCHEMA', functionname='INIT_SCHEMA')] ).Set( 1 ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # Line Palletizer/schema.mod:34
        # ## COMMENT:Possible action ##
        # Line Palletizer/schema.mod:35
        # ## COMMENT: OrderProd <number of product> <disposition> ##
        # Line Palletizer/schema.mod:36
        # ## COMMENT: StopQueue <queue> ##
        # Line Palletizer/schema.mod:37
        # ## COMMENT: StartQueue <queue> ##
        # Line Palletizer/schema.mod:38
        # ## COMMENT: TakeProduct x y z rot ##
        # Line Palletizer/schema.mod:39
        # ## COMMENT: PlaceProduct type x x1 y y1 z z1 rot x x1 y y1 z z1 rot ##
        # Line Palletizer/schema.mod:40
        # ## COMMENT: OrderPallet ##
        # Line Palletizer/schema.mod:41
        # ## COMMENT: TakePallet ##
        # Line Palletizer/schema.mod:42
        # ## COMMENT: PlacePallet ##
        # Line Palletizer/schema.mod:43
        # ## COMMENT: ExitPallet ##
        # Line Palletizer/schema.mod:44
        # ## COMMENT: TakeSheet ##
        # Line Palletizer/schema.mod:45
        # ## COMMENT: PlaceSheet ##
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='ActionType_Name', modulename='SCHEMA', functionname='INIT_SCHEMA').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='ORDER_QUEUE', modulename='SCHEMA', functionname='INIT_SCHEMA'), 1] ).Set( 'OrderProd [ 3, 2 ]' ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='ActionType_Name', modulename='SCHEMA', functionname='INIT_SCHEMA').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='ORDER_QUEUE', modulename='SCHEMA', functionname='INIT_SCHEMA'), 2] ).Set( 'StopQueue 1' ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='ActionType_Name', modulename='SCHEMA', functionname='INIT_SCHEMA').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='MAIN_QUEUE', modulename='SCHEMA', functionname='INIT_SCHEMA'), 1] ).Set( 'ExitPallet' ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='ActionType_Name', modulename='SCHEMA', functionname='INIT_SCHEMA').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='MAIN_QUEUE', modulename='SCHEMA', functionname='INIT_SCHEMA'), 2] ).Set( 'OrderPallet' ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='ActionType_Name', modulename='SCHEMA', functionname='INIT_SCHEMA').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='MAIN_QUEUE', modulename='SCHEMA', functionname='INIT_SCHEMA'), 3] ).Set( 'TakePallet' ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='ActionType_Name', modulename='SCHEMA', functionname='INIT_SCHEMA').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='MAIN_QUEUE', modulename='SCHEMA', functionname='INIT_SCHEMA'), 4] ).Set( 'PlacePallet' ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='ActionType_Name', modulename='SCHEMA', functionname='INIT_SCHEMA').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='MAIN_QUEUE', modulename='SCHEMA', functionname='INIT_SCHEMA'), 5] ).Set( 'StartQueue 1' ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='ActionType_Name', modulename='SCHEMA', functionname='INIT_SCHEMA').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='MAIN_QUEUE', modulename='SCHEMA', functionname='INIT_SCHEMA'), 6] ).Set( 'TakeProduct [ 0, 0, 0, 0 ]' ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='ActionType_Name', modulename='SCHEMA', functionname='INIT_SCHEMA').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='MAIN_QUEUE', modulename='SCHEMA', functionname='INIT_SCHEMA'), 7] ).Set( 'StartQueue 1' ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='ActionType_Name', modulename='SCHEMA', functionname='INIT_SCHEMA').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='MAIN_QUEUE', modulename='SCHEMA', functionname='INIT_SCHEMA'), 8] ).Set( 'PlaceProduct [ 1, 10, 1, 20, 2, 30, 3, 90, 0, 0, 0, 0, 0, 0, 0]' ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST INIT_SCHEMA
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='ActionType_Name', modulename='SCHEMA', functionname='INIT_SCHEMA').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='MAIN_QUEUE', modulename='SCHEMA', functionname='INIT_SCHEMA'), 9] ).Set( 'ExitPallet' ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=INIT_SCHEMA, modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('INIT_SCHEMA', pyrapid.Symbol.CreateProcedure(OrderedDict(), rapid_proc_INIT_SCHEMA, error_rapid_proc_INIT_SCHEMA, undo_rapid_proc_INIT_SCHEMA), 'SCHEMA')
del rapid_proc_INIT_SCHEMA
# End Procedure Definition
# end routine declaration
##################################################################
pyrapid.Symbols().PopScope()
################### End module SCHEMA ####################
# Line Palletizer/maintask.mod:1
################### Start module MAINTASK ####################
pyrapid.Symbols().PushScope('MAINTASK', None)
##################################################################
# Line Palletizer/maintask.mod:2
# ## COMMENT:python rapid2py.py -i Palletizer/schema.mod -s -f schema.py ##
# Line Palletizer/maintask.mod:3
# ## COMMENT:python rapid2py.py -e MAIN -i Palletizer/settings.mod -i Palletizer/gloadschema.mod -i Palletizer/schema.mod -i Palletizer/maintask.mod -f pallettizer.py -r ##
# Line Palletizer/maintask.mod:4
# ## COMMENT: ##
# Line Palletizer/maintask.mod:5
# ## COMMENT: ##
# Line Palletizer/maintask.mod:7
# ## COMMENT: this type contain the action that has to be done ##
# Line Palletizer/maintask.mod:8
# ## COMMENT: if nProdLine=-1 or nQueue=-1 or nStep=-1 means nothing to do ##
############################# start type definition
# Line Palletizer/maintask.mod:9

class rapid_todoType (pyrapid.rapid_struct):
    def __init__(self, val=None):
        pyrapid.rapid_struct.__init__(self, [ 'nProdLine','nQueue','nStep' ], [ pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK',functionname=None).data,pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK',functionname=None).data,pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK',functionname=None).data ])
        if not(val  is None):
            self.Set( val )
            
    def Set(self, val):
        if isinstance(val, type(self)):
            self.val = val.val
        else:
            pyrapid.rapid_struct.Set(self, val)

pyrapid.Symbols().AddModuleSym('MAINTASK', 'todoType', pyrapid.Symbol.CreateDataType(rapid_todoType))
del rapid_todoType
# end type definition
############################# start type definition
# Line Palletizer/maintask.mod:15

class rapid_TakeProdType (pyrapid.rapid_struct):
    def __init__(self, val=None):
        pyrapid.rapid_struct.__init__(self, [ 'x','y','z','rot' ], [ pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK',functionname=None).data,pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK',functionname=None).data,pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK',functionname=None).data,pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK',functionname=None).data ])
        if not(val  is None):
            self.Set( val )
            
    def Set(self, val):
        if isinstance(val, type(self)):
            self.val = val.val
        else:
            pyrapid.rapid_struct.Set(self, val)

pyrapid.Symbols().AddModuleSym('MAINTASK', 'TakeProdType', pyrapid.Symbol.CreateDataType(rapid_TakeProdType))
del rapid_TakeProdType
# end type definition
############################# start type definition
# Line Palletizer/maintask.mod:22

class rapid_PlateProdType (pyrapid.rapid_struct):
    def __init__(self, val=None):
        pyrapid.rapid_struct.__init__(self, [ 'type','x1','acc_x1','y1','acc_y1','z1','acc_z1','rot1','x2','acc_x2','y2','acc_y2','z2','acc_z2','rot2' ], [ pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK',functionname=None).data,pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK',functionname=None).data,pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK',functionname=None).data,pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK',functionname=None).data,pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK',functionname=None).data,pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK',functionname=None).data,pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK',functionname=None).data,pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK',functionname=None).data,pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK',functionname=None).data,pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK',functionname=None).data,pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK',functionname=None).data,pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK',functionname=None).data,pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK',functionname=None).data,pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK',functionname=None).data,pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK',functionname=None).data ])
        if not(val  is None):
            self.Set( val )
            
    def Set(self, val):
        if isinstance(val, type(self)):
            self.val = val.val
        else:
            pyrapid.rapid_struct.Set(self, val)

pyrapid.Symbols().AddModuleSym('MAINTASK', 'PlateProdType', pyrapid.Symbol.CreateDataType(rapid_PlateProdType))
del rapid_PlateProdType
# end type definition
# Line Palletizer/maintask.mod:41
# ## COMMENT:  GLOBAL VARIABLE ##
############################# start declaration
# Line Palletizer/maintask.mod:42
pyrapid.Symbols().AddGlobalSym('bContinueExecution', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='bool', modulename='MAINTASK', functionname=None).data(True)))
# end declaration
# Line Palletizer/maintask.mod:44
# ## COMMENT:  GLOBAL VARIABLE USED IN AUTOMATIC ##
############################# start declaration
# Line Palletizer/maintask.mod:46
pyrapid.Symbols().AddGlobalSym('A_bForceLoadSchemas', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='bool', modulename='MAINTASK', functionname=None).data(False)))
# end declaration
# Line Palletizer/maintask.mod:48
# ## COMMENT:  GLOBAL VARIABLE USED IN MANUAL ##
############################# start routine declaration
# Line Palletizer/maintask.mod:51
# Start Function Definition
def error_rapid_func_HasToRun (local_exception):
    return 0
def undo_rapid_func_HasToRun ():
    pass
def rapid_func_HasToRun (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='HasToRun', invalue=local_args_scope):
        pass
        # data definitions
        # stantments
        #StatementAST HasToRun
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:52
                return ( pyrapid.Symbols().GetSymbol(symbolname='bContinueExecution', modulename='MAINTASK', functionname='HasToRun').data.Get() )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='HasToRun', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='HasToRun', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' HasToRun(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=HasToRun, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' HasToRun(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('HasToRun', pyrapid.Symbol.CreateFunction(OrderedDict(), pyrapid.Symbols().GetSymbol('bool', 'MAINTASK', None), rapid_func_HasToRun, error_rapid_func_HasToRun, undo_rapid_func_HasToRun), 'MAINTASK')
del rapid_func_HasToRun
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:55
# Start Function Definition
def error_rapid_func_IsAutomatic (local_exception):
    return 0
def undo_rapid_func_IsAutomatic ():
    pass
def rapid_func_IsAutomatic (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='IsAutomatic', invalue=local_args_scope):
        pass
        # data definitions
        # stantments
        #StatementAST IsAutomatic
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:56
                return ( True )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsAutomatic', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsAutomatic', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' IsAutomatic(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsAutomatic, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' IsAutomatic(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('IsAutomatic', pyrapid.Symbol.CreateFunction(OrderedDict(), pyrapid.Symbols().GetSymbol('bool', 'MAINTASK', None), rapid_func_IsAutomatic, error_rapid_func_IsAutomatic, undo_rapid_func_IsAutomatic), 'MAINTASK')
del rapid_func_IsAutomatic
# End Function Definition
# end routine declaration
# Line Palletizer/maintask.mod:59
# ## COMMENT: robot go in parking position and waith to arrive there ##
############################# start routine declaration
# Line Palletizer/maintask.mod:60
# Start Procedure Definition
def error_rapid_proc_GoHome (local_exception):
    return 0
def undo_rapid_proc_GoHome ():
    pass
def rapid_proc_GoHome (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='GoHome', invalue=local_args_scope):
        pass
        # data definitions
        # stantments
        #StatementAST GoHome
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='GoHome').data('GO TO PARK'))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='GoHome').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='GoHome', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='GoHome', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' GoHome(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=GoHome, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' GoHome(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # Line Palletizer/maintask.mod:62
        # ## COMMENT:todo ##
        #StatementAST GoHome
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure WaitTime
                parameters_actual = OrderedDict()
                parameters_actual['Time'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='GoHome').data(1))
                pyrapid.Symbols().GetSymbol(symbolname='WaitTime', modulename='MAINTASK', functionname='GoHome').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='GoHome', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='GoHome', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' GoHome(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=GoHome, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' GoHome(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('GoHome', pyrapid.Symbol.CreateProcedure(OrderedDict(), rapid_proc_GoHome, error_rapid_proc_GoHome, undo_rapid_proc_GoHome), 'MAINTASK')
del rapid_proc_GoHome
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:66
# Start Function Definition
def error_rapid_func_IsPalletExiting (local_exception):
    return 0
def undo_rapid_func_IsPalletExiting ():
    pass
def rapid_func_IsPalletExiting (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='IsPalletExiting', invalue=local_args_scope):
        pass
        # data definitions
        # stantments
        #StatementAST IsPalletExiting
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:67
                return ( pyrapid.Symbols().GetSymbol(symbolname='r_PalletExiting', modulename='MAINTASK', functionname='IsPalletExiting').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='nProdLine', modulename='MAINTASK', functionname='IsPalletExiting')] ).Get() )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPalletExiting', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPalletExiting', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' IsPalletExiting(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsPalletExiting, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' IsPalletExiting(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('IsPalletExiting', pyrapid.Symbol.CreateFunction(OrderedDict([('nProdLine', ('required', 'NORMAL', 'num', 0, []))]), pyrapid.Symbols().GetSymbol('bool', 'MAINTASK', None), rapid_func_IsPalletExiting, error_rapid_func_IsPalletExiting, undo_rapid_func_IsPalletExiting), 'MAINTASK')
del rapid_func_IsPalletExiting
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:70
# Start Procedure Definition
def error_rapid_proc_SetPalletExiting (local_exception):
    return 0
def undo_rapid_proc_SetPalletExiting ():
    pass
def rapid_proc_SetPalletExiting (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='SetPalletExiting', invalue=local_args_scope):
        pass
        # data definitions
        # stantments
        #StatementAST SetPalletExiting
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='r_PalletExiting', modulename='MAINTASK', functionname='SetPalletExiting').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='nProdLine', modulename='MAINTASK', functionname='SetPalletExiting')] ).Set( True ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='SetPalletExiting', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='SetPalletExiting', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' SetPalletExiting(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=SetPalletExiting, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' SetPalletExiting(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('SetPalletExiting', pyrapid.Symbol.CreateProcedure(OrderedDict([('nProdLine', ('required', 'NORMAL', 'num', 0, []))]), rapid_proc_SetPalletExiting, error_rapid_proc_SetPalletExiting, undo_rapid_proc_SetPalletExiting), 'MAINTASK')
del rapid_proc_SetPalletExiting
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:74
# Start Procedure Definition
def error_rapid_proc_ResetPalletExiting (local_exception):
    return 0
def undo_rapid_proc_ResetPalletExiting ():
    pass
def rapid_proc_ResetPalletExiting (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='ResetPalletExiting', invalue=local_args_scope):
        pass
        # data definitions
        # stantments
        #StatementAST ResetPalletExiting
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='r_PalletExiting', modulename='MAINTASK', functionname='ResetPalletExiting').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='nProdLine', modulename='MAINTASK', functionname='ResetPalletExiting')] ).Set( False ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ResetPalletExiting', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ResetPalletExiting', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ResetPalletExiting(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ResetPalletExiting, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ResetPalletExiting(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('ResetPalletExiting', pyrapid.Symbol.CreateProcedure(OrderedDict([('nProdLine', ('required', 'NORMAL', 'num', 0, []))]), rapid_proc_ResetPalletExiting, error_rapid_proc_ResetPalletExiting, undo_rapid_proc_ResetPalletExiting), 'MAINTASK')
del rapid_proc_ResetPalletExiting
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:78
# Start Function Definition
def error_rapid_func_IsTakeProduct (local_exception):
    return 0
def undo_rapid_func_IsTakeProduct ():
    pass
def rapid_func_IsTakeProduct (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='IsTakeProduct', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line Palletizer/maintask.mod:79
        pyrapid.Symbols().AddScopeSym('spacepos', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='IsTakeProduct').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:80
        pyrapid.Symbols().AddScopeSym('basecommand', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsTakeProduct').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:81
        pyrapid.Symbols().AddScopeSym('tmp', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsTakeProduct').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:82
        pyrapid.Symbols().AddScopeSym('prod', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='PlateProdType', modulename='MAINTASK', functionname='IsTakeProduct').data([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:83
        pyrapid.Symbols().AddScopeSym('command_to_find', pyrapid.Symbol.CreateConst(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsTakeProduct').data('PlaceProduct')))
        # end declaration
        # stantments
        #StatementAST IsTakeProduct
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='spacepos', modulename='MAINTASK', functionname='IsTakeProduct').data.Set( pyrapid.Symbols().GetSymbol(symbolname='StrFind', modulename='MAINTASK', functionname='IsTakeProduct').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsTakeProduct').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='IsTakeProduct').data.Get())),'ChPos':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='IsTakeProduct').data(1)),'Set':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsTakeProduct').data(' '))} ) ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakeProduct', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakeProduct', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' IsTakeProduct(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsTakeProduct, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' IsTakeProduct(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST IsTakeProduct
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:87
                if (( pyrapid.Symbols().GetSymbol(symbolname='spacepos', modulename='MAINTASK', functionname='IsTakeProduct').data.Get() == ( pyrapid.Symbols().GetSymbol(symbolname='StrLen', modulename='MAINTASK', functionname='IsTakeProduct').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsTakeProduct').data(pyrapid.Symbols().GetSymbol(symbolname='command_to_find', modulename='MAINTASK', functionname='IsTakeProduct').data.Get()))} ) + 1 ) )) :
                    pass
                    #StatementAST IsTakeProduct
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            pyrapid.Symbols().GetSymbol(symbolname='basecommand', modulename='MAINTASK', functionname='IsTakeProduct').data.Set( pyrapid.Symbols().GetSymbol(symbolname='StrPart', modulename='MAINTASK', functionname='IsTakeProduct').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsTakeProduct').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='IsTakeProduct').data.Get())),'ChPos':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='IsTakeProduct').data(1)),'Len':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='IsTakeProduct').data(pyrapid.Symbols().GetSymbol(symbolname='StrLen', modulename='MAINTASK', functionname='IsTakeProduct').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsTakeProduct').data(pyrapid.Symbols().GetSymbol(symbolname='command_to_find', modulename='MAINTASK', functionname='IsTakeProduct').data.Get()))} )))} ) ) 
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakeProduct', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakeProduct', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' IsTakeProduct(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsTakeProduct, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' IsTakeProduct(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                    #StatementAST IsTakeProduct
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line Palletizer/maintask.mod:89
                            if (( pyrapid.Symbols().GetSymbol(symbolname='basecommand', modulename='MAINTASK', functionname='IsTakeProduct').data.Get() == pyrapid.Symbols().GetSymbol(symbolname='command_to_find', modulename='MAINTASK', functionname='IsTakeProduct').data.Get() )) :
                                pass
                                #StatementAST IsTakeProduct
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        pyrapid.Symbols().GetSymbol(symbolname='tmp', modulename='MAINTASK', functionname='IsTakeProduct').data.Set( pyrapid.Symbols().GetSymbol(symbolname='StrPart', modulename='MAINTASK', functionname='IsTakeProduct').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsTakeProduct').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='IsTakeProduct').data.Get())),'ChPos':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='IsTakeProduct').data(( pyrapid.Symbols().GetSymbol(symbolname='spacepos', modulename='MAINTASK', functionname='IsTakeProduct').data.Get() + 1 ))),'Len':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='IsTakeProduct').data(( pyrapid.Symbols().GetSymbol(symbolname='StrLen', modulename='MAINTASK', functionname='IsTakeProduct').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsTakeProduct').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='IsTakeProduct').data.Get()))} ) - ( pyrapid.Symbols().GetSymbol(symbolname='spacepos', modulename='MAINTASK', functionname='IsTakeProduct').data.Get() - 1 ) )))} ) ) 
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakeProduct', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakeProduct', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' IsTakeProduct(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsTakeProduct, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' IsTakeProduct(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                #StatementAST IsTakeProduct
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Line Palletizer/maintask.mod:91
                                        if (pyrapid.Symbols().GetSymbol(symbolname='StrToVal', modulename='MAINTASK', functionname='IsTakeProduct').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsTakeProduct').data(pyrapid.Symbols().GetSymbol(symbolname='tmp', modulename='MAINTASK', functionname='IsTakeProduct').data.Get())),'Val':pyrapid.Symbols().GetSymbol(symbolname='prod', modulename='MAINTASK', functionname='IsTakeProduct')} )) :
                                            pass
                                            #StatementAST IsTakeProduct
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    pyrapid.Symbols().GetSymbol(symbolname='x', modulename='MAINTASK', functionname='IsTakeProduct').data.Set( pyrapid.Symbols().GetSymbol(symbolname='prod', modulename='MAINTASK', functionname='IsTakeProduct').data.GetElem('x').Get() ) 
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakeProduct', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakeProduct', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' IsTakeProduct(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsTakeProduct, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' IsTakeProduct(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                            #StatementAST IsTakeProduct
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    pyrapid.Symbols().GetSymbol(symbolname='y', modulename='MAINTASK', functionname='IsTakeProduct').data.Set( pyrapid.Symbols().GetSymbol(symbolname='prod', modulename='MAINTASK', functionname='IsTakeProduct').data.GetElem('y').Get() ) 
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakeProduct', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakeProduct', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' IsTakeProduct(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsTakeProduct, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' IsTakeProduct(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                            #StatementAST IsTakeProduct
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    pyrapid.Symbols().GetSymbol(symbolname='z', modulename='MAINTASK', functionname='IsTakeProduct').data.Set( pyrapid.Symbols().GetSymbol(symbolname='prod', modulename='MAINTASK', functionname='IsTakeProduct').data.GetElem('z').Get() ) 
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakeProduct', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakeProduct', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' IsTakeProduct(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsTakeProduct, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' IsTakeProduct(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                            #StatementAST IsTakeProduct
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    pyrapid.Symbols().GetSymbol(symbolname='rot', modulename='MAINTASK', functionname='IsTakeProduct').data.Set( pyrapid.Symbols().GetSymbol(symbolname='prod', modulename='MAINTASK', functionname='IsTakeProduct').data.GetElem('rot').Get() ) 
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakeProduct', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakeProduct', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' IsTakeProduct(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsTakeProduct, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' IsTakeProduct(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                            #StatementAST IsTakeProduct
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    # Line Palletizer/maintask.mod:98
                                                    return ( True )
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakeProduct', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakeProduct', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' IsTakeProduct(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsTakeProduct, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' IsTakeProduct(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakeProduct', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakeProduct', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' IsTakeProduct(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsTakeProduct, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' IsTakeProduct(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakeProduct', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakeProduct', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' IsTakeProduct(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsTakeProduct, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' IsTakeProduct(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakeProduct', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakeProduct', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' IsTakeProduct(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsTakeProduct, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' IsTakeProduct(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST IsTakeProduct
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:102
                return ( False )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakeProduct', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakeProduct', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' IsTakeProduct(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsTakeProduct, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' IsTakeProduct(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('IsTakeProduct', pyrapid.Symbol.CreateFunction(OrderedDict([('command', ('required', 'NORMAL', 'string', 0, [])), ('x', ('required', 'VAR', 'num', 0, [])), ('y', ('required', 'VAR', 'num', 0, [])), ('z', ('required', 'VAR', 'num', 0, [])), ('rot', ('required', 'VAR', 'num', 0, []))]), pyrapid.Symbols().GetSymbol('bool', 'MAINTASK', None), rapid_func_IsTakeProduct, error_rapid_func_IsTakeProduct, undo_rapid_func_IsTakeProduct), 'MAINTASK')
del rapid_func_IsTakeProduct
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:105
# Start Function Definition
def error_rapid_func_IsPlaceProduct (local_exception):
    return 0
def undo_rapid_func_IsPlaceProduct ():
    pass
def rapid_func_IsPlaceProduct (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='IsPlaceProduct', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line Palletizer/maintask.mod:106
        pyrapid.Symbols().AddScopeSym('spacepos', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='IsPlaceProduct').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:107
        pyrapid.Symbols().AddScopeSym('basecommand', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsPlaceProduct').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:108
        pyrapid.Symbols().AddScopeSym('tmp', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsPlaceProduct').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:109
        pyrapid.Symbols().AddScopeSym('prod', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='TakeProdType', modulename='MAINTASK', functionname='IsPlaceProduct').data([0, 0, 0, 0])))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:110
        pyrapid.Symbols().AddScopeSym('command_to_find', pyrapid.Symbol.CreateConst(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsPlaceProduct').data('TakeProduct')))
        # end declaration
        # stantments
        #StatementAST IsPlaceProduct
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='spacepos', modulename='MAINTASK', functionname='IsPlaceProduct').data.Set( pyrapid.Symbols().GetSymbol(symbolname='StrFind', modulename='MAINTASK', functionname='IsPlaceProduct').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsPlaceProduct').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='IsPlaceProduct').data.Get())),'ChPos':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='IsPlaceProduct').data(1)),'Set':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsPlaceProduct').data(' '))} ) ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsPlaceProduct, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST IsPlaceProduct
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:114
                if (( pyrapid.Symbols().GetSymbol(symbolname='spacepos', modulename='MAINTASK', functionname='IsPlaceProduct').data.Get() == ( pyrapid.Symbols().GetSymbol(symbolname='StrLen', modulename='MAINTASK', functionname='IsPlaceProduct').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsPlaceProduct').data(pyrapid.Symbols().GetSymbol(symbolname='command_to_find', modulename='MAINTASK', functionname='IsPlaceProduct').data.Get()))} ) + 1 ) )) :
                    pass
                    #StatementAST IsPlaceProduct
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            pyrapid.Symbols().GetSymbol(symbolname='basecommand', modulename='MAINTASK', functionname='IsPlaceProduct').data.Set( pyrapid.Symbols().GetSymbol(symbolname='StrPart', modulename='MAINTASK', functionname='IsPlaceProduct').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsPlaceProduct').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='IsPlaceProduct').data.Get())),'ChPos':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='IsPlaceProduct').data(1)),'Len':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='IsPlaceProduct').data(pyrapid.Symbols().GetSymbol(symbolname='StrLen', modulename='MAINTASK', functionname='IsPlaceProduct').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsPlaceProduct').data(pyrapid.Symbols().GetSymbol(symbolname='command_to_find', modulename='MAINTASK', functionname='IsPlaceProduct').data.Get()))} )))} ) ) 
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsPlaceProduct, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                    #StatementAST IsPlaceProduct
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line Palletizer/maintask.mod:116
                            if (( pyrapid.Symbols().GetSymbol(symbolname='basecommand', modulename='MAINTASK', functionname='IsPlaceProduct').data.Get() == pyrapid.Symbols().GetSymbol(symbolname='command_to_find', modulename='MAINTASK', functionname='IsPlaceProduct').data.Get() )) :
                                pass
                                #StatementAST IsPlaceProduct
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        pyrapid.Symbols().GetSymbol(symbolname='tmp', modulename='MAINTASK', functionname='IsPlaceProduct').data.Set( pyrapid.Symbols().GetSymbol(symbolname='StrPart', modulename='MAINTASK', functionname='IsPlaceProduct').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsPlaceProduct').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='IsPlaceProduct').data.Get())),'ChPos':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='IsPlaceProduct').data(( pyrapid.Symbols().GetSymbol(symbolname='spacepos', modulename='MAINTASK', functionname='IsPlaceProduct').data.Get() + 1 ))),'Len':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='IsPlaceProduct').data(( pyrapid.Symbols().GetSymbol(symbolname='StrLen', modulename='MAINTASK', functionname='IsPlaceProduct').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsPlaceProduct').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='IsPlaceProduct').data.Get()))} ) - ( pyrapid.Symbols().GetSymbol(symbolname='spacepos', modulename='MAINTASK', functionname='IsPlaceProduct').data.Get() - 1 ) )))} ) ) 
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsPlaceProduct, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                #StatementAST IsPlaceProduct
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Line Palletizer/maintask.mod:118
                                        if (pyrapid.Symbols().GetSymbol(symbolname='StrToVal', modulename='MAINTASK', functionname='IsPlaceProduct').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsPlaceProduct').data(pyrapid.Symbols().GetSymbol(symbolname='tmp', modulename='MAINTASK', functionname='IsPlaceProduct').data.Get())),'Val':pyrapid.Symbols().GetSymbol(symbolname='prod', modulename='MAINTASK', functionname='IsPlaceProduct')} )) :
                                            pass
                                            #StatementAST IsPlaceProduct
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    pyrapid.Symbols().GetSymbol(symbolname='index', modulename='MAINTASK', functionname='IsPlaceProduct').data.Set( pyrapid.Symbols().GetSymbol(symbolname='prod', modulename='MAINTASK', functionname='IsPlaceProduct').data.GetElem('type').Get() ) 
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsPlaceProduct, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                            #StatementAST IsPlaceProduct
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    pyrapid.Symbols().GetSymbol(symbolname='x', modulename='MAINTASK', functionname='IsPlaceProduct').data.GetElem( [1] ).Set( pyrapid.Symbols().GetSymbol(symbolname='prod', modulename='MAINTASK', functionname='IsPlaceProduct').data.GetElem('x1').Get() ) 
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsPlaceProduct, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                            #StatementAST IsPlaceProduct
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    pyrapid.Symbols().GetSymbol(symbolname='x', modulename='MAINTASK', functionname='IsPlaceProduct').data.GetElem( [2] ).Set( pyrapid.Symbols().GetSymbol(symbolname='prod', modulename='MAINTASK', functionname='IsPlaceProduct').data.GetElem('x2').Get() ) 
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsPlaceProduct, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                            #StatementAST IsPlaceProduct
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    pyrapid.Symbols().GetSymbol(symbolname='y', modulename='MAINTASK', functionname='IsPlaceProduct').data.GetElem( [1] ).Set( pyrapid.Symbols().GetSymbol(symbolname='prod', modulename='MAINTASK', functionname='IsPlaceProduct').data.GetElem('y1').Get() ) 
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsPlaceProduct, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                            #StatementAST IsPlaceProduct
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    pyrapid.Symbols().GetSymbol(symbolname='y', modulename='MAINTASK', functionname='IsPlaceProduct').data.GetElem( [2] ).Set( pyrapid.Symbols().GetSymbol(symbolname='prod', modulename='MAINTASK', functionname='IsPlaceProduct').data.GetElem('y2').Get() ) 
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsPlaceProduct, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                            #StatementAST IsPlaceProduct
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    pyrapid.Symbols().GetSymbol(symbolname='z', modulename='MAINTASK', functionname='IsPlaceProduct').data.GetElem( [1] ).Set( pyrapid.Symbols().GetSymbol(symbolname='prod', modulename='MAINTASK', functionname='IsPlaceProduct').data.GetElem('z1').Get() ) 
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsPlaceProduct, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                            #StatementAST IsPlaceProduct
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    pyrapid.Symbols().GetSymbol(symbolname='z', modulename='MAINTASK', functionname='IsPlaceProduct').data.GetElem( [2] ).Set( pyrapid.Symbols().GetSymbol(symbolname='prod', modulename='MAINTASK', functionname='IsPlaceProduct').data.GetElem('z2').Get() ) 
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsPlaceProduct, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                            #StatementAST IsPlaceProduct
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    pyrapid.Symbols().GetSymbol(symbolname='rot', modulename='MAINTASK', functionname='IsPlaceProduct').data.GetElem( [1] ).Set( pyrapid.Symbols().GetSymbol(symbolname='prod', modulename='MAINTASK', functionname='IsPlaceProduct').data.GetElem('rot1').Get() ) 
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsPlaceProduct, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                            #StatementAST IsPlaceProduct
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    pyrapid.Symbols().GetSymbol(symbolname='rot', modulename='MAINTASK', functionname='IsPlaceProduct').data.GetElem( [2] ).Set( pyrapid.Symbols().GetSymbol(symbolname='prod', modulename='MAINTASK', functionname='IsPlaceProduct').data.GetElem('rot2').Get() ) 
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsPlaceProduct, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                            #StatementAST IsPlaceProduct
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    pyrapid.Symbols().GetSymbol(symbolname='acc_x', modulename='MAINTASK', functionname='IsPlaceProduct').data.GetElem( [1] ).Set( pyrapid.Symbols().GetSymbol(symbolname='prod', modulename='MAINTASK', functionname='IsPlaceProduct').data.GetElem('acc_x1').Get() ) 
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsPlaceProduct, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                            #StatementAST IsPlaceProduct
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    pyrapid.Symbols().GetSymbol(symbolname='acc_x', modulename='MAINTASK', functionname='IsPlaceProduct').data.GetElem( [2] ).Set( pyrapid.Symbols().GetSymbol(symbolname='prod', modulename='MAINTASK', functionname='IsPlaceProduct').data.GetElem('acc_x2').Get() ) 
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsPlaceProduct, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                            #StatementAST IsPlaceProduct
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    pyrapid.Symbols().GetSymbol(symbolname='acc_y', modulename='MAINTASK', functionname='IsPlaceProduct').data.GetElem( [1] ).Set( pyrapid.Symbols().GetSymbol(symbolname='prod', modulename='MAINTASK', functionname='IsPlaceProduct').data.GetElem('acc_y1').Get() ) 
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsPlaceProduct, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                            #StatementAST IsPlaceProduct
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    pyrapid.Symbols().GetSymbol(symbolname='acc_y', modulename='MAINTASK', functionname='IsPlaceProduct').data.GetElem( [2] ).Set( pyrapid.Symbols().GetSymbol(symbolname='prod', modulename='MAINTASK', functionname='IsPlaceProduct').data.GetElem('acc_y2').Get() ) 
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsPlaceProduct, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                            #StatementAST IsPlaceProduct
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    pyrapid.Symbols().GetSymbol(symbolname='acc_z', modulename='MAINTASK', functionname='IsPlaceProduct').data.GetElem( [1] ).Set( pyrapid.Symbols().GetSymbol(symbolname='prod', modulename='MAINTASK', functionname='IsPlaceProduct').data.GetElem('acc_z1').Get() ) 
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsPlaceProduct, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                            #StatementAST IsPlaceProduct
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    pyrapid.Symbols().GetSymbol(symbolname='acc_z', modulename='MAINTASK', functionname='IsPlaceProduct').data.GetElem( [2] ).Set( pyrapid.Symbols().GetSymbol(symbolname='prod', modulename='MAINTASK', functionname='IsPlaceProduct').data.GetElem('acc_z2').Get() ) 
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsPlaceProduct, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                            #StatementAST IsPlaceProduct
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    # Line Palletizer/maintask.mod:141
                                                    return ( True )
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsPlaceProduct, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsPlaceProduct, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsPlaceProduct, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsPlaceProduct, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST IsPlaceProduct
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:145
                return ( False )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsPlaceProduct, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceProduct(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('IsPlaceProduct', pyrapid.Symbol.CreateFunction(OrderedDict([('command', ('required', 'NORMAL', 'string', 0, [])), ('index', ('required', 'VAR', 'num', 0, [])), ('x', ('required', 'VAR', 'num', 1, [])), ('y', ('required', 'VAR', 'num', 1, [])), ('z', ('required', 'VAR', 'num', 1, [])), ('rot', ('required', 'VAR', 'num', 1, [])), ('acc_x', ('required', 'VAR', 'num', 1, [])), ('acc_y', ('required', 'VAR', 'num', 1, [])), ('acc_z', ('required', 'VAR', 'num', 1, []))]), pyrapid.Symbols().GetSymbol('bool', 'MAINTASK', None), rapid_func_IsPlaceProduct, error_rapid_func_IsPlaceProduct, undo_rapid_func_IsPlaceProduct), 'MAINTASK')
del rapid_func_IsPlaceProduct
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:148
# Start Function Definition
def error_rapid_func_IsOrderProduct (local_exception):
    return 0
def undo_rapid_func_IsOrderProduct ():
    pass
def rapid_func_IsOrderProduct (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='IsOrderProduct', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line Palletizer/maintask.mod:149
        pyrapid.Symbols().AddScopeSym('spacepos', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='IsOrderProduct').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:150
        pyrapid.Symbols().AddScopeSym('basecommand', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsOrderProduct').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:151
        pyrapid.Symbols().AddScopeSym('tmp', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsOrderProduct').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:152
        pyrapid.Symbols().AddScopeSym('prod', pyrapid.Symbol.CreateVar( pyrapid.rapid_array([2], pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='IsOrderProduct').data, [0, 0]) ))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:153
        pyrapid.Symbols().AddScopeSym('command_to_find', pyrapid.Symbol.CreateConst(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsOrderProduct').data('OrderProd')))
        # end declaration
        # stantments
        #StatementAST IsOrderProduct
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='spacepos', modulename='MAINTASK', functionname='IsOrderProduct').data.Set( pyrapid.Symbols().GetSymbol(symbolname='StrFind', modulename='MAINTASK', functionname='IsOrderProduct').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsOrderProduct').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='IsOrderProduct').data.Get())),'ChPos':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='IsOrderProduct').data(1)),'Set':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsOrderProduct').data(' '))} ) ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsOrderProduct', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsOrderProduct', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' IsOrderProduct(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsOrderProduct, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' IsOrderProduct(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST IsOrderProduct
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:157
                if (( pyrapid.Symbols().GetSymbol(symbolname='spacepos', modulename='MAINTASK', functionname='IsOrderProduct').data.Get() == ( pyrapid.Symbols().GetSymbol(symbolname='StrLen', modulename='MAINTASK', functionname='IsOrderProduct').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsOrderProduct').data(pyrapid.Symbols().GetSymbol(symbolname='command_to_find', modulename='MAINTASK', functionname='IsOrderProduct').data.Get()))} ) + 1 ) )) :
                    pass
                    #StatementAST IsOrderProduct
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            pyrapid.Symbols().GetSymbol(symbolname='basecommand', modulename='MAINTASK', functionname='IsOrderProduct').data.Set( pyrapid.Symbols().GetSymbol(symbolname='StrPart', modulename='MAINTASK', functionname='IsOrderProduct').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsOrderProduct').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='IsOrderProduct').data.Get())),'ChPos':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='IsOrderProduct').data(1)),'Len':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='IsOrderProduct').data(pyrapid.Symbols().GetSymbol(symbolname='StrLen', modulename='MAINTASK', functionname='IsOrderProduct').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsOrderProduct').data(pyrapid.Symbols().GetSymbol(symbolname='command_to_find', modulename='MAINTASK', functionname='IsOrderProduct').data.Get()))} )))} ) ) 
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsOrderProduct', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsOrderProduct', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' IsOrderProduct(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsOrderProduct, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' IsOrderProduct(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                    #StatementAST IsOrderProduct
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line Palletizer/maintask.mod:159
                            if (( pyrapid.Symbols().GetSymbol(symbolname='basecommand', modulename='MAINTASK', functionname='IsOrderProduct').data.Get() == pyrapid.Symbols().GetSymbol(symbolname='command_to_find', modulename='MAINTASK', functionname='IsOrderProduct').data.Get() )) :
                                pass
                                #StatementAST IsOrderProduct
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        pyrapid.Symbols().GetSymbol(symbolname='tmp', modulename='MAINTASK', functionname='IsOrderProduct').data.Set( pyrapid.Symbols().GetSymbol(symbolname='StrPart', modulename='MAINTASK', functionname='IsOrderProduct').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsOrderProduct').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='IsOrderProduct').data.Get())),'ChPos':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='IsOrderProduct').data(( pyrapid.Symbols().GetSymbol(symbolname='spacepos', modulename='MAINTASK', functionname='IsOrderProduct').data.Get() + 1 ))),'Len':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='IsOrderProduct').data(( pyrapid.Symbols().GetSymbol(symbolname='StrLen', modulename='MAINTASK', functionname='IsOrderProduct').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsOrderProduct').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='IsOrderProduct').data.Get()))} ) - ( pyrapid.Symbols().GetSymbol(symbolname='spacepos', modulename='MAINTASK', functionname='IsOrderProduct').data.Get() - 1 ) )))} ) ) 
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsOrderProduct', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsOrderProduct', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' IsOrderProduct(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsOrderProduct, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' IsOrderProduct(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                #StatementAST IsOrderProduct
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Line Palletizer/maintask.mod:161
                                        if (pyrapid.Symbols().GetSymbol(symbolname='StrToVal', modulename='MAINTASK', functionname='IsOrderProduct').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsOrderProduct').data(pyrapid.Symbols().GetSymbol(symbolname='tmp', modulename='MAINTASK', functionname='IsOrderProduct').data.Get())),'Val':pyrapid.Symbols().GetSymbol(symbolname='prod', modulename='MAINTASK', functionname='IsOrderProduct')} )) :
                                            pass
                                            #StatementAST IsOrderProduct
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    pyrapid.Symbols().GetSymbol(symbolname='nprod', modulename='MAINTASK', functionname='IsOrderProduct').data.Set( pyrapid.Symbols().GetSymbol(symbolname='prod', modulename='MAINTASK', functionname='IsOrderProduct').data.GetElem( [1] ).Get() ) 
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsOrderProduct', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsOrderProduct', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' IsOrderProduct(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsOrderProduct, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' IsOrderProduct(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                            #StatementAST IsOrderProduct
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    pyrapid.Symbols().GetSymbol(symbolname='disposition', modulename='MAINTASK', functionname='IsOrderProduct').data.Set( pyrapid.Symbols().GetSymbol(symbolname='prod', modulename='MAINTASK', functionname='IsOrderProduct').data.GetElem( [2] ).Get() ) 
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsOrderProduct', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsOrderProduct', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' IsOrderProduct(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsOrderProduct, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' IsOrderProduct(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                            #StatementAST IsOrderProduct
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    # Line Palletizer/maintask.mod:164
                                                    return ( True )
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsOrderProduct', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsOrderProduct', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' IsOrderProduct(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsOrderProduct, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' IsOrderProduct(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsOrderProduct', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsOrderProduct', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' IsOrderProduct(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsOrderProduct, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' IsOrderProduct(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsOrderProduct', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsOrderProduct', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' IsOrderProduct(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsOrderProduct, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' IsOrderProduct(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsOrderProduct', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsOrderProduct', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' IsOrderProduct(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsOrderProduct, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' IsOrderProduct(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST IsOrderProduct
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:168
                return ( False )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsOrderProduct', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsOrderProduct', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' IsOrderProduct(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsOrderProduct, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' IsOrderProduct(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('IsOrderProduct', pyrapid.Symbol.CreateFunction(OrderedDict([('command', ('required', 'NORMAL', 'string', 0, [])), ('nprod', ('required', 'VAR', 'num', 0, [])), ('disposition', ('required', 'VAR', 'num', 0, []))]), pyrapid.Symbols().GetSymbol('bool', 'MAINTASK', None), rapid_func_IsOrderProduct, error_rapid_func_IsOrderProduct, undo_rapid_func_IsOrderProduct), 'MAINTASK')
del rapid_func_IsOrderProduct
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:171
# Start Function Definition
def error_rapid_func_IsStartQueue (local_exception):
    return 0
def undo_rapid_func_IsStartQueue ():
    pass
def rapid_func_IsStartQueue (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='IsStartQueue', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line Palletizer/maintask.mod:172
        pyrapid.Symbols().AddScopeSym('spacepos', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='IsStartQueue').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:173
        pyrapid.Symbols().AddScopeSym('basecommand', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsStartQueue').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:174
        pyrapid.Symbols().AddScopeSym('tmp', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsStartQueue').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:175
        pyrapid.Symbols().AddScopeSym('command_to_find', pyrapid.Symbol.CreateConst(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsStartQueue').data('StartQueue')))
        # end declaration
        # stantments
        #StatementAST IsStartQueue
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='spacepos', modulename='MAINTASK', functionname='IsStartQueue').data.Set( pyrapid.Symbols().GetSymbol(symbolname='StrFind', modulename='MAINTASK', functionname='IsStartQueue').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsStartQueue').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='IsStartQueue').data.Get())),'ChPos':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='IsStartQueue').data(1)),'Set':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsStartQueue').data(' '))} ) ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStartQueue', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStartQueue', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' IsStartQueue(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsStartQueue, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' IsStartQueue(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST IsStartQueue
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:179
                if (( pyrapid.Symbols().GetSymbol(symbolname='spacepos', modulename='MAINTASK', functionname='IsStartQueue').data.Get() == ( pyrapid.Symbols().GetSymbol(symbolname='StrLen', modulename='MAINTASK', functionname='IsStartQueue').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsStartQueue').data(pyrapid.Symbols().GetSymbol(symbolname='command_to_find', modulename='MAINTASK', functionname='IsStartQueue').data.Get()))} ) + 1 ) )) :
                    pass
                    #StatementAST IsStartQueue
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            pyrapid.Symbols().GetSymbol(symbolname='basecommand', modulename='MAINTASK', functionname='IsStartQueue').data.Set( pyrapid.Symbols().GetSymbol(symbolname='StrPart', modulename='MAINTASK', functionname='IsStartQueue').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsStartQueue').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='IsStartQueue').data.Get())),'ChPos':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='IsStartQueue').data(1)),'Len':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='IsStartQueue').data(pyrapid.Symbols().GetSymbol(symbolname='StrLen', modulename='MAINTASK', functionname='IsStartQueue').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsStartQueue').data(pyrapid.Symbols().GetSymbol(symbolname='command_to_find', modulename='MAINTASK', functionname='IsStartQueue').data.Get()))} )))} ) ) 
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStartQueue', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStartQueue', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' IsStartQueue(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsStartQueue, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' IsStartQueue(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                    #StatementAST IsStartQueue
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line Palletizer/maintask.mod:181
                            if (( pyrapid.Symbols().GetSymbol(symbolname='basecommand', modulename='MAINTASK', functionname='IsStartQueue').data.Get() == pyrapid.Symbols().GetSymbol(symbolname='command_to_find', modulename='MAINTASK', functionname='IsStartQueue').data.Get() )) :
                                pass
                                #StatementAST IsStartQueue
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        pyrapid.Symbols().GetSymbol(symbolname='tmp', modulename='MAINTASK', functionname='IsStartQueue').data.Set( pyrapid.Symbols().GetSymbol(symbolname='StrPart', modulename='MAINTASK', functionname='IsStartQueue').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsStartQueue').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='IsStartQueue').data.Get())),'ChPos':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='IsStartQueue').data(( pyrapid.Symbols().GetSymbol(symbolname='spacepos', modulename='MAINTASK', functionname='IsStartQueue').data.Get() + 1 ))),'Len':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='IsStartQueue').data(( pyrapid.Symbols().GetSymbol(symbolname='StrLen', modulename='MAINTASK', functionname='IsStartQueue').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsStartQueue').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='IsStartQueue').data.Get()))} ) - ( pyrapid.Symbols().GetSymbol(symbolname='spacepos', modulename='MAINTASK', functionname='IsStartQueue').data.Get() - 1 ) )))} ) ) 
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStartQueue', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStartQueue', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' IsStartQueue(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsStartQueue, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' IsStartQueue(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                #StatementAST IsStartQueue
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Line Palletizer/maintask.mod:183
                                        if (pyrapid.Symbols().GetSymbol(symbolname='StrToVal', modulename='MAINTASK', functionname='IsStartQueue').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsStartQueue').data(pyrapid.Symbols().GetSymbol(symbolname='tmp', modulename='MAINTASK', functionname='IsStartQueue').data.Get())),'Val':pyrapid.Symbols().GetSymbol(symbolname='queue', modulename='MAINTASK', functionname='IsStartQueue')} )) :
                                            pass
                                            #StatementAST IsStartQueue
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    # Line Palletizer/maintask.mod:184
                                                    return ( True )
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStartQueue', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStartQueue', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' IsStartQueue(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsStartQueue, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' IsStartQueue(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStartQueue', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStartQueue', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' IsStartQueue(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsStartQueue, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' IsStartQueue(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStartQueue', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStartQueue', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' IsStartQueue(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsStartQueue, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' IsStartQueue(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStartQueue', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStartQueue', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' IsStartQueue(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsStartQueue, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' IsStartQueue(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST IsStartQueue
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:188
                return ( False )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStartQueue', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStartQueue', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' IsStartQueue(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsStartQueue, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' IsStartQueue(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('IsStartQueue', pyrapid.Symbol.CreateFunction(OrderedDict([('command', ('required', 'NORMAL', 'string', 0, [])), ('queue', ('required', 'VAR', 'num', 0, []))]), pyrapid.Symbols().GetSymbol('bool', 'MAINTASK', None), rapid_func_IsStartQueue, error_rapid_func_IsStartQueue, undo_rapid_func_IsStartQueue), 'MAINTASK')
del rapid_func_IsStartQueue
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:191
# Start Function Definition
def error_rapid_func_IsStopQueue (local_exception):
    return 0
def undo_rapid_func_IsStopQueue ():
    pass
def rapid_func_IsStopQueue (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='IsStopQueue', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line Palletizer/maintask.mod:192
        pyrapid.Symbols().AddScopeSym('spacepos', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='IsStopQueue').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:193
        pyrapid.Symbols().AddScopeSym('basecommand', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsStopQueue').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:194
        pyrapid.Symbols().AddScopeSym('tmp', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsStopQueue').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:195
        pyrapid.Symbols().AddScopeSym('command_to_find', pyrapid.Symbol.CreateConst(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsStopQueue').data('StopQueue')))
        # end declaration
        # stantments
        #StatementAST IsStopQueue
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='spacepos', modulename='MAINTASK', functionname='IsStopQueue').data.Set( pyrapid.Symbols().GetSymbol(symbolname='StrFind', modulename='MAINTASK', functionname='IsStopQueue').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsStopQueue').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='IsStopQueue').data.Get())),'ChPos':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='IsStopQueue').data(1)),'Set':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsStopQueue').data(' '))} ) ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStopQueue', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStopQueue', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' IsStopQueue(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsStopQueue, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' IsStopQueue(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST IsStopQueue
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:198
                if (( pyrapid.Symbols().GetSymbol(symbolname='spacepos', modulename='MAINTASK', functionname='IsStopQueue').data.Get() == ( pyrapid.Symbols().GetSymbol(symbolname='StrLen', modulename='MAINTASK', functionname='IsStopQueue').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsStopQueue').data(pyrapid.Symbols().GetSymbol(symbolname='command_to_find', modulename='MAINTASK', functionname='IsStopQueue').data.Get()))} ) + 1 ) )) :
                    pass
                    #StatementAST IsStopQueue
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            pyrapid.Symbols().GetSymbol(symbolname='basecommand', modulename='MAINTASK', functionname='IsStopQueue').data.Set( pyrapid.Symbols().GetSymbol(symbolname='StrPart', modulename='MAINTASK', functionname='IsStopQueue').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsStopQueue').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='IsStopQueue').data.Get())),'ChPos':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='IsStopQueue').data(1)),'Len':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='IsStopQueue').data(pyrapid.Symbols().GetSymbol(symbolname='StrLen', modulename='MAINTASK', functionname='IsStopQueue').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsStopQueue').data(pyrapid.Symbols().GetSymbol(symbolname='command_to_find', modulename='MAINTASK', functionname='IsStopQueue').data.Get()))} )))} ) ) 
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStopQueue', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStopQueue', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' IsStopQueue(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsStopQueue, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' IsStopQueue(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                    #StatementAST IsStopQueue
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line Palletizer/maintask.mod:200
                            if (( pyrapid.Symbols().GetSymbol(symbolname='basecommand', modulename='MAINTASK', functionname='IsStopQueue').data.Get() == pyrapid.Symbols().GetSymbol(symbolname='command_to_find', modulename='MAINTASK', functionname='IsStopQueue').data.Get() )) :
                                pass
                                #StatementAST IsStopQueue
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        pyrapid.Symbols().GetSymbol(symbolname='tmp', modulename='MAINTASK', functionname='IsStopQueue').data.Set( pyrapid.Symbols().GetSymbol(symbolname='StrPart', modulename='MAINTASK', functionname='IsStopQueue').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsStopQueue').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='IsStopQueue').data.Get())),'ChPos':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='IsStopQueue').data(( pyrapid.Symbols().GetSymbol(symbolname='spacepos', modulename='MAINTASK', functionname='IsStopQueue').data.Get() + 1 ))),'Len':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='IsStopQueue').data(( pyrapid.Symbols().GetSymbol(symbolname='StrLen', modulename='MAINTASK', functionname='IsStopQueue').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsStopQueue').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='IsStopQueue').data.Get()))} ) - ( pyrapid.Symbols().GetSymbol(symbolname='spacepos', modulename='MAINTASK', functionname='IsStopQueue').data.Get() - 1 ) )))} ) ) 
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStopQueue', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStopQueue', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' IsStopQueue(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsStopQueue, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' IsStopQueue(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                #StatementAST IsStopQueue
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Line Palletizer/maintask.mod:202
                                        if (pyrapid.Symbols().GetSymbol(symbolname='StrToVal', modulename='MAINTASK', functionname='IsStopQueue').data( {'Str':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsStopQueue').data(pyrapid.Symbols().GetSymbol(symbolname='tmp', modulename='MAINTASK', functionname='IsStopQueue').data.Get())),'Val':pyrapid.Symbols().GetSymbol(symbolname='queue', modulename='MAINTASK', functionname='IsStopQueue')} )) :
                                            pass
                                            #StatementAST IsStopQueue
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    # Line Palletizer/maintask.mod:203
                                                    return ( True )
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStopQueue', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStopQueue', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' IsStopQueue(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsStopQueue, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' IsStopQueue(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStopQueue', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStopQueue', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' IsStopQueue(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsStopQueue, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' IsStopQueue(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStopQueue', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStopQueue', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' IsStopQueue(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsStopQueue, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' IsStopQueue(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStopQueue', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStopQueue', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' IsStopQueue(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsStopQueue, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' IsStopQueue(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST IsStopQueue
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:207
                return ( False )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStopQueue', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsStopQueue', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' IsStopQueue(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsStopQueue, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' IsStopQueue(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('IsStopQueue', pyrapid.Symbol.CreateFunction(OrderedDict([('command', ('required', 'NORMAL', 'string', 0, [])), ('queue', ('required', 'VAR', 'num', 0, []))]), pyrapid.Symbols().GetSymbol('bool', 'MAINTASK', None), rapid_func_IsStopQueue, error_rapid_func_IsStopQueue, undo_rapid_func_IsStopQueue), 'MAINTASK')
del rapid_func_IsStopQueue
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:211
# Start Function Definition
def error_rapid_func_IsOrderPallet (local_exception):
    return 0
def undo_rapid_func_IsOrderPallet ():
    pass
def rapid_func_IsOrderPallet (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='IsOrderPallet', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line Palletizer/maintask.mod:212
        pyrapid.Symbols().AddScopeSym('command_to_find', pyrapid.Symbol.CreateConst(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsOrderPallet').data('OrderPallet')))
        # end declaration
        # stantments
        #StatementAST IsOrderPallet
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:214
                if (( pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='IsOrderPallet').data.Get() == pyrapid.Symbols().GetSymbol(symbolname='command_to_find', modulename='MAINTASK', functionname='IsOrderPallet').data.Get() )) :
                    pass
                    #StatementAST IsOrderPallet
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line Palletizer/maintask.mod:215
                            return ( True )
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsOrderPallet', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsOrderPallet', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' IsOrderPallet(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsOrderPallet, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' IsOrderPallet(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                else:
                    #StatementAST IsOrderPallet
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line Palletizer/maintask.mod:217
                            return ( False )
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsOrderPallet', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsOrderPallet', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' IsOrderPallet(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsOrderPallet, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' IsOrderPallet(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsOrderPallet', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsOrderPallet', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' IsOrderPallet(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsOrderPallet, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' IsOrderPallet(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('IsOrderPallet', pyrapid.Symbol.CreateFunction(OrderedDict([('command', ('required', 'NORMAL', 'string', 0, []))]), pyrapid.Symbols().GetSymbol('bool', 'MAINTASK', None), rapid_func_IsOrderPallet, error_rapid_func_IsOrderPallet, undo_rapid_func_IsOrderPallet), 'MAINTASK')
del rapid_func_IsOrderPallet
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:221
# Start Function Definition
def error_rapid_func_IsTakePallet (local_exception):
    return 0
def undo_rapid_func_IsTakePallet ():
    pass
def rapid_func_IsTakePallet (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='IsTakePallet', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line Palletizer/maintask.mod:222
        pyrapid.Symbols().AddScopeSym('command_to_find', pyrapid.Symbol.CreateConst(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsTakePallet').data('TakePallet')))
        # end declaration
        # stantments
        #StatementAST IsTakePallet
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:224
                if (( pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='IsTakePallet').data.Get() == pyrapid.Symbols().GetSymbol(symbolname='command_to_find', modulename='MAINTASK', functionname='IsTakePallet').data.Get() )) :
                    pass
                    #StatementAST IsTakePallet
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line Palletizer/maintask.mod:225
                            return ( True )
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakePallet', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakePallet', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' IsTakePallet(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsTakePallet, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' IsTakePallet(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                else:
                    #StatementAST IsTakePallet
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line Palletizer/maintask.mod:227
                            return ( False )
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakePallet', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakePallet', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' IsTakePallet(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsTakePallet, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' IsTakePallet(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakePallet', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakePallet', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' IsTakePallet(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsTakePallet, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' IsTakePallet(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('IsTakePallet', pyrapid.Symbol.CreateFunction(OrderedDict([('command', ('required', 'NORMAL', 'string', 0, []))]), pyrapid.Symbols().GetSymbol('bool', 'MAINTASK', None), rapid_func_IsTakePallet, error_rapid_func_IsTakePallet, undo_rapid_func_IsTakePallet), 'MAINTASK')
del rapid_func_IsTakePallet
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:231
# Start Function Definition
def error_rapid_func_IsPlacePallet (local_exception):
    return 0
def undo_rapid_func_IsPlacePallet ():
    pass
def rapid_func_IsPlacePallet (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='IsPlacePallet', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line Palletizer/maintask.mod:232
        pyrapid.Symbols().AddScopeSym('command_to_find', pyrapid.Symbol.CreateConst(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsPlacePallet').data('PlacePallet')))
        # end declaration
        # stantments
        #StatementAST IsPlacePallet
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:234
                if (( pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='IsPlacePallet').data.Get() == pyrapid.Symbols().GetSymbol(symbolname='command_to_find', modulename='MAINTASK', functionname='IsPlacePallet').data.Get() )) :
                    pass
                    #StatementAST IsPlacePallet
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line Palletizer/maintask.mod:235
                            return ( True )
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlacePallet', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlacePallet', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' IsPlacePallet(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsPlacePallet, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' IsPlacePallet(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                else:
                    #StatementAST IsPlacePallet
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line Palletizer/maintask.mod:237
                            return ( False )
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlacePallet', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlacePallet', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' IsPlacePallet(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsPlacePallet, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' IsPlacePallet(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlacePallet', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlacePallet', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' IsPlacePallet(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsPlacePallet, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' IsPlacePallet(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('IsPlacePallet', pyrapid.Symbol.CreateFunction(OrderedDict([('command', ('required', 'NORMAL', 'string', 0, []))]), pyrapid.Symbols().GetSymbol('bool', 'MAINTASK', None), rapid_func_IsPlacePallet, error_rapid_func_IsPlacePallet, undo_rapid_func_IsPlacePallet), 'MAINTASK')
del rapid_func_IsPlacePallet
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:241
# Start Function Definition
def error_rapid_func_IsExitPallet (local_exception):
    return 0
def undo_rapid_func_IsExitPallet ():
    pass
def rapid_func_IsExitPallet (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='IsExitPallet', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line Palletizer/maintask.mod:242
        pyrapid.Symbols().AddScopeSym('command_to_find', pyrapid.Symbol.CreateConst(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsExitPallet').data('ExitPallet')))
        # end declaration
        # stantments
        #StatementAST IsExitPallet
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:244
                if (( pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='IsExitPallet').data.Get() == pyrapid.Symbols().GetSymbol(symbolname='command_to_find', modulename='MAINTASK', functionname='IsExitPallet').data.Get() )) :
                    pass
                    #StatementAST IsExitPallet
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line Palletizer/maintask.mod:245
                            return ( True )
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsExitPallet', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsExitPallet', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' IsExitPallet(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsExitPallet, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' IsExitPallet(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                else:
                    #StatementAST IsExitPallet
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line Palletizer/maintask.mod:247
                            return ( False )
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsExitPallet', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsExitPallet', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' IsExitPallet(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsExitPallet, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' IsExitPallet(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsExitPallet', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsExitPallet', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' IsExitPallet(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsExitPallet, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' IsExitPallet(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('IsExitPallet', pyrapid.Symbol.CreateFunction(OrderedDict([('command', ('required', 'NORMAL', 'string', 0, []))]), pyrapid.Symbols().GetSymbol('bool', 'MAINTASK', None), rapid_func_IsExitPallet, error_rapid_func_IsExitPallet, undo_rapid_func_IsExitPallet), 'MAINTASK')
del rapid_func_IsExitPallet
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:251
# Start Function Definition
def error_rapid_func_IsTakeSheet (local_exception):
    return 0
def undo_rapid_func_IsTakeSheet ():
    pass
def rapid_func_IsTakeSheet (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='IsTakeSheet', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line Palletizer/maintask.mod:252
        pyrapid.Symbols().AddScopeSym('command_to_find', pyrapid.Symbol.CreateConst(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsTakeSheet').data('TakeSheet')))
        # end declaration
        # stantments
        #StatementAST IsTakeSheet
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:254
                if (( pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='IsTakeSheet').data.Get() == pyrapid.Symbols().GetSymbol(symbolname='command_to_find', modulename='MAINTASK', functionname='IsTakeSheet').data.Get() )) :
                    pass
                    #StatementAST IsTakeSheet
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line Palletizer/maintask.mod:255
                            return ( True )
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakeSheet', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakeSheet', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' IsTakeSheet(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsTakeSheet, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' IsTakeSheet(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                else:
                    #StatementAST IsTakeSheet
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line Palletizer/maintask.mod:257
                            return ( False )
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakeSheet', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakeSheet', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' IsTakeSheet(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsTakeSheet, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' IsTakeSheet(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakeSheet', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsTakeSheet', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' IsTakeSheet(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsTakeSheet, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' IsTakeSheet(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('IsTakeSheet', pyrapid.Symbol.CreateFunction(OrderedDict([('command', ('required', 'NORMAL', 'string', 0, []))]), pyrapid.Symbols().GetSymbol('bool', 'MAINTASK', None), rapid_func_IsTakeSheet, error_rapid_func_IsTakeSheet, undo_rapid_func_IsTakeSheet), 'MAINTASK')
del rapid_func_IsTakeSheet
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:261
# Start Function Definition
def error_rapid_func_IsPlaceSheet (local_exception):
    return 0
def undo_rapid_func_IsPlaceSheet ():
    pass
def rapid_func_IsPlaceSheet (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='IsPlaceSheet', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line Palletizer/maintask.mod:262
        pyrapid.Symbols().AddScopeSym('command_to_find', pyrapid.Symbol.CreateConst(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='IsPlaceSheet').data('PlaceSheet')))
        # end declaration
        # stantments
        #StatementAST IsPlaceSheet
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:264
                if (( pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='IsPlaceSheet').data.Get() == pyrapid.Symbols().GetSymbol(symbolname='command_to_find', modulename='MAINTASK', functionname='IsPlaceSheet').data.Get() )) :
                    pass
                    #StatementAST IsPlaceSheet
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line Palletizer/maintask.mod:265
                            return ( True )
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceSheet', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceSheet', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceSheet(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsPlaceSheet, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceSheet(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                else:
                    #StatementAST IsPlaceSheet
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line Palletizer/maintask.mod:267
                            return ( False )
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceSheet', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceSheet', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceSheet(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsPlaceSheet, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceSheet(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceSheet', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='IsPlaceSheet', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceSheet(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=IsPlaceSheet, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' IsPlaceSheet(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('IsPlaceSheet', pyrapid.Symbol.CreateFunction(OrderedDict([('command', ('required', 'NORMAL', 'string', 0, []))]), pyrapid.Symbols().GetSymbol('bool', 'MAINTASK', None), rapid_func_IsPlaceSheet, error_rapid_func_IsPlaceSheet, undo_rapid_func_IsPlaceSheet), 'MAINTASK')
del rapid_func_IsPlaceSheet
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:272
# Start Procedure Definition
def error_rapid_proc_ASetLoadSchema (local_exception):
    return 0
def undo_rapid_proc_ASetLoadSchema ():
    pass
def rapid_proc_ASetLoadSchema (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='ASetLoadSchema', invalue=local_args_scope):
        pass
        # data definitions
        # stantments
        #StatementAST ASetLoadSchema
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='A_bForceLoadSchemas', modulename='MAINTASK', functionname='ASetLoadSchema').data.Set( True ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ASetLoadSchema', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ASetLoadSchema', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ASetLoadSchema(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ASetLoadSchema, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ASetLoadSchema(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('ASetLoadSchema', pyrapid.Symbol.CreateProcedure(OrderedDict(), rapid_proc_ASetLoadSchema, error_rapid_proc_ASetLoadSchema, undo_rapid_proc_ASetLoadSchema), 'MAINTASK')
del rapid_proc_ASetLoadSchema
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:276
# Start Procedure Definition
def error_rapid_proc_AResetLoadSchema (local_exception):
    return 0
def undo_rapid_proc_AResetLoadSchema ():
    pass
def rapid_proc_AResetLoadSchema (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='AResetLoadSchema', invalue=local_args_scope):
        pass
        # data definitions
        # stantments
        #StatementAST AResetLoadSchema
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='A_bForceLoadSchemas', modulename='MAINTASK', functionname='AResetLoadSchema').data.Set( False ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetLoadSchema', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetLoadSchema', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' AResetLoadSchema(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AResetLoadSchema, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' AResetLoadSchema(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('AResetLoadSchema', pyrapid.Symbol.CreateProcedure(OrderedDict(), rapid_proc_AResetLoadSchema, error_rapid_proc_AResetLoadSchema, undo_rapid_proc_AResetLoadSchema), 'MAINTASK')
del rapid_proc_AResetLoadSchema
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:280
# Start Function Definition
def error_rapid_func_ASchemasHasToBeLoaded (local_exception):
    return 0
def undo_rapid_func_ASchemasHasToBeLoaded ():
    pass
def rapid_func_ASchemasHasToBeLoaded (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='ASchemasHasToBeLoaded', invalue=local_args_scope):
        pass
        # data definitions
        # stantments
        #StatementAST ASchemasHasToBeLoaded
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:281
                return ( pyrapid.Symbols().GetSymbol(symbolname='A_bForceLoadSchemas', modulename='MAINTASK', functionname='ASchemasHasToBeLoaded').data.Get() )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ASchemasHasToBeLoaded', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ASchemasHasToBeLoaded', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ASchemasHasToBeLoaded(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ASchemasHasToBeLoaded, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ASchemasHasToBeLoaded(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('ASchemasHasToBeLoaded', pyrapid.Symbol.CreateFunction(OrderedDict(), pyrapid.Symbols().GetSymbol('bool', 'MAINTASK', None), rapid_func_ASchemasHasToBeLoaded, error_rapid_func_ASchemasHasToBeLoaded, undo_rapid_func_ASchemasHasToBeLoaded), 'MAINTASK')
del rapid_func_ASchemasHasToBeLoaded
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:286
# Start Procedure Definition
def error_rapid_proc_ALoadSchema (local_exception):
    #StatementAST ALoadSchema
    # Call procedure TPWrite
    parameters_actual = OrderedDict()
    parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='ALoadSchema').data('ERRORE IN ALOADSCHEMA'))
    pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='ALoadSchema').data(parameters_actual)
    del parameters_actual
    # End Call procedure
    #StatementAST ALoadSchema
    # Line Palletizer/maintask.mod:328
    if (( pyrapid.Symbols().GetSymbol(symbolname='ERRNO', modulename='MAINTASK', functionname='ALoadSchema').data.Get() == pyrapid.Symbols().GetSymbol(symbolname='ERR_UNLOAD', modulename='MAINTASK', functionname='ALoadSchema').data.Get() )) :
        pass
        #StatementAST ALoadSchema
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='ALoadSchema').data('ERRORE UNLOAD'))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='ALoadSchema').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ALoadSchema, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST ALoadSchema
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:330
                return 2
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ALoadSchema, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
    # Line Palletizer/maintask.mod:331
    elif (( ( pyrapid.Symbols().GetSymbol(symbolname='ERRNO', modulename='MAINTASK', functionname='ALoadSchema').data.Get() == pyrapid.Symbols().GetSymbol(symbolname='ERR_REFUNKPRC', modulename='MAINTASK', functionname='ALoadSchema').data.Get() ) or ( pyrapid.Symbols().GetSymbol(symbolname='ERRNO', modulename='MAINTASK', functionname='ALoadSchema').data.Get() == pyrapid.Symbols().GetSymbol(symbolname='ERR_CALLPROC', modulename='MAINTASK', functionname='ALoadSchema').data.Get() ) )) :
        pass
        #StatementAST ALoadSchema
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='ALoadSchema').data('Errore loading schema'))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='ALoadSchema').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ALoadSchema, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST ALoadSchema
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='SchemaType_Valid', modulename='MAINTASK', functionname='ALoadSchema').data.Set( pyrapid.Symbols().GetSymbol(symbolname='False', modulename='MAINTASK', functionname='ALoadSchema').data.Get() ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ALoadSchema, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST ALoadSchema
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:334
                if (pyrapid.Symbols().IsInScope('Update')) :
                    pass
                    #StatementAST ALoadSchema
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line Palletizer/maintask.mod:335
                            return 3
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ALoadSchema, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                else:
                    #StatementAST ALoadSchema
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line Palletizer/maintask.mod:337
                            return 2
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ALoadSchema, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ALoadSchema, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
    return 0
def undo_rapid_proc_ALoadSchema ():
    pass
def rapid_proc_ALoadSchema (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='ALoadSchema', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line Palletizer/maintask.mod:287
        pyrapid.Symbols().AddScopeSym('i', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='ALoadSchema').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:288
        pyrapid.Symbols().AddScopeSym('j', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='ALoadSchema').data(None)))
        # end declaration
        # Line Palletizer/maintask.mod:290
        # ## COMMENT: add backup schema ##
        # stantments
        #StatementAST ALoadSchema
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure UnLoad
                parameters_actual = OrderedDict()
                parameters_actual['FilePath'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='ALoadSchema').data('schema.mod'))
                pyrapid.Symbols().GetSymbol(symbolname='UnLoad', modulename='MAINTASK', functionname='ALoadSchema').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ALoadSchema, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST ALoadSchema
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure Load
                parameters_actual = OrderedDict()
                parameters_actual['FilePath'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='ALoadSchema').data('schema.mod'))
                pyrapid.Symbols().GetSymbol(symbolname='Load', modulename='MAINTASK', functionname='ALoadSchema').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ALoadSchema, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST ALoadSchema
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='ALoadSchema').data('INIT MODULE'))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='ALoadSchema').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ALoadSchema, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST ALoadSchema
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure INIT_SCHEMA
                parameters_actual = OrderedDict()
                pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='MAINTASK', functionname='ALoadSchema').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ALoadSchema, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST ALoadSchema
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='r_SchemaType_Valid', modulename='MAINTASK', functionname='ALoadSchema').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='nsch', modulename='MAINTASK', functionname='ALoadSchema')] ).Set( pyrapid.Symbols().GetSymbol(symbolname='SchemaType_Valid', modulename='MAINTASK', functionname='ALoadSchema').data.Get() ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ALoadSchema, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST ALoadSchema
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:298
                if (( pyrapid.Symbols().GetSymbol(symbolname='r_SchemaType_Valid', modulename='MAINTASK', functionname='ALoadSchema').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='nsch', modulename='MAINTASK', functionname='ALoadSchema')] ).Get() == True )) :
                    pass
                    #StatementAST ALoadSchema
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Call procedure TPWrite
                            parameters_actual = OrderedDict()
                            parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='ALoadSchema').data('RUNNING SCHEMA:'))
                            # Line Palletizer/maintask.mod:299
                            parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='ALoadSchema').data(pyrapid.Symbols().GetSymbol(symbolname='nsch', modulename='MAINTASK', functionname='ALoadSchema').data.Get()))
                            pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='ALoadSchema').data(parameters_actual)
                            del parameters_actual
                            # End Call procedure
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ALoadSchema, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                    #StatementAST ALoadSchema
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            pyrapid.Symbols().GetSymbol(symbolname='r_ProductType', modulename='MAINTASK', functionname='ALoadSchema').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='nsch', modulename='MAINTASK', functionname='ALoadSchema')] ).Set( pyrapid.Symbols().GetSymbol(symbolname='ProductType', modulename='MAINTASK', functionname='ALoadSchema').data.Get() ) 
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ALoadSchema, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                    #StatementAST ALoadSchema
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            pyrapid.Symbols().GetSymbol(symbolname='r_GripperType', modulename='MAINTASK', functionname='ALoadSchema').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='nsch', modulename='MAINTASK', functionname='ALoadSchema')] ).Set( pyrapid.Symbols().GetSymbol(symbolname='GripperType', modulename='MAINTASK', functionname='ALoadSchema').data.Get() ) 
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ALoadSchema, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                    #StatementAST ALoadSchema
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            pyrapid.Symbols().GetSymbol(symbolname='r_TakeLine', modulename='MAINTASK', functionname='ALoadSchema').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='nsch', modulename='MAINTASK', functionname='ALoadSchema')] ).Set( pyrapid.Symbols().GetSymbol(symbolname='TakeLine', modulename='MAINTASK', functionname='ALoadSchema').data.Get() ) 
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ALoadSchema, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                    #StatementAST ALoadSchema
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line Palletizer/maintask.mod:306
                            # FOR Statement
                            pyrapid.Symbols().GetSymbol(symbolname='j', modulename='MAINTASK', functionname='ALoadSchema').data.Set( 1 ) 
                            while ( pyrapid.Symbols().GetSymbol(symbolname='j', modulename='MAINTASK', functionname='ALoadSchema').data.Get() <= (pyrapid.Symbols().GetSymbol(symbolname='nQueueForSchema', modulename='MAINTASK', functionname='ALoadSchema').data.Get())): 
                                #StatementAST ALoadSchema
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        pyrapid.Symbols().GetSymbol(symbolname='r_SchemaType_NSteps', modulename='MAINTASK', functionname='ALoadSchema').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='nsch', modulename='MAINTASK', functionname='ALoadSchema'), pyrapid.Symbols().GetSymbol(symbolname='j', modulename='MAINTASK', functionname='ALoadSchema')] ).Set( pyrapid.Symbols().GetSymbol(symbolname='SchemaType_NSteps', modulename='MAINTASK', functionname='ALoadSchema').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='j', modulename='MAINTASK', functionname='ALoadSchema')] ).Get() ) 
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ALoadSchema, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                #StatementAST ALoadSchema
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        pyrapid.Symbols().GetSymbol(symbolname='r_SchemaType_RunSteps', modulename='MAINTASK', functionname='ALoadSchema').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='nsch', modulename='MAINTASK', functionname='ALoadSchema'), pyrapid.Symbols().GetSymbol(symbolname='j', modulename='MAINTASK', functionname='ALoadSchema')] ).Set( pyrapid.Symbols().GetSymbol(symbolname='SchemaType_RunSteps', modulename='MAINTASK', functionname='ALoadSchema').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='j', modulename='MAINTASK', functionname='ALoadSchema')] ).Get() ) 
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ALoadSchema, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                #StatementAST ALoadSchema
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Line Palletizer/maintask.mod:311
                                        # FOR Statement
                                        pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='ALoadSchema').data.Set( 1 ) 
                                        while ( pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='ALoadSchema').data.Get() <= (pyrapid.Symbols().GetSymbol(symbolname='r_SchemaType_NSteps', modulename='MAINTASK', functionname='ALoadSchema').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='nsch', modulename='MAINTASK', functionname='ALoadSchema'), pyrapid.Symbols().GetSymbol(symbolname='j', modulename='MAINTASK', functionname='ALoadSchema')] ).Get())): 
                                            #StatementAST ALoadSchema
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    pyrapid.Symbols().GetSymbol(symbolname='r_ActionType_Name', modulename='MAINTASK', functionname='ALoadSchema').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='nsch', modulename='MAINTASK', functionname='ALoadSchema'), pyrapid.Symbols().GetSymbol(symbolname='j', modulename='MAINTASK', functionname='ALoadSchema'), pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='ALoadSchema')] ).Set( pyrapid.Symbols().GetSymbol(symbolname='ActionType_Name', modulename='MAINTASK', functionname='ALoadSchema').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='j', modulename='MAINTASK', functionname='ALoadSchema'), pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='ALoadSchema')] ).Get() ) 
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ALoadSchema, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                            pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='ALoadSchema').data.Set( pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='ALoadSchema').data.Get() + (1) ) 
                                        # END FOR Statement
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ALoadSchema, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                pyrapid.Symbols().GetSymbol(symbolname='j', modulename='MAINTASK', functionname='ALoadSchema').data.Set( pyrapid.Symbols().GetSymbol(symbolname='j', modulename='MAINTASK', functionname='ALoadSchema').data.Get() + (1) ) 
                            # END FOR Statement
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ALoadSchema, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ALoadSchema, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # Line Palletizer/maintask.mod:317
        # ## COMMENT:TPWrite "TEST INIT SCHEMA", \Bool:=SchemaType_Valid; ##
        #StatementAST ALoadSchema
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure UnLoad
                parameters_actual = OrderedDict()
                parameters_actual['FilePath'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='ALoadSchema').data('schema.mod'))
                pyrapid.Symbols().GetSymbol(symbolname='UnLoad', modulename='MAINTASK', functionname='ALoadSchema').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ALoadSchema, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST ALoadSchema
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='r_QueuePaused', modulename='MAINTASK', functionname='ALoadSchema').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='nsch', modulename='MAINTASK', functionname='ALoadSchema'), pyrapid.Symbols().GetSymbol(symbolname='ORDER_QUEUE', modulename='MAINTASK', functionname='ALoadSchema')] ).Set( True ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ALoadSchema, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST ALoadSchema
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='r_QueuePaused', modulename='MAINTASK', functionname='ALoadSchema').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='nsch', modulename='MAINTASK', functionname='ALoadSchema'), pyrapid.Symbols().GetSymbol(symbolname='MAIN_QUEUE', modulename='MAINTASK', functionname='ALoadSchema')] ).Set( False ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ALoadSchema, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchema(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # Line Palletizer/maintask.mod:324
        # ## COMMENT:add undo wuth restore backup ##
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('ALoadSchema', pyrapid.Symbol.CreateProcedure(OrderedDict([('nsch', ('required', 'NORMAL', 'num', 0, [])), ('Update', ('switch', None, None, None, []))]), rapid_proc_ALoadSchema, error_rapid_proc_ALoadSchema, undo_rapid_proc_ALoadSchema), 'MAINTASK')
del rapid_proc_ALoadSchema
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:343
# Start Procedure Definition
def error_rapid_proc_AResetAllSchemas (local_exception):
    return 0
def undo_rapid_proc_AResetAllSchemas ():
    pass
def rapid_proc_AResetAllSchemas (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='AResetAllSchemas', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line Palletizer/maintask.mod:344
        pyrapid.Symbols().AddScopeSym('i', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AResetAllSchemas').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:345
        pyrapid.Symbols().AddScopeSym('j', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AResetAllSchemas').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:346
        pyrapid.Symbols().AddScopeSym('k', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AResetAllSchemas').data(None)))
        # end declaration
        # stantments
        #StatementAST AResetAllSchemas
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='AResetAllSchemas').data('RESET ALL SCHEMAS'))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='AResetAllSchemas').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetAllSchemas', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetAllSchemas', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' AResetAllSchemas(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AResetAllSchemas, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' AResetAllSchemas(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST AResetAllSchemas
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:350
                # FOR Statement
                pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='AResetAllSchemas').data.Set( 1 ) 
                while ( pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='AResetAllSchemas').data.Get() <= (pyrapid.Symbols().GetSymbol(symbolname='nPLACELINE', modulename='MAINTASK', functionname='AResetAllSchemas').data.Get())): 
                    #StatementAST AResetAllSchemas
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Call procedure TPWrite
                            parameters_actual = OrderedDict()
                            parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='AResetAllSchemas').data('Stop Schema '))
                            # Line Palletizer/maintask.mod:351
                            parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AResetAllSchemas').data(pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='AResetAllSchemas').data.Get()))
                            pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='AResetAllSchemas').data(parameters_actual)
                            del parameters_actual
                            # End Call procedure
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetAllSchemas', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetAllSchemas', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' AResetAllSchemas(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AResetAllSchemas, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' AResetAllSchemas(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                    #StatementAST AResetAllSchemas
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            pyrapid.Symbols().GetSymbol(symbolname='r_SchemaType_Valid', modulename='MAINTASK', functionname='AResetAllSchemas').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='AResetAllSchemas')] ).Set( False ) 
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetAllSchemas', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetAllSchemas', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' AResetAllSchemas(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AResetAllSchemas, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' AResetAllSchemas(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                    #StatementAST AResetAllSchemas
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line Palletizer/maintask.mod:354
                            # FOR Statement
                            pyrapid.Symbols().GetSymbol(symbolname='j', modulename='MAINTASK', functionname='AResetAllSchemas').data.Set( 1 ) 
                            while ( pyrapid.Symbols().GetSymbol(symbolname='j', modulename='MAINTASK', functionname='AResetAllSchemas').data.Get() <= (pyrapid.Symbols().GetSymbol(symbolname='nQueueForSchema', modulename='MAINTASK', functionname='AResetAllSchemas').data.Get())): 
                                #StatementAST AResetAllSchemas
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        pyrapid.Symbols().GetSymbol(symbolname='r_QueuePaused', modulename='MAINTASK', functionname='AResetAllSchemas').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='AResetAllSchemas'), pyrapid.Symbols().GetSymbol(symbolname='j', modulename='MAINTASK', functionname='AResetAllSchemas')] ).Set( False ) 
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetAllSchemas', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetAllSchemas', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' AResetAllSchemas(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AResetAllSchemas, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' AResetAllSchemas(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                #StatementAST AResetAllSchemas
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        pyrapid.Symbols().GetSymbol(symbolname='r_SchemaType_NSteps', modulename='MAINTASK', functionname='AResetAllSchemas').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='AResetAllSchemas'), pyrapid.Symbols().GetSymbol(symbolname='j', modulename='MAINTASK', functionname='AResetAllSchemas')] ).Set( 0 ) 
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetAllSchemas', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetAllSchemas', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' AResetAllSchemas(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AResetAllSchemas, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' AResetAllSchemas(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                #StatementAST AResetAllSchemas
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        pyrapid.Symbols().GetSymbol(symbolname='r_SchemaType_RunSteps', modulename='MAINTASK', functionname='AResetAllSchemas').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='AResetAllSchemas'), pyrapid.Symbols().GetSymbol(symbolname='j', modulename='MAINTASK', functionname='AResetAllSchemas')] ).Set( 0 ) 
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetAllSchemas', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetAllSchemas', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' AResetAllSchemas(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AResetAllSchemas, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' AResetAllSchemas(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                #StatementAST AResetAllSchemas
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Line Palletizer/maintask.mod:358
                                        # FOR Statement
                                        pyrapid.Symbols().GetSymbol(symbolname='k', modulename='MAINTASK', functionname='AResetAllSchemas').data.Set( 1 ) 
                                        while ( pyrapid.Symbols().GetSymbol(symbolname='k', modulename='MAINTASK', functionname='AResetAllSchemas').data.Get() <= (pyrapid.Symbols().GetSymbol(symbolname='MAX_STEP', modulename='MAINTASK', functionname='AResetAllSchemas').data.Get())): 
                                            #StatementAST AResetAllSchemas
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    pyrapid.Symbols().GetSymbol(symbolname='r_ActionType_Name', modulename='MAINTASK', functionname='AResetAllSchemas').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='AResetAllSchemas'), pyrapid.Symbols().GetSymbol(symbolname='j', modulename='MAINTASK', functionname='AResetAllSchemas'), pyrapid.Symbols().GetSymbol(symbolname='k', modulename='MAINTASK', functionname='AResetAllSchemas')] ).Set( '' ) 
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetAllSchemas', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetAllSchemas', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' AResetAllSchemas(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AResetAllSchemas, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' AResetAllSchemas(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                            pyrapid.Symbols().GetSymbol(symbolname='k', modulename='MAINTASK', functionname='AResetAllSchemas').data.Set( pyrapid.Symbols().GetSymbol(symbolname='k', modulename='MAINTASK', functionname='AResetAllSchemas').data.Get() + (1) ) 
                                        # END FOR Statement
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetAllSchemas', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetAllSchemas', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' AResetAllSchemas(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AResetAllSchemas, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' AResetAllSchemas(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                pyrapid.Symbols().GetSymbol(symbolname='j', modulename='MAINTASK', functionname='AResetAllSchemas').data.Set( pyrapid.Symbols().GetSymbol(symbolname='j', modulename='MAINTASK', functionname='AResetAllSchemas').data.Get() + (1) ) 
                            # END FOR Statement
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetAllSchemas', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetAllSchemas', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' AResetAllSchemas(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AResetAllSchemas, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' AResetAllSchemas(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                    #StatementAST AResetAllSchemas
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            pyrapid.Symbols().GetSymbol(symbolname='r_ProductType', modulename='MAINTASK', functionname='AResetAllSchemas').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='AResetAllSchemas')] ).Set( [0, 0, 0, 0, 0] ) 
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetAllSchemas', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetAllSchemas', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' AResetAllSchemas(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AResetAllSchemas, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' AResetAllSchemas(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                    #StatementAST AResetAllSchemas
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            pyrapid.Symbols().GetSymbol(symbolname='r_PalletType', modulename='MAINTASK', functionname='AResetAllSchemas').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='AResetAllSchemas')] ).Set( [0, 0, 0, 0, 0] ) 
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetAllSchemas', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetAllSchemas', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' AResetAllSchemas(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AResetAllSchemas, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' AResetAllSchemas(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                    #StatementAST AResetAllSchemas
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            pyrapid.Symbols().GetSymbol(symbolname='r_SheetType', modulename='MAINTASK', functionname='AResetAllSchemas').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='AResetAllSchemas')] ).Set( [0, 0, 0, 0, 0] ) 
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetAllSchemas', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetAllSchemas', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' AResetAllSchemas(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AResetAllSchemas, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' AResetAllSchemas(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                    #StatementAST AResetAllSchemas
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            pyrapid.Symbols().GetSymbol(symbolname='r_GripperType', modulename='MAINTASK', functionname='AResetAllSchemas').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='AResetAllSchemas')] ).Set( 0 ) 
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetAllSchemas', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetAllSchemas', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' AResetAllSchemas(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AResetAllSchemas, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' AResetAllSchemas(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                    #StatementAST AResetAllSchemas
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            pyrapid.Symbols().GetSymbol(symbolname='r_TakeLine', modulename='MAINTASK', functionname='AResetAllSchemas').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='AResetAllSchemas')] ).Set( 0 ) 
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetAllSchemas', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetAllSchemas', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' AResetAllSchemas(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AResetAllSchemas, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' AResetAllSchemas(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                    # Line Palletizer/maintask.mod:369
                    # ## COMMENT: todo delete schema ##
                    pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='AResetAllSchemas').data.Set( pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='AResetAllSchemas').data.Get() + (1) ) 
                # END FOR Statement
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetAllSchemas', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AResetAllSchemas', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' AResetAllSchemas(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AResetAllSchemas, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' AResetAllSchemas(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # Line Palletizer/maintask.mod:371
        # ## COMMENT: todo gestione errore del delete schema ##
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('AResetAllSchemas', pyrapid.Symbol.CreateProcedure(OrderedDict(), rapid_proc_AResetAllSchemas, error_rapid_proc_AResetAllSchemas, undo_rapid_proc_AResetAllSchemas), 'MAINTASK')
del rapid_proc_AResetAllSchemas
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:374
# Start Procedure Definition
def error_rapid_proc_ALoadSchemas (local_exception):
    return 0
def undo_rapid_proc_ALoadSchemas ():
    pass
def rapid_proc_ALoadSchemas (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='ALoadSchemas', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line Palletizer/maintask.mod:375
        pyrapid.Symbols().AddScopeSym('i', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='ALoadSchemas').data(None)))
        # end declaration
        # stantments
        #StatementAST ALoadSchemas
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='ALoadSchemas').data('LOAD/RELOAD ALL SCHEMAS'))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='ALoadSchemas').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchemas', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchemas', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchemas(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ALoadSchemas, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchemas(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST ALoadSchemas
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:379
                # FOR Statement
                pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='ALoadSchemas').data.Set( 1 ) 
                while ( pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='ALoadSchemas').data.Get() <= (pyrapid.Symbols().GetSymbol(symbolname='nPLACELINE', modulename='MAINTASK', functionname='ALoadSchemas').data.Get())): 
                    #StatementAST ALoadSchemas
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Call procedure ALoadSchema
                            parameters_actual = OrderedDict()
                            parameters_actual['nsch'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='ALoadSchemas').data(pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='ALoadSchemas').data.Get()))
                            pyrapid.Symbols().GetSymbol(symbolname='ALoadSchema', modulename='MAINTASK', functionname='ALoadSchemas').data(parameters_actual)
                            del parameters_actual
                            # End Call procedure
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchemas', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchemas', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchemas(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ALoadSchemas, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchemas(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                    pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='ALoadSchemas').data.Set( pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='ALoadSchemas').data.Get() + (1) ) 
                # END FOR Statement
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchemas', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchemas', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchemas(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ALoadSchemas, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchemas(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST ALoadSchemas
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='ALoadSchemas').data('END LOAD/RELOAD ALL SCHEMAS'))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='ALoadSchemas').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchemas', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ALoadSchemas', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchemas(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ALoadSchemas, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ALoadSchemas(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('ALoadSchemas', pyrapid.Symbol.CreateProcedure(OrderedDict(), rapid_proc_ALoadSchemas, error_rapid_proc_ALoadSchemas, undo_rapid_proc_ALoadSchemas), 'MAINTASK')
del rapid_proc_ALoadSchemas
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:387
# Start Procedure Definition
def error_rapid_proc_AStartQueue (local_exception):
    return 0
def undo_rapid_proc_AStartQueue ():
    pass
def rapid_proc_AStartQueue (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='AStartQueue', invalue=local_args_scope):
        pass
        # data definitions
        # stantments
        #StatementAST AStartQueue
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='AStartQueue').data('IsStartQueue on queue:'))
                # Line Palletizer/maintask.mod:388
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AStartQueue').data(pyrapid.Symbols().GetSymbol(symbolname='nQueue', modulename='MAINTASK', functionname='AStartQueue').data.Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='AStartQueue').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AStartQueue', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AStartQueue', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' AStartQueue(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AStartQueue, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' AStartQueue(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST AStartQueue
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='r_QueuePaused', modulename='MAINTASK', functionname='AStartQueue').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='nProdLine', modulename='MAINTASK', functionname='AStartQueue'), pyrapid.Symbols().GetSymbol(symbolname='nQueue', modulename='MAINTASK', functionname='AStartQueue')] ).Set( False ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AStartQueue', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AStartQueue', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' AStartQueue(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AStartQueue, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' AStartQueue(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('AStartQueue', pyrapid.Symbol.CreateProcedure(OrderedDict([('nProdLine', ('required', 'NORMAL', 'num', 0, [])), ('nQueue', ('required', 'NORMAL', 'num', 0, []))]), rapid_proc_AStartQueue, error_rapid_proc_AStartQueue, undo_rapid_proc_AStartQueue), 'MAINTASK')
del rapid_proc_AStartQueue
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:392
# Start Procedure Definition
def error_rapid_proc_AStopQueue (local_exception):
    return 0
def undo_rapid_proc_AStopQueue ():
    pass
def rapid_proc_AStopQueue (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='AStopQueue', invalue=local_args_scope):
        pass
        # data definitions
        # stantments
        #StatementAST AStopQueue
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='AStopQueue').data('IsStopQueue on queue:'))
                # Line Palletizer/maintask.mod:393
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AStopQueue').data(pyrapid.Symbols().GetSymbol(symbolname='nQueue', modulename='MAINTASK', functionname='AStopQueue').data.Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='AStopQueue').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AStopQueue', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AStopQueue', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' AStopQueue(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AStopQueue, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' AStopQueue(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST AStopQueue
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='r_QueuePaused', modulename='MAINTASK', functionname='AStopQueue').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='nProdLine', modulename='MAINTASK', functionname='AStopQueue'), pyrapid.Symbols().GetSymbol(symbolname='nQueue', modulename='MAINTASK', functionname='AStopQueue')] ).Set( True ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AStopQueue', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AStopQueue', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' AStopQueue(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AStopQueue, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' AStopQueue(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('AStopQueue', pyrapid.Symbol.CreateProcedure(OrderedDict([('nProdLine', ('required', 'NORMAL', 'num', 0, [])), ('nQueue', ('required', 'NORMAL', 'num', 0, []))]), rapid_proc_AStopQueue, error_rapid_proc_AStopQueue, undo_rapid_proc_AStopQueue), 'MAINTASK')
del rapid_proc_AStopQueue
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:397
# Start Procedure Definition
def error_rapid_proc_AOrderProduct (local_exception):
    return 0
def undo_rapid_proc_AOrderProduct ():
    pass
def rapid_proc_AOrderProduct (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='AOrderProduct', invalue=local_args_scope):
        pass
        # data definitions
        # stantments
        #StatementAST AOrderProduct
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='AOrderProduct').data('ORDER PRODUCT'))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='AOrderProduct').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AOrderProduct', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AOrderProduct', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' AOrderProduct(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AOrderProduct, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' AOrderProduct(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST AOrderProduct
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='AOrderProduct').data('LINE:'))
                # Line Palletizer/maintask.mod:399
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AOrderProduct').data(pyrapid.Symbols().GetSymbol(symbolname='nProdLine', modulename='MAINTASK', functionname='AOrderProduct').data.Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='AOrderProduct').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AOrderProduct', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AOrderProduct', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' AOrderProduct(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AOrderProduct, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' AOrderProduct(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST AOrderProduct
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='AOrderProduct').data('SRC LINE:'))
                # Line Palletizer/maintask.mod:400
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AOrderProduct').data(pyrapid.Symbols().GetSymbol(symbolname='r_TakeLine', modulename='MAINTASK', functionname='AOrderProduct').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='nProdLine', modulename='MAINTASK', functionname='AOrderProduct')] ).Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='AOrderProduct').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AOrderProduct', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AOrderProduct', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' AOrderProduct(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AOrderProduct, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' AOrderProduct(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST AOrderProduct
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='AOrderProduct').data('nprod:'))
                # Line Palletizer/maintask.mod:401
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AOrderProduct').data(pyrapid.Symbols().GetSymbol(symbolname='nProd', modulename='MAINTASK', functionname='AOrderProduct').data.Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='AOrderProduct').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AOrderProduct', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AOrderProduct', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' AOrderProduct(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AOrderProduct, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' AOrderProduct(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST AOrderProduct
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='AOrderProduct').data('disp:'))
                # Line Palletizer/maintask.mod:402
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AOrderProduct').data(pyrapid.Symbols().GetSymbol(symbolname='Dispo', modulename='MAINTASK', functionname='AOrderProduct').data.Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='AOrderProduct').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AOrderProduct', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AOrderProduct', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' AOrderProduct(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AOrderProduct, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' AOrderProduct(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('AOrderProduct', pyrapid.Symbol.CreateProcedure(OrderedDict([('nProdLine', ('required', 'NORMAL', 'num', 0, [])), ('nProd', ('required', 'NORMAL', 'num', 0, [])), ('Dispo', ('required', 'NORMAL', 'num', 0, []))]), rapid_proc_AOrderProduct, error_rapid_proc_AOrderProduct, undo_rapid_proc_AOrderProduct), 'MAINTASK')
del rapid_proc_AOrderProduct
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:405
# Start Procedure Definition
def error_rapid_proc_AOrderPallet (local_exception):
    return 0
def undo_rapid_proc_AOrderPallet ():
    pass
def rapid_proc_AOrderPallet (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='AOrderPallet', invalue=local_args_scope):
        pass
        # data definitions
        # stantments
        #StatementAST AOrderPallet
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='AOrderPallet').data('ORDER PALLET'))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='AOrderPallet').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AOrderPallet', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AOrderPallet', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' AOrderPallet(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AOrderPallet, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' AOrderPallet(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST AOrderPallet
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='AOrderPallet').data('LINE:'))
                # Line Palletizer/maintask.mod:407
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AOrderPallet').data(pyrapid.Symbols().GetSymbol(symbolname='nProdLine', modulename='MAINTASK', functionname='AOrderPallet').data.Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='AOrderPallet').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AOrderPallet', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AOrderPallet', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' AOrderPallet(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AOrderPallet, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' AOrderPallet(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('AOrderPallet', pyrapid.Symbol.CreateProcedure(OrderedDict([('nProdLine', ('required', 'NORMAL', 'num', 0, []))]), rapid_proc_AOrderPallet, error_rapid_proc_AOrderPallet, undo_rapid_proc_AOrderPallet), 'MAINTASK')
del rapid_proc_AOrderPallet
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:410
# Start Procedure Definition
def error_rapid_proc_ATakePallet (local_exception):
    return 0
def undo_rapid_proc_ATakePallet ():
    pass
def rapid_proc_ATakePallet (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='ATakePallet', invalue=local_args_scope):
        pass
        # data definitions
        # stantments
        #StatementAST ATakePallet
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='ATakePallet').data('TAKE PALLET'))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='ATakePallet').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ATakePallet', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ATakePallet', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ATakePallet(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ATakePallet, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ATakePallet(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST ATakePallet
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='ATakePallet').data('LINE:'))
                # Line Palletizer/maintask.mod:412
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='ATakePallet').data(pyrapid.Symbols().GetSymbol(symbolname='nProdLine', modulename='MAINTASK', functionname='ATakePallet').data.Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='ATakePallet').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ATakePallet', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ATakePallet', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ATakePallet(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ATakePallet, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ATakePallet(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # Line Palletizer/maintask.mod:413
        # ## COMMENT:todo ##
        #StatementAST ATakePallet
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure WaitTime
                parameters_actual = OrderedDict()
                parameters_actual['Time'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='ATakePallet').data(1))
                pyrapid.Symbols().GetSymbol(symbolname='WaitTime', modulename='MAINTASK', functionname='ATakePallet').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ATakePallet', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ATakePallet', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ATakePallet(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ATakePallet, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ATakePallet(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('ATakePallet', pyrapid.Symbol.CreateProcedure(OrderedDict([('nProdLine', ('required', 'NORMAL', 'num', 0, []))]), rapid_proc_ATakePallet, error_rapid_proc_ATakePallet, undo_rapid_proc_ATakePallet), 'MAINTASK')
del rapid_proc_ATakePallet
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:417
# Start Procedure Definition
def error_rapid_proc_APlacePallet (local_exception):
    return 0
def undo_rapid_proc_APlacePallet ():
    pass
def rapid_proc_APlacePallet (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='APlacePallet', invalue=local_args_scope):
        pass
        # data definitions
        # stantments
        #StatementAST APlacePallet
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='APlacePallet').data('PLACE PALLET'))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='APlacePallet').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlacePallet', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlacePallet', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' APlacePallet(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=APlacePallet, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' APlacePallet(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST APlacePallet
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='APlacePallet').data('LINE:'))
                # Line Palletizer/maintask.mod:419
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='APlacePallet').data(pyrapid.Symbols().GetSymbol(symbolname='nProdLine', modulename='MAINTASK', functionname='APlacePallet').data.Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='APlacePallet').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlacePallet', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlacePallet', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' APlacePallet(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=APlacePallet, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' APlacePallet(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # Line Palletizer/maintask.mod:420
        # ## COMMENT:todo ##
        #StatementAST APlacePallet
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure WaitTime
                parameters_actual = OrderedDict()
                parameters_actual['Time'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='APlacePallet').data(1))
                pyrapid.Symbols().GetSymbol(symbolname='WaitTime', modulename='MAINTASK', functionname='APlacePallet').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlacePallet', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlacePallet', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' APlacePallet(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=APlacePallet, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' APlacePallet(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('APlacePallet', pyrapid.Symbol.CreateProcedure(OrderedDict([('nProdLine', ('required', 'NORMAL', 'num', 0, []))]), rapid_proc_APlacePallet, error_rapid_proc_APlacePallet, undo_rapid_proc_APlacePallet), 'MAINTASK')
del rapid_proc_APlacePallet
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:424
# Start Procedure Definition
def error_rapid_proc_AExitPallet (local_exception):
    return 0
def undo_rapid_proc_AExitPallet ():
    pass
def rapid_proc_AExitPallet (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='AExitPallet', invalue=local_args_scope):
        pass
        # data definitions
        # stantments
        #StatementAST AExitPallet
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='AExitPallet').data('EXIT PALLET'))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='AExitPallet').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExitPallet', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExitPallet', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' AExitPallet(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AExitPallet, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' AExitPallet(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST AExitPallet
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='AExitPallet').data('LINE:'))
                # Line Palletizer/maintask.mod:426
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExitPallet').data(pyrapid.Symbols().GetSymbol(symbolname='nProdLine', modulename='MAINTASK', functionname='AExitPallet').data.Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='AExitPallet').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExitPallet', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExitPallet', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' AExitPallet(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AExitPallet, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' AExitPallet(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST AExitPallet
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure SetPalletExiting
                parameters_actual = OrderedDict()
                parameters_actual['nProdLine'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExitPallet').data(pyrapid.Symbols().GetSymbol(symbolname='nProdLine', modulename='MAINTASK', functionname='AExitPallet').data.Get()))
                pyrapid.Symbols().GetSymbol(symbolname='SetPalletExiting', modulename='MAINTASK', functionname='AExitPallet').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExitPallet', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExitPallet', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' AExitPallet(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AExitPallet, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' AExitPallet(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('AExitPallet', pyrapid.Symbol.CreateProcedure(OrderedDict([('nProdLine', ('required', 'NORMAL', 'num', 0, []))]), rapid_proc_AExitPallet, error_rapid_proc_AExitPallet, undo_rapid_proc_AExitPallet), 'MAINTASK')
del rapid_proc_AExitPallet
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:430
# Start Procedure Definition
def error_rapid_proc_ATakeSheet (local_exception):
    return 0
def undo_rapid_proc_ATakeSheet ():
    pass
def rapid_proc_ATakeSheet (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='ATakeSheet', invalue=local_args_scope):
        pass
        # data definitions
        # stantments
        #StatementAST ATakeSheet
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='ATakeSheet').data('TAKE Sheet'))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='ATakeSheet').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ATakeSheet', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ATakeSheet', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ATakeSheet(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ATakeSheet, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ATakeSheet(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST ATakeSheet
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='ATakeSheet').data('LINE:'))
                # Line Palletizer/maintask.mod:432
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='ATakeSheet').data(pyrapid.Symbols().GetSymbol(symbolname='nProdLine', modulename='MAINTASK', functionname='ATakeSheet').data.Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='ATakeSheet').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ATakeSheet', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ATakeSheet', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ATakeSheet(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ATakeSheet, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ATakeSheet(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('ATakeSheet', pyrapid.Symbol.CreateProcedure(OrderedDict([('nProdLine', ('required', 'NORMAL', 'num', 0, []))]), rapid_proc_ATakeSheet, error_rapid_proc_ATakeSheet, undo_rapid_proc_ATakeSheet), 'MAINTASK')
del rapid_proc_ATakeSheet
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:435
# Start Procedure Definition
def error_rapid_proc_APlaceSheet (local_exception):
    return 0
def undo_rapid_proc_APlaceSheet ():
    pass
def rapid_proc_APlaceSheet (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='APlaceSheet', invalue=local_args_scope):
        pass
        # data definitions
        # stantments
        #StatementAST APlaceSheet
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='APlaceSheet').data('PLACE Sheet'))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='APlaceSheet').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceSheet', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceSheet', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' APlaceSheet(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=APlaceSheet, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' APlaceSheet(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST APlaceSheet
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='APlaceSheet').data('LINE:'))
                # Line Palletizer/maintask.mod:437
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='APlaceSheet').data(pyrapid.Symbols().GetSymbol(symbolname='nProdLine', modulename='MAINTASK', functionname='APlaceSheet').data.Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='APlaceSheet').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceSheet', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceSheet', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' APlaceSheet(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=APlaceSheet, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' APlaceSheet(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('APlaceSheet', pyrapid.Symbol.CreateProcedure(OrderedDict([('nProdLine', ('required', 'NORMAL', 'num', 0, []))]), rapid_proc_APlaceSheet, error_rapid_proc_APlaceSheet, undo_rapid_proc_APlaceSheet), 'MAINTASK')
del rapid_proc_APlaceSheet
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:441
# Start Procedure Definition
def error_rapid_proc_ATakeProd (local_exception):
    return 0
def undo_rapid_proc_ATakeProd ():
    pass
def rapid_proc_ATakeProd (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='ATakeProd', invalue=local_args_scope):
        pass
        # data definitions
        # stantments
        #StatementAST ATakeProd
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='ATakeProd').data('PLACE TAKE Prod'))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='ATakeProd').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ATakeProd', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ATakeProd', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ATakeProd(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ATakeProd, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ATakeProd(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST ATakeProd
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='ATakeProd').data('LINE:'))
                # Line Palletizer/maintask.mod:443
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='ATakeProd').data(pyrapid.Symbols().GetSymbol(symbolname='nProdLine', modulename='MAINTASK', functionname='ATakeProd').data.Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='ATakeProd').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ATakeProd', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ATakeProd', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ATakeProd(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ATakeProd, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ATakeProd(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST ATakeProd
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='ATakeProd').data('X:'))
                # Line Palletizer/maintask.mod:444
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='ATakeProd').data(pyrapid.Symbols().GetSymbol(symbolname='x', modulename='MAINTASK', functionname='ATakeProd').data.Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='ATakeProd').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ATakeProd', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ATakeProd', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ATakeProd(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ATakeProd, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ATakeProd(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST ATakeProd
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='ATakeProd').data('Y:'))
                # Line Palletizer/maintask.mod:445
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='ATakeProd').data(pyrapid.Symbols().GetSymbol(symbolname='y', modulename='MAINTASK', functionname='ATakeProd').data.Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='ATakeProd').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ATakeProd', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ATakeProd', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ATakeProd(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ATakeProd, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ATakeProd(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST ATakeProd
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='ATakeProd').data('Z:'))
                # Line Palletizer/maintask.mod:446
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='ATakeProd').data(pyrapid.Symbols().GetSymbol(symbolname='z', modulename='MAINTASK', functionname='ATakeProd').data.Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='ATakeProd').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ATakeProd', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ATakeProd', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ATakeProd(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ATakeProd, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ATakeProd(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST ATakeProd
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='ATakeProd').data('rot:'))
                # Line Palletizer/maintask.mod:447
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='ATakeProd').data(pyrapid.Symbols().GetSymbol(symbolname='rot', modulename='MAINTASK', functionname='ATakeProd').data.Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='ATakeProd').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ATakeProd', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='ATakeProd', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' ATakeProd(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=ATakeProd, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' ATakeProd(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('ATakeProd', pyrapid.Symbol.CreateProcedure(OrderedDict([('nProdLine', ('required', 'NORMAL', 'num', 0, [])), ('x', ('required', 'NORMAL', 'num', 0, [])), ('y', ('required', 'NORMAL', 'num', 0, [])), ('z', ('required', 'NORMAL', 'num', 0, [])), ('rot', ('required', 'NORMAL', 'num', 0, []))]), rapid_proc_ATakeProd, error_rapid_proc_ATakeProd, undo_rapid_proc_ATakeProd), 'MAINTASK')
del rapid_proc_ATakeProd
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:450
# Start Procedure Definition
def error_rapid_proc_APlaceSingleProd (local_exception):
    return 0
def undo_rapid_proc_APlaceSingleProd ():
    pass
def rapid_proc_APlaceSingleProd (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='APlaceSingleProd', invalue=local_args_scope):
        pass
        # data definitions
        # stantments
        #StatementAST APlaceSingleProd
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='APlaceSingleProd').data('PLACE Single Prod'))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='APlaceSingleProd').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceSingleProd', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceSingleProd', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' APlaceSingleProd(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=APlaceSingleProd, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' APlaceSingleProd(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST APlaceSingleProd
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='APlaceSingleProd').data('LINE:'))
                # Line Palletizer/maintask.mod:452
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='APlaceSingleProd').data(pyrapid.Symbols().GetSymbol(symbolname='nProdLine', modulename='MAINTASK', functionname='APlaceSingleProd').data.Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='APlaceSingleProd').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceSingleProd', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceSingleProd', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' APlaceSingleProd(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=APlaceSingleProd, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' APlaceSingleProd(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST APlaceSingleProd
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='APlaceSingleProd').data('X:'))
                # Line Palletizer/maintask.mod:453
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='APlaceSingleProd').data(pyrapid.Symbols().GetSymbol(symbolname='x', modulename='MAINTASK', functionname='APlaceSingleProd').data.Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='APlaceSingleProd').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceSingleProd', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceSingleProd', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' APlaceSingleProd(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=APlaceSingleProd, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' APlaceSingleProd(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST APlaceSingleProd
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='APlaceSingleProd').data('Y:'))
                # Line Palletizer/maintask.mod:454
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='APlaceSingleProd').data(pyrapid.Symbols().GetSymbol(symbolname='y', modulename='MAINTASK', functionname='APlaceSingleProd').data.Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='APlaceSingleProd').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceSingleProd', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceSingleProd', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' APlaceSingleProd(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=APlaceSingleProd, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' APlaceSingleProd(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST APlaceSingleProd
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='APlaceSingleProd').data('Z:'))
                # Line Palletizer/maintask.mod:455
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='APlaceSingleProd').data(pyrapid.Symbols().GetSymbol(symbolname='z', modulename='MAINTASK', functionname='APlaceSingleProd').data.Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='APlaceSingleProd').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceSingleProd', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceSingleProd', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' APlaceSingleProd(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=APlaceSingleProd, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' APlaceSingleProd(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST APlaceSingleProd
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='APlaceSingleProd').data('rot:'))
                # Line Palletizer/maintask.mod:456
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='APlaceSingleProd').data(pyrapid.Symbols().GetSymbol(symbolname='rot', modulename='MAINTASK', functionname='APlaceSingleProd').data.Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='APlaceSingleProd').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceSingleProd', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceSingleProd', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' APlaceSingleProd(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=APlaceSingleProd, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' APlaceSingleProd(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST APlaceSingleProd
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='APlaceSingleProd').data('acc X:'))
                # Line Palletizer/maintask.mod:457
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='APlaceSingleProd').data(pyrapid.Symbols().GetSymbol(symbolname='acc_x', modulename='MAINTASK', functionname='APlaceSingleProd').data.Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='APlaceSingleProd').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceSingleProd', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceSingleProd', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' APlaceSingleProd(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=APlaceSingleProd, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' APlaceSingleProd(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST APlaceSingleProd
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='APlaceSingleProd').data('acc Y:'))
                # Line Palletizer/maintask.mod:458
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='APlaceSingleProd').data(pyrapid.Symbols().GetSymbol(symbolname='acc_y', modulename='MAINTASK', functionname='APlaceSingleProd').data.Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='APlaceSingleProd').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceSingleProd', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceSingleProd', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' APlaceSingleProd(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=APlaceSingleProd, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' APlaceSingleProd(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST APlaceSingleProd
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='APlaceSingleProd').data('acc Z:'))
                # Line Palletizer/maintask.mod:459
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='APlaceSingleProd').data(pyrapid.Symbols().GetSymbol(symbolname='acc_z', modulename='MAINTASK', functionname='APlaceSingleProd').data.Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='APlaceSingleProd').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceSingleProd', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceSingleProd', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' APlaceSingleProd(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=APlaceSingleProd, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' APlaceSingleProd(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('APlaceSingleProd', pyrapid.Symbol.CreateProcedure(OrderedDict([('nProdLine', ('required', 'NORMAL', 'num', 0, [])), ('x', ('required', 'NORMAL', 'num', 0, [])), ('y', ('required', 'NORMAL', 'num', 0, [])), ('z', ('required', 'NORMAL', 'num', 0, [])), ('rot', ('required', 'NORMAL', 'num', 0, [])), ('acc_x', ('required', 'NORMAL', 'num', 0, [])), ('acc_y', ('required', 'NORMAL', 'num', 0, [])), ('acc_z', ('required', 'NORMAL', 'num', 0, []))]), rapid_proc_APlaceSingleProd, error_rapid_proc_APlaceSingleProd, undo_rapid_proc_APlaceSingleProd), 'MAINTASK')
del rapid_proc_APlaceSingleProd
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:462
# Start Procedure Definition
def error_rapid_proc_APlaceDoubleProd (local_exception):
    return 0
def undo_rapid_proc_APlaceDoubleProd ():
    pass
def rapid_proc_APlaceDoubleProd (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='APlaceDoubleProd', invalue=local_args_scope):
        pass
        # data definitions
        # stantments
        #StatementAST APlaceDoubleProd
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='APlaceDoubleProd').data('PLACE Double Prod'))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='APlaceDoubleProd').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=APlaceDoubleProd, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST APlaceDoubleProd
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='APlaceDoubleProd').data('LINE:'))
                # Line Palletizer/maintask.mod:464
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='APlaceDoubleProd').data(pyrapid.Symbols().GetSymbol(symbolname='nProdLine', modulename='MAINTASK', functionname='APlaceDoubleProd').data.Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='APlaceDoubleProd').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=APlaceDoubleProd, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST APlaceDoubleProd
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='APlaceDoubleProd').data('X:'))
                # Line Palletizer/maintask.mod:465
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='APlaceDoubleProd').data(pyrapid.Symbols().GetSymbol(symbolname='x', modulename='MAINTASK', functionname='APlaceDoubleProd').data.GetElem( [1] ).Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='APlaceDoubleProd').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=APlaceDoubleProd, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST APlaceDoubleProd
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='APlaceDoubleProd').data('Y:'))
                # Line Palletizer/maintask.mod:466
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='APlaceDoubleProd').data(pyrapid.Symbols().GetSymbol(symbolname='y', modulename='MAINTASK', functionname='APlaceDoubleProd').data.GetElem( [1] ).Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='APlaceDoubleProd').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=APlaceDoubleProd, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST APlaceDoubleProd
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='APlaceDoubleProd').data('Z:'))
                # Line Palletizer/maintask.mod:467
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='APlaceDoubleProd').data(pyrapid.Symbols().GetSymbol(symbolname='z', modulename='MAINTASK', functionname='APlaceDoubleProd').data.GetElem( [1] ).Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='APlaceDoubleProd').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=APlaceDoubleProd, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST APlaceDoubleProd
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='APlaceDoubleProd').data('rot:'))
                # Line Palletizer/maintask.mod:468
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='APlaceDoubleProd').data(pyrapid.Symbols().GetSymbol(symbolname='rot', modulename='MAINTASK', functionname='APlaceDoubleProd').data.GetElem( [1] ).Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='APlaceDoubleProd').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=APlaceDoubleProd, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST APlaceDoubleProd
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='APlaceDoubleProd').data('acc X:'))
                # Line Palletizer/maintask.mod:469
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='APlaceDoubleProd').data(pyrapid.Symbols().GetSymbol(symbolname='acc_x', modulename='MAINTASK', functionname='APlaceDoubleProd').data.GetElem( [1] ).Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='APlaceDoubleProd').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=APlaceDoubleProd, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST APlaceDoubleProd
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='APlaceDoubleProd').data('acc Y:'))
                # Line Palletizer/maintask.mod:470
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='APlaceDoubleProd').data(pyrapid.Symbols().GetSymbol(symbolname='acc_y', modulename='MAINTASK', functionname='APlaceDoubleProd').data.GetElem( [1] ).Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='APlaceDoubleProd').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=APlaceDoubleProd, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST APlaceDoubleProd
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='APlaceDoubleProd').data('acc Z:'))
                # Line Palletizer/maintask.mod:471
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='APlaceDoubleProd').data(pyrapid.Symbols().GetSymbol(symbolname='acc_z', modulename='MAINTASK', functionname='APlaceDoubleProd').data.GetElem( [1] ).Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='APlaceDoubleProd').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=APlaceDoubleProd, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST APlaceDoubleProd
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='APlaceDoubleProd').data('X:'))
                # Line Palletizer/maintask.mod:473
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='APlaceDoubleProd').data(pyrapid.Symbols().GetSymbol(symbolname='x', modulename='MAINTASK', functionname='APlaceDoubleProd').data.GetElem( [2] ).Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='APlaceDoubleProd').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=APlaceDoubleProd, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST APlaceDoubleProd
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='APlaceDoubleProd').data('Y:'))
                # Line Palletizer/maintask.mod:474
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='APlaceDoubleProd').data(pyrapid.Symbols().GetSymbol(symbolname='y', modulename='MAINTASK', functionname='APlaceDoubleProd').data.GetElem( [2] ).Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='APlaceDoubleProd').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=APlaceDoubleProd, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST APlaceDoubleProd
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='APlaceDoubleProd').data('Z:'))
                # Line Palletizer/maintask.mod:475
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='APlaceDoubleProd').data(pyrapid.Symbols().GetSymbol(symbolname='z', modulename='MAINTASK', functionname='APlaceDoubleProd').data.GetElem( [2] ).Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='APlaceDoubleProd').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=APlaceDoubleProd, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST APlaceDoubleProd
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='APlaceDoubleProd').data('rot:'))
                # Line Palletizer/maintask.mod:476
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='APlaceDoubleProd').data(pyrapid.Symbols().GetSymbol(symbolname='rot', modulename='MAINTASK', functionname='APlaceDoubleProd').data.GetElem( [2] ).Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='APlaceDoubleProd').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=APlaceDoubleProd, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST APlaceDoubleProd
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='APlaceDoubleProd').data('acc X:'))
                # Line Palletizer/maintask.mod:477
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='APlaceDoubleProd').data(pyrapid.Symbols().GetSymbol(symbolname='acc_x', modulename='MAINTASK', functionname='APlaceDoubleProd').data.GetElem( [2] ).Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='APlaceDoubleProd').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=APlaceDoubleProd, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST APlaceDoubleProd
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='APlaceDoubleProd').data('acc Y:'))
                # Line Palletizer/maintask.mod:478
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='APlaceDoubleProd').data(pyrapid.Symbols().GetSymbol(symbolname='acc_y', modulename='MAINTASK', functionname='APlaceDoubleProd').data.GetElem( [2] ).Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='APlaceDoubleProd').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=APlaceDoubleProd, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST APlaceDoubleProd
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='APlaceDoubleProd').data('acc Z:'))
                # Line Palletizer/maintask.mod:479
                parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='APlaceDoubleProd').data(pyrapid.Symbols().GetSymbol(symbolname='acc_z', modulename='MAINTASK', functionname='APlaceDoubleProd').data.GetElem( [2] ).Get()))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='APlaceDoubleProd').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=APlaceDoubleProd, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' APlaceDoubleProd(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('APlaceDoubleProd', pyrapid.Symbol.CreateProcedure(OrderedDict([('nProdLine', ('required', 'NORMAL', 'num', 0, [])), ('x', ('required', 'NORMAL', 'num', 1, [])), ('y', ('required', 'NORMAL', 'num', 1, [])), ('z', ('required', 'NORMAL', 'num', 1, [])), ('rot', ('required', 'NORMAL', 'num', 1, [])), ('acc_x', ('required', 'NORMAL', 'num', 1, [])), ('acc_y', ('required', 'NORMAL', 'num', 1, [])), ('acc_z', ('required', 'NORMAL', 'num', 1, []))]), rapid_proc_APlaceDoubleProd, error_rapid_proc_APlaceDoubleProd, undo_rapid_proc_APlaceDoubleProd), 'MAINTASK')
del rapid_proc_APlaceDoubleProd
# End Procedure Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:483
# Start Function Definition
def error_rapid_func_CommandCanBeExecuted (local_exception):
    return 0
def undo_rapid_func_CommandCanBeExecuted ():
    pass
def rapid_func_CommandCanBeExecuted (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='CommandCanBeExecuted', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line Palletizer/maintask.mod:484
        pyrapid.Symbols().AddScopeSym('fullcommand', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='CommandCanBeExecuted').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:485
        pyrapid.Symbols().AddScopeSym('param_queue1', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='CommandCanBeExecuted').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:486
        pyrapid.Symbols().AddScopeSym('param_queue2', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='CommandCanBeExecuted').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:487
        pyrapid.Symbols().AddScopeSym('param_queue3', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='CommandCanBeExecuted').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:488
        pyrapid.Symbols().AddScopeSym('param_queue4', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='CommandCanBeExecuted').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:490
        pyrapid.Symbols().AddScopeSym('v_param_queue1', pyrapid.Symbol.CreateVar( pyrapid.rapid_array([2], pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='CommandCanBeExecuted').data, None) ))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:491
        pyrapid.Symbols().AddScopeSym('v_param_queue2', pyrapid.Symbol.CreateVar( pyrapid.rapid_array([2], pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='CommandCanBeExecuted').data, None) ))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:492
        pyrapid.Symbols().AddScopeSym('v_param_queue3', pyrapid.Symbol.CreateVar( pyrapid.rapid_array([2], pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='CommandCanBeExecuted').data, None) ))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:493
        pyrapid.Symbols().AddScopeSym('v_param_queue4', pyrapid.Symbol.CreateVar( pyrapid.rapid_array([2], pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='CommandCanBeExecuted').data, None) ))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:494
        pyrapid.Symbols().AddScopeSym('v_param_queue5', pyrapid.Symbol.CreateVar( pyrapid.rapid_array([2], pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='CommandCanBeExecuted').data, None) ))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:495
        pyrapid.Symbols().AddScopeSym('v_param_queue6', pyrapid.Symbol.CreateVar( pyrapid.rapid_array([2], pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='CommandCanBeExecuted').data, None) ))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:496
        pyrapid.Symbols().AddScopeSym('v_param_queue7', pyrapid.Symbol.CreateVar( pyrapid.rapid_array([2], pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='CommandCanBeExecuted').data, None) ))
        # end declaration
        # stantments
        #StatementAST CommandCanBeExecuted
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:498
                if (pyrapid.Symbols().GetSymbol(symbolname='r_QueuePaused', modulename='MAINTASK', functionname='CommandCanBeExecuted').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='CommandCanBeExecuted').data.GetElem('nProdLine'), pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='CommandCanBeExecuted').data.GetElem('nQueue')] ).Get()) :
                    pass
                    #StatementAST CommandCanBeExecuted
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line Palletizer/maintask.mod:499
                            return ( False )
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=CommandCanBeExecuted, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                else:
                    #StatementAST CommandCanBeExecuted
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            pyrapid.Symbols().GetSymbol(symbolname='fullcommand', modulename='MAINTASK', functionname='CommandCanBeExecuted').data.Set( pyrapid.Symbols().GetSymbol(symbolname='r_ActionType_Name', modulename='MAINTASK', functionname='CommandCanBeExecuted').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='CommandCanBeExecuted').data.GetElem('nProdLine'), pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='CommandCanBeExecuted').data.GetElem('nQueue'), pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='CommandCanBeExecuted').data.GetElem('nStep')] ).Get() ) 
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=CommandCanBeExecuted, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                    #StatementAST CommandCanBeExecuted
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line Palletizer/maintask.mod:503
                            if (pyrapid.Symbols().GetSymbol(symbolname='IsStartQueue', modulename='MAINTASK', functionname='CommandCanBeExecuted').data( {'command':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='CommandCanBeExecuted').data(pyrapid.Symbols().GetSymbol(symbolname='fullcommand', modulename='MAINTASK', functionname='CommandCanBeExecuted').data.Get())),'queue':pyrapid.Symbols().GetSymbol(symbolname='param_queue1', modulename='MAINTASK', functionname='CommandCanBeExecuted')} )) :
                                pass
                                #StatementAST CommandCanBeExecuted
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Line Palletizer/maintask.mod:504
                                        return ( True )
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=CommandCanBeExecuted, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                            # Line Palletizer/maintask.mod:505
                            elif (pyrapid.Symbols().GetSymbol(symbolname='IsStopQueue', modulename='MAINTASK', functionname='CommandCanBeExecuted').data( {'command':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='CommandCanBeExecuted').data(pyrapid.Symbols().GetSymbol(symbolname='fullcommand', modulename='MAINTASK', functionname='CommandCanBeExecuted').data.Get())),'queue':pyrapid.Symbols().GetSymbol(symbolname='param_queue1', modulename='MAINTASK', functionname='CommandCanBeExecuted')} )) :
                                pass
                                #StatementAST CommandCanBeExecuted
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Line Palletizer/maintask.mod:506
                                        return ( True )
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=CommandCanBeExecuted, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                            # Line Palletizer/maintask.mod:507
                            elif (pyrapid.Symbols().GetSymbol(symbolname='IsOrderProduct', modulename='MAINTASK', functionname='CommandCanBeExecuted').data( {'command':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='CommandCanBeExecuted').data(pyrapid.Symbols().GetSymbol(symbolname='fullcommand', modulename='MAINTASK', functionname='CommandCanBeExecuted').data.Get())),'nprod':pyrapid.Symbols().GetSymbol(symbolname='param_queue1', modulename='MAINTASK', functionname='CommandCanBeExecuted'),'disposition':pyrapid.Symbols().GetSymbol(symbolname='param_queue2', modulename='MAINTASK', functionname='CommandCanBeExecuted')} )) :
                                pass
                                #StatementAST CommandCanBeExecuted
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Line Palletizer/maintask.mod:508
                                        return ( True )
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=CommandCanBeExecuted, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                            # Line Palletizer/maintask.mod:509
                            elif (pyrapid.Symbols().GetSymbol(symbolname='IsOrderPallet', modulename='MAINTASK', functionname='CommandCanBeExecuted').data( {'command':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='CommandCanBeExecuted').data(pyrapid.Symbols().GetSymbol(symbolname='fullcommand', modulename='MAINTASK', functionname='CommandCanBeExecuted').data.Get()))} )) :
                                pass
                                #StatementAST CommandCanBeExecuted
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Line Palletizer/maintask.mod:510
                                        if (pyrapid.Symbols().GetSymbol(symbolname='IsPalletExiting', modulename='MAINTASK', functionname='CommandCanBeExecuted').data( {'nProdLine':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='CommandCanBeExecuted').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='CommandCanBeExecuted').data.GetElem('nProdLine').Get()))} )) :
                                            pass
                                            #StatementAST CommandCanBeExecuted
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    # Line Palletizer/maintask.mod:511
                                                    return ( False )
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=CommandCanBeExecuted, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=CommandCanBeExecuted, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                # Line Palletizer/maintask.mod:513
                                # ## COMMENT:TODO NO PALLET PRESENT ##
                                #StatementAST CommandCanBeExecuted
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Line Palletizer/maintask.mod:514
                                        return ( True )
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=CommandCanBeExecuted, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                            # Line Palletizer/maintask.mod:515
                            elif (pyrapid.Symbols().GetSymbol(symbolname='IsTakePallet', modulename='MAINTASK', functionname='CommandCanBeExecuted').data( {'command':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='CommandCanBeExecuted').data(pyrapid.Symbols().GetSymbol(symbolname='fullcommand', modulename='MAINTASK', functionname='CommandCanBeExecuted').data.Get()))} )) :
                                pass
                                #StatementAST CommandCanBeExecuted
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Line Palletizer/maintask.mod:516
                                        if (pyrapid.Symbols().GetSymbol(symbolname='IsPalletExiting', modulename='MAINTASK', functionname='CommandCanBeExecuted').data( {'nProdLine':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='CommandCanBeExecuted').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='CommandCanBeExecuted').data.GetElem('nProdLine').Get()))} )) :
                                            pass
                                            #StatementAST CommandCanBeExecuted
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    # Line Palletizer/maintask.mod:517
                                                    return ( False )
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=CommandCanBeExecuted, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=CommandCanBeExecuted, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                # Line Palletizer/maintask.mod:519
                                # ## COMMENT:TODO NO PALLET PRESENT ##
                                #StatementAST CommandCanBeExecuted
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Line Palletizer/maintask.mod:520
                                        return ( True )
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=CommandCanBeExecuted, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                            # Line Palletizer/maintask.mod:521
                            elif (pyrapid.Symbols().GetSymbol(symbolname='IsPlacePallet', modulename='MAINTASK', functionname='CommandCanBeExecuted').data( {'command':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='CommandCanBeExecuted').data(pyrapid.Symbols().GetSymbol(symbolname='fullcommand', modulename='MAINTASK', functionname='CommandCanBeExecuted').data.Get()))} )) :
                                pass
                                #StatementAST CommandCanBeExecuted
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Line Palletizer/maintask.mod:522
                                        if (pyrapid.Symbols().GetSymbol(symbolname='IsPalletExiting', modulename='MAINTASK', functionname='CommandCanBeExecuted').data( {'nProdLine':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='CommandCanBeExecuted').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='CommandCanBeExecuted').data.GetElem('nProdLine').Get()))} )) :
                                            pass
                                            #StatementAST CommandCanBeExecuted
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    # Line Palletizer/maintask.mod:523
                                                    return ( False )
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=CommandCanBeExecuted, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=CommandCanBeExecuted, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                # Line Palletizer/maintask.mod:525
                                # ## COMMENT:TODO NO PALLET PRESENT ##
                                #StatementAST CommandCanBeExecuted
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Line Palletizer/maintask.mod:526
                                        return ( True )
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=CommandCanBeExecuted, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                            # Line Palletizer/maintask.mod:527
                            elif (pyrapid.Symbols().GetSymbol(symbolname='IsExitPallet', modulename='MAINTASK', functionname='CommandCanBeExecuted').data( {'command':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='CommandCanBeExecuted').data(pyrapid.Symbols().GetSymbol(symbolname='fullcommand', modulename='MAINTASK', functionname='CommandCanBeExecuted').data.Get()))} )) :
                                pass
                                #StatementAST CommandCanBeExecuted
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Line Palletizer/maintask.mod:528
                                        return ( True )
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=CommandCanBeExecuted, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                            # Line Palletizer/maintask.mod:529
                            elif (pyrapid.Symbols().GetSymbol(symbolname='IsTakeSheet', modulename='MAINTASK', functionname='CommandCanBeExecuted').data( {'command':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='CommandCanBeExecuted').data(pyrapid.Symbols().GetSymbol(symbolname='fullcommand', modulename='MAINTASK', functionname='CommandCanBeExecuted').data.Get()))} )) :
                                pass
                                #StatementAST CommandCanBeExecuted
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Line Palletizer/maintask.mod:530
                                        return ( True )
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=CommandCanBeExecuted, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                            # Line Palletizer/maintask.mod:531
                            elif (pyrapid.Symbols().GetSymbol(symbolname='IsPlaceSheet', modulename='MAINTASK', functionname='CommandCanBeExecuted').data( {'command':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='CommandCanBeExecuted').data(pyrapid.Symbols().GetSymbol(symbolname='fullcommand', modulename='MAINTASK', functionname='CommandCanBeExecuted').data.Get()))} )) :
                                pass
                                #StatementAST CommandCanBeExecuted
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Line Palletizer/maintask.mod:532
                                        return ( True )
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=CommandCanBeExecuted, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                            # Line Palletizer/maintask.mod:533
                            elif (pyrapid.Symbols().GetSymbol(symbolname='IsTakeProduct', modulename='MAINTASK', functionname='CommandCanBeExecuted').data( {'command':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='CommandCanBeExecuted').data(pyrapid.Symbols().GetSymbol(symbolname='fullcommand', modulename='MAINTASK', functionname='CommandCanBeExecuted').data.Get())),'x':pyrapid.Symbols().GetSymbol(symbolname='param_queue1', modulename='MAINTASK', functionname='CommandCanBeExecuted'),'y':pyrapid.Symbols().GetSymbol(symbolname='param_queue2', modulename='MAINTASK', functionname='CommandCanBeExecuted'),'z':pyrapid.Symbols().GetSymbol(symbolname='param_queue3', modulename='MAINTASK', functionname='CommandCanBeExecuted'),'rot':pyrapid.Symbols().GetSymbol(symbolname='param_queue4', modulename='MAINTASK', functionname='CommandCanBeExecuted')} )) :
                                pass
                                #StatementAST CommandCanBeExecuted
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Line Palletizer/maintask.mod:534
                                        return ( True )
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=CommandCanBeExecuted, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                            # Line Palletizer/maintask.mod:535
                            elif (pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK', functionname='CommandCanBeExecuted').data( {'command':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='CommandCanBeExecuted').data(pyrapid.Symbols().GetSymbol(symbolname='fullcommand', modulename='MAINTASK', functionname='CommandCanBeExecuted').data.Get())),'index':pyrapid.Symbols().GetSymbol(symbolname='param_queue1', modulename='MAINTASK', functionname='CommandCanBeExecuted'),'x':pyrapid.Symbols().GetSymbol(symbolname='v_param_queue1', modulename='MAINTASK', functionname='CommandCanBeExecuted'),'y':pyrapid.Symbols().GetSymbol(symbolname='v_param_queue2', modulename='MAINTASK', functionname='CommandCanBeExecuted'),'z':pyrapid.Symbols().GetSymbol(symbolname='v_param_queue3', modulename='MAINTASK', functionname='CommandCanBeExecuted'),'rot':pyrapid.Symbols().GetSymbol(symbolname='v_param_queue4', modulename='MAINTASK', functionname='CommandCanBeExecuted'),'acc_x':pyrapid.Symbols().GetSymbol(symbolname='v_param_queue5', modulename='MAINTASK', functionname='CommandCanBeExecuted'),'acc_y':pyrapid.Symbols().GetSymbol(symbolname='v_param_queue6', modulename='MAINTASK', functionname='CommandCanBeExecuted'),'acc_z':pyrapid.Symbols().GetSymbol(symbolname='v_param_queue7', modulename='MAINTASK', functionname='CommandCanBeExecuted')} )) :
                                pass
                                #StatementAST CommandCanBeExecuted
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Line Palletizer/maintask.mod:536
                                        return ( True )
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=CommandCanBeExecuted, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                            else:
                                #StatementAST CommandCanBeExecuted
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Call procedure TPWrite
                                        parameters_actual = OrderedDict()
                                        parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='CommandCanBeExecuted').data(( 'command not yet supported and so can not be done: ' + pyrapid.Symbols().GetSymbol(symbolname='fullcommand', modulename='MAINTASK', functionname='CommandCanBeExecuted').data.Get() )))
                                        pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='CommandCanBeExecuted').data(parameters_actual)
                                        del parameters_actual
                                        # End Call procedure
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=CommandCanBeExecuted, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                #StatementAST CommandCanBeExecuted
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Line Palletizer/maintask.mod:539
                                        return ( False )
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=CommandCanBeExecuted, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=CommandCanBeExecuted, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=CommandCanBeExecuted, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST CommandCanBeExecuted
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:542
                return ( False )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=CommandCanBeExecuted, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' CommandCanBeExecuted(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('CommandCanBeExecuted', pyrapid.Symbol.CreateFunction(OrderedDict([('command', ('required', 'NORMAL', 'todoType', 0, []))]), pyrapid.Symbols().GetSymbol('bool', 'MAINTASK', None), rapid_func_CommandCanBeExecuted, error_rapid_func_CommandCanBeExecuted, undo_rapid_func_CommandCanBeExecuted), 'MAINTASK')
del rapid_func_CommandCanBeExecuted
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:545
# Start Procedure Definition
def error_rapid_proc_AExecute (local_exception):
    return 0
def undo_rapid_proc_AExecute ():
    pass
def rapid_proc_AExecute (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='AExecute', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line Palletizer/maintask.mod:546
        pyrapid.Symbols().AddScopeSym('fullcommand', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='AExecute').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:547
        pyrapid.Symbols().AddScopeSym('param_queue1', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:548
        pyrapid.Symbols().AddScopeSym('param_queue2', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:549
        pyrapid.Symbols().AddScopeSym('param_queue3', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:550
        pyrapid.Symbols().AddScopeSym('param_queue4', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:552
        pyrapid.Symbols().AddScopeSym('v_param_queue1', pyrapid.Symbol.CreateVar( pyrapid.rapid_array([2], pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data, None) ))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:553
        pyrapid.Symbols().AddScopeSym('v_param_queue2', pyrapid.Symbol.CreateVar( pyrapid.rapid_array([2], pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data, None) ))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:554
        pyrapid.Symbols().AddScopeSym('v_param_queue3', pyrapid.Symbol.CreateVar( pyrapid.rapid_array([2], pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data, None) ))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:555
        pyrapid.Symbols().AddScopeSym('v_param_queue4', pyrapid.Symbol.CreateVar( pyrapid.rapid_array([2], pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data, None) ))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:556
        pyrapid.Symbols().AddScopeSym('v_param_queue5', pyrapid.Symbol.CreateVar( pyrapid.rapid_array([2], pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data, None) ))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:557
        pyrapid.Symbols().AddScopeSym('v_param_queue6', pyrapid.Symbol.CreateVar( pyrapid.rapid_array([2], pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data, None) ))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:558
        pyrapid.Symbols().AddScopeSym('v_param_queue7', pyrapid.Symbol.CreateVar( pyrapid.rapid_array([2], pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data, None) ))
        # end declaration
        # stantments
        #StatementAST AExecute
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='fullcommand', modulename='MAINTASK', functionname='AExecute').data.Set( pyrapid.Symbols().GetSymbol(symbolname='r_ActionType_Name', modulename='MAINTASK', functionname='AExecute').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='AExecute').data.GetElem('nProdLine'), pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='AExecute').data.GetElem('nQueue'), pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='AExecute').data.GetElem('nStep')] ).Get() ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AExecute, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST AExecute
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:562
                if (pyrapid.Symbols().GetSymbol(symbolname='IsStartQueue', modulename='MAINTASK', functionname='AExecute').data( {'command':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='fullcommand', modulename='MAINTASK', functionname='AExecute').data.Get())),'queue':pyrapid.Symbols().GetSymbol(symbolname='param_queue1', modulename='MAINTASK', functionname='AExecute')} )) :
                    pass
                    #StatementAST AExecute
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Call procedure AStartQueue
                            parameters_actual = OrderedDict()
                            parameters_actual['nProdLine'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='AExecute').data.GetElem('nProdLine').Get()))
                            parameters_actual['nQueue'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='param_queue1', modulename='MAINTASK', functionname='AExecute').data.Get()))
                            pyrapid.Symbols().GetSymbol(symbolname='AStartQueue', modulename='MAINTASK', functionname='AExecute').data(parameters_actual)
                            del parameters_actual
                            # End Call procedure
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AExecute, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                # Line Palletizer/maintask.mod:564
                elif (pyrapid.Symbols().GetSymbol(symbolname='IsStopQueue', modulename='MAINTASK', functionname='AExecute').data( {'command':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='fullcommand', modulename='MAINTASK', functionname='AExecute').data.Get())),'queue':pyrapid.Symbols().GetSymbol(symbolname='param_queue1', modulename='MAINTASK', functionname='AExecute')} )) :
                    pass
                    #StatementAST AExecute
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Call procedure AStopQueue
                            parameters_actual = OrderedDict()
                            parameters_actual['nProdLine'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='AExecute').data.GetElem('nProdLine').Get()))
                            parameters_actual['nQueue'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='param_queue1', modulename='MAINTASK', functionname='AExecute').data.Get()))
                            pyrapid.Symbols().GetSymbol(symbolname='AStopQueue', modulename='MAINTASK', functionname='AExecute').data(parameters_actual)
                            del parameters_actual
                            # End Call procedure
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AExecute, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                # Line Palletizer/maintask.mod:566
                elif (pyrapid.Symbols().GetSymbol(symbolname='IsOrderProduct', modulename='MAINTASK', functionname='AExecute').data( {'command':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='fullcommand', modulename='MAINTASK', functionname='AExecute').data.Get())),'nprod':pyrapid.Symbols().GetSymbol(symbolname='param_queue1', modulename='MAINTASK', functionname='AExecute'),'disposition':pyrapid.Symbols().GetSymbol(symbolname='param_queue2', modulename='MAINTASK', functionname='AExecute')} )) :
                    pass
                    #StatementAST AExecute
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Call procedure AOrderProduct
                            parameters_actual = OrderedDict()
                            parameters_actual['nProdLine'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='AExecute').data.GetElem('nProdLine').Get()))
                            parameters_actual['nProd'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='param_queue1', modulename='MAINTASK', functionname='AExecute').data.Get()))
                            parameters_actual['Dispo'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='param_queue2', modulename='MAINTASK', functionname='AExecute').data.Get()))
                            pyrapid.Symbols().GetSymbol(symbolname='AOrderProduct', modulename='MAINTASK', functionname='AExecute').data(parameters_actual)
                            del parameters_actual
                            # End Call procedure
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AExecute, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                # Line Palletizer/maintask.mod:568
                elif (pyrapid.Symbols().GetSymbol(symbolname='IsOrderPallet', modulename='MAINTASK', functionname='AExecute').data( {'command':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='fullcommand', modulename='MAINTASK', functionname='AExecute').data.Get()))} )) :
                    pass
                    #StatementAST AExecute
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Call procedure AOrderPallet
                            parameters_actual = OrderedDict()
                            parameters_actual['nProdLine'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='AExecute').data.GetElem('nProdLine').Get()))
                            pyrapid.Symbols().GetSymbol(symbolname='AOrderPallet', modulename='MAINTASK', functionname='AExecute').data(parameters_actual)
                            del parameters_actual
                            # End Call procedure
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AExecute, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                # Line Palletizer/maintask.mod:570
                elif (pyrapid.Symbols().GetSymbol(symbolname='IsTakePallet', modulename='MAINTASK', functionname='AExecute').data( {'command':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='fullcommand', modulename='MAINTASK', functionname='AExecute').data.Get()))} )) :
                    pass
                    #StatementAST AExecute
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Call procedure ATakePallet
                            parameters_actual = OrderedDict()
                            parameters_actual['nProdLine'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='AExecute').data.GetElem('nProdLine').Get()))
                            pyrapid.Symbols().GetSymbol(symbolname='ATakePallet', modulename='MAINTASK', functionname='AExecute').data(parameters_actual)
                            del parameters_actual
                            # End Call procedure
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AExecute, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                # Line Palletizer/maintask.mod:572
                elif (pyrapid.Symbols().GetSymbol(symbolname='IsPlacePallet', modulename='MAINTASK', functionname='AExecute').data( {'command':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='fullcommand', modulename='MAINTASK', functionname='AExecute').data.Get()))} )) :
                    pass
                    #StatementAST AExecute
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Call procedure APlacePallet
                            parameters_actual = OrderedDict()
                            parameters_actual['nProdLine'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='AExecute').data.GetElem('nProdLine').Get()))
                            pyrapid.Symbols().GetSymbol(symbolname='APlacePallet', modulename='MAINTASK', functionname='AExecute').data(parameters_actual)
                            del parameters_actual
                            # End Call procedure
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AExecute, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                # Line Palletizer/maintask.mod:574
                elif (pyrapid.Symbols().GetSymbol(symbolname='IsExitPallet', modulename='MAINTASK', functionname='AExecute').data( {'command':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='fullcommand', modulename='MAINTASK', functionname='AExecute').data.Get()))} )) :
                    pass
                    #StatementAST AExecute
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Call procedure AExitPallet
                            parameters_actual = OrderedDict()
                            parameters_actual['nProdLine'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='AExecute').data.GetElem('nProdLine').Get()))
                            pyrapid.Symbols().GetSymbol(symbolname='AExitPallet', modulename='MAINTASK', functionname='AExecute').data(parameters_actual)
                            del parameters_actual
                            # End Call procedure
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AExecute, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                # Line Palletizer/maintask.mod:576
                elif (pyrapid.Symbols().GetSymbol(symbolname='IsTakeSheet', modulename='MAINTASK', functionname='AExecute').data( {'command':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='fullcommand', modulename='MAINTASK', functionname='AExecute').data.Get()))} )) :
                    pass
                    #StatementAST AExecute
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Call procedure ATakeSheet
                            parameters_actual = OrderedDict()
                            parameters_actual['nProdLine'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='AExecute').data.GetElem('nProdLine').Get()))
                            pyrapid.Symbols().GetSymbol(symbolname='ATakeSheet', modulename='MAINTASK', functionname='AExecute').data(parameters_actual)
                            del parameters_actual
                            # End Call procedure
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AExecute, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                # Line Palletizer/maintask.mod:578
                elif (pyrapid.Symbols().GetSymbol(symbolname='IsPlaceSheet', modulename='MAINTASK', functionname='AExecute').data( {'command':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='fullcommand', modulename='MAINTASK', functionname='AExecute').data.Get()))} )) :
                    pass
                    #StatementAST AExecute
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Call procedure APlaceSheet
                            parameters_actual = OrderedDict()
                            parameters_actual['nProdLine'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='AExecute').data.GetElem('nProdLine').Get()))
                            pyrapid.Symbols().GetSymbol(symbolname='APlaceSheet', modulename='MAINTASK', functionname='AExecute').data(parameters_actual)
                            del parameters_actual
                            # End Call procedure
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AExecute, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                # Line Palletizer/maintask.mod:580
                elif (pyrapid.Symbols().GetSymbol(symbolname='IsTakeProduct', modulename='MAINTASK', functionname='AExecute').data( {'command':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='fullcommand', modulename='MAINTASK', functionname='AExecute').data.Get())),'x':pyrapid.Symbols().GetSymbol(symbolname='param_queue1', modulename='MAINTASK', functionname='AExecute'),'y':pyrapid.Symbols().GetSymbol(symbolname='param_queue2', modulename='MAINTASK', functionname='AExecute'),'z':pyrapid.Symbols().GetSymbol(symbolname='param_queue3', modulename='MAINTASK', functionname='AExecute'),'rot':pyrapid.Symbols().GetSymbol(symbolname='param_queue4', modulename='MAINTASK', functionname='AExecute')} )) :
                    pass
                    #StatementAST AExecute
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Call procedure ATakeProd
                            parameters_actual = OrderedDict()
                            parameters_actual['nProdLine'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='AExecute').data.GetElem('nProdLine').Get()))
                            parameters_actual['x'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='param_queue1', modulename='MAINTASK', functionname='AExecute').data.Get()))
                            parameters_actual['y'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='param_queue2', modulename='MAINTASK', functionname='AExecute').data.Get()))
                            parameters_actual['z'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='param_queue3', modulename='MAINTASK', functionname='AExecute').data.Get()))
                            parameters_actual['rot'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='param_queue4', modulename='MAINTASK', functionname='AExecute').data.Get()))
                            pyrapid.Symbols().GetSymbol(symbolname='ATakeProd', modulename='MAINTASK', functionname='AExecute').data(parameters_actual)
                            del parameters_actual
                            # End Call procedure
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AExecute, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                # Line Palletizer/maintask.mod:582
                elif (pyrapid.Symbols().GetSymbol(symbolname='IsPlaceProduct', modulename='MAINTASK', functionname='AExecute').data( {'command':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='fullcommand', modulename='MAINTASK', functionname='AExecute').data.Get())),'index':pyrapid.Symbols().GetSymbol(symbolname='param_queue1', modulename='MAINTASK', functionname='AExecute'),'x':pyrapid.Symbols().GetSymbol(symbolname='v_param_queue1', modulename='MAINTASK', functionname='AExecute'),'y':pyrapid.Symbols().GetSymbol(symbolname='v_param_queue2', modulename='MAINTASK', functionname='AExecute'),'z':pyrapid.Symbols().GetSymbol(symbolname='v_param_queue3', modulename='MAINTASK', functionname='AExecute'),'rot':pyrapid.Symbols().GetSymbol(symbolname='v_param_queue4', modulename='MAINTASK', functionname='AExecute'),'acc_x':pyrapid.Symbols().GetSymbol(symbolname='v_param_queue5', modulename='MAINTASK', functionname='AExecute'),'acc_y':pyrapid.Symbols().GetSymbol(symbolname='v_param_queue6', modulename='MAINTASK', functionname='AExecute'),'acc_z':pyrapid.Symbols().GetSymbol(symbolname='v_param_queue7', modulename='MAINTASK', functionname='AExecute')} )) :
                    pass
                    #StatementAST AExecute
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line Palletizer/maintask.mod:583
                            if (( pyrapid.Symbols().GetSymbol(symbolname='param_queue1', modulename='MAINTASK', functionname='AExecute').data.Get() == 1 )) :
                                pass
                                #StatementAST AExecute
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Call procedure APlaceSingleProd
                                        parameters_actual = OrderedDict()
                                        parameters_actual['nProdLine'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='AExecute').data.GetElem('nProdLine').Get()))
                                        parameters_actual['x'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='v_param_queue1', modulename='MAINTASK', functionname='AExecute').data.GetElem( [1] ).Get()))
                                        parameters_actual['y'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='v_param_queue2', modulename='MAINTASK', functionname='AExecute').data.GetElem( [1] ).Get()))
                                        parameters_actual['z'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='v_param_queue3', modulename='MAINTASK', functionname='AExecute').data.GetElem( [1] ).Get()))
                                        parameters_actual['rot'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='v_param_queue4', modulename='MAINTASK', functionname='AExecute').data.GetElem( [1] ).Get()))
                                        parameters_actual['acc_x'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='v_param_queue5', modulename='MAINTASK', functionname='AExecute').data.GetElem( [1] ).Get()))
                                        parameters_actual['acc_y'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='v_param_queue6', modulename='MAINTASK', functionname='AExecute').data.GetElem( [1] ).Get()))
                                        parameters_actual['acc_z'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='v_param_queue7', modulename='MAINTASK', functionname='AExecute').data.GetElem( [1] ).Get()))
                                        pyrapid.Symbols().GetSymbol(symbolname='APlaceSingleProd', modulename='MAINTASK', functionname='AExecute').data(parameters_actual)
                                        del parameters_actual
                                        # End Call procedure
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AExecute, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                            # Line Palletizer/maintask.mod:585
                            elif (( pyrapid.Symbols().GetSymbol(symbolname='param_queue1', modulename='MAINTASK', functionname='AExecute').data.Get() == 2 )) :
                                pass
                                #StatementAST AExecute
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Call procedure APlaceDoubleProd
                                        parameters_actual = OrderedDict()
                                        parameters_actual['nProdLine'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data(pyrapid.Symbols().GetSymbol(symbolname='command', modulename='MAINTASK', functionname='AExecute').data.GetElem('nProdLine').Get()))
                                        parameters_actual['x'] = pyrapid.Symbol.CreateVar( pyrapid.rapid_array([], pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data, pyrapid.Symbols().GetSymbol(symbolname='v_param_queue1', modulename='MAINTASK', functionname='AExecute').data.Get()))
                                        parameters_actual['y'] = pyrapid.Symbol.CreateVar( pyrapid.rapid_array([], pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data, pyrapid.Symbols().GetSymbol(symbolname='v_param_queue2', modulename='MAINTASK', functionname='AExecute').data.Get()))
                                        parameters_actual['z'] = pyrapid.Symbol.CreateVar( pyrapid.rapid_array([], pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data, pyrapid.Symbols().GetSymbol(symbolname='v_param_queue3', modulename='MAINTASK', functionname='AExecute').data.Get()))
                                        parameters_actual['rot'] = pyrapid.Symbol.CreateVar( pyrapid.rapid_array([], pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data, pyrapid.Symbols().GetSymbol(symbolname='v_param_queue4', modulename='MAINTASK', functionname='AExecute').data.Get()))
                                        parameters_actual['acc_x'] = pyrapid.Symbol.CreateVar( pyrapid.rapid_array([], pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data, pyrapid.Symbols().GetSymbol(symbolname='v_param_queue5', modulename='MAINTASK', functionname='AExecute').data.Get()))
                                        parameters_actual['acc_y'] = pyrapid.Symbol.CreateVar( pyrapid.rapid_array([], pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data, pyrapid.Symbols().GetSymbol(symbolname='v_param_queue6', modulename='MAINTASK', functionname='AExecute').data.Get()))
                                        parameters_actual['acc_z'] = pyrapid.Symbol.CreateVar( pyrapid.rapid_array([], pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AExecute').data, pyrapid.Symbols().GetSymbol(symbolname='v_param_queue7', modulename='MAINTASK', functionname='AExecute').data.Get()))
                                        pyrapid.Symbols().GetSymbol(symbolname='APlaceDoubleProd', modulename='MAINTASK', functionname='AExecute').data(parameters_actual)
                                        del parameters_actual
                                        # End Call procedure
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AExecute, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                            else:
                                #StatementAST AExecute
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Call procedure TPWrite
                                        parameters_actual = OrderedDict()
                                        parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='AExecute').data(( 'ERRORE: ' + pyrapid.Symbols().GetSymbol(symbolname='fullcommand', modulename='MAINTASK', functionname='AExecute').data.Get() )))
                                        pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='AExecute').data(parameters_actual)
                                        del parameters_actual
                                        # End Call procedure
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AExecute, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AExecute, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                else:
                    #StatementAST AExecute
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Call procedure TPWrite
                            parameters_actual = OrderedDict()
                            parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='AExecute').data(( 'command not yet supported: ' + pyrapid.Symbols().GetSymbol(symbolname='fullcommand', modulename='MAINTASK', functionname='AExecute').data.Get() )))
                            pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='AExecute').data(parameters_actual)
                            del parameters_actual
                            # End Call procedure
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AExecute, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AExecute, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' AExecute(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('AExecute', pyrapid.Symbol.CreateProcedure(OrderedDict([('command', ('required', 'NORMAL', 'todoType', 0, []))]), rapid_proc_AExecute, error_rapid_proc_AExecute, undo_rapid_proc_AExecute), 'MAINTASK')
del rapid_proc_AExecute
# End Procedure Definition
# end routine declaration
# Line Palletizer/maintask.mod:596
# ## COMMENT: This function return the action that has to be done ##
# Line Palletizer/maintask.mod:597
# ## COMMENT: ##
############################# start routine declaration
# Line Palletizer/maintask.mod:598
# Start Function Definition
def error_rapid_func_AThereIsSomethingToDo (local_exception):
    return 0
def undo_rapid_func_AThereIsSomethingToDo ():
    pass
def rapid_func_AThereIsSomethingToDo (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='AThereIsSomethingToDo', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line Palletizer/maintask.mod:599
        pyrapid.Symbols().AddScopeSym('res', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='todoType', modulename='MAINTASK', functionname='AThereIsSomethingToDo').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:600
        pyrapid.Symbols().AddScopeSym('i', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AThereIsSomethingToDo').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:601
        pyrapid.Symbols().AddScopeSym('j', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AThereIsSomethingToDo').data(None)))
        # end declaration
        # stantments
        #StatementAST AThereIsSomethingToDo
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:603
                # FOR Statement
                pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='AThereIsSomethingToDo').data.Set( 1 ) 
                while ( pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='AThereIsSomethingToDo').data.Get() <= (pyrapid.Symbols().GetSymbol(symbolname='nPLACELINE', modulename='MAINTASK', functionname='AThereIsSomethingToDo').data.Get())): 
                    #StatementAST AThereIsSomethingToDo
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line Palletizer/maintask.mod:604
                            if (pyrapid.Symbols().GetSymbol(symbolname='r_SchemaType_Valid', modulename='MAINTASK', functionname='AThereIsSomethingToDo').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='AThereIsSomethingToDo')] ).Get()) :
                                pass
                                #StatementAST AThereIsSomethingToDo
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Line Palletizer/maintask.mod:605
                                        # FOR Statement
                                        pyrapid.Symbols().GetSymbol(symbolname='j', modulename='MAINTASK', functionname='AThereIsSomethingToDo').data.Set( 1 ) 
                                        while ( pyrapid.Symbols().GetSymbol(symbolname='j', modulename='MAINTASK', functionname='AThereIsSomethingToDo').data.Get() <= (pyrapid.Symbols().GetSymbol(symbolname='nQueueForSchema', modulename='MAINTASK', functionname='AThereIsSomethingToDo').data.Get())): 
                                            #StatementAST AThereIsSomethingToDo
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    pyrapid.Symbols().GetSymbol(symbolname='res', modulename='MAINTASK', functionname='AThereIsSomethingToDo').data.GetElem('nProdLine').Set( pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='AThereIsSomethingToDo').data.Get() ) 
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingToDo', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingToDo', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingToDo(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AThereIsSomethingToDo, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingToDo(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                            #StatementAST AThereIsSomethingToDo
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    pyrapid.Symbols().GetSymbol(symbolname='res', modulename='MAINTASK', functionname='AThereIsSomethingToDo').data.GetElem('nQueue').Set( pyrapid.Symbols().GetSymbol(symbolname='j', modulename='MAINTASK', functionname='AThereIsSomethingToDo').data.Get() ) 
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingToDo', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingToDo', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingToDo(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AThereIsSomethingToDo, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingToDo(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                            #StatementAST AThereIsSomethingToDo
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    pyrapid.Symbols().GetSymbol(symbolname='res', modulename='MAINTASK', functionname='AThereIsSomethingToDo').data.GetElem('nStep').Set( pyrapid.Symbols().GetSymbol(symbolname='r_SchemaType_RunSteps', modulename='MAINTASK', functionname='AThereIsSomethingToDo').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='AThereIsSomethingToDo'), pyrapid.Symbols().GetSymbol(symbolname='j', modulename='MAINTASK', functionname='AThereIsSomethingToDo')] ).Get() ) 
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingToDo', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingToDo', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingToDo(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AThereIsSomethingToDo, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingToDo(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                            #StatementAST AThereIsSomethingToDo
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    # Line Palletizer/maintask.mod:611
                                                    if (pyrapid.Symbols().GetSymbol(symbolname='CommandCanBeExecuted', modulename='MAINTASK', functionname='AThereIsSomethingToDo').data( {'command':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='todoType', modulename='MAINTASK', functionname='AThereIsSomethingToDo').data(pyrapid.Symbols().GetSymbol(symbolname='res', modulename='MAINTASK', functionname='AThereIsSomethingToDo').data.Get()))} )) :
                                                        pass
                                                        #StatementAST AThereIsSomethingToDo
                                                        retry_stantment = True
                                                        while retry_stantment:
                                                            retry_stantment = False
                                                            try:
                                                                # Line Palletizer/maintask.mod:612
                                                                return ( pyrapid.Symbols().GetSymbol(symbolname='res', modulename='MAINTASK', functionname='AThereIsSomethingToDo').data.Get() )
                                                            except pyrapid.RapidException, ex:
                                                                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingToDo', modulename='MAINTASK').error_call
                                                                if not(error_manager_call is None):
                                                                    error_manager = error_manager_call(ex)
                                                                    if error_manager == 1:
                                                                        retry_stantment = error_manager
                                                                    elif error_manager == 2:
                                                                        pass
                                                                    else:
                                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingToDo', modulename='MAINTASK').undo_call
                                                                        if not(undo_manager_call is None):
                                                                            undo_manager_call()
                                                                        raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingToDo(%d) -'%(pyrapid.lineno(),))
                                                                else:
                                                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AThereIsSomethingToDo, modulename='MAINTASK').undo_call
                                                                    if not(undo_manager_call is None):
                                                                        undo_manager_call()
                                                                    raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingToDo(%d) -'%(pyrapid.lineno(),))
                                                                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingToDo', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingToDo', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingToDo(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AThereIsSomethingToDo, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingToDo(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                            # Line Palletizer/maintask.mod:615
                                            # ## COMMENT:!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ##
                                            pyrapid.Symbols().GetSymbol(symbolname='j', modulename='MAINTASK', functionname='AThereIsSomethingToDo').data.Set( pyrapid.Symbols().GetSymbol(symbolname='j', modulename='MAINTASK', functionname='AThereIsSomethingToDo').data.Get() + (1) ) 
                                        # END FOR Statement
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingToDo', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingToDo', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingToDo(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AThereIsSomethingToDo, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingToDo(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingToDo', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingToDo', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingToDo(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AThereIsSomethingToDo, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingToDo(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                    pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='AThereIsSomethingToDo').data.Set( pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='AThereIsSomethingToDo').data.Get() + (1) ) 
                # END FOR Statement
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingToDo', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingToDo', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingToDo(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AThereIsSomethingToDo, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingToDo(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST AThereIsSomethingToDo
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='res', modulename='MAINTASK', functionname='AThereIsSomethingToDo').data.GetElem('nProdLine').Set( ( not 1 ) ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingToDo', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingToDo', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingToDo(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AThereIsSomethingToDo, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingToDo(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST AThereIsSomethingToDo
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='res', modulename='MAINTASK', functionname='AThereIsSomethingToDo').data.GetElem('nQueue').Set( ( not 1 ) ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingToDo', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingToDo', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingToDo(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AThereIsSomethingToDo, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingToDo(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST AThereIsSomethingToDo
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                pyrapid.Symbols().GetSymbol(symbolname='res', modulename='MAINTASK', functionname='AThereIsSomethingToDo').data.GetElem('nStep').Set( ( not 1 ) ) 
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingToDo', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingToDo', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingToDo(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AThereIsSomethingToDo, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingToDo(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST AThereIsSomethingToDo
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:622
                return ( pyrapid.Symbols().GetSymbol(symbolname='res', modulename='MAINTASK', functionname='AThereIsSomethingToDo').data.Get() )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingToDo', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingToDo', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingToDo(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AThereIsSomethingToDo, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingToDo(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('AThereIsSomethingToDo', pyrapid.Symbol.CreateFunction(OrderedDict(), pyrapid.Symbols().GetSymbol('todoType', 'MAINTASK', None), rapid_func_AThereIsSomethingToDo, error_rapid_func_AThereIsSomethingToDo, undo_rapid_func_AThereIsSomethingToDo), 'MAINTASK')
del rapid_func_AThereIsSomethingToDo
# End Function Definition
# end routine declaration
# Line Palletizer/maintask.mod:625
# ## COMMENT: This function return True if there is almost one line running ##
# Line Palletizer/maintask.mod:626
# ## COMMENT: ##
############################# start routine declaration
# Line Palletizer/maintask.mod:627
# Start Function Definition
def error_rapid_func_AThereIsSomethingRunning (local_exception):
    return 0
def undo_rapid_func_AThereIsSomethingRunning ():
    pass
def rapid_func_AThereIsSomethingRunning (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='AThereIsSomethingRunning', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line Palletizer/maintask.mod:628
        pyrapid.Symbols().AddScopeSym('i', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='AThereIsSomethingRunning').data(None)))
        # end declaration
        # stantments
        #StatementAST AThereIsSomethingRunning
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:629
                # FOR Statement
                pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='AThereIsSomethingRunning').data.Set( 1 ) 
                while ( pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='AThereIsSomethingRunning').data.Get() <= (pyrapid.Symbols().GetSymbol(symbolname='nPLACELINE', modulename='MAINTASK', functionname='AThereIsSomethingRunning').data.Get())): 
                    #StatementAST AThereIsSomethingRunning
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line Palletizer/maintask.mod:630
                            if (pyrapid.Symbols().GetSymbol(symbolname='r_SchemaType_Valid', modulename='MAINTASK', functionname='AThereIsSomethingRunning').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='AThereIsSomethingRunning')] ).Get()) :
                                pass
                                #StatementAST AThereIsSomethingRunning
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Line Palletizer/maintask.mod:631
                                        return ( True )
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingRunning', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingRunning', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingRunning(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AThereIsSomethingRunning, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingRunning(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingRunning', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingRunning', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingRunning(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AThereIsSomethingRunning, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingRunning(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                    pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='AThereIsSomethingRunning').data.Set( pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='AThereIsSomethingRunning').data.Get() + (1) ) 
                # END FOR Statement
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingRunning', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingRunning', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingRunning(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AThereIsSomethingRunning, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingRunning(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST AThereIsSomethingRunning
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:634
                return ( False )
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingRunning', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingRunning', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingRunning(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=AThereIsSomethingRunning, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' AThereIsSomethingRunning(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # end stantment
pyrapid.Symbols().AddGlobalSym('AThereIsSomethingRunning', pyrapid.Symbol.CreateFunction(OrderedDict(), pyrapid.Symbols().GetSymbol('bool', 'MAINTASK', None), rapid_func_AThereIsSomethingRunning, error_rapid_func_AThereIsSomethingRunning, undo_rapid_func_AThereIsSomethingRunning), 'MAINTASK')
del rapid_func_AThereIsSomethingRunning
# End Function Definition
# end routine declaration
############################# start routine declaration
# Line Palletizer/maintask.mod:637
# Start Procedure Definition
def error_rapid_proc_GlobalReset (local_exception):
    return 0
def undo_rapid_proc_GlobalReset ():
    pass
def rapid_proc_GlobalReset (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='GlobalReset', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line Palletizer/maintask.mod:638
        pyrapid.Symbols().AddScopeSym('i', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='GlobalReset').data(None)))
        # end declaration
        # stantments
        #StatementAST GlobalReset
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:639
                # FOR Statement
                pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='GlobalReset').data.Set( 1 ) 
                while ( pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='GlobalReset').data.Get() <= (pyrapid.Symbols().GetSymbol(symbolname='nPLACELINE', modulename='MAINTASK', functionname='GlobalReset').data.Get())): 
                    #StatementAST GlobalReset
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            pyrapid.Symbols().GetSymbol(symbolname='r_PalletExiting', modulename='MAINTASK', functionname='GlobalReset').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='GlobalReset')] ).Set( False ) 
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='GlobalReset', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='GlobalReset', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' GlobalReset(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=GlobalReset, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' GlobalReset(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                    pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='GlobalReset').data.Set( pyrapid.Symbols().GetSymbol(symbolname='i', modulename='MAINTASK', functionname='GlobalReset').data.Get() + (1) ) 
                # END FOR Statement
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='GlobalReset', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='GlobalReset', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' GlobalReset(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=GlobalReset, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' GlobalReset(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('GlobalReset', pyrapid.Symbol.CreateProcedure(OrderedDict(), rapid_proc_GlobalReset, error_rapid_proc_GlobalReset, undo_rapid_proc_GlobalReset), 'MAINTASK')
del rapid_proc_GlobalReset
# End Procedure Definition
# end routine declaration
# Line Palletizer/maintask.mod:644
# ## COMMENT: This is the task that make the real job ##
# Line Palletizer/maintask.mod:645
# ## COMMENT: ##
############################# start routine declaration
# Line Palletizer/maintask.mod:646
# Start Procedure Definition
def error_rapid_proc_MAIN_AUTOMATIC (local_exception):
    return 0
def undo_rapid_proc_MAIN_AUTOMATIC ():
    pass
def rapid_proc_MAIN_AUTOMATIC (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='MAIN_AUTOMATIC', invalue=local_args_scope):
        pass
        # data definitions
        ############################# start declaration
        # Line Palletizer/maintask.mod:647
        pyrapid.Symbols().AddScopeSym('nDescheduleTime', pyrapid.Symbol.CreateConst(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(1.0)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:648
        pyrapid.Symbols().AddScopeSym('bAutomaticContineExecution', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='bool', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(True)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:649
        pyrapid.Symbols().AddScopeSym('cTimeDoNothing', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='clock', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:650
        pyrapid.Symbols().AddScopeSym('bDoneSomething', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='bool', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(None)))
        # end declaration
        ############################# start declaration
        # Line Palletizer/maintask.mod:651
        pyrapid.Symbols().AddScopeSym('ActionToDo', pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='todoType', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(None)))
        # end declaration
        # stantments
        #StatementAST MAIN_AUTOMATIC
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure ClkReset
                parameters_actual = OrderedDict()
                parameters_actual['Clock'] = pyrapid.Symbols().GetSymbol(symbolname='cTimeDoNothing', modulename='MAINTASK', functionname='MAIN_AUTOMATIC')
                pyrapid.Symbols().GetSymbol(symbolname='ClkReset', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST MAIN_AUTOMATIC
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure ClkStart
                parameters_actual = OrderedDict()
                parameters_actual['Clock'] = pyrapid.Symbols().GetSymbol(symbolname='cTimeDoNothing', modulename='MAINTASK', functionname='MAIN_AUTOMATIC')
                pyrapid.Symbols().GetSymbol(symbolname='ClkStart', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST MAIN_AUTOMATIC
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data('START AUTOMATIC TASK'))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST MAIN_AUTOMATIC
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure GlobalReset
                parameters_actual = OrderedDict()
                pyrapid.Symbols().GetSymbol(symbolname='GlobalReset', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST MAIN_AUTOMATIC
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure GoHome
                parameters_actual = OrderedDict()
                pyrapid.Symbols().GetSymbol(symbolname='GoHome', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # Line Palletizer/maintask.mod:660
        # ## COMMENT: go to park ##
        #StatementAST MAIN_AUTOMATIC
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure ASetLoadSchema
                parameters_actual = OrderedDict()
                pyrapid.Symbols().GetSymbol(symbolname='ASetLoadSchema', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # Line Palletizer/maintask.mod:661
        # ## COMMENT: set to load schema when it will be possible ##
        #StatementAST MAIN_AUTOMATIC
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure AResetAllSchemas
                parameters_actual = OrderedDict()
                pyrapid.Symbols().GetSymbol(symbolname='AResetAllSchemas', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # Line Palletizer/maintask.mod:662
        # ## COMMENT: stop all schemas ##
        #StatementAST MAIN_AUTOMATIC
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:664
                # WHILE Statement
                while ( pyrapid.Symbols().GetSymbol(symbolname='bAutomaticContineExecution', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.Get()): 
                    pass
                    #StatementAST MAIN_AUTOMATIC
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            pyrapid.Symbols().GetSymbol(symbolname='bDoneSomething', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.Set( False ) 
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                    # Line Palletizer/maintask.mod:667
                    # ## COMMENT: check action to do ##
                    #StatementAST MAIN_AUTOMATIC
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line Palletizer/maintask.mod:668
                            if (pyrapid.Symbols().GetSymbol(symbolname='ASchemasHasToBeLoaded', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data( {} )) :
                                pass
                                #StatementAST MAIN_AUTOMATIC
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Call procedure ClkReset
                                        parameters_actual = OrderedDict()
                                        parameters_actual['Clock'] = pyrapid.Symbols().GetSymbol(symbolname='cTimeDoNothing', modulename='MAINTASK', functionname='MAIN_AUTOMATIC')
                                        pyrapid.Symbols().GetSymbol(symbolname='ClkReset', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(parameters_actual)
                                        del parameters_actual
                                        # End Call procedure
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                #StatementAST MAIN_AUTOMATIC
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Call procedure AResetLoadSchema
                                        parameters_actual = OrderedDict()
                                        pyrapid.Symbols().GetSymbol(symbolname='AResetLoadSchema', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(parameters_actual)
                                        del parameters_actual
                                        # End Call procedure
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                #StatementAST MAIN_AUTOMATIC
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Call procedure ALoadSchemas
                                        parameters_actual = OrderedDict()
                                        pyrapid.Symbols().GetSymbol(symbolname='ALoadSchemas', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(parameters_actual)
                                        del parameters_actual
                                        # End Call procedure
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                # Line Palletizer/maintask.mod:671
                                # ## COMMENT: load or reload all the schemas ##
                                #StatementAST MAIN_AUTOMATIC
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        pyrapid.Symbols().GetSymbol(symbolname='bDoneSomething', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.Set( True ) 
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                    #StatementAST MAIN_AUTOMATIC
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            pyrapid.Symbols().GetSymbol(symbolname='ActionToDo', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.Set( pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingToDo', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data( {} ) ) 
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                    #StatementAST MAIN_AUTOMATIC
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line Palletizer/maintask.mod:676
                            if (( ( pyrapid.Symbols().GetSymbol(symbolname='ActionToDo', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.GetElem('nProdLine').Get() != ( not 1 ) ) and ( ( pyrapid.Symbols().GetSymbol(symbolname='ActionToDo', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.GetElem('nQueue').Get() != ( not 1 ) ) and ( pyrapid.Symbols().GetSymbol(symbolname='ActionToDo', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.GetElem('nStep').Get() != ( not 1 ) ) ) )) :
                                pass
                                #StatementAST MAIN_AUTOMATIC
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Call procedure TPWrite
                                        parameters_actual = OrderedDict()
                                        parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(( 'DO ACTION ON LINE ' + ( pyrapid.Symbols().GetSymbol(symbolname='NumToStr', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data( {'Val':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(pyrapid.Symbols().GetSymbol(symbolname='ActionToDo', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.GetElem('nProdLine').Get())),'Dec':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(10))} ) + ( ' QUEUE ' + ( pyrapid.Symbols().GetSymbol(symbolname='NumToStr', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data( {'Val':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(pyrapid.Symbols().GetSymbol(symbolname='ActionToDo', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.GetElem('nQueue').Get())),'Dec':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(10))} ) + ( ' STEP ' + pyrapid.Symbols().GetSymbol(symbolname='NumToStr', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data( {'Val':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(pyrapid.Symbols().GetSymbol(symbolname='ActionToDo', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.GetElem('nStep').Get())),'Dec':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(10))} ) ) ) ) ) )))
                                        pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(parameters_actual)
                                        del parameters_actual
                                        # End Call procedure
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                #StatementAST MAIN_AUTOMATIC
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        pyrapid.Symbols().GetSymbol(symbolname='bDoneSomething', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.Set( True ) 
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                #StatementAST MAIN_AUTOMATIC
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Call procedure TPWrite
                                        parameters_actual = OrderedDict()
                                        parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(( 'Do Step:' + pyrapid.Symbols().GetSymbol(symbolname='r_ActionType_Name', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='ActionToDo', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.GetElem('nProdLine'), pyrapid.Symbols().GetSymbol(symbolname='ActionToDo', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.GetElem('nQueue'), pyrapid.Symbols().GetSymbol(symbolname='ActionToDo', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.GetElem('nStep')] ).Get() )))
                                        pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(parameters_actual)
                                        del parameters_actual
                                        # End Call procedure
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                #StatementAST MAIN_AUTOMATIC
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Call procedure AExecute
                                        parameters_actual = OrderedDict()
                                        parameters_actual['command'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='todoType', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(pyrapid.Symbols().GetSymbol(symbolname='ActionToDo', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.Get()))
                                        pyrapid.Symbols().GetSymbol(symbolname='AExecute', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(parameters_actual)
                                        del parameters_actual
                                        # End Call procedure
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                # Line Palletizer/maintask.mod:684
                                # ## COMMENT:go to next step ##
                                #StatementAST MAIN_AUTOMATIC
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        pyrapid.Symbols().GetSymbol(symbolname='r_SchemaType_RunSteps', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='ActionToDo', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.GetElem('nProdLine'), pyrapid.Symbols().GetSymbol(symbolname='ActionToDo', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.GetElem('nQueue')] ).Set( ( pyrapid.Symbols().GetSymbol(symbolname='ActionToDo', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.GetElem('nStep').Get() + 1 ) ) 
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                #StatementAST MAIN_AUTOMATIC
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Line Palletizer/maintask.mod:687
                                        if (( pyrapid.Symbols().GetSymbol(symbolname='r_SchemaType_RunSteps', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='ActionToDo', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.GetElem('nProdLine'), pyrapid.Symbols().GetSymbol(symbolname='ActionToDo', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.GetElem('nQueue')] ).Get() > pyrapid.Symbols().GetSymbol(symbolname='r_SchemaType_NSteps', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='ActionToDo', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.GetElem('nProdLine'), pyrapid.Symbols().GetSymbol(symbolname='ActionToDo', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.GetElem('nQueue')] ).Get() )) :
                                            pass
                                            #StatementAST MAIN_AUTOMATIC
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    # Call procedure TPWrite
                                                    parameters_actual = OrderedDict()
                                                    parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data('Go to next pallet for queue:'))
                                                    # Line Palletizer/maintask.mod:688
                                                    parameters_actual['Num'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(pyrapid.Symbols().GetSymbol(symbolname='ActionToDo', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.GetElem('nQueue').Get()))
                                                    pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(parameters_actual)
                                                    del parameters_actual
                                                    # End Call procedure
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                            #StatementAST MAIN_AUTOMATIC
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    pyrapid.Symbols().GetSymbol(symbolname='r_SchemaType_RunSteps', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.GetElem( [pyrapid.Symbols().GetSymbol(symbolname='ActionToDo', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.GetElem('nProdLine'), pyrapid.Symbols().GetSymbol(symbolname='ActionToDo', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.GetElem('nQueue')] ).Set( 1 ) 
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                    #StatementAST MAIN_AUTOMATIC
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line Palletizer/maintask.mod:694
                            if (( pyrapid.Symbols().GetSymbol(symbolname='bDoneSomething', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.Get() == False )) :
                                pass
                                #StatementAST MAIN_AUTOMATIC
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Call procedure TPWrite
                                        parameters_actual = OrderedDict()
                                        parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data('Nothing to do'))
                                        pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(parameters_actual)
                                        del parameters_actual
                                        # End Call procedure
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                #StatementAST MAIN_AUTOMATIC
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Line Palletizer/maintask.mod:696
                                        if (( pyrapid.Symbols().GetSymbol(symbolname='ClkRead', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data( {'Clock':pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname='clock', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(pyrapid.Symbols().GetSymbol(symbolname='cTimeDoNothing', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.Get()))} ) > 5 )) :
                                            pass
                                            # Line Palletizer/maintask.mod:696
                                            # ## COMMENT: if there is nothing to do for more than 5 seconds park the robot ##
                                            #StatementAST MAIN_AUTOMATIC
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    # Call procedure ClkReset
                                                    parameters_actual = OrderedDict()
                                                    parameters_actual['Clock'] = pyrapid.Symbols().GetSymbol(symbolname='cTimeDoNothing', modulename='MAINTASK', functionname='MAIN_AUTOMATIC')
                                                    pyrapid.Symbols().GetSymbol(symbolname='ClkReset', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(parameters_actual)
                                                    del parameters_actual
                                                    # End Call procedure
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                            #StatementAST MAIN_AUTOMATIC
                                            retry_stantment = True
                                            while retry_stantment:
                                                retry_stantment = False
                                                try:
                                                    # Call procedure GoHome
                                                    parameters_actual = OrderedDict()
                                                    pyrapid.Symbols().GetSymbol(symbolname='GoHome', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(parameters_actual)
                                                    del parameters_actual
                                                    # End Call procedure
                                                except pyrapid.RapidException, ex:
                                                    error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                                                    if not(error_manager_call is None):
                                                        error_manager = error_manager_call(ex)
                                                        if error_manager == 1:
                                                            retry_stantment = error_manager
                                                        elif error_manager == 2:
                                                            pass
                                                        else:
                                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                                                            if not(undo_manager_call is None):
                                                                undo_manager_call()
                                                            raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                                    else:
                                                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                                                        if not(undo_manager_call is None):
                                                            undo_manager_call()
                                                        raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                                    pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                            # Line Palletizer/maintask.mod:698
                                            # ## COMMENT: go to park ##
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                #StatementAST MAIN_AUTOMATIC
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Call procedure WaitTime
                                        parameters_actual = OrderedDict()
                                        parameters_actual['Time'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(pyrapid.Symbols().GetSymbol(symbolname='nDescheduleTime', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.Get()))
                                        pyrapid.Symbols().GetSymbol(symbolname='WaitTime', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(parameters_actual)
                                        del parameters_actual
                                        # End Call procedure
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                                # Line Palletizer/maintask.mod:700
                                # ## COMMENT:deschedule process ##
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                    #StatementAST MAIN_AUTOMATIC
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            pyrapid.Symbols().GetSymbol(symbolname='bAutomaticContineExecution', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data.Set( pyrapid.Symbols().GetSymbol(symbolname='AThereIsSomethingRunning', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data( {} ) ) 
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                # END WHILE Statement
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        #StatementAST MAIN_AUTOMATIC
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data('END AUTOMATIC TASK'))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='MAIN_AUTOMATIC').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_AUTOMATIC, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' MAIN_AUTOMATIC(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('MAIN_AUTOMATIC', pyrapid.Symbol.CreateProcedure(OrderedDict(), rapid_proc_MAIN_AUTOMATIC, error_rapid_proc_MAIN_AUTOMATIC, undo_rapid_proc_MAIN_AUTOMATIC), 'MAINTASK')
del rapid_proc_MAIN_AUTOMATIC
# End Procedure Definition
# end routine declaration
# Line Palletizer/maintask.mod:710
# ## COMMENT: this is the test loop ##
# Line Palletizer/maintask.mod:711
# ## COMMENT: ##
############################# start routine declaration
# Line Palletizer/maintask.mod:712
# Start Procedure Definition
def error_rapid_proc_MAIN_MANUAL (local_exception):
    return 0
def undo_rapid_proc_MAIN_MANUAL ():
    pass
def rapid_proc_MAIN_MANUAL (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='MAIN_MANUAL', invalue=local_args_scope):
        pass
        # data definitions
        # stantments
        #StatementAST MAIN_MANUAL
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='MAIN_MANUAL').data('START TEST'))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='MAIN_MANUAL').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_MANUAL', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_MANUAL', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' MAIN_MANUAL(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_MANUAL, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' MAIN_MANUAL(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # Line Palletizer/maintask.mod:714
        # ## COMMENT: ##
        # Line Palletizer/maintask.mod:715
        # ## COMMENT: perform test ##
        # Line Palletizer/maintask.mod:716
        # ## COMMENT: ##
        #StatementAST MAIN_MANUAL
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Call procedure TPWrite
                parameters_actual = OrderedDict()
                parameters_actual['String'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='string', modulename='MAINTASK', functionname='MAIN_MANUAL').data('END TEST'))
                pyrapid.Symbols().GetSymbol(symbolname='TPWrite', modulename='MAINTASK', functionname='MAIN_MANUAL').data(parameters_actual)
                del parameters_actual
                # End Call procedure
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_MANUAL', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN_MANUAL', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' MAIN_MANUAL(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN_MANUAL, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' MAIN_MANUAL(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('MAIN_MANUAL', pyrapid.Symbol.CreateProcedure(OrderedDict(), rapid_proc_MAIN_MANUAL, error_rapid_proc_MAIN_MANUAL, undo_rapid_proc_MAIN_MANUAL), 'MAINTASK')
del rapid_proc_MAIN_MANUAL
# End Procedure Definition
# end routine declaration
# Line Palletizer/maintask.mod:720
# ## COMMENT: MAIN PROGRAM ##
# Line Palletizer/maintask.mod:721
# ## COMMENT: this has to be configured to work in the main task as a single loop ##
############################# start routine declaration
# Line Palletizer/maintask.mod:722
# Start Procedure Definition
def error_rapid_proc_MAIN (local_exception):
    return 0
def undo_rapid_proc_MAIN ():
    pass
def rapid_proc_MAIN (local_args_scope):
    with pyrapid.Symbols().Scope(modulename='MAINTASK', functionname='MAIN', invalue=local_args_scope):
        pass
        # data definitions
        # Line Palletizer/maintask.mod:723
        # ## COMMENT: loop foreever ##
        # stantments
        #StatementAST MAIN
        retry_stantment = True
        while retry_stantment:
            retry_stantment = False
            try:
                # Line Palletizer/maintask.mod:724
                # WHILE Statement
                while ( pyrapid.Symbols().GetSymbol(symbolname='HasToRun', modulename='MAINTASK', functionname='MAIN').data( {} )): 
                    pass
                    #StatementAST MAIN
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Line Palletizer/maintask.mod:726
                            if (pyrapid.Symbols().GetSymbol(symbolname='IsAutomatic', modulename='MAINTASK', functionname='MAIN').data( {} )) :
                                pass
                                # Line Palletizer/maintask.mod:727
                                # ## COMMENT: if the system is in automatic  ##
                                # Line Palletizer/maintask.mod:728
                                # ## COMMENT: means that the palletizer loop is working ##
                                #StatementAST MAIN
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Call procedure MAIN_AUTOMATIC
                                        parameters_actual = OrderedDict()
                                        pyrapid.Symbols().GetSymbol(symbolname='MAIN_AUTOMATIC', modulename='MAINTASK', functionname='MAIN').data(parameters_actual)
                                        del parameters_actual
                                        # End Call procedure
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' MAIN(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' MAIN(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                            else:
                                # Line Palletizer/maintask.mod:731
                                # ## COMMENT: if the system is in manual  ##
                                # Line Palletizer/maintask.mod:732
                                # ## COMMENT: means that the test loop is working ##
                                #StatementAST MAIN
                                retry_stantment = True
                                while retry_stantment:
                                    retry_stantment = False
                                    try:
                                        # Call procedure MAIN_MANUAL
                                        parameters_actual = OrderedDict()
                                        pyrapid.Symbols().GetSymbol(symbolname='MAIN_MANUAL', modulename='MAINTASK', functionname='MAIN').data(parameters_actual)
                                        del parameters_actual
                                        # End Call procedure
                                    except pyrapid.RapidException, ex:
                                        error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN', modulename='MAINTASK').error_call
                                        if not(error_manager_call is None):
                                            error_manager = error_manager_call(ex)
                                            if error_manager == 1:
                                                retry_stantment = error_manager
                                            elif error_manager == 2:
                                                pass
                                            else:
                                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN', modulename='MAINTASK').undo_call
                                                if not(undo_manager_call is None):
                                                    undo_manager_call()
                                                raise pyrapid.RapidException(ex.code, ex.message+' MAIN(%d) -'%(pyrapid.lineno(),))
                                        else:
                                            undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN, modulename='MAINTASK').undo_call
                                            if not(undo_manager_call is None):
                                                undo_manager_call()
                                            raise pyrapid.RapidException(ex.code, ex.message+' MAIN(%d) -'%(pyrapid.lineno(),))
                                        pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' MAIN(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' MAIN(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                    # Line Palletizer/maintask.mod:736
                    # ## COMMENT: wait to avoit to loop too quick and to be sure that ##
                    # Line Palletizer/maintask.mod:737
                    # ## COMMENT: the main will be stopped with the robot velocity = 0 ##
                    #StatementAST MAIN
                    retry_stantment = True
                    while retry_stantment:
                        retry_stantment = False
                        try:
                            # Call procedure WaitTime
                            parameters_actual = OrderedDict()
                            # Line Palletizer/maintask.mod:738
                            parameters_actual['InPos'] = pyrapid.Symbol.CreateNone()
                            parameters_actual['Time'] = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname='num', modulename='MAINTASK', functionname='MAIN').data(1))
                            pyrapid.Symbols().GetSymbol(symbolname='WaitTime', modulename='MAINTASK', functionname='MAIN').data(parameters_actual)
                            del parameters_actual
                            # End Call procedure
                        except pyrapid.RapidException, ex:
                            error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN', modulename='MAINTASK').error_call
                            if not(error_manager_call is None):
                                error_manager = error_manager_call(ex)
                                if error_manager == 1:
                                    retry_stantment = error_manager
                                elif error_manager == 2:
                                    pass
                                else:
                                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN', modulename='MAINTASK').undo_call
                                    if not(undo_manager_call is None):
                                        undo_manager_call()
                                    raise pyrapid.RapidException(ex.code, ex.message+' MAIN(%d) -'%(pyrapid.lineno(),))
                            else:
                                undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN, modulename='MAINTASK').undo_call
                                if not(undo_manager_call is None):
                                    undo_manager_call()
                                raise pyrapid.RapidException(ex.code, ex.message+' MAIN(%d) -'%(pyrapid.lineno(),))
                            pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
                # END WHILE Statement
            except pyrapid.RapidException, ex:
                error_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN', modulename='MAINTASK').error_call
                if not(error_manager_call is None):
                    error_manager = error_manager_call(ex)
                    if error_manager == 1:
                        retry_stantment = error_manager
                    elif error_manager == 2:
                        pass
                    else:
                        undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='MAIN', modulename='MAINTASK').undo_call
                        if not(undo_manager_call is None):
                            undo_manager_call()
                        raise pyrapid.RapidException(ex.code, ex.message+' MAIN(%d) -'%(pyrapid.lineno(),))
                else:
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=MAIN, modulename='MAINTASK').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' MAIN(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1206
pyrapid.Symbols().AddGlobalSym('MAIN', pyrapid.Symbol.CreateProcedure(OrderedDict(), rapid_proc_MAIN, error_rapid_proc_MAIN, undo_rapid_proc_MAIN), 'MAINTASK')
del rapid_proc_MAIN
# End Procedure Definition
# end routine declaration
##################################################################
pyrapid.Symbols().PopScope()
################### End module MAINTASK ####################
if __name__ == '__main__':
    pyrapid.Symbols().GetSymbol('MAIN', modulename=None).data({})
