# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src/docgen/example.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['openstep_plist.util', 'openstep_plist.parser'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='DocGen',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='DocGen',
)

app = BUNDLE(
    coll,
    name='DocGen.app',
    icon=None,
    bundle_identifier=None,
    info_plist={
        'CFBundleName': 'DocGen',
        'CFBundleDisplayName': 'DocGen',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'NSHighResolutionCapable': True,
    },
)