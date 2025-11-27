from distutils.core import setup
setup(
  name = 'soteriarpc',         
  packages = ['soteriarpc'],   
  version = '0.1',      
  license='MIT',     
  description = 'Simple Soteria RPC library',
  keywords = ['SOTERIA', 'RPC'], 
  install_requires=[
          'requests'
      ],
  classifiers=[
    'Development Status :: Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
