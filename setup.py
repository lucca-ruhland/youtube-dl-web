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
    package_data={'': ['youtube_dl_web/static/', 'youtube_dl_web/templates/']},
    install_requires=[
        'flask',
        'flask_bootstrap',
        'flask_nav',
        'flask_wtf',
        'flask_debug',
        'wtforms',
        'youtube_dl',
        'gunicorn',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'youtube-dl-web = youtube_dl_web.main:main'
        ]
    }
)
