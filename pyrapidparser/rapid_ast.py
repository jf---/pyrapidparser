#-----------------------------------------------------------------
# ** ATTENTION **
# This code was automatically generated from the file:
# _rapid_ast.cfg 
#
# Do not modify it directly. Modify the configuration file and
# run the generator again.
# ** ** *** ** **
#
# pyRAPIDparser: rapid_ast.py
#
# AST Node classes.
#
# Copyright (C) 2008-2012, Eli Bendersky
# License: BSD
#-----------------------------------------------------------------


import sys
from ast_gen import UnknownShow, Node, NodeVisitor, NodeCompare

class IdentifierAST(Node):
    def __init__(self, name, coord=None):
        self.name = name
        self.coord = coord

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('name',)

class ModulesAST (Node):
    def __init__(self, module_list , coord=None):
        self.module_list  = module_list 
        self.coord = coord

    def children(self):
        nodelist = []
        for i, child in enumerate(self.module_list  or []):
            nodelist.append(("module_list [%d]" % (i,), child))
        return tuple(nodelist)

    attr_names = ()

class ModuleAttributeAST(Node):
    def __init__(self, name, coord=None):
        self.name = name
        self.coord = coord

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('name',)

class ModuleAST(Node):
    def __init__(self, module_name, module_attribute, type_definitions, data_definitions, routine_definitions, coord=None):
        self.module_name = module_name
        self.module_attribute = module_attribute
        self.type_definitions = type_definitions
        self.data_definitions = data_definitions
        self.routine_definitions = routine_definitions
        self.coord = coord

    def children(self):
        nodelist = []
        if self.module_name is not None: nodelist.append(("module_name", self.module_name))
        for i, child in enumerate(self.module_attribute or []):
            nodelist.append(("module_attribute[%d]" % (i,), child))
        for i, child in enumerate(self.type_definitions or []):
            nodelist.append(("type_definitions[%d]" % (i,), child))
        for i, child in enumerate(self.data_definitions or []):
            nodelist.append(("data_definitions[%d]" % (i,), child))
        for i, child in enumerate(self.routine_definitions or []):
            nodelist.append(("routine_definitions[%d]" % (i,), child))
        return tuple(nodelist)

    attr_names = ()

class CommentAST(Node):
    def __init__(self, comment, coord=None):
        self.comment = comment
        self.coord = coord

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('comment',)

class TypeDefAST(Node):
    def __init__(self, type, definition, coord=None):
        self.type = type
        self.definition = definition
        self.coord = coord

    def children(self):
        nodelist = []
        if self.definition is not None: nodelist.append(("definition", self.definition))
        return tuple(nodelist)

    attr_names = ('type',)

class RecordDefAST(Node):
    def __init__(self, record_name, components, coord=None):
        self.record_name = record_name
        self.components = components
        self.coord = coord

    def children(self):
        nodelist = []
        if self.record_name is not None: nodelist.append(("record_name", self.record_name))
        for i, child in enumerate(self.components or []):
            nodelist.append(("components[%d]" % (i,), child))
        return tuple(nodelist)

    attr_names = ()

class RecordComponentDefAST(Node):
    def __init__(self, data_type, record_component_name, coord=None):
        self.data_type = data_type
        self.record_component_name = record_component_name
        self.coord = coord

    def children(self):
        nodelist = []
        if self.data_type is not None: nodelist.append(("data_type", self.data_type))
        if self.record_component_name is not None: nodelist.append(("record_component_name", self.record_component_name))
        return tuple(nodelist)

    attr_names = ()

class AliasDefATS(Node):
    def __init__(self, type_name, alias_name, coord=None):
        self.type_name = type_name
        self.alias_name = alias_name
        self.coord = coord

    def children(self):
        nodelist = []
        if self.type_name is not None: nodelist.append(("type_name", self.type_name))
        if self.alias_name is not None: nodelist.append(("alias_name", self.alias_name))
        return tuple(nodelist)

    attr_names = ()

class DataDefATS(Node):
    def __init__(self, type, definition, coord=None):
        self.type = type
        self.definition = definition
        self.coord = coord

    def children(self):
        nodelist = []
        if self.definition is not None: nodelist.append(("definition", self.definition))
        return tuple(nodelist)

    attr_names = ('type',)

class RoutineDeclarationATS(Node):
    def __init__(self, type, definition, coord=None):
        self.type = type
        self.definition = definition
        self.coord = coord

    def children(self):
        nodelist = []
        if self.definition is not None: nodelist.append(("definition", self.definition))
        return tuple(nodelist)

    attr_names = ('type',)

