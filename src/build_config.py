import sys
import os

def get_build_config():
    return {
        'name': 'Desktop Assistant',
        'version': '1.0.0',
        'description': 'A desktop assistant application',
        'author': 'Your Name',
        'icon_path': os.path.join('src', 'resources', 'app.ico'),
        'main_script': os.path.join('src', 'main.py'),
        'hidden_imports': [
            'tkinter',
            'requests',
            'bs4',
            'logging',
        ],
        'additional_files': [
            ('src/resources/*', 'resources'),
            ('config.json', '.')
        ]
    } 