import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='skill-1400',
    version='1.0.0',
    author='Vitaliy Zarubin',
    author_email='keygenqt@gmail.com',
    description='Solving tasks from the book "1400 задач по программированию"',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://git.pinxterapp.com/android/app-colors',
    packages=setuptools.find_packages(exclude=['*tests.*', '*tests']),
    include_package_data=True,
    py_modules=['colors'],
    install_requires=[
        'click',
        'matplotlib'
    ],
    python_requires='>=3.6',
    entry_points="""
        [console_scripts]
        colors = colors.__main__:cli
    """
)
