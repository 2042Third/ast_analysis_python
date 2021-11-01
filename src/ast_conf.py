Module(
  body=[
    ImportFrom(
      module='tkinter',
      names=[
        alias(name='*')],
      level=0),
    ImportFrom(
      module='PIL',
      names=[
        alias(name='ImageTk'),
        alias(name='Image')],
      level=0),
    Import(
      names=[
        alias(name='shutil')]),
    Import(
      names=[
        alias(name='os')]),
    Import(
      names=[
        alias(name='easygui')]),
    ImportFrom(
      module='tkinter',
      names=[
        alias(name='filedialog')],
      level=0),
    ImportFrom(
      module='tkinter',
      names=[
        alias(name='messagebox', asname='mb')],
      level=0),
    FunctionDef(
      name='open_window',
      args=arguments(
        posonlyargs=[],
        args=[],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Assign(
          targets=[
            Name(id='read', ctx=Store())],
          value=Call(
            func=Attribute(
              value=Name(id='easygui', ctx=Load()),
              attr='fileopenbox',
              ctx=Load()),
            args=[],
            keywords=[])),
        Return(
          value=Name(id='read', ctx=Load()))],
      decorator_list=[]),
    FunctionDef(
      name='open_file',
      args=arguments(
        posonlyargs=[],
        args=[],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Assign(
          targets=[
            Name(id='string', ctx=Store())],
          value=Call(
            func=Name(id='open_window', ctx=Load()),
            args=[],
            keywords=[])),
        Try(
          body=[
            Expr(
              value=Call(
                func=Attribute(
                  value=Name(id='os', ctx=Load()),
                  attr='startfile',
                  ctx=Load()),
                args=[
                  Name(id='string', ctx=Load())],
                keywords=[]))],
          handlers=[
            ExceptHandler(
              body=[
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Name(id='mb', ctx=Load()),
                      attr='showinfo',
                      ctx=Load()),
                    args=[
                      Constant(value='confirmation'),
                      Constant(value='File not found!')],
                    keywords=[]))])],
          orelse=[],
          finalbody=[])],
      decorator_list=[]),
    FunctionDef(
      name='copy_file',
      args=arguments(
        posonlyargs=[],
        args=[],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Assign(
          targets=[
            Name(id='source1', ctx=Store())],
          value=Call(
            func=Name(id='open_window', ctx=Load()),
            args=[],
            keywords=[])),
        Assign(
          targets=[
            Name(id='destination1', ctx=Store())],
          value=Call(
            func=Attribute(
              value=Name(id='filedialog', ctx=Load()),
              attr='askdirectory',
              ctx=Load()),
            args=[],
            keywords=[])),
        Expr(
          value=Call(
            func=Attribute(
              value=Name(id='shutil', ctx=Load()),
              attr='copy',
              ctx=Load()),
            args=[
              Name(id='source1', ctx=Load()),
              Name(id='destination1', ctx=Load())],
            keywords=[])),
        Expr(
          value=Call(
            func=Attribute(
              value=Name(id='mb', ctx=Load()),
              attr='showinfo',
              ctx=Load()),
            args=[
              Constant(value='confirmation'),
              Constant(value='File Copied !')],
            keywords=[]))],
      decorator_list=[]),
    FunctionDef(
      name='delete_file',
      args=arguments(
        posonlyargs=[],
        args=[],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Assign(
          targets=[
            Name(id='del_file', ctx=Store())],
          value=Call(
            func=Name(id='open_window', ctx=Load()),
            args=[],
            keywords=[])),
        If(
          test=Call(
            func=Attribute(
              value=Attribute(
                value=Name(id='os', ctx=Load()),
                attr='path',
                ctx=Load()),
              attr='exists',
              ctx=Load()),
            args=[
              Name(id='del_file', ctx=Load())],
            keywords=[]),
          body=[
            Expr(
              value=Call(
                func=Attribute(
                  value=Name(id='os', ctx=Load()),
                  attr='remove',
                  ctx=Load()),
                args=[
                  Name(id='del_file', ctx=Load())],
                keywords=[]))],
          orelse=[
            Expr(
              value=Call(
                func=Attribute(
                  value=Name(id='mb', ctx=Load()),
                  attr='showinfo',
                  ctx=Load()),
                args=[
                  Constant(value='confirmation'),
                  Constant(value='File not found !')],
                keywords=[]))])],
      decorator_list=[]),
    FunctionDef(
      name='rename_file',
      args=arguments(
        posonlyargs=[],
        args=[],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Assign(
          targets=[
            Name(id='chosenFile', ctx=Store())],
          value=Call(
            func=Name(id='open_window', ctx=Load()),
            args=[],
            keywords=[])),
        Assign(
          targets=[
            Name(id='path1', ctx=Store())],
          value=Call(
            func=Attribute(
              value=Attribute(
                value=Name(id='os', ctx=Load()),
                attr='path',
                ctx=Load()),
              attr='dirname',
              ctx=Load()),
            args=[
              Name(id='chosenFile', ctx=Load())],
            keywords=[])),
        Assign(
          targets=[
            Name(id='extension', ctx=Store())],
          value=Subscript(
            value=Call(
              func=Attribute(
                value=Attribute(
                  value=Name(id='os', ctx=Load()),
                  attr='path',
                  ctx=Load()),
                attr='splitext',
                ctx=Load()),
              args=[
                Name(id='chosenFile', ctx=Load())],
              keywords=[]),
            slice=Constant(value=1),
            ctx=Load())),
        Expr(
          value=Call(
            func=Name(id='print', ctx=Load()),
            args=[
              Constant(value='Enter new name for the chosen file')],
            keywords=[])),
        Assign(
          targets=[
            Name(id='newName', ctx=Store())],
          value=Call(
            func=Name(id='input', ctx=Load()),
            args=[],
            keywords=[])),
        Assign(
          targets=[
            Name(id='path', ctx=Store())],
          value=Call(
            func=Attribute(
              value=Attribute(
                value=Name(id='os', ctx=Load()),
                attr='path',
                ctx=Load()),
              attr='join',
              ctx=Load()),
            args=[
              Name(id='path1', ctx=Load()),
              BinOp(
                left=Name(id='newName', ctx=Load()),
                op=Add(),
                right=Name(id='extension', ctx=Load()))],
            keywords=[])),
        Expr(
          value=Call(
            func=Name(id='print', ctx=Load()),
            args=[
              Name(id='path', ctx=Load())],
            keywords=[])),
        Expr(
          value=Call(
            func=Attribute(
              value=Name(id='os', ctx=Load()),
              attr='rename',
              ctx=Load()),
            args=[
              Name(id='chosenFile', ctx=Load()),
              Name(id='path', ctx=Load())],
            keywords=[])),
        Expr(
          value=Call(
            func=Attribute(
              value=Name(id='mb', ctx=Load()),
              attr='showinfo',
              ctx=Load()),
            args=[
              Constant(value='confirmation'),
              Constant(value='File Renamed !')],
            keywords=[]))],
      decorator_list=[]),
    FunctionDef(
      name='move_file',
      args=arguments(
        posonlyargs=[],
        args=[],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Assign(
          targets=[
            Name(id='source', ctx=Store())],
          value=Call(
            func=Name(id='open_window', ctx=Load()),
            args=[],
            keywords=[])),
        Assign(
          targets=[
            Name(id='destination', ctx=Store())],
          value=Call(
            func=Attribute(
              value=Name(id='filedialog', ctx=Load()),
              attr='askdirectory',
              ctx=Load()),
            args=[],
            keywords=[])),
        If(
          test=Compare(
            left=Name(id='source', ctx=Load()),
            ops=[
              Eq()],
            comparators=[
              Name(id='destination', ctx=Load())]),
          body=[
            Expr(
              value=Call(
                func=Attribute(
                  value=Name(id='mb', ctx=Load()),
                  attr='showinfo',
                  ctx=Load()),
                args=[
                  Constant(value='confirmation'),
                  Constant(value='Source and destination are same')],
                keywords=[]))],
          orelse=[
            Expr(
              value=Call(
                func=Attribute(
                  value=Name(id='shutil', ctx=Load()),
                  attr='move',
                  ctx=Load()),
                args=[
                  Name(id='source', ctx=Load()),
                  Name(id='destination', ctx=Load())],
                keywords=[])),
            Expr(
              value=Call(
                func=Attribute(
                  value=Name(id='mb', ctx=Load()),
                  attr='showinfo',
                  ctx=Load()),
                args=[
                  Constant(value='confirmation'),
                  Constant(value='File Moved !')],
                keywords=[]))])],
      decorator_list=[]),
    FunctionDef(
      name='make_folder',
      args=arguments(
        posonlyargs=[],
        args=[],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Assign(
          targets=[
            Name(id='newFolderPath', ctx=Store())],
          value=Call(
            func=Attribute(
              value=Name(id='filedialog', ctx=Load()),
              attr='askdirectory',
              ctx=Load()),
            args=[],
            keywords=[])),
        Expr(
          value=Call(
            func=Name(id='print', ctx=Load()),
            args=[
              Constant(value='Enter name of new folder')],
            keywords=[])),
        Assign(
          targets=[
            Name(id='newFolder', ctx=Store())],
          value=Call(
            func=Name(id='input', ctx=Load()),
            args=[],
            keywords=[])),
        Assign(
          targets=[
            Name(id='path', ctx=Store())],
          value=Call(
            func=Attribute(
              value=Attribute(
                value=Name(id='os', ctx=Load()),
                attr='path',
                ctx=Load()),
              attr='join',
              ctx=Load()),
            args=[
              Name(id='newFolderPath', ctx=Load()),
              Name(id='newFolder', ctx=Load())],
            keywords=[])),
        Expr(
          value=Call(
            func=Attribute(
              value=Name(id='os', ctx=Load()),
              attr='mkdir',
              ctx=Load()),
            args=[
              Name(id='path', ctx=Load())],
            keywords=[])),
        Expr(
          value=Call(
            func=Attribute(
              value=Name(id='mb', ctx=Load()),
              attr='showinfo',
              ctx=Load()),
            args=[
              Constant(value='confirmation'),
              Constant(value='Folder created !')],
            keywords=[]))],
      decorator_list=[]),
    FunctionDef(
      name='remove_folder',
      args=arguments(
        posonlyargs=[],
        args=[],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Assign(
          targets=[
            Name(id='delFolder', ctx=Store())],
          value=Call(
            func=Attribute(
              value=Name(id='filedialog', ctx=Load()),
              attr='askdirectory',
              ctx=Load()),
            args=[],
            keywords=[])),
        Expr(
          value=Call(
            func=Attribute(
              value=Name(id='os', ctx=Load()),
              attr='rmdir',
              ctx=Load()),
            args=[
              Name(id='delFolder', ctx=Load())],
            keywords=[])),
        Expr(
          value=Call(
            func=Attribute(
              value=Name(id='mb', ctx=Load()),
              attr='showinfo',
              ctx=Load()),
            args=[
              Constant(value='confirmation'),
              Constant(value='Folder Deleted !')],
            keywords=[]))],
      decorator_list=[]),
    FunctionDef(
      name='list_files',
      args=arguments(
        posonlyargs=[],
        args=[],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Assign(
          targets=[
            Name(id='folderList', ctx=Store())],
          value=Call(
            func=Attribute(
              value=Name(id='filedialog', ctx=Load()),
              attr='askdirectory',
              ctx=Load()),
            args=[],
            keywords=[])),
        Assign(
          targets=[
            Name(id='sortlist', ctx=Store())],
          value=Call(
            func=Name(id='sorted', ctx=Load()),
            args=[
              Call(
                func=Attribute(
                  value=Name(id='os', ctx=Load()),
                  attr='listdir',
                  ctx=Load()),
                args=[
                  Name(id='folderList', ctx=Load())],
                keywords=[])],
            keywords=[])),
        Assign(
          targets=[
            Name(id='i', ctx=Store())],
          value=Constant(value=0)),
        Expr(
          value=Call(
            func=Name(id='print', ctx=Load()),
            args=[
              Constant(value='Files in '),
              Name(id='folderList', ctx=Load()),
              Constant(value='folder are:')],
            keywords=[])),
        While(
          test=Compare(
            left=Name(id='i', ctx=Load()),
            ops=[
              Lt()],
            comparators=[
              Call(
                func=Name(id='len', ctx=Load()),
                args=[
                  Name(id='sortlist', ctx=Load())],
                keywords=[])]),
          body=[
            Expr(
              value=Call(
                func=Name(id='print', ctx=Load()),
                args=[
                  BinOp(
                    left=Subscript(
                      value=Name(id='sortlist', ctx=Load()),
                      slice=Name(id='i', ctx=Load()),
                      ctx=Load()),
                    op=Add(),
                    right=Constant(value='\n'))],
                keywords=[])),
            AugAssign(
              target=Name(id='i', ctx=Store()),
              op=Add(),
              value=Constant(value=1))],
          orelse=[])],
      decorator_list=[]),
    Assign(
      targets=[
        Name(id='root', ctx=Store())],
      value=Call(
        func=Name(id='Tk', ctx=Load()),
        args=[],
        keywords=[])),
    Expr(
      value=Call(
        func=Attribute(
          value=Call(
            func=Name(id='Label', ctx=Load()),
            args=[
              Name(id='root', ctx=Load())],
            keywords=[
              keyword(
                arg='text',
                value=Constant(value='TechVidvan File Manager')),
              keyword(
                arg='font',
                value=Tuple(
                  elts=[
                    Constant(value='Helvetica'),
                    Constant(value=16)],
                  ctx=Load())),
              keyword(
                arg='fg',
                value=Constant(value='blue'))]),
          attr='grid',
          ctx=Load()),
        args=[],
        keywords=[
          keyword(
            arg='row',
            value=Constant(value=5)),
          keyword(
            arg='column',
            value=Constant(value=2))])),
    Expr(
      value=Call(
        func=Attribute(
          value=Call(
            func=Name(id='Button', ctx=Load()),
            args=[
              Name(id='root', ctx=Load())],
            keywords=[
              keyword(
                arg='text',
                value=Constant(value='Open a File')),
              keyword(
                arg='command',
                value=Name(id='open_file', ctx=Load()))]),
          attr='grid',
          ctx=Load()),
        args=[],
        keywords=[
          keyword(
            arg='row',
            value=Constant(value=15)),
          keyword(
            arg='column',
            value=Constant(value=2))])),
    Expr(
      value=Call(
        func=Attribute(
          value=Call(
            func=Name(id='Button', ctx=Load()),
            args=[
              Name(id='root', ctx=Load())],
            keywords=[
              keyword(
                arg='text',
                value=Constant(value='Copy a File')),
              keyword(
                arg='command',
                value=Name(id='copy_file', ctx=Load()))]),
          attr='grid',
          ctx=Load()),
        args=[],
        keywords=[
          keyword(
            arg='row',
            value=Constant(value=25)),
          keyword(
            arg='column',
            value=Constant(value=2))])),
    Expr(
      value=Call(
        func=Attribute(
          value=Call(
            func=Name(id='Button', ctx=Load()),
            args=[
              Name(id='root', ctx=Load())],
            keywords=[
              keyword(
                arg='text',
                value=Constant(value='Delete a File')),
              keyword(
                arg='command',
                value=Name(id='delete_file', ctx=Load()))]),
          attr='grid',
          ctx=Load()),
        args=[],
        keywords=[
          keyword(
            arg='row',
            value=Constant(value=35)),
          keyword(
            arg='column',
            value=Constant(value=2))])),
    Expr(
      value=Call(
        func=Attribute(
          value=Call(
            func=Name(id='Button', ctx=Load()),
            args=[
              Name(id='root', ctx=Load())],
            keywords=[
              keyword(
                arg='text',
                value=Constant(value='Rename a File')),
              keyword(
                arg='command',
                value=Name(id='rename_file', ctx=Load()))]),
          attr='grid',
          ctx=Load()),
        args=[],
        keywords=[
          keyword(
            arg='row',
            value=Constant(value=45)),
          keyword(
            arg='column',
            value=Constant(value=2))])),
    Expr(
      value=Call(
        func=Attribute(
          value=Call(
            func=Name(id='Button', ctx=Load()),
            args=[
              Name(id='root', ctx=Load())],
            keywords=[
              keyword(
                arg='text',
                value=Constant(value='Move a File')),
              keyword(
                arg='command',
                value=Name(id='move_file', ctx=Load()))]),
          attr='grid',
          ctx=Load()),
        args=[],
        keywords=[
          keyword(
            arg='row',
            value=Constant(value=55)),
          keyword(
            arg='column',
            value=Constant(value=2))])),
    Expr(
      value=Call(
        func=Attribute(
          value=Call(
            func=Name(id='Button', ctx=Load()),
            args=[
              Name(id='root', ctx=Load())],
            keywords=[
              keyword(
                arg='text',
                value=Constant(value='Make a Folder')),
              keyword(
                arg='command',
                value=Name(id='make_folder', ctx=Load()))]),
          attr='grid',
          ctx=Load()),
        args=[],
        keywords=[
          keyword(
            arg='row',
            value=Constant(value=75)),
          keyword(
            arg='column',
            value=Constant(value=2))])),
    Expr(
      value=Call(
        func=Attribute(
          value=Call(
            func=Name(id='Button', ctx=Load()),
            args=[
              Name(id='root', ctx=Load())],
            keywords=[
              keyword(
                arg='text',
                value=Constant(value='Remove a Folder')),
              keyword(
                arg='command',
                value=Name(id='remove_folder', ctx=Load()))]),
          attr='grid',
          ctx=Load()),
        args=[],
        keywords=[
          keyword(
            arg='row',
            value=Constant(value=65)),
          keyword(
            arg='column',
            value=Constant(value=2))])),
    Expr(
      value=Call(
        func=Attribute(
          value=Call(
            func=Name(id='Button', ctx=Load()),
            args=[
              Name(id='root', ctx=Load())],
            keywords=[
              keyword(
                arg='text',
                value=Constant(value='List all Files in Directory')),
              keyword(
                arg='command',
                value=Name(id='list_files', ctx=Load()))]),
          attr='grid',
          ctx=Load()),
        args=[],
        keywords=[
          keyword(
            arg='row',
            value=Constant(value=85)),
          keyword(
            arg='column',
            value=Constant(value=2))])),
    Expr(
      value=Call(
        func=Attribute(
          value=Name(id='root', ctx=Load()),
          attr='mainloop',
          ctx=Load()),
        args=[],
        keywords=[]))],
  type_ignores=[])