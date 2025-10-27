#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CVD 语法解析器测试脚本
使用生成的 ANTLR 解析器解析 CVD 设备反应腔控制脚本
"""

from antlr4 import FileStream, CommonTokenStream
from cvdLexer import cvdLexer
from cvdParser import cvdParser
import sys


def main():
    # 读取输入文件（可以通过命令行参数指定）
    input_file = sys.argv[1] if len(sys.argv) > 1 else "cvd_sample.txt"
    
    try:
        # 创建输入流
        input_stream = FileStream(input_file, encoding='utf-8')
        
        # 创建词法分析器
        lexer = cvdLexer(input_stream)
        
        # 创建词法分析器错误监听器
        class LexerErrorListener:
            def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
                print(f"词法分析错误 第 {line} 行, 第 {column} 列: {msg}")
        
        lexer.removeErrorListeners()
        lexer.addErrorListener(LexerErrorListener())
        
        # 创建标记流
        stream = CommonTokenStream(lexer)
        
        # 创建语法分析器
        parser = cvdParser(stream)
        
        # 创建语法分析器错误监听器
        class ParserErrorListener:
            def __init__(self):
                self.errors = []
            
            def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
                error_msg = f"语法分析错误 第 {line} 行, 第 {column} 列: {msg}"
                print(error_msg)
                self.errors.append(error_msg)
            
            def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
                pass
            
            def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
                pass
            
            def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
                pass
        
        error_listener = ParserErrorListener()
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)
        
        print("=" * 60)
        print(f"开始解析文件: {input_file}")
        print("=" * 60)
        
        # 解析脚本
        tree = parser.script()
        
        # 检查是否有错误
        if error_listener.errors:
            print(f"\n⚠ 解析过程中发现 {len(error_listener.errors)} 个错误：")
            for error in error_listener.errors:
                print(f"  - {error}")
        else:
            print("\n✓ 解析成功！没有语法错误。")
        
        # 提取摘要信息
        params = []
        vars = []
        steps = []
        until_stmts = []
        
        def extract_info(node):
            if hasattr(node, 'getRuleIndex'):
                rule_index = node.getRuleIndex()
                rule_name = parser.ruleNames[rule_index] if rule_index < len(parser.ruleNames) else "unknown"
                
                # 提取参数声明
                if rule_name == 'paramDecl' and hasattr(node, 'IDENT') and node.IDENT():
                    # 检查是否有 runtime 关键字（通过遍历子节点）
                    is_runtime = False
                    if hasattr(node, 'getChildCount'):
                        for i in range(node.getChildCount()):
                            child = node.getChild(i)
                            if hasattr(child, 'getText') and child.getText() == 'runtime':
                                is_runtime = True
                                break
                    
                    var_name = node.IDENT().getText()
                    # 尝试提取表达式值
                    if hasattr(node, 'expr') and node.expr():
                        expr_text = node.expr().getText()
                        params.append({
                            'name': var_name,
                            'runtime': is_runtime,
                            'value': expr_text
                        })
                
                # 提取变量声明
                elif rule_name == 'varDecl' and hasattr(node, 'IDENT') and node.IDENT():
                    var_name = node.IDENT().getText()
                    if hasattr(node, 'expr') and node.expr():
                        expr_text = node.expr().getText()
                        vars.append({
                            'name': var_name,
                            'value': expr_text
                        })
                
                # 提取步骤声明
                elif rule_name == 'stepDecl' and hasattr(node, 'STRING') and node.STRING():
                    step_name = node.STRING().getText()
                    step_duration = ""
                    if hasattr(node, 'NUMBER') and node.NUMBER():
                        step_duration = node.NUMBER().getText()
                    steps.append({
                        'name': step_name,
                        'duration': step_duration
                    })
                
                # 提取 until 语句
                elif rule_name == 'untilStmt':
                    if hasattr(node, 'conditionExpr') and node.conditionExpr():
                        cond_text = node.conditionExpr().getText()
                        until_stmts.append({
                            'condition': cond_text
                        })
            
            # 递归遍历子节点
            if hasattr(node, 'getChildCount'):
                for i in range(node.getChildCount()):
                    extract_info(node.getChild(i))
        
        extract_info(tree)
        
        # 打印摘要
        print("\n" + "=" * 60)
        print("📊 解析摘要")
        print("=" * 60)
        
        # 打印参数声明
        if params:
            print(f"\n🔧 参数声明 (共 {len(params)} 个):")
            runtime_params = [p for p in params if p['runtime']]
            non_runtime_params = [p for p in params if not p['runtime']]
            
            if runtime_params:
                print("  Runtime 参数:")
                for p in runtime_params:
                    print(f"    {p['name']} = {p['value']}")
            
            if non_runtime_params:
                print("  普通参数:")
                for p in non_runtime_params:
                    print(f"    {p['name']} = {p['value']}")
        else:
            print("\n🔧 参数声明: 无")
        
        # 打印变量声明
        if vars:
            print(f"\n📝 变量声明 (共 {len(vars)} 个):")
            for v in vars:
                print(f"    {v['name']} = {v['value']}")
        else:
            print("\n📝 变量声明: 无")
        
        # 打印步骤声明
        if steps:
            print(f"\n📋 步骤声明 (共 {len(steps)} 个):")
            for i, s in enumerate(steps, 1):
                duration_str = f"时长: {s['duration']}秒" if s['duration'] else "时长: 未指定"
                print(f"  {i}. {s['name']} ({duration_str})")
        else:
            print("\n📋 步骤声明: 无")
        
        # 打印 until 语句
        if until_stmts:
            print(f"\n⏳ Until 条件语句 (共 {len(until_stmts)} 个):")
            for i, u in enumerate(until_stmts, 1):
                print(f"  {i}. until {u['condition']}")
        else:
            print("\n⏳ Until 条件语句: 无")
        
        # 统计信息
        statement_count = len(params) + len(vars) + len(steps) + len(until_stmts)
        
        print(f"\n{'='*60}")
        print(f"统计信息: 共解析到 {statement_count} 条语句")
        print(f"{'='*60}")
        
        return len(error_listener.errors) == 0
        
    except FileNotFoundError:
        print(f"错误: 找不到文件 '{input_file}'")
        return False
    except Exception as e:
        print(f"错误: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
