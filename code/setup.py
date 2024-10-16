import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='groove2groove',
    version='0.0.1',
    author='Ondřej Cífka',
    description='Music style transfer and style translation models',
    long_description=long_description,
    long_description_content_type='text/markdown',  # If your README is in Markdown
    url='https://github.com/cifkao/groove2groove',
    python_requires='>=3.6',
    install_requires=[
        'scipy>=1.2.0'
    ],
    extras_require={
        'gpu': ['museflow[gpu] @ git+https://github.com/cifkao/museflow'],
        'nogpu': ['museflow[nogpu] @ git+https://github.com/cifkao/museflow'],
    },
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
