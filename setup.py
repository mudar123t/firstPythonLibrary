from setuptools import setup, find_packages

setup(
    name='dataMnp',
    version='0.1.0',
    description='A comprehensive library for data preprocessing tasks',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Mudar Shawakh',
    author_email='shawakhmudar@gmail.com',
    url='https://github.com/mudar123t/DataAnalyse',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'pandas',
        'scikit-learn',
        'nltk',
    ],
    include_package_data=True,
    license='MIT'
)

