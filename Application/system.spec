# -*- mode: python ; coding: utf-8 -*-
block_cipher = None


a = Analysis(['real_login.py'],
             pathex=['C:\\Users\\SAMSUNG\\Desktop\\program'],
             binaries=[],
             datas=[('.\\geckodriver.exe','.'),
		('.\\관리.jpg','.'),
		('.\\보보험사.jpg','.'),
		('.\\pcx.jpg','.'),
		('.\\사고고.png','.'),
		('.\\로고.png','.'),
		('.\\iccon.ico','.'),
		('.\\한강바이크 사고처리 내역서.xlsx','.')],
             hiddenimports=[],
             hookspath='C:\\Anaconda3\\envs\\bikebank\\Lib\\site-packages\\PyInstaller\\hooks',
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='a_real_login',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False, icon= '.\\iccon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='a_real_login')
