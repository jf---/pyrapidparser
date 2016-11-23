# from browse_rapid_ast import EvaluateRapidExpression
# import rapid_ast
# import os
# import os.path
# import rapid_parser
#
# import run.pyrapid as pyrapid
#
#
# # if options.standard:
# # import glob
# #
# # for i in glob.glob('./default/*.sys'):
# # with open(i,"r") as f:
# #             ltext.append( (i, f.read()) )
#
# def parse_rapid_file(_path, fname):
#     pth = os.path.join(_path, fname)
#     assert os.path.isdir(_path), "{0} is not a valid path".format(_path)
#     assert os.path.isfile(pth), "{0} is not a valid file".format(pth)
#
#     ltext = []
#
#     with open(pth, "r") as f:
#         f_read = f.read()
#         ltext.append((pth, f_read))
#
#     attriblist = []
#     for fname, text in ltext:
#         print "PARSING: " + str(fname)
#         parser = rapid_parser.RAPIDParser(lex_optimize=True,
#                                           yacc_debug=False,
#                                           yacc_optimize=False,
#                                           start_from='module_declaration_list'
#         )
#
#         attriblist += parser.parse(text, fname, debuglevel=0).module_list
#
#     allmodule = rapid_ast.ModulesAST(attriblist)
#
#     class allnames(rapid_ast.NodeVisitor):
#         def __init__(self):
#             self.names = set()
#
#         # def visit_Module(self, node):
#         #     self.generic_visit(node)
#         #     print sorted(self.names)
#
#         # def visit_StatementAST(self, node):
#         #     # self.names.add(node.id)
#         #     print "node statement: {0}".format(node)
#
#         #
#         # def visit_IdentifierAST(self, node, **kwargs):
#         #     print "identifier:", node
#         #
#         #         for (child_name, child) in self.children():
#         #
#         #         print "identifier child"
#         #
#         #         if ( child is None or
#         #              isinstance(child, str) or
#         #              isinstance(child, int) or
#         #              isinstance(child, float) or
#         #              isinstance(child, bool) ):
#         #
#         #             print "child: {0}\n{1}".format( child_name, child)
#         #
#         #         else:
#         #             child.show()
#
#         def visit_ProcedureCallAST(self, node, **kwargs):
#             #procedure is IdentifierAST or ExpressionAST
#             #arguments list of ProcedureArgumentAST
#
#
#
#             try:
#                 procedure_name = node.procedure.name
#             except:
#                 ######################## TODO procedure_name can be the result of an expression ExpressionAST
#                 # the following code works only con constant expression
#                 compute = EvaluateRapidExpression(self.module_name, self.function_name)
#                 compute.visit(node.procedure, **kwargs)
#                 procedure_name = compute.return_value
#             else:
#                 if procedure_name == "MoveL":
#                     print "yo, move l bitch!"
#
#
#             #add possibility to make python conversion without have the procudere prototype
#             #this is usefull in case of expression has procedure
#             try:
#                 refsym = pyrapid.Symbols().GetSymbol(symbolname=procedure_name) #, modulename=self.module_name, functionname=self.function_name)
#             except KeyError:
#                 refsym = None
#
#
#             if refsym is None:
#                 pass
#                 # raise Exception("procedure %s used in module %s function %s not defined"%(procedure_name, self.module_name, self.function_name))z
#                 return
#
#             procedure_call = refsym.data
#             if refsym.type != pyrapid.Symbol.SYM_TYPE_PROCEDURE:
#                 raise Exception("symbol %s used in module %s function %s has to be a procedure"%(procedure_name, self.module_name, self.function_name))
#
#             parameters_defined = refsym.parameters
#             parameters_index = [0]
#             defined = []
#
#             #compute parameter list
#
#             kwargs["parameters_defined"] = parameters_defined
#             kwargs["parameters_index"] = parameters_index
#             kwargs["defined"] = defined
#             for i in node.arguments:
#                 self.visit(i, **kwargs)
#
#             for ik,iv in parameters_defined.iteritems():
#                 if iv[0]=='required':
#                     try:
#                         defined.index(ik)
#                     except ValueError:
#                         raise Exception("argument %s is required (%s,%s)"%(ik,str(parameters_defined),str(defined)))
#
#
#             # ProcedureCallAST:
#             #   IdentifierAST: MoveL
#             #   ProcedureArgumentAST: Required
#             #     AggregateAST:
#             #       AggregateAST:
#             #         Operator1AST: -, <rapid_ast.LiteralATS object at 0x10192a590>
#             #         Operator1AST: -, <rapid_ast.LiteralATS object at 0x10192a790>
#             #         LiteralATS: 973.0
#             #       AggregateAST:
#             #         LiteralATS: 0.011458
#             #         LiteralATS: 0.707014
#             #         Operator1AST: -, <rapid_ast.LiteralATS object at 0x10192aa10>
#             #         LiteralATS: 0.011458
#             #       AggregateAST:
#             #         Operator1AST: -, <rapid_ast.LiteralATS object at 0x10192a910>
#             #         LiteralATS: 0
#             #         Operator1AST: -, <rapid_ast.LiteralATS object at 0x10192ad10>
#             #         LiteralATS: 0
#             #       AggregateAST:
#             #         LiteralATS: 9000000000.0
#             #         LiteralATS: 9000000000.0
#             #         LiteralATS: 9000000000.0
#             #         LiteralATS: 9000000000.0
#             #         LiteralATS: 9000000000.0
#             #         LiteralATS: 9000000000.0
#
#
#         def visit_AggregateAST(self, node, **kwargs):
#             print "yo, aggr", node
#
#
#     xxx = allnames().visit(attriblist[0])
#
#     print "XXX", xxx
#
#
# # create a visitor, looping over the module variable declarations
# # the procedures, etc...
#
#
# # print allmodule
#
# parse_rapid_file("/Users/jelleferinga/GIT/pyrapidparser/test", "calib_2.prg")




#!/usr/bin/python
from browse_rapid_ast import EvaluateRapidExpression, ensure_dir
import rapid_ast
import os
import os.path
import run.pyrapid as pyrapid
import copy
import rapid_parser
from collections import OrderedDict

import logging

log = logging.getLogger(__name__)




