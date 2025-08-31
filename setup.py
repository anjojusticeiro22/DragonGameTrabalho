from cx_Freeze import setup, Executable

executables = [
    Executable(
        'main.py',
        base=None,
        icon='./asset/Icon.ico'
    )
]
setup(
    name='Dragon Adventure',
    version='1.1',
    description='Dragon Adventure Game',
    options={'build_exe': {'packages': ['pygame']}},
    executables=executables
)