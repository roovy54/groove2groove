import setuptools

setuptools.setup(
    name='groove2groove',
    version='0.0.1',  # Add a version for clarity
    author='Ondřej Cífka',
    description='Music style transfer and style translation models',
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
        'License :: OSI Approved :: MIT License',  # Add license info if available
        'Operating System :: OS Independent',
    ],
)