class LiteralATS(Node):
    def __init__(self, value, coord=None):
        self.value = value
        self.coord = coord

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('value',)

class VarDeclarationAST(Node):
    def __init__(self, type, variable_instance, coord=None):
        self.type = type
        self.variable_instance = variable_instance
        self.coord = coord

    def children(self):
        nodelist = []
        if self.type is not None: nodelist.append(("type", self.type))
        if self.variable_instance is not None: nodelist.append(("variable_instance", self.variable_instance))
        return tuple(nodelist)

    attr_names = ()

class PersDeclarationAST(Node):
    def __init__(self, type, variable_instance, coord=None):
        self.type = type
        self.variable_instance = variable_instance
        self.coord = coord

    def children(self):
        nodelist = []
        if self.type is not None: nodelist.append(("type", self.type))
        if self.variable_instance is not None: nodelist.append(("variable_instance", self.variable_instance))
        return tuple(nodelist)

    attr_names = ()

class ConstDeclarationAST (Node):
    def __init__(self, type, variable_instance, coord=None):
        self.type = type
        self.variable_instance = variable_instance
        self.coord = coord

    def children(self):
        nodelist = []
        if self.type is not None: nodelist.append(("type", self.type))
        if self.variable_instance is not None: nodelist.append(("variable_instance", self.variable_instance))
        return tuple(nodelist)

    attr_names = ()

class VarDefinitionAST(Node):
    def __init__(self, name, value, size, coord=None):
        self.name = name
        self.value = value
        self.size = size
        self.coord = coord

    def children(self):
        nodelist = []
        if self.name is not None: nodelist.append(("name", self.name))
        if self.value is not None: nodelist.append(("value", self.value))
        for i, child in enumerate(self.size or []):
            nodelist.append(("size[%d]" % (i,), child))
        return tuple(nodelist)

    attr_names = ()

class ConstExpressionAST(Node):
    def __init__(self, expression, coord=None):
        self.expression = expression
        self.coord = coord

    def children(self):
        nodelist = []
        if self.expression is not None: nodelist.append(("expression", self.expression))
        return tuple(nodelist)

    attr_names = ()

class ExpressionAST(Node):
    def __init__(self, expr, coord=None):
        self.expr = expr
        self.coord = coord

    def children(self):
        nodelist = []
        if self.expr is not None: nodelist.append(("expr", self.expr))
        return tuple(nodelist)

    attr_names = ()

class Operator1AST (Node):
    def __init__(self, operator, par1, coord=None):
        self.operator = operator
        self.par1 = par1
        self.coord = coord

    def children(self):
        nodelist = []
        return tuple(nodelist)

    attr_names = ('operator','par1',)

class Operator2AST (Node):
    def __init__(self, operator, par1, par2, coord=None):
        self.operator = operator
        self.par1 = par1
        self.par2 = par2
        self.coord = coord

    def children(self):
        nodelist = []
        if self.par1 is not None: nodelist.append(("par1", self.par1))
        if self.par2 is not None: nodelist.append(("par2", self.par2))
        return tuple(nodelist)

    attr_names = ('operator',)

class AggregateAST (Node):
    def __init__(self, expr, coord=None):
        self.expr = expr
        self.coord = coord

    def children(self):
        nodelist = []
        for i, child in enumerate(self.expr or []):
            nodelist.append(("expr[%d]" % (i,), child))
        return tuple(nodelist)

    attr_names = ()

class VariableAST(Node):
    def __init__(self, var, index, component, coord=None):
        self.var = var
        self.index = index
        self.component = component
        self.coord = coord

    def children(self):
        nodelist = []
        if self.var is not None: nodelist.append(("var", self.var))
        if self.component is not None: nodelist.append(("component", self.component))
        for i, child in enumerate(self.index or []):
            nodelist.append(("index[%d]" % (i,), child))
        return tuple(nodelist)

    attr_names = ()

class FunctionCallAST (Node):
    def __init__(self, function, arguments, coord=None):
        self.function = function
        self.arguments = arguments
        self.coord = coord

    def children(self):
        nodelist = []
        if self.function is not None: nodelist.append(("function", self.function))
        for i, child in enumerate(self.arguments or []):
            nodelist.append(("arguments[%d]" % (i,), child))
        return tuple(nodelist)

    attr_names = ()

