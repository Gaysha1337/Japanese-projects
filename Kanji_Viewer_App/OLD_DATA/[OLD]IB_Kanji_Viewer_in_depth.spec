# -*- mode: python ; coding: utf-8 -*-
import sys, os
from kivy_deps import sdl2, glew

# Hooks
from kivymd import hooks_path as kivymd_hooks_path
from kivy.tools.packaging import pyinstaller_hooks as hooks

# Get all kivy hidden dependencies 
block_cipher = None
kivy_deps_all = hooks.get_deps_all()
kivy_factory_modules = hooks.get_factory_modules()

# list of modules to exclude from analysis
excludes_a = ['Tkinter', '_tkinter', 'twisted', 'docutils', 'pygments','enchant']

# list of hiddenimports
hiddenimports = kivy_deps_all['hiddenimports'] + kivy_factory_modules


a = Analysis(['C:\\Users\\dimit\\Desktop\\Cloned_Repos\\Japanese-projects\\Kanji_Viewer_App\\main.py'],
             pathex=['C:\\Users\\dimit\\Desktop\\Cloned_Repos\\Japanese-projects\\Kanji_Viewer_App'],
             binaries=[],
             datas=[],
             hiddenimports=hiddenimports,
             hookspath=[kivymd_hooks_path],
             runtime_hooks=[],
             excludes=excludes_a,
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz, Tree(".", excludes=["*.txt"]),
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
          name='IB_Kanji_Viewer',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='C:\\Users\\dimit\\Desktop\\Cloned_Repos\\Japanese-projects\\Kanji_Viewer_App\\web_hi_res_512.ico')
