import os
import sys
import shutil
from src.build_config import get_build_config

def create_spec_file():
    config = get_build_config()
    
    spec_content = f"""# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['{config["main_script"]}'],
    pathex=[],
    binaries=[],
    datas={config["additional_files"]},
    hiddenimports={config["hidden_imports"]},
    hookspath=[],
    hooksconfig={{}},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='{config["name"]}',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['{config["icon_path"]}'],
)
"""
    
    with open('desktop_assistant.spec', 'w') as f:
        f.write(spec_content)

def build():
    # 确保资源目录存在
    os.makedirs('src/resources', exist_ok=True)
    
    # 检查图标文件是否存在
    config = get_build_config()
    if not os.path.exists(config['icon_path']):
        print(f"Warning: Icon file not found at {config['icon_path']}")
        print("Using default icon...")
        # 可以在这里添加代码来生成或下载默认图标
    
    # 创建spec文件
    create_spec_file()
    
    # 运行PyInstaller
    os.system('pyinstaller desktop_assistant.spec --clean')

if __name__ == '__main__':
    build() 