class ProcedureCallAST (Node):
    def __init__(self, procedure, arguments, coord=None):
        self.procedure = procedure
        self.arguments = arguments
        self.coord = coord

    def children(self):
        nodelist = []
        if self.procedure is not None: nodelist.append(("procedure", self.procedure))
        for i, child in enumerate(self.arguments or []):
            nodelist.append(("arguments[%d]" % (i,), child))
        return tuple(nodelist)

    attr_names = ()

class FunctionArgumentAST (Node):
    def __init__(self, type, argumentname, argumentvalue, coord=None):
        self.type = type
        self.argumentname = argumentname
        self.argumentvalue = argumentvalue
        self.coord = coord

    def children(self):
        nodelist = []
        if self.argumentname is not None: nodelist.append(("argumentname", self.argumentname))
        if self.argumentvalue is not None: nodelist.append(("argumentvalue", self.argumentvalue))
        return tuple(nodelist)

    attr_names = ('type',)

class ProcedureArgumentAST (Node):
    def __init__(self, type, argumentname, argumentvalue, coord=None):
        self.type = type
        self.argumentname = argumentname
        self.argumentvalue = argumentvalue
        self.coord = coord

    def children(self):
        nodelist = []
        if self.argumentname is not None: nodelist.append(("argumentname", self.argumentname))
        if self.argumentvalue is not None: nodelist.append(("argumentvalue", self.argumentvalue))
        return tuple(nodelist)

    attr_names = ('type',)

class ProcedureDeclarationAST (Node):
    def __init__(self, procedure_name, parameter_list, data_definitions, statement_list, routine_backward, routine_error, routine_undo, coord=None):
        self.procedure_name = procedure_name
        self.parameter_list = parameter_list
        self.data_definitions = data_definitions
        self.statement_list = statement_list
        self.routine_backward = routine_backward
        self.routine_error = routine_error
        self.routine_undo = routine_undo
        self.coord = coord

    def children(self):
        nodelist = []
        if self.procedure_name is not None: nodelist.append(("procedure_name", self.procedure_name))
        if self.routine_backward is not None: nodelist.append(("routine_backward", self.routine_backward))
        if self.routine_error is not None: nodelist.append(("routine_error", self.routine_error))
        if self.routine_undo is not None: nodelist.append(("routine_undo", self.routine_undo))
        for i, child in enumerate(self.parameter_list or []):
            nodelist.append(("parameter_list[%d]" % (i,), child))
        for i, child in enumerate(self.data_definitions or []):
            nodelist.append(("data_definitions[%d]" % (i,), child))
        for i, child in enumerate(self.statement_list or []):
            nodelist.append(("statement_list[%d]" % (i,), child))
        return tuple(nodelist)

    attr_names = ()

class FunctionDeclarationAST (Node):
    def __init__(self, data_type, function_name, parameter_list, data_definitions, statement_list, routine_error, routine_undo, coord=None):
        self.data_type = data_type
        self.function_name = function_name
        self.parameter_list = parameter_list
        self.data_definitions = data_definitions
        self.statement_list = statement_list
        self.routine_error = routine_error
        self.routine_undo = routine_undo
        self.coord = coord

    def children(self):
        nodelist = []
        if self.data_type is not None: nodelist.append(("data_type", self.data_type))
        if self.function_name is not None: nodelist.append(("function_name", self.function_name))
        if self.routine_error is not None: nodelist.append(("routine_error", self.routine_error))
        if self.routine_undo is not None: nodelist.append(("routine_undo", self.routine_undo))
        for i, child in enumerate(self.parameter_list or []):
            nodelist.append(("parameter_list[%d]" % (i,), child))
        for i, child in enumerate(self.data_definitions or []):
            nodelist.append(("data_definitions[%d]" % (i,), child))
        for i, child in enumerate(self.statement_list or []):
            nodelist.append(("statement_list[%d]" % (i,), child))
        return tuple(nodelist)

    attr_names = ()

class TrapDeclarationAST (Node):
    def __init__(self, procedure_name, data_definitions, statement_list, routine_error, routine_undo, coord=None):
        self.procedure_name = procedure_name
        self.data_definitions = data_definitions
        self.statement_list = statement_list
        self.routine_error = routine_error
        self.routine_undo = routine_undo
        self.coord = coord

    def children(self):
        nodelist = []
        if self.procedure_name is not None: nodelist.append(("procedure_name", self.procedure_name))
        if self.routine_error is not None: nodelist.append(("routine_error", self.routine_error))
        if self.routine_undo is not None: nodelist.append(("routine_undo", self.routine_undo))
        for i, child in enumerate(self.data_definitions or []):
            nodelist.append(("data_definitions[%d]" % (i,), child))
        for i, child in enumerate(self.statement_list or []):
            nodelist.append(("statement_list[%d]" % (i,), child))
        return tuple(nodelist)

    attr_names = ()

