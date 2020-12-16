import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='youtube-dl-web',
    version='0.0.1',
    author='Lucca Ruhland',
    author_email='lucca.ruhland@gmx.net',
    description='web frontend for youtube-dl',
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'youtube-dl-web = youtube_dl_web.main:main'
        ]
    }
)
