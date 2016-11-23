#this file is an automatic traslation of rapid code
import sys
sys.path.append('..')
import pyrapid
from collections import OrderedDict
import copy
import sys
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # Line Pallettizer/schema.mod:34
        # ## COMMENT:Possible action ##
        # Line Pallettizer/schema.mod:35
        # ## COMMENT: OrderProd <number of product> <disposition> ##
        # Line Pallettizer/schema.mod:36
        # ## COMMENT: StopQueue <queue> ##
        # Line Pallettizer/schema.mod:37
        # ## COMMENT: StartQueue <queue> ##
        # Line Pallettizer/schema.mod:38
        # ## COMMENT: TakeProduct x y z rot ##
        # Line Pallettizer/schema.mod:39
        # ## COMMENT: PlaceProduct type x x1 y y1 z z1 rot x x1 y y1 z z1 rot ##
        # Line Pallettizer/schema.mod:40
        # ## COMMENT: OrderPallet ##
        # Line Pallettizer/schema.mod:41
        # ## COMMENT: TakePallet ##
        # Line Pallettizer/schema.mod:42
        # ## COMMENT: PlacePallet ##
        # Line Pallettizer/schema.mod:43
        # ## COMMENT: ExitPallet ##
        # Line Pallettizer/schema.mod:44
        # ## COMMENT: TakeSheet ##
        # Line Pallettizer/schema.mod:45
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
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
                    undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname='INIT_SCHEMA', modulename='SCHEMA').undo_call
                    if not(undo_manager_call is None):
                        undo_manager_call()
                    raise pyrapid.RapidException(ex.code, ex.message+' INIT_SCHEMA(%d) -'%(pyrapid.lineno(),))
                pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)
        # backward stantment
        if False:
            pass
        # end stantment
# rapid2py.py line:1214
pyrapid.Symbols().AddGlobalSym('INIT_SCHEMA', pyrapid.Symbol.CreateProcedure(OrderedDict(), rapid_proc_INIT_SCHEMA, error_rapid_proc_INIT_SCHEMA, undo_rapid_proc_INIT_SCHEMA), 'SCHEMA')
del rapid_proc_INIT_SCHEMA
# End Procedure Definition
# end routine declaration
##################################################################
pyrapid.Symbols().PopScope()
################### End module SCHEMA ####################