class RoutineBackwardAST (Node):
    def __init__(self, statement_list, coord=None):
        self.statement_list = statement_list
        self.coord = coord

    def children(self):
        nodelist = []
        for i, child in enumerate(self.statement_list or []):
            nodelist.append(("statement_list[%d]" % (i,), child))
        return tuple(nodelist)

    attr_names = ()

class RoutineErrorAST (Node):
    def __init__(self, error_number_list, statement_list, coord=None):
        self.error_number_list = error_number_list
        self.statement_list = statement_list
        self.coord = coord

    def children(self):
        nodelist = []
        for i, child in enumerate(self.error_number_list or []):
            nodelist.append(("error_number_list[%d]" % (i,), child))
        for i, child in enumerate(self.statement_list or []):
            nodelist.append(("statement_list[%d]" % (i,), child))
        return tuple(nodelist)

    attr_names = ()

class RoutineUndoAST (Node):
    def __init__(self, statement_list, coord=None):
        self.statement_list = statement_list
        self.coord = coord

    def children(self):
        nodelist = []
        for i, child in enumerate(self.statement_list or []):
            nodelist.append(("statement_list[%d]" % (i,), child))
        return tuple(nodelist)

    attr_names = ()

class StatementAST(Node):
    def __init__(self, statement, coord=None):
        self.statement = statement
        self.coord = coord

    def children(self):
        nodelist = []
        if self.statement is not None: nodelist.append(("statement", self.statement))
        return tuple(nodelist)

    attr_names = ()

class LabelAST(Node):
    def __init__(self, name, coord=None):
        self.name = name
        self.coord = coord

    def children(self):
        nodelist = []
        if self.name is not None: nodelist.append(("name", self.name))
        return tuple(nodelist)

    attr_names = ()

class AssignmentStatementAST (Node):
    def __init__(self, dest, source, coord=None):
        self.dest = dest
        self.source = source
        self.coord = coord

    def children(self):
        nodelist = []
        if self.dest is not None: nodelist.append(("dest", self.dest))
        if self.source is not None: nodelist.append(("source", self.source))
        return tuple(nodelist)

    attr_names = ()

class GotoStatementAST (Node):
    def __init__(self, dest, coord=None):
        self.dest = dest
        self.coord = coord

    def children(self):
        nodelist = []
        if self.dest is not None: nodelist.append(("dest", self.dest))
        return tuple(nodelist)

    attr_names = ()

class ReturnStatementAST (Node):
    def __init__(self, result, coord=None):
        self.result = result
        self.coord = coord

    def children(self):
        nodelist = []
        if self.result is not None: nodelist.append(("result", self.result))
        return tuple(nodelist)

    attr_names = ()

class RaiseStatementAST (Node):
    def __init__(self, error_number, coord=None):
        self.error_number = error_number
        self.coord = coord

    def children(self):
        nodelist = []
        if self.error_number is not None: nodelist.append(("error_number", self.error_number))
        return tuple(nodelist)

    attr_names = ()

class ExitStatementAST (Node):
    def __init__(self, coord=None):
        self.coord = coord

    def children(self):
        return ()

    attr_names = ()

class RetryStatementAST (Node):
    def __init__(self, coord=None):
        self.coord = coord

    def children(self):
        return ()

    attr_names = ()

class TrynextStatementAST (Node):
    def __init__(self, coord=None):
        self.coord = coord

    def children(self):
        return ()

    attr_names = ()

class ConnectStatementAST (Node):
    def __init__(self, connect_taget, trap, coord=None):
        self.connect_taget = connect_taget
        self.trap = trap
        self.coord = coord

    def children(self):
        nodelist = []
        if self.connect_taget is not None: nodelist.append(("connect_taget", self.connect_taget))
        if self.trap is not None: nodelist.append(("trap", self.trap))
        return tuple(nodelist)

    attr_names = ()

