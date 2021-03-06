from setuptools import setup, find_packages
setup(
    name = 'tidal-dl',
    version="2020.2.28.1",
    license="Apache2",
    description = "Yusuf Usta Version",

    author = 'YaronH',
    author_email = "yaronhuang@qq.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires=["aigpy>=2020.2.28.0", "requests", "ffmpeg", "pycryptodome", "pydub", ],
    entry_points={'console_scripts': [ 'tidal-dl = tidal_dl:main', ]}
)
