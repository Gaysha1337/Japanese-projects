# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2, glew
from kivymd import hooks_path as kivymd_hooks_path

block_cipher = None

added_files = [
    ("DATA","DATA"),
    ("C:\\Users\\dimit\\Desktop\\Cloned_Repos\\Japanese-projects\\Kanji_Viewer_App\\web_hi_res_512.ico","."),
    ("C:\\Users\\dimit\\Desktop\\Cloned_Repos\\Japanese-projects\\Kanji_Viewer_App\\web_hi_res_512.png",".")
    ]

a = Analysis(['C:\\Users\\dimit\\Desktop\\Cloned_Repos\\Japanese-projects\\Kanji_Viewer_App\\main.py'],
             pathex=['C:\\Users\\dimit\\Desktop\\Cloned_Repos\\Japanese-projects\\Kanji_Viewer_App'],
             binaries=[],
             datas=added_files,
             hiddenimports=['win32file','win32timezone'],
             hookspath=[kivymd_hooks_path],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          Tree('C:\\Users\\dimit\\Desktop\\Cloned_Repos\\Japanese-projects\\Kanji_Viewer_App'),
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
          name='IB Kanji Viewer',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , 
          icon='C:\\Users\\dimit\\Desktop\\Cloned_Repos\\Japanese-projects\\Kanji_Viewer_App\\web_hi_res_512.ico')