class TraslateRapidToPython( rapid_ast.NodeVisitor ):

    def __init__(self, out_filename="rapid_program.py", out_folder="run"):
        self.file_module_name = None
        self.file_module = None
        self.module_name = None
        self.module_attribute = []
        self.function_name = None
        self.return_type = None
        self.indent_module = 0
        self.directory = out_folder
        ensure_dir(self.directory)
        self.file_module_name = os.path.join(self.directory, out_filename)
        self.file_module = open(self.file_module_name, "w")

    def close(self, entrypoint=None):
        if not(entrypoint is None):
            self.pushModuleScope()
            modulename = None
            entrypoint_list = entrypoint.split('.')
            if len(entrypoint_list)==2:
                modulename = entrypoint_list[0]
                procname = entrypoint_list[1]
            else:
                procname = entrypoint
            self.popModuleScope()
        if not (self.file_module is None):
            self.file_module.close()

    def simple_writeindent(self):
        if not (self.file_module is None):
            self.file_module.write (" " * self.indent_module)

    def simple_writemodule(self, a="\n"):
        if not (self.file_module is None):
            self.file_module.write (a)

    def writemodule(self, a):
        if not (self.file_module is None):
            self.file_module.write ((" " * self.indent_module) + a + "\n")

    def ModuleScope(self):
        class Scope():
            def __init__(self, this):
                self.this = this

            def __enter__(self):
                self.this.pushModuleScope()

            def __exit__(self, type, value, traceback):
                self.this.popModuleScope()
        return Scope(self)

    def pushModuleScope(self):
        self.indent_module += 4

    def popModuleScope(self):
        self.indent_module -= 4

    def visit_IdentifierAST(self, node, **kwargs):
        pass

    def visit_ModuleAttributeAST(self, node, **kwargs):
        #ModuleAttributeAST: [ name ]
        self.module_attribute.append(node.name)

    def pre_visit_ModuleAST(self, node, **kwargs):
        """
            1. create a folder with module name
            2. create a file __init.__py inside the 1. folder
            3. create a file modulename.py  inside the 1. folder
        """
        if not (node.coord is None):
            #self.writemodule("# Line %s"%(str(node.coord),))
            pass
        self.indent_module = 0
        self.function_name = None
        self.return_type = None
        self.module_attribute = []

        #module_name*, module_attribute**, type_definitions**, data_definitions**, routine_definitions**
        self.module_name = node.module_name.name
        if self.module_name is None:
            print("Module name not defined default will be used")
            self.module_name = "default"

        #self.writemodule( "################### Start module %s ####################" % (self.module_name,))
        pyrapid.Symbols().PushScope(modulename=self.module_name, functionname=self.function_name, invalue={})
        # #self.writemodule( "pyrapid.Symbols().PushScope(%s, %s)"%(repr(self.module_name), repr(self.function_name), ))
        #self.writemodule( "##################################################################")


    def post_visit_ModuleAST(self, node, **kwargs):
        """
              1. write on the __init__.py the global symbol
              2. close the opend file
        """

        #self.writemodule( "##################################################################")
        pyrapid.Symbols().PopScope()
        # #self.writemodule( "pyrapid.Symbols().PopScope()")
        #self.writemodule( "################### End module %s ####################" % (self.module_name,))

        self.indent_module = 0

        self.module_name = None
        self.module_attribute = []
        self.function_name = None
        self.return_type = None


    def visit_CommentAST(self, node, **kwargs):
        if not (node.coord is None):
            #self.writemodule("# Line %s"%(str(node.coord),))
            pass
        const_python_start = "python:"

        print("check for a reference to a CAD file or other useful attr's hidden in comments")

        # if node.comment.startswith(const_python_start):
        #     ##self.writemodule( "# from python comment ...")
        #     # #self.writemodule( node.comment[len(const_python_start):])
        # else:
        #     # #self.writemodule( "# ## COMMENT:" + node.comment +" ##")

    def pre_visit_TypeDefAST(self, node, **kwargs):
        # if not (node.coord is None):
        #     #self.writemodule("# Line %s"%(str(node.coord),))
        # #self.writemodule("############################# start type definition")
        self.tmp_TypeDefAST_data = node.type

    def post_visit_TypeDefAST(self, node, **kwargs):
        del self.tmp_TypeDefAST_data
        # #self.writemodule("# end type definition")

    def visit_AliasDefATS(self, node, **kwargs):
        if not (node.coord is None):
            # #self.writemodule("# Line %s"%(str(node.coord),))
            pass
        typename = node.type_name.name
        aliasname = node.alias_name.name
        if typename is None:
            raise Exception("conversion not possible because type_name is not defined")
        if aliasname is None:
            raise Exception("conversion not possible because type_name is not defined")

        refsym = pyrapid.Symbols().GetSymbol(typename, self.module_name, self.function_name)
        if refsym is None:
            raise Exception("reference to unknown type")
        if refsym.type != pyrapid.Symbol.SYM_TYPE_DATATYPE:
            raise Exception("ALIAS to symbol that is not a typedef")
        newsym = refsym.data

        if self.tmp_TypeDefAST_data is None:
            pyrapid.Symbols().AddGlobalSym(aliasname, pyrapid.Symbol.CreateDataType(newsym))
            # #self.writemodule( "pyrapid.Symbols().AddGlobalSym(%s, pyrapid.Symbol.CreateDataType(pyrapid.Symbols().GetSymbol(symbolname=%s, modulename=%s, functionname=%s).data))"%(repr(aliasname), repr(typename), repr(self.module_name), repr(self.function_name), ))
        else:
            pyrapid.Symbols().AddModuleSym(self.module_name, aliasname, pyrapid.Symbol.CreateDataType(newsym))
            # #self.writemodule( "pyrapid.Symbols().AddModuleSym(%s, %s, pyrapid.Symbol.CreateDataType(pyrapid.Symbols().GetSymbol(symbolname=%s, modulename=%s, functionname=%s).data))"%(repr(self.module_name), repr(aliasname), repr(typename), repr(self.module_name), repr(self.function_name), ))
    #
    def visit_RecordDefAST(self, node, **kwargs):
        if not (node.coord is None):
            # #self.writemodule("# Line %s"%(str(node.coord),))
            pass
        record_name = node.record_name.name
        components = node.components

        attributetype= []
        attributename= []

        for i in components:
            data_type = i.data_type.name
            record_component_name = i.record_component_name.name
            attributename.append(repr(record_component_name))
            attributetype.append("pyrapid.Symbols().GetSymbol(symbolname=%s, modulename=%s,functionname=%s).data"%(repr(data_type),repr(self.module_name), repr(self.function_name)))

        attributetype = ",".join(attributetype)
        attributename = ",".join(attributename)

        record = """
class rapid_%s (pyrapid.rapid_struct):
    def __init__(self, val=None):
        pyrapid.rapid_struct.__init__(self, [ %s ], [ %s ])
        if not(val  is None):
            self.Set( val )

    def Set(self, val):
        if isinstance(val, type(self)):
            self.val = val.val
        else:
            pyrapid.rapid_struct.Set(self, val)
""" % (record_name, attributename, attributetype)

        define_class = compile(record,"in_memory_compile","single")
        eval(define_class)

        # #self.writemodule(record)

        if self.tmp_TypeDefAST_data is None:
            pyrapid.Symbols().AddGlobalSym(record_name, pyrapid.Symbol.CreateDataType(eval("rapid_%s" % (record_name,))))
            # #self.writemodule( "pyrapid.Symbols().AddGlobalSym(%s, pyrapid.Symbol.CreateDataType(rapid_%s))"%(repr(record_name), record_name,))
        else:
            pyrapid.Symbols().AddModuleSym(self.module_name, record_name, pyrapid.Symbol.CreateDataType(eval("rapid_%s" % (record_name,))))
            # #self.writemodule( "pyrapid.Symbols().AddModuleSym(%s, %s, pyrapid.Symbol.CreateDataType(rapid_%s))"%(repr(self.module_name), repr(record_name), record_name, ))

        # #self.writemodule("del rapid_%s"%(record_name,))

    def pre_visit_DataDefATS(self, node, **kwargs):
        # #self.writemodule("############################# start declaration")
        if not (node.coord is None):
            # #self.writemodule("# Line %s"%(str(node.coord),))
            pass
        self.tmp_DataDefATS_data = node.type

    def post_visit_DataDefATS(self, node, **kwargs):
        del self.tmp_DataDefATS_data
        # #self.writemodule("# end declaration")


    def VarConstPersDeclaration(self, node, createvar, createvars, **kwargs):
        scope = self.tmp_DataDefATS_data
        vartype = node.type.name
        varinstance_name = node.variable_instance.name.name
        varinstance_value = node.variable_instance.value
        varinstance_size = node.variable_instance.size

        if not(varinstance_value is None):
            compute = EvaluateRapidExpression(self.module_name, self.function_name)
            compute.visit(varinstance_value, **kwargs)
            varinstance_value = compute.return_value



        symbol = pyrapid.Symbols().GetSymbol(vartype, self.module_name, self.function_name)
        if symbol is None:
            symbol = pyrapid.Symbols().GetSymbol(vartype, self.module_name, self.function_name)

        if len(varinstance_size)==0:

            """

            TODO: BUG!!!

            """

            if not hasattr(symbol, "data"):
                log.error("symbol is None for vartype {0}".format(vartype))
                return

            getvar = createvar(symbol.data(varinstance_value))
            sgetvar = "%s(pyrapid.Symbols().GetSymbol(symbolname=%s, modulename=%s, functionname=%s).data(%s))" % ( createvars, repr(vartype), repr(self.module_name), repr(self.function_name), repr(varinstance_value) )
        else:
            size = []
            for i in varinstance_size:
                compute = EvaluateRapidExpression(self.module_name, self.function_name)
                compute.visit(i, **kwargs)
                size.append(compute.return_value)
            getvar = createvar(   pyrapid.rapid_array(size, symbol.data, varinstance_value ) )
            sgetvar = "%s( pyrapid.rapid_array(%s, pyrapid.Symbols().GetSymbol(symbolname=%s, modulename=%s, functionname=%s).data, %s) )" % ( createvars, str(size), repr(vartype), repr(self.module_name), repr(self.function_name), repr(varinstance_value) )

        return (varinstance_name, getvar, sgetvar)


    def visit_VarDeclarationAST(self, node, **kwargs):
        if not (node.coord is None):
            # #self.writemodule("# Line %s"%(str(node.coord),))
            pass
        varinstance_name, getvar, sgetvar = self.VarConstPersDeclaration(node, pyrapid.Symbol.CreateVar, "pyrapid.Symbol.CreateVar")

        if self.tmp_DataDefATS_data is None:
            if self.function_name is None:
                #module declaration it is GLOBAL
                pyrapid.Symbols().AddGlobalSym( varinstance_name, getvar )
                # #self.writemodule( "pyrapid.Symbols().AddGlobalSym(%s, %s)"%(repr(varinstance_name), sgetvar) )
            else:
                #function declaration it is in the Scope of the function
                print("warning: variable %s is local to the function %s" % (varinstance_name, self.function_name))
                pyrapid.Symbols().AddScopeSym( varinstance_name, getvar )
                # #self.writemodule( "pyrapid.Symbols().AddScopeSym(%s, %s)"%(repr(varinstance_name), sgetvar) )
        else:
            if self.function_name is None:
                #module declaration it is LOCAL in the module
                pyrapid.Symbols().AddModuleSym( self.module_name, varinstance_name, getvar )
                # #self.writemodule( "pyrapid.Symbols().AddModuleSym(%s, %s, %s)"%(repr(self.module_name), repr(varinstance_name), sgetvar) )
            else:
                #function declaration it is in the Scope of the function
                pyrapid.Symbols().AddScopeSym( varinstance_name, getvar )
                # #self.writemodule( "pyrapid.Symbols().AddScopeSym(%s, %s)"%(repr(varinstance_name), sgetvar) )

    def visit_ConstDeclarationAST(self, node, **kwargs):
        if not (node.coord is None):
            # #self.writemodule("# Line %s"%(str(node.coord),))
            pass
        varinstance_name, getvar, sgetvar = self.VarConstPersDeclaration(node, pyrapid.Symbol.CreateConst, "pyrapid.Symbol.CreateConst")

        if self.tmp_DataDefATS_data is None:
            if self.function_name is None:
                #module declaration it is GLOBAL
                pyrapid.Symbols().AddGlobalSym( varinstance_name, getvar )
                # #self.writemodule( "pyrapid.Symbols().AddGlobalSym(%s, %s)"%(repr(varinstance_name), sgetvar) )
            else:
                #function declaration it is in the Scope of the function
                print("warning: variable %s is local to the function %s" % (varinstance_name, self.function_name))
                pyrapid.Symbols().AddScopeSym( varinstance_name, getvar )
                # #self.writemodule( "pyrapid.Symbols().AddScopeSym(%s, %s)"%(repr(varinstance_name), sgetvar) )
        else:
            if self.function_name is None:
                #module declaration it is LOCAL in the module
                pyrapid.Symbols().AddModuleSym( self.module_name, varinstance_name, getvar )
                # #self.writemodule( "pyrapid.Symbols().AddModuleSym(%s, %s, %s)"%(repr(self.module_name), repr(varinstance_name), sgetvar) )
            else:
                #function declaration it is in the Scope of the function
                pyrapid.Symbols().AddScopeSym( varinstance_name, getvar )
                # #self.writemodule( "pyrapid.Symbols().AddScopeSym(%s, %s)"%(repr(varinstance_name), sgetvar) )

    def visit_PersDeclarationAST(self, node, **kwargs):
        if not (node.coord is None):
            # #self.writemodule("# Line %s"%(str(node.coord),))
            pass


        try:
            varinstance_name, getvar, sgetvar = self.VarConstPersDeclaration(node, pyrapid.Symbol.CreatePers, "pyrapid.Symbol.CreatePers")
        except TypeError:
            if node.type.name == "wobjdata":
                log.error("issue with node: {0}".format(node))
                return
            else:
                raise

        if hasattr(getvar, "data"):
            print("getvar type: {0}, \ndata:\n{1}".format(getvar.vartype, getvar.data.val))

        if self.tmp_DataDefATS_data is None:
            if self.function_name is None:
                #module declaration it is GLOBAL
                pyrapid.Symbols().AddGlobalSym( varinstance_name, getvar )
                # #self.writemodule( "pyrapid.Symbols().AddGlobalSym(%s, %s)"%(repr(varinstance_name), sgetvar) )
            else:
                #function declaration it is in the Scope of the function
                pyrapid.Symbols().AddScopeSym( varinstance_name, getvar )
                # #self.writemodule( "pyrapid.Symbols().AddScopeSym(%s, %s)"%(repr(varinstance_name), sgetvar) )
        else:
            if self.function_name is None:
                #module declaration it is LOCAL in the module
                pyrapid.Symbols().AddModuleSym( self.module_name, varinstance_name, getvar )
                # #self.writemodule( "pyrapid.Symbols().AddModuleSym(%s, %s, %s)"%(repr(self.module_name), repr(varinstance_name), sgetvar) )
            else:
                #function declaration it is in the Scope of the function
                pyrapid.Symbols().AddLocalSym(self.module_name, self.function_name, varinstance_name, getvar )
                # #self.writemodule( "pyrapid.Symbols().AddLocalSym($s, %s, %s, %s)"%(repr(self.module_name), repr(self.function_name), repr(varinstance_name), sgetvar) )

    def pre_visit_RoutineDeclarationATS(self, node, **kwargs):
        # #self.writemodule("############################# start routine declaration")
        self.tmp_outineDeclarationATS_data = node.type

    def post_visit_RoutineDeclarationATS(self, node, **kwargs):
        del self.tmp_outineDeclarationATS_data
        # #self.writemodule("# end routine declaration")

    def visit_ParameterDefinitionAST(self, node, **kwargs):
        #parameter_type stringa
        #type IdentifierAST
        #name IdentifierAST
        #size int or None
        paramtype = node.parameter_type
        pname = node.name.name
        ptype = node.type.name
        psize = node.size

        self.lastparamadded = pname

        if self.params.has_key(pname):
            raise Exception("parameter %s already defined"%(pname,))
        else:
            self.params[pname] = ("required", paramtype, ptype, psize, [])

    def visit_OptionalParameterDefinitionAST(self, node, **kwargs):
        #parameter None or ParameterDefinitionAST or SwitchParameterDefinitionAST
        #switchs list of None or ParameterDefinitionAST or SwitchParameterDefinitionAST

        self.visit(node.parameter, **kwargs)

        list_switch = set()
        list_switch.update([self.lastparamadded])

        for i in node.switchs:
            self.visit(i, **kwargs)
            list_switch.update([self.lastparamadded])

        for i in list_switch:
            old0, old1, old2, old3, old4 = self.params[i]
            old4 = copy.copy(list_switch)
            old4.remove(i)
            if old0 == "required":
                self.params[i] = ( "optional", old1, old2, old3, list(old4) )
            else:
                self.params[i] = ( "switch", old1, old2, old3, list(old4) )


    def visit_SwitchParameterDefinitionAST(self, node, **kwargs):
        #name IdentifierAST
        pname = node.name.name

        self.lastparamadded = pname

        if self.params.has_key(pname):
            raise Exception("parameter %s already defined"%(pname,))
        else:
            self.params[pname] = ("switch", None, None, None, [])

    def visit_ExpressionAST(self, node, **kwargs):
        #expr is None or AggregateAST or Operator1AST or Operator2AST or FunctionCallAST or VariableAST or ExpressionAST or LiteralATS
        if node.expr is None:
            return
        else:
            self.visit(node.expr, **kwargs)

    def visit_AggregateAST(self, node, **kwargs):


        print("i guess looping through a list?")

        # self.simple_writemodule("[")
        if len(node.expr)>0:
            for i in node.expr[:-1]:
                self.visit(i, **kwargs)
                # self.simple_writemodule(", ")
            self.visit(node.expr[-1], **kwargs)
        # self.simple_writemodule("]")

    def visit_Operator1AST(self, node, **kwargs):
        if not(node.operator is None):
            # self.simple_writemodule("( not ")
            self.visit(node.par1, **kwargs)
            self.simple_writemodule(" )")
        else:
            # self.visit(node.par1, **kwargs)
            pass

    def visit_Operator2AST(self, node, **kwargs):
        # self.simple_writemodule("( ")
        self.visit(node.par1, **kwargs)
        # self.simple_writemodule(" ")

        if node.operator == "=":
            # self.simple_writemodule("==")
            pass
        elif node.operator == "DIV":
            # self.simple_writemodule("//")
            pass
        elif node.operator == "MOD":
            # self.simple_writemodule("%")
            pass
        elif node.operator == "<>":
            # self.simple_writemodule("!=")
            pass
        elif node.operator == "OR":
            # self.simple_writemodule("or")
            pass
        elif node.operator == "AND":
            # self.simple_writemodule("and")
            pass
        elif node.operator == "XOR":
            # self.simple_writemodule("^")
            pass
        else:
            self.simple_writemodule(node.operator)
        # self.simple_writemodule(" ")
        self.visit(node.par2, **kwargs)
        # self.simple_writemodule(" )")

    def visit_LiteralATS(self, node, **kwargs):
        #value is int or float or string
        if isinstance(node.value, str):
            # self.simple_writemodule(repr(node.value))
            pass
        else:
            # self.simple_writemodule(str(node.value))
            pass

    def visit_VariableAST(self, node, bget_VariableAST=True, bsym_VariableAST=True, **kwargs):
        varindexlist = node.index
        varcomponent = node.component

        if bget_VariableAST:
            bsym_VariableAST = True

        if varcomponent is None:
            if len(varindexlist)==0:
                if isinstance(node.var, rapid_ast.VariableAST):
                    self.visit( node.var, **kwargs )
                else:
                    # self.simple_writemodule( "pyrapid.Symbols().GetSymbol(symbolname=%s, modulename=%s, functionname=%s)" % ( repr(node.var.name), repr(self.module_name), repr(self.function_name) ) )
                    pass
                if bsym_VariableAST:
                    # self.simple_writemodule( ".data" )
                    pass
            else:
                if isinstance(node.var, rapid_ast.VariableAST):
                    self.visit( node.var, **kwargs )
                else:
                    # self.simple_writemodule( "pyrapid.Symbols().GetSymbol(symbolname=%s, modulename=%s, functionname=%s).data" % ( repr(node.var.name), repr(self.module_name), repr(self.function_name) ) )
                    pass
                # self.simple_writemodule( ".GetElem( ["  )

                for i in varindexlist[:-1]:
                    self.visit( i, bget_VariableAST=False, bsym_VariableAST=False, **kwargs )
                    # self.simple_writemodule( ", ")
                self.visit( varindexlist[-1], bget_VariableAST=False, bsym_VariableAST=False, **kwargs )

                # self.simple_writemodule( "] )" )
        else:
            if isinstance(node.var, rapid_ast.VariableAST):
                self.visit(node.var, bget_VariableAST=False, bsym_VariableAST=True, **kwargs)
                # self.simple_writemodule( ".GetElem(%s)" % ( repr(varcomponent.name), ) )
            else:
                raise Exception("if there is a component we need a variable as data before .")


        if bget_VariableAST:
            pass # self.simple_writemodule( ".Get()" )

    def visit_StatementAST(self, node, error_statement=False, undo_statement=False, **kwargs):
        if not (node.coord is None):
            pass # #self.writemodule("# Line %s"%(str(node.coord),))
        # #self.writemodule("#StatementAST %s"%(self.function_name,))
        if error_statement or undo_statement:
            self.visit(node.statement,  **kwargs)
        else:
            #self.writemodule("retry_stantment = True")
            pass #self.writemodule("while retry_stantment:")
            with self.ModuleScope():
                #self.writemodule("retry_stantment = False")
                pass #self.writemodule("try:")
                with self.ModuleScope():
                    self.visit(node.statement, **kwargs)
                #self.writemodule("except pyrapid.RapidException, ex:")
                with self.ModuleScope():
                    pass #self.writemodule("error_manager_call = pyrapid.Symbols().GetSymbol(symbolname=%s, modulename=%s).error_call" % ( repr(self.function_name), repr(self.module_name) ))
                    #self.writemodule("if not(error_manager_call is None):")
                    with self.ModuleScope():
                        pass #self.writemodule("error_manager = error_manager_call(ex)")
                        #self.writemodule("if error_manager == 1:")  # retry
                        with self.ModuleScope():
                            pass #self.writemodule("retry_stantment = error_manager")  # retry
                        #self.writemodule("elif error_manager == 2:")  # trynext
                        with self.ModuleScope():
                            pass #self.writemodule("pass")  # trynext
                        #self.writemodule("else:")  # propagate exception
                        with self.ModuleScope():
                            pass #execute undo
                            #self.writemodule("undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=%s, modulename=%s).undo_call" % ( repr(self.function_name), repr(self.module_name) ))
                            #self.writemodule("if not(undo_manager_call is None):")
                            with self.ModuleScope():
                                pass #self.writemodule("undo_manager_call()")
                            ##self.writemodule("raise")
                            #self.writemodule("raise pyrapid.RapidException(ex.code, ex.message+' %s(%%d) -'%%(pyrapid.lineno(),))"%(self.function_name,))  # propagate exception
                    #self.writemodule("else:")
                    with self.ModuleScope():
                        #execute undo
                        #self.writemodule("undo_manager_call = pyrapid.Symbols().GetSymbol(symbolname=%s, modulename=%s).undo_call" % ( self.function_name, repr(self.module_name) ))
                        #self.writemodule("if not(undo_manager_call is None):")
                        with self.ModuleScope():
                            pass #self.writemodule("undo_manager_call()")
                        ##self.writemodule("raise")
                        #self.writemodule("raise pyrapid.RapidException(ex.code, ex.message+' %s(%%d) -'%%(pyrapid.lineno(),))"%(self.function_name,))  # propagate exception
                    #self.writemodule("pyrapid.Symbols().GetSymbol(symbolname='ERRNO').data.Set(-1)")

    def visit_AssignmentStatementAST(self, node, **kwargs):
        #dest* is VariableAST
        #source*
        if not (node.coord is None):
            pass #self.writemodule("# Line %s"%(str(node.coord),))
        self.simple_writeindent()
        self.visit(node.dest, bget_VariableAST=False, bsym_VariableAST=True, **kwargs)
        self.simple_writemodule( ".Set( " )
        self.visit(node.source, **kwargs)
        self.simple_writemodule(" ) ")
        self.simple_writemodule()

    def visit_GotoStatementAST(self, node, **kwargs):
        if not (node.coord is None):
            pass #self.writemodule("# Line %s"%(str(node.coord),))
        labelname = "."+node.dest.name
        #self.writemodule("goto "+labelname)

    def visit_LabelAST(self, node, **kwargs):
        if not (node.coord is None):
            pass #self.writemodule("# Line %s"%(str(node.coord),))
        labelname = "."+node.name.name
        #self.writemodule("label "+labelname)

    def visit_RaiseStatementAST(self, node, **kwargs):
        #error_number
        if not (node.coord is None):
            pass #self.writemodule("# Line %s"%(str(node.coord),))
        if node.error_number is None:
            pass #self.writemodule("return 3")
            ##self.writemodule("raise")
        elif isinstance(node.error_number, rapid_ast.IdentifierAST):
            #node.error_number.name has to be a valid symbol
            ##self.writemodule("raise")
            name = node.error_number.name
            #self.writemodule('raise pyrapid.RapidException(pyrapid.Symbols().GetSymbol(symbolname=%s, modulename=%s, functionname=%s).data.Get(),%s)'%(repr(name), repr(self.module_name), repr(self.function_name), repr(name),))
        elif isinstance(node.error_number, int) or isinstance(node.error_number, float):
            pass #self.writemodule('raise pyrapid.RapidException(%d,"unknown")'%(node.error_number,))



    def visit_ReturnStatementAST(self, node, **kwargs):
        if not (node.coord is None):
            pass #self.writemodule("# Line %s"%(str(node.coord),))
        self.simple_writeindent()

        if node.result is None:
            if not(self.return_type is None):
                raise Exception("function %s return nothing"%(self.function_name,))
            self.simple_writemodule( "return " )
        else:
            if self.return_type is None:
                raise Exception("procedure %s return a type"%(self.function_name,))
            self.simple_writemodule( "return ( " )
            self.visit(node.result, **kwargs)
            self.simple_writemodule(" )")
        self.simple_writemodule()

    def visit_ExitStatementAST(self, node, **kwargs):
        if not (node.coord is None):
            pass #self.writemodule("# Line %s"%(str(node.coord),))

        #self.writemodule("sys.exit(1)")

    def visit_RetryStatementAST(self, node, error_statement, **kwargs):
        if not (node.coord is None):
            pass #self.writemodule("# Line %s"%(str(node.coord),))
        #self.writemodule("return 1")

    def visit_TrynextStatementAST(self, node, error_statement, **kwargs):
        if not (node.coord is None):
            pass #self.writemodule("# Line %s"%(str(node.coord),))
        #self.writemodule("return 2")

    def visit_ConnectStatementAST(self, node, **kwargs):
        if not (node.coord is None):
            pass #self.writemodule("# Line %s"%(str(node.coord),))
        raise Exception("Connect not yet supported")

    def visit_IfStatement(self, node, **kwargs):
        #condition*, statement_list**, elseif_list**, else_statement_list**
        if not (node.coord is None):
            pass #self.writemodule("# Line %s"%(str(node.coord),))
        self.simple_writeindent()
        self.simple_writemodule( "if (" )
        self.visit(node.condition, **kwargs)
        self.simple_writemodule( ") :" )
        self.simple_writemodule()
        with self.ModuleScope():
            #self.writemodule("pass")

            for i in node.statement_list:
                self.visit(i, **kwargs)

        for i in node.elseif_list:
            self.visit(i, **kwargs)

        if len(node.else_statement_list)>0:
            #self.writemodule("else:")
            with self.ModuleScope():
                for i in node.else_statement_list:
                    self.visit(i, **kwargs)

    def visit_ElseIfStatement(self, node, **kwargs):
        #condition*, statement_list**
        if not (node.coord is None):
            pass #self.writemodule("# Line %s"%(str(node.coord),))
        self.simple_writeindent()
        self.simple_writemodule( "elif (" )
        self.visit(node.condition, **kwargs)
        self.simple_writemodule( ") :" )
        self.simple_writemodule()
        with self.ModuleScope():
            #self.writemodule("pass")

            for i in node.statement_list:
                self.visit(i, **kwargs)

    def visit_ForStatement(self, node, **kwargs):
        #loop_variable*, ifrom*, ito*, istep*, statement_list**
        if not (node.coord is None):
            pass #self.writemodule("# Line %s"%(str(node.coord),))
        #self.writemodule("# FOR Statement")
        self.simple_writeindent()
        self.simple_writemodule( "pyrapid.Symbols().GetSymbol(symbolname=%s, modulename=%s, functionname=%s).data.Set( " % ( repr(node.loop_variable.name), repr(self.module_name), repr(self.function_name) ) )
        self.visit(node.ifrom, **kwargs)
        self.simple_writemodule(" ) ")
        self.simple_writemodule()

        self.simple_writeindent()
        self.simple_writemodule("while ( ")
        self.simple_writemodule( "pyrapid.Symbols().GetSymbol(symbolname=%s, modulename=%s, functionname=%s).data.Get() <= (" % ( repr(node.loop_variable.name), repr(self.module_name), repr(self.function_name) ) )
        self.visit(node.ito, **kwargs)
        self.simple_writemodule( ")" )
        self.simple_writemodule("): ")
        self.simple_writemodule()
        with self.ModuleScope():
            for i in node.statement_list:
                self.visit(i, **kwargs)

            self.simple_writeindent()
            self.simple_writemodule( "pyrapid.Symbols().GetSymbol(symbolname=%s, modulename=%s, functionname=%s).data.Set( " % ( repr(node.loop_variable.name), repr(self.module_name), repr(self.function_name) ) )
            self.simple_writemodule( "pyrapid.Symbols().GetSymbol(symbolname=%s, modulename=%s, functionname=%s).data.Get() + (" % ( repr(node.loop_variable.name), repr(self.module_name), repr(self.function_name) ) )
            self.visit(node.ifrom, **kwargs)
            self.simple_writemodule(") ) ")
            self.simple_writemodule()
        #self.writemodule("# END FOR Statement")

    def visit_WhileStatement(self, node, **kwargs):
        #condition*, statement_list****
        if not (node.coord is None):
            pass #self.writemodule("# Line %s"%(str(node.coord),))
        #self.writemodule("# WHILE Statement")
        self.simple_writeindent()
        self.simple_writemodule("while ( ")
        self.visit(node.condition, **kwargs)
        self.simple_writemodule("): ")
        self.simple_writemodule()
        with self.ModuleScope():
            #self.writemodule("pass")
            for i in node.statement_list:
                self.visit(i, **kwargs)

        #self.writemodule("# END WHILE Statement")

    ##
    def visit_TestStatement(self, node, **kwargs):
        #expression*, cases**, default**
        if not (node.coord is None):
            pass #self.writemodule("# Line %s"%(str(node.coord),))
        #self.writemodule("# TEST Statement")
        self.simple_writeindent()
        self.simple_writemodule("val = ( ")
        self.visit(node.expression, **kwargs)
        self.simple_writemodule(") ")
        self.simple_writemodule()
        #self.writemodule("if False:")
        with self.ModuleScope():
            pass #self.writemodule("pass")
        for i in node.cases:
            self.visit(i, **kwargs)
        if len(node.default)>0:
            #self.writemodule("else:")
            with self.ModuleScope():
                for i in node.default:
                    self.visit(i, **kwargs)

        #self.writemodule("# END TEST Statement")

    def visit_CaseStatement(self, node, **kwargs):
        #test_value**, statement_list**
        if not (node.coord is None):
            pass #self.writemodule("# Line %s"%(str(node.coord),))
        #self.writemodule("# CASE Statement")
        self.simple_writeindent()
        self.simple_writemodule("elif (")
        for i in node.test_value[:-1]:
            self.simple_writemodule("(val == (")
            self.visit(i, **kwargs)
            self.simple_writemodule(")) or ")
        self.simple_writemodule("(val == (")
        self.visit(node.test_value[-1], **kwargs)
        self.simple_writemodule("))")
        self.simple_writemodule("): ")
        self.simple_writemodule()
        with self.ModuleScope():
            #self.writemodule("pass")
            for i in node.statement_list:
                self.visit(i, **kwargs)
        #self.writemodule("# END CASE Statement")
    ##

    def visit_FunctionArgumentAST(self, node, parameters_defined, parameters_index, defined, **kwargs):
        #type "Required" or "Optional" or "Conditional" or None
        #argumentname is IdentifierAST or None
        #argumentvalue is ExpressionAST ... or VariableAST or None

        if node.type is None:
            raise Exception("function parameter not completly defined")

        in_parameters_index = parameters_index
        parameters_index = in_parameters_index.pop()

        if node.argumentname is None:
            if isinstance(parameters_index, int):
                while True:
                    try:
                        argumentname = parameters_defined.keys()[parameters_index]
                    except:
                        raise Exception("too much parameters")
                    parameters_index += 1
                    if isinstance(node.argumentvalue, rapid_ast.VariableAST) and parameters_defined[argumentname][0] == "switch":
                        continue
                    break
            else:
                raise Exception("positional parameter after a named one")
        else:
            argumentname = node.argumentname.name
            if parameters_defined.keys()[parameters_index] == argumentname:
                parameters_index += 1
            else:
                parameters_index = None

        try:
            defined.index(argumentname)
            raise Exception("argument %s already defined"%(argumentname,))
        except ValueError:
            pass

        try:
            parameters_defined[argumentname]
        except:
            raise Exception("%s is not a valid parameter"%(argumentname))

        defined.append(argumentname)
        self.simple_writemodule( "%s:" % (repr(argumentname),))
        if isinstance(node.argumentvalue, rapid_ast.VariableAST):
            #todo add check type
            #take the type of the symbol parameters_defined[argumentname] and compare it with
            #
            #vartype = parameters_defined[argumentname][2]
            #varsize = parameters_defined[argumentname][2]
            #
            if parameters_defined[argumentname][1]=="NORMAL":

                #todo make type compare
                vartype = parameters_defined[argumentname][2]
                varinstance_size = parameters_defined[argumentname][3]
                if varinstance_size==0:
                    self.simple_writemodule("pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname=%s, modulename=%s, functionname=%s).data(" % ( repr(vartype), repr(self.module_name), repr(self.function_name) ))
                    self.visit( node.argumentvalue, parameters_defined=parameters_defined, parameters_index=parameters_index, defined=defined, **kwargs )
                    self.simple_writemodule("))")
                else:
                    self.simple_writemodule("pyrapid.Symbol.CreateVar( pyrapid.rapid_array([], pyrapid.Symbols().GetSymbol(symbolname=%s, modulename=%s, functionname=%s).data, " % ( repr(vartype), repr(self.module_name), repr(self.function_name) ) )
                    self.visit( node.argumentvalue, parameters_defined=parameters_defined, parameters_index=parameters_index, defined=defined, **kwargs )
                    self.simple_writemodule("))")

            elif parameters_defined[argumentname][1] in ("VAR", "PERS", "INOUT"):
                self.visit(node.argumentvalue, parameters_defined=parameters_defined, parameters_index=parameters_index, defined=defined, bget_VariableAST=False, bsym_VariableAST=False, **kwargs)
            else:
                raise Exception("Only NORMAL, VAR, PERS, and INOUT are supported (%s) if the input is a variable (module name %s, function name %s, argument name %s)"%(str(parameters_defined[argumentname]), self.module_name, self.function_name, argumentname,))
        else:
            if parameters_defined[argumentname][0] == "switch":
                self.simple_writemodule("pyrapid.Symbol.CreateNone()")
            elif (parameters_defined[argumentname][1]=="NORMAL") or (parameters_defined[argumentname][1]=="INOUT"):
                vartype = parameters_defined[argumentname][2]
                varinstance_size = parameters_defined[argumentname][3]
                if varinstance_size==0:
                    self.simple_writemodule("pyrapid.Symbol.CreateVar( pyrapid.Symbols().GetSymbol(symbolname=%s, modulename=%s, functionname=%s).data(" % ( repr(vartype), repr(self.module_name), repr(self.function_name) ))
                    self.visit( node.argumentvalue, parameters_defined=parameters_defined, parameters_index=parameters_index, defined=defined, **kwargs )
                    self.simple_writemodule("))")
                else:
                    self.simple_writemodule("pyrapid.Symbol.CreateVar( pyrapid.rapid_array([], pyrapid.Symbols().GetSymbol(symbolname=%s, modulename=%s, functionname=%s).data, " % ( repr(vartype), repr(self.module_name), repr(self.function_name) ) )
                    self.visit( node.argumentvalue, parameters_defined=parameters_defined, parameters_index=parameters_index, defined=defined, **kwargs )
                    self.simple_writemodule("))")
            else:
                raise Exception("only NORMAL or INOUT are supported if the input is an expression")

        in_parameters_index.append(parameters_index)

    def visit_ProcedureArgumentAST(self, node, parameters_defined, parameters_index, defined, **kwargs):
        #type "Required" or "Optional" or "Conditional" or None
        #argumentname is IdentifierAST or None
        #argumentvalue is ExpressionAST ... or VariableAST or None

        if not (node.coord is None):
            pass #self.writemodule("# Line %s"%(str(node.coord),))

        if node.type is None:
            raise Exception("procedure parameter not completly defined")

        in_parameters_index = parameters_index
        parameters_index = in_parameters_index.pop()

        if node.argumentname is None:
            if isinstance(parameters_index, int):
                while True:
                    try:
                        argumentname = parameters_defined.keys()[parameters_index]
                    except:
                        raise Exception("too much parameters")
                    parameters_index += 1
                    if isinstance(node.argumentvalue, rapid_ast.VariableAST) and parameters_defined[argumentname][0] == "switch":
                        continue
                    break
            else:
                raise Exception("positional parameter after a named one")
        else:
            argumentname = node.argumentname.name
            if parameters_defined.keys()[parameters_index] == argumentname:
                parameters_index += 1
            else:
                parameters_index = None

        try:
            defined.index(argumentname)
            raise Exception("argument %s already defined"%(argumentname,))
        except ValueError:
            pass

        try:
            parameters_defined[argumentname]
        except:
            raise Exception("%s is not a valid parameter"%(argumentname))

        defined.append(argumentname)

        if isinstance(node.argumentvalue, rapid_ast.VariableAST):
            #todo add check type
            #take the type of the symbol parameters_defined[argumentname] and compare it with
            #
            #vartype = parameters_defined[argumentname][2]
            #varsize = parameters_defined[argumentname][2]
            #
            if parameters_defined[argumentname][1]=="NORMAL":
                #todo make type compare
                vartype = parameters_defined[argumentname][2]
                varinstance_size = parameters_defined[argumentname][3]
                self.simple_writeindent()
                self.simple_writemodule( "parameters_actual[%s] = " % (repr(argumentname),))
                if varinstance_size==0:
                    self.simple_writemodule("pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname=%s, modulename=%s, functionname=%s).data(" % ( repr(vartype), repr(self.module_name), repr(self.function_name) ))
                    self.visit( node.argumentvalue, parameters_defined=parameters_defined, parameters_index=parameters_index, defined=defined, **kwargs )
                    self.simple_writemodule("))")
                else:
                    self.simple_writemodule("pyrapid.Symbol.CreateVar( pyrapid.rapid_array([], pyrapid.Symbols().GetSymbol(symbolname=%s, modulename=%s, functionname=%s).data, " % ( repr(vartype), repr(self.module_name), repr(self.function_name) ) )
                    self.visit( node.argumentvalue, parameters_defined=parameters_defined, parameters_index=parameters_index, defined=defined, **kwargs )
                    self.simple_writemodule("))")
                self.simple_writemodule( )
            elif parameters_defined[argumentname][1] in ( "VAR", "PERS", "INOUT"):
                self.simple_writeindent()
                self.simple_writemodule( "parameters_actual[%s] = " % (repr(argumentname),))
                self.visit(node.argumentvalue, parameters_defined=parameters_defined, parameters_index=parameters_index, defined=defined, bget_VariableAST=False, bsym_VariableAST=False, **kwargs)
                self.simple_writemodule( )
            else:
                raise Exception("Only NORMAL, VAR, PERS, and INOUT are supported (%s) if the input is a variable (module name %s, function name %s, argument name %s)"%(str(parameters_defined[argumentname]), self.module_name, self.function_name, argumentname,))
        else:
            if parameters_defined[argumentname][0] == "switch":
                self.simple_writeindent()
                self.simple_writemodule( "parameters_actual[%s] = " % (repr(argumentname),))
                self.simple_writemodule("pyrapid.Symbol.CreateNone()")
                self.simple_writemodule( )
            elif (parameters_defined[argumentname][1]=="NORMAL") or (parameters_defined[argumentname][1]=="INOUT"):
                vartype = parameters_defined[argumentname][2]
                varinstance_size = parameters_defined[argumentname][3]
                self.simple_writeindent()
                self.simple_writemodule( "parameters_actual[%s] = " % (repr(argumentname),))
                if varinstance_size==0:
                    self.simple_writemodule("pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(symbolname=%s, modulename=%s, functionname=%s).data(" % ( repr(vartype), repr(self.module_name), repr(self.function_name) ))
                    self.visit( node.argumentvalue, parameters_defined=parameters_defined, parameters_index=parameters_index, defined=defined, **kwargs )
                    self.simple_writemodule("))")
                else:
                    self.simple_writemodule("pyrapid.Symbol.CreateVar( pyrapid.rapid_array([], pyrapid.Symbols().GetSymbol(symbolname=%s, modulename=%s, functionname=%s).data, " % ( repr(vartype), repr(self.module_name), repr(self.function_name) ) )
                    self.visit( node.argumentvalue, parameters_defined=parameters_defined, parameters_index=parameters_index, defined=defined, **kwargs )
                    self.simple_writemodule("))")
                self.simple_writemodule( )
            else:
                raise Exception("only NORMAL or INOUT are supported if the input is an expression, received=%s"%(parameters_defined[argumentname][1],))

        in_parameters_index.append(parameters_index)

    def visit_FunctionCallAST(self, node, **kwargs):
        #function is IdentifierAST or ExpressionAST
        #arguments list of FunctionArgumentAST

        function_name = node.function.name

        # SPECIAL FUNCTION #
        if function_name=="Present":
            if len(node.arguments)!=1:
                raise Exception("Present function accept one parameter")
            if node.arguments[0].type=="Required":
                if node.arguments[0].argumentname is None:
                    if isinstance(node.arguments[0].argumentvalue, rapid_ast.VariableAST):
                        if isinstance(node.arguments[0].argumentvalue.var, rapid_ast.IdentifierAST):
                            self.simple_writemodule("pyrapid.Symbols().IsInScope(%s)"%(repr(node.arguments[0].argumentvalue.var.name)))
                        else:
                            raise Exception("Present function accept one sympol Variable as parameter")
                    else:
                        raise Exception("Present function accept one Variable as parameter")
                else:
                    raise Exception("Present function accept one unqualified name")
            else:
                raise Exception("Present function accept one required unqualified name")
        elif function_name=="Dim":
            if len(node.arguments)!=2:
                raise Exception("Dim function accept 2 parameter")
            if node.arguments[0].type=="Required":
                if (node.arguments[0].argumentname is None) or (node.arguments[0].argumentname=="ArrPar"):
                    if isinstance(node.arguments[0].argumentvalue, rapid_ast.VariableAST):
                        if isinstance(node.arguments[0].argumentvalue.var, rapid_ast.IdentifierAST):
                            pass
                        else:
                            raise Exception("Dim function first param has to be a sympol Variable")
                    else:
                        raise Exception("Dim function first param has to be a sympol Variable")
                else:
                    raise Exception("Dim function first parameter ArrPar")
            else:
                raise Exception("Dim function first parameter has to be Reuired")
            if node.arguments[1].type=="Required":
                if (node.arguments[0].argumentname is None) or (node.arguments[0].argumentname=="DimNo"):
                    pass
                else:
                    raise Exception("Dim function first parameter ArrPar")
            else:
                raise Exception("Dim function first parameter has to be Reuired")

            self.simple_writemodule("pyrapid.Symbols().GetSymbol(symbolname=%s, modulename=%s, functionname=%s).data.GetSize(**{"%(repr(node.arguments[0].argumentvalue.var.name), repr(self.module_name), repr(self.function_name)) )
            parameters_defined = OrderedDict()
            parameters_defined["ArrPar"] = ("Required", "REF", 'anytype', 0, [])
            parameters_defined["DimNo"] = ("Required", "NORMAL", 'num', 0, [])
            parameters_index = [1]
            defined = []
            kwargs["parameters_defined"] = parameters_defined
            kwargs["parameters_index"] = parameters_index
            kwargs["defined"] = defined
            self.visit(node.arguments[1], **kwargs)
            self.simple_writemodule("})")
        elif function_name=="IsVar":
            if len(node.arguments)!=1:
                raise Exception("IsVar function accept one parameter")
        elif function_name=="IsPers":
            if len(node.arguments)!=1:
                raise Exception("IsPers function accept one parameter")
        else:
            # NORMAL FUNCTION #
            refsym = pyrapid.Symbols().GetSymbol(symbolname=function_name, modulename=self.module_name, functionname=self.function_name)
            if refsym is None:
                raise Exception("procedure %s used in module %s function %s not defined"%(function_name, self.module_name, self.function_name))
            procedure_call = refsym.data
            if refsym.type != pyrapid.Symbol.SYM_TYPE_FUNCTION:
                raise Exception("symbol %s used in module %s function %s has to be a procedure"%(function_name, self.module_name, self.function_name))

            parameters_defined = refsym.parameters
            parameters_index = [0]
            defined = []

            #compute parameter list

            self.simple_writemodule("pyrapid.Symbols().GetSymbol(symbolname=%s, modulename=%s, functionname=%s).data( {" % ( repr(function_name), repr(self.module_name), repr(self.function_name) ))

            kwargs["parameters_defined"] = parameters_defined
            kwargs["parameters_index"] = parameters_index
            kwargs["defined"] = defined
            if len(node.arguments)>0:
                for i in node.arguments[:-1]:
                    self.visit(i, **kwargs)
                    self.simple_writemodule(",")
                self.visit(node.arguments[-1], **kwargs)

            self.simple_writemodule("} )")

            for ik,iv in parameters_defined.iteritems():
                if iv[0]=='required':
                    try:
                        defined.index(ik)
                    except ValueError:
                        raise Exception("argument %s is required"%(ik,))


    def visit_ProcedureCallAST(self, node, **kwargs):
        #procedure is IdentifierAST or ExpressionAST
        #arguments list of ProcedureArgumentAST

        if not (node.coord is None):
            pass #self.writemodule("# Line %s"%(str(node.coord),))


        try:
            procedure_name = node.procedure.name
        except:
            ######################## TODO procedure_name can be the result of an expression ExpressionAST
            # the following code works only con constant expression
            compute = EvaluateRapidExpression(self.module_name, self.function_name)
            compute.visit(node.procedure, **kwargs)
            procedure_name = compute.return_value
            #

        #SPECIAL PROCEDURE
        if procedure_name=="WaitUntil":
            #TODO
            #WaitUntil \InPos Cond \MaxTime \TimeFlag
            #self.writemodule("import time")
            self.simple_writeindent()
            self.simple_writemodule("while ( ")

            for i in range(len(node.arguments)):
                argn = node.arguments[i].argumentname
                argv = node.arguments[i].argumentvalue
                if argn!="InPos":
                    self.visit(argv, **kwargs)
                    break

            self.simple_writemodule("): ")
            self.simple_writemodule()
            with self.ModuleScope():
                pass #self.writemodule("time.sleep(0.1)")
        else:
            #add possibility to make python conversion without have the procudere prototype
            #this is usefull in case of expression has procedure
            #self.writemodule("# Call procedure %s"%(procedure_name,))
            refsym = pyrapid.Symbols().GetSymbol(symbolname=procedure_name, modulename=self.module_name, functionname=self.function_name)


            if refsym is None:
                log.error("no support for command: {0}".format(node.procedure.name))
                # raise Exception("procedure %s used in module %s function %s not defined"%(procedure_name, self.module_name, self.function_name))


            if refsym is not None:
                procedure_call = refsym.data
                if refsym.type != pyrapid.Symbol.SYM_TYPE_PROCEDURE:
                    raise Exception("symbol %s used in module %s function %s has to be a procedure"%(procedure_name, self.module_name, self.function_name))

                parameters_defined = refsym.parameters
                parameters_index = [0]
                defined = []

                #self.writemodule("parameters_actual = OrderedDict()")
                #compute parameter list

                kwargs["parameters_defined"] = parameters_defined
                kwargs["parameters_index"] = parameters_index
                kwargs["defined"] = defined
                for i in node.arguments:
                    self.visit(i, **kwargs)

                for ik,iv in parameters_defined.iteritems():
                    if iv[0]=='required':
                        try:
                            defined.index(ik)
                        except ValueError:
                            raise Exception("argument %s is required (%s,%s)"%(ik,str(parameters_defined),str(defined)))

                #self.writemodule("pyrapid.Symbols().GetSymbol(symbolname=%s, modulename=%s, functionname=%s).data(parameters_actual)" % ( repr(procedure_name), repr(self.module_name), repr(self.function_name) ))

                #self.writemodule("del parameters_actual")
                #self.writemodule("# End Call procedure")


    def visit_ProcedureDeclarationAST(self, node, **kwargs):
        #procedure_name*, parameter_list**, data_definitions**, statement_list**, routine_backward*, routine_error*, routine_undo*

        if not (node.coord is None):
            pass #self.writemodule("# Line %s"%(str(node.coord),))

        #self.writemodule("# Start Procedure Definition")

        self.return_type = None

        self.params = OrderedDict()
        self.lastparamadded = None

        for i in node.parameter_list:
            #ParameterDefinitionAST or OptionalParameterDefinitionAST or SwitchParameterDefinitionAST or None
            self.visit(i, **kwargs)

        self.function_name =  node.procedure_name.name

        params = repr(self.params)

        def _rapid_proc_(local_args_scope):
            pass

        def _error_rapid_proc_(local_exception):
            pass

        def _undo_rapid_proc_():
            pass

        if self.tmp_outineDeclarationATS_data is None:
            pyrapid.Symbols().AddGlobalSym(self.function_name, pyrapid.Symbol.CreateProcedure(self.params, _rapid_proc_, _error_rapid_proc_, _undo_rapid_proc_), self.module_name)
        else:
            pyrapid.Symbols().AddModuleSym(self.module_name, self.function_name, pyrapid.Symbol.CreateProcedure(self.params, _rapid_proc_, _error_rapid_proc_, _undo_rapid_proc_))

        #self.writemodule("def error_rapid_proc_%s (local_exception):" % (self.function_name,))
        with self.ModuleScope():
            #add parameter

            if not ( node.routine_error is None ):
                self.visit(node.routine_error, error_statement=True, **kwargs)

            #self.writemodule("return 0")

        #self.writemodule("def undo_rapid_proc_%s ():" % (self.function_name,))
        with self.ModuleScope():
            #add parameter
            #self.writemodule("pass")

            if not ( node.routine_undo is None ):
                self.visit(node.routine_undo, undo_statement=True, **kwargs)


        #self.writemodule("def rapid_proc_%s (local_args_scope):" % (self.function_name,))

        with self.ModuleScope():

            with pyrapid.Symbols().Scope(modulename=self.module_name, functionname=self.function_name, invalue={}):
                for ik,iv in self.params.iteritems():
                    vartype, paramtype, ptype, psize, pdep = iv
                    if vartype=="switch":
                        getvar = pyrapid.Symbol.CreateNone()
                    else:
                        try:
                            if psize==0:
                                getvar = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(ptype, self.module_name, self.function_name).data())
                            else:
                                getvar = pyrapid.Symbol.CreateVar(pyrapid.rapid_array([], pyrapid.Symbols().GetSymbol(ptype, self.module_name, self.function_name).data) )
                        except:
                            raise Exception("error progrably not defined symbol %s (module %s, function %s)"%(ptype, self.module_name, self.function_name))
                    pyrapid.Symbols().AddScopeSym(ik, getvar)
                #self.writemodule( "with pyrapid.Symbols().Scope(modulename=%s, functionname=%s, invalue=local_args_scope):"%(repr(self.module_name), repr(self.function_name)))
                with self.ModuleScope():
                    #self.writemodule("pass")
                    #self.writemodule("# data definitions")

                    for i in node.data_definitions:
                        self.visit(i, **kwargs)

                    #self.writemodule("# stantments")

                    for i in node.statement_list:
                        self.visit(i, **kwargs)

                    #self.writemodule("# backward stantment")
                    #self.writemodule("if False:")
                    with self.ModuleScope():
                        #self.writemodule("pass")

                        if not ( node.routine_backward is None ):
                            self.visit(node.routine_backward, **kwargs)

                    #self.writemodule("# end stantment")


        if self.tmp_outineDeclarationATS_data is None:
            pass #self.writemodule("# rapid2py.py line:%d"%( pyrapid.lineno(), ))
            #self.writemodule( "pyrapid.Symbols().AddGlobalSym(%s, pyrapid.Symbol.CreateProcedure(%s, rapid_proc_%s, error_rapid_proc_%s, undo_rapid_proc_%s), %s)"%(repr(self.function_name), params, self.function_name, self.function_name, self.function_name, repr(self.module_name),))
        else:
            pass #self.writemodule("# rapid2py.py line:%d"%( pyrapid.lineno(), ))
            #self.writemodule( "pyrapid.Symbols().AddModuleSym(%s, %s, pyrapid.Symbol.CreateProcedure(%s, rapid_proc_%s, error_rapid_proc_%s, undo_rapid_proc_%s))"%(repr(self.module_name), repr(self.function_name), params, self.function_name, self.function_name, self.function_name, ))

        #self.writemodule("del rapid_proc_%s" % (self.function_name,))

        self.function_name =  None
        self.return_type = None

        del self.params

        #self.writemodule("# End Procedure Definition")

    def visit_FunctionDeclarationAST(self, node, **kwargs):
        #data_type* function_name*, parameter_list**, data_definitions**, statement_list**, routine_error*, routine_undo*

        if not (node.coord is None):
            pass #self.writemodule("# Line %s"%(str(node.coord),))

        #self.writemodule("# Start Function Definition")

        self.return_type = node.data_type.name

        returntype = pyrapid.Symbols().GetSymbol(self.return_type, self.module_name, self.function_name)
        sreturntype = "pyrapid.Symbols().GetSymbol(%s, %s, %s)" %(repr(self.return_type), repr(self.module_name), repr(self.function_name))

        self.params = OrderedDict()
        self.lastparamadded = None

        for i in node.parameter_list:
            #ParameterDefinitionAST or OptionalParameterDefinitionAST or SwitchParameterDefinitionAST or None
            self.visit(i, **kwargs)

        self.function_name =  node.function_name.name

        params = repr(self.params)

        def _rapid_func_(local_args_scope):
            pass

        def _error_rapid_func_(local_exception):
            pass

        def _undo_rapid_func_():
            pass

        if self.tmp_outineDeclarationATS_data is None:
            pyrapid.Symbols().AddGlobalSym(self.function_name, pyrapid.Symbol.CreateFunction(self.params, returntype, _rapid_func_, _error_rapid_func_, _undo_rapid_func_), self.module_name)
        else:
            pyrapid.Symbols().AddModuleSym(self.module_name, self.function_name, pyrapid.Symbol.CreateFunction(self.params, returntype, _rapid_proc_, _error_rapid_func_, _undo_rapid_func_))

        #self.writemodule("def error_rapid_func_%s (local_exception):" % (self.function_name,))
        with self.ModuleScope():
            #add parameter

            if not ( node.routine_error is None ):
                self.visit(node.routine_error, error_statement=True, **kwargs)

            #self.writemodule("return 0")

        #self.writemodule("def undo_rapid_func_%s ():" % (self.function_name,))
        with self.ModuleScope():
            #add parameter
            #self.writemodule("pass")

            if not ( node.routine_undo is None ):
                self.visit(node.routine_undo, undo_statement=True, **kwargs)


        #self.writemodule("def rapid_func_%s (local_args_scope):" % (self.function_name))

        with self.ModuleScope():

            with pyrapid.Symbols().Scope(modulename=self.module_name, functionname=self.function_name, invalue={}):

                for ik,iv in self.params.iteritems():
                    vartype, paramtype, ptype, psize, pdep = iv
                    if vartype=="switch":
                        getvar = pyrapid.Symbol.CreateNone()
                    else:
                        if psize==0:
                            getvar = pyrapid.Symbol.CreateVar(pyrapid.Symbols().GetSymbol(ptype, self.module_name, self.function_name).data())
                        else:
                            getvar = pyrapid.Symbol.CreateVar(pyrapid.rapid_array([], pyrapid.Symbols().GetSymbol(ptype, self.module_name, self.function_name).data) )
                    pyrapid.Symbols().AddScopeSym(ik, getvar)

                #self.writemodule( "with pyrapid.Symbols().Scope(modulename=%s, functionname=%s, invalue=local_args_scope):"%(repr(self.module_name), repr(self.function_name)))
                with self.ModuleScope():
                    #self.writemodule("pass")
                    #self.writemodule("# data definitions")

                    for i in node.data_definitions:
                        self.visit(i, **kwargs)

                    #self.writemodule("# stantments")

                    for i in node.statement_list:
                        self.visit(i, **kwargs)

                    #self.writemodule("# end stantment")

        if self.tmp_outineDeclarationATS_data is None:
            pass #self.writemodule( "pyrapid.Symbols().AddGlobalSym(%s, pyrapid.Symbol.CreateFunction(%s, %s, rapid_func_%s, error_rapid_func_%s, undo_rapid_func_%s), %s)"%(repr(self.function_name), params, sreturntype, self.function_name, self.function_name, self.function_name, repr(self.module_name),))
        else:
            pass #self.writemodule( "pyrapid.Symbols().AddModuleSym(%s, %s, pyrapid.Symbol.CreateFunction(%s, %s, rapid_func_%s, error_rapid_func_%s, undo_rapid_func_%s))"%(repr(self.module_name), params, sreturntype, repr(self.function_name), self.function_name, self.function_name, self.function_name, ))

        #self.writemodule("del rapid_func_%s" % (self.function_name,))

        self.function_name =  None
        self.return_type = None

        del self.params

        #self.writemodule("# End Function Definition")

    #

def parse_rapid_file(_path, fname):
    pth = os.path.join(_path, fname)
    assert os.path.isdir(_path), "{0} is not a valid path".format(_path)
    assert os.path.isfile(pth), "{0} is not a valid file".format(pth)

    ltext = []

    with open(pth, "r") as f:
        f_read = f.read()
        ltext.append((pth, f_read))

    attriblist = []
    for fname, text in ltext:
        print("PARSING: " + str(fname))
        parser = rapid_parser.RAPIDParser(lex_optimize=True,
                                          yacc_debug=False,
                                          yacc_optimize=False,
                                          start_from='module_declaration_list'
        )

        attriblist += parser.parse(text, fname, debuglevel=0).module_list

    allmodule = rapid_ast.ModulesAST(attriblist)
    traslate = TraslateRapidToPython(out_filename=fname+".py", out_folder=_path)

    try:
        traslate.visit(allmodule)
    except KeyError:
        log.exception("wobjdata")
        # allmodule.show()

if __name__ == '__main__':
    parse_rapid_file("/Users/jelleferinga/GIT/pyrapidparser/test", "calib_2.prg")