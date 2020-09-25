1.安装打包程序
```
pip install py2app
```

2.生成setup.py文件
```
py2applet --make-setup main.py
```
如果上面执行不成功则执行下面这条语句，明明这个路径在PATH中，为何要这样执行？难道和系统的冲突？
```
/Users/fred/Library/Python/3.8/bin/py2applet --make-setup main.py
```

3.打包-A添加所有依赖 推荐
```
python3 setup.py py2app -A
```

4.!问题,应该是macos系统库冲突问题，回头用其他机器试一下的
```
fred@freddeMBP ~ % python3
Python 3.8.2 (default, Aug 25 2020, 09:23:57) 
[Clang 12.0.0 (clang-1200.0.32.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import tkinter
>>> tkinter.Tk()
DEPRECATION WARNING: The system version of Tk is deprecated and may be removed in a future release. Please don't rely on it. Set TK_SILENCE_DEPRECATION=1 to suppress this warning.
```