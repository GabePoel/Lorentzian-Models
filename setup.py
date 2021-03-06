import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()
    
setuptools.setup(
    name = 'lorentzian_models',
    version = '0.1',
    author = 'Gabriel Perko-Engel',
    author_email = 'gpe@berkeley.edu',
    description = 'For finding and processing Lorentzian line shapes. Backend'
    ' for `peak_finder`.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    license = 'MIT',
    url = 'https://github.com/GabePoel/Lorentzian-Models',
    packages = setuptools.find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Physics'
    ],
    python_requires = '>=3/6',
    install_requires = ['tensorflow', 'peak_finder'],
    # package_data = {
    #     # Include anything found in the "trained_models" subdirectory
    #     'peak_finder': [
    #         '*',
    #         '*/*',
    #         '*/*/*',
    #         '*/*/*/*'
    #         # 'simple_class/*', 
    #         # 'simple_class_backup/*', 
    #         # 'simple_count/*', 
    #         # 'simple_count_backup/*'
    #         # 'tight_wiggle/*',
    #         # 'tight_wiggle_backup/*',
    #         # 'wide_wiggle/*',
    #         # 'wide_wiggle_backup/*'
    #         ]
    # }
)
