"""
Setup script for LLM Abstraction System

© 2025-2030 All rights reserved Ashutosh Sinha
email: ajsinha@gmail.com
"""

from setuptools import setup, find_packages
import os

# Read the README file
readme_path = os.path.join('docs', 'EXAMPLE README.md')
with open(readme_path, 'r', encoding='utf-8') as f:
    long_description = f.read()

# Read requirements
with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name='llm-abstraction-system',
    version='1.0.0',
    author='Ashutosh Sinha',
    author_email='ajsinha@gmail.com',
    description='A comprehensive, configuration-driven framework for LLM interactions',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ajsinha/llm-abstraction-system',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires='>=3.8',
    install_requires=requirements,
    include_package_data=True,
    package_data={
        'llm_abstraction_system': [
            'llmconfig/*.json',
            'llmconfig/*.properties',
        ],
    },
    entry_points={
        'console_scripts': [
            'llm-system=llm_abstraction_system.examples.basic_usage:main',
        ],
    },
    keywords='llm ai machine-learning anthropic openai google llama',
    project_urls={
        'Documentation': 'https://github.com/ajsinha/llm-abstraction-system/docs',
        'Source': 'https://github.com/ajsinha/llm-abstraction-system',
    },
)
