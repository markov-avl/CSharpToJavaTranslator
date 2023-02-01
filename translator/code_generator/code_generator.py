from translator.syntactical_analyzer import Program, declaration


class CodeGenerator:
    @staticmethod
    def generate(program: Program) -> str:
        import_usings = [decl for decl in program.declarations if isinstance(decl, declaration.ImportUsing)]
        classes = [decl for decl in program.declarations if isinstance(decl, declaration.Class)]

        java_import_usings = '\n'.join(import_using.to_java() for import_using in import_usings)
        java_classes = '\n\n'.join(class_.to_java() for class_ in classes)

        return '\n\n'.join(java_code for java_code in (java_import_usings, java_classes) if java_code)
