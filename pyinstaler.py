import  os
if __name__ == '__main__':
    from PyInstaller.__main__ import run
    opts=['Rename.py','-w','-F','--icon=icon.ico']
    run(opts)