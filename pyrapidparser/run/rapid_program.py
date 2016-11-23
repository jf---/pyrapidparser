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
# Line test/wobj_issue.prg:2
################### Start module ODC ####################
pyrapid.Symbols().PushScope('ODC', None)
##################################################################
############################# start declaration
# Line test/wobj_issue.prg:4
pyrapid.Symbols().AddGlobalSym('hotwire', pyrapid.Symbol.CreatePers(pyrapid.Symbols().GetSymbol(symbolname='tooldata', modulename='ODC', functionname=None).data([True, [[0.0, 0.0, 733.0], [1.0, 0.0, 0.0, 0.0]], [10.0, [0.04, 0.0, 733.0], [1, 0, 0, 0], 0, 0, 0]])))
# end declaration
##################################################################
pyrapid.Symbols().PopScope()
################### End module ODC ####################