class IfStatement(Node):
    def __init__(self, condition, statement_list, elseif_list, else_statement_list, coord=None):
        self.condition = condition
        self.statement_list = statement_list
        self.elseif_list = elseif_list
        self.else_statement_list = else_statement_list
        self.coord = coord

    def children(self):
        nodelist = []
        if self.condition is not None: nodelist.append(("condition", self.condition))
        for i, child in enumerate(self.statement_list or []):
            nodelist.append(("statement_list[%d]" % (i,), child))
        for i, child in enumerate(self.elseif_list or []):
            nodelist.append(("elseif_list[%d]" % (i,), child))
        for i, child in enumerate(self.else_statement_list or []):
            nodelist.append(("else_statement_list[%d]" % (i,), child))
        return tuple(nodelist)

    attr_names = ()

class ElseIfStatement(Node):
    def __init__(self, condition, statement_list, coord=None):
        self.condition = condition
        self.statement_list = statement_list
        self.coord = coord

    def children(self):
        nodelist = []
        if self.condition is not None: nodelist.append(("condition", self.condition))
        for i, child in enumerate(self.statement_list or []):
            nodelist.append(("statement_list[%d]" % (i,), child))
        return tuple(nodelist)

    attr_names = ()

class ForStatement(Node):
    def __init__(self, loop_variable, ifrom, ito, istep, statement_list, coord=None):
        self.loop_variable = loop_variable
        self.ifrom = ifrom
        self.ito = ito
        self.istep = istep
        self.statement_list = statement_list
        self.coord = coord

    def children(self):
        nodelist = []
        if self.loop_variable is not None: nodelist.append(("loop_variable", self.loop_variable))
        if self.ifrom is not None: nodelist.append(("ifrom", self.ifrom))
        if self.ito is not None: nodelist.append(("ito", self.ito))
        if self.istep is not None: nodelist.append(("istep", self.istep))
        for i, child in enumerate(self.statement_list or []):
            nodelist.append(("statement_list[%d]" % (i,), child))
        return tuple(nodelist)

    attr_names = ()

class WhileStatement(Node):
    def __init__(self, condition, statement_list, coord=None):
        self.condition = condition
        self.statement_list = statement_list
        self.coord = coord

    def children(self):
        nodelist = []
        if self.condition is not None: nodelist.append(("condition", self.condition))
        for i, child in enumerate(self.statement_list or []):
            nodelist.append(("statement_list[%d]" % (i,), child))
        return tuple(nodelist)

    attr_names = ()

class TestStatement(Node):
    def __init__(self, expression, cases, default, coord=None):
        self.expression = expression
        self.cases = cases
        self.default = default
        self.coord = coord

    def children(self):
        nodelist = []
        if self.expression is not None: nodelist.append(("expression", self.expression))
        for i, child in enumerate(self.cases or []):
            nodelist.append(("cases[%d]" % (i,), child))
        for i, child in enumerate(self.default or []):
            nodelist.append(("default[%d]" % (i,), child))
        return tuple(nodelist)

    attr_names = ()

class CaseStatement(Node):
    def __init__(self, test_value, statement_list, coord=None):
        self.test_value = test_value
        self.statement_list = statement_list
        self.coord = coord

    def children(self):
        nodelist = []
        for i, child in enumerate(self.test_value or []):
            nodelist.append(("test_value[%d]" % (i,), child))
        for i, child in enumerate(self.statement_list or []):
            nodelist.append(("statement_list[%d]" % (i,), child))
        return tuple(nodelist)

    attr_names = ()

class ParameterDefinitionAST(Node):
    def __init__(self, parameter_type, type, name, size, coord=None):
        self.parameter_type = parameter_type
        self.type = type
        self.name = name
        self.size = size
        self.coord = coord

    def children(self):
        nodelist = []
        if self.type is not None: nodelist.append(("type", self.type))
        if self.name is not None: nodelist.append(("name", self.name))
        return tuple(nodelist)

    attr_names = ('parameter_type','size',)

class SwitchParameterDefinitionAST(Node):
    def __init__(self, name, coord=None):
        self.name = name
        self.coord = coord

    def children(self):
        nodelist = []
        if self.name is not None: nodelist.append(("name", self.name))
        return tuple(nodelist)

    attr_names = ()

class OptionalParameterDefinitionAST (Node):
    def __init__(self, parameter, switchs, coord=None):
        self.parameter = parameter
        self.switchs = switchs
        self.coord = coord

    def children(self):
        nodelist = []
        if self.parameter is not None: nodelist.append(("parameter", self.parameter))
        for i, child in enumerate(self.switchs or []):
            nodelist.append(("switchs[%d]" % (i,), child))
        return tuple(nodelist)

    attr_names = ()

