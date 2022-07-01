from setuptools import setup

#before running the code read the attached readme. and after use: "python3 builder-app-OSX-only.py" py2app

APP = ["****"] #name of main code of cat-net
OPTIONS = {
    'iconfile':'cat-net-icon.icns', #icon file. FOR ONLY MAC USE .icns FILE NOT .ico
    'argv_emulation': True,
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)
