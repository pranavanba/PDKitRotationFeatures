from setuptools import setup

setup(
    name='PDKitRotationFeatures',
    version='0.0.2',
    description='package wrapper for gait feature pipeline',
    author='Aryton Tediarjo and Larsson Omberg',
    author_email='aryton.tediarjo@sagebase.org',
    packages=['PDKitRotationFeatures'],
    install_requires=["numpy==1.20.0",
                      "pandas==1.0.3",
                      "scipy==1.7.3",
                      "pdkit==1.2",
                      "scikit-learn==1.0.2",
                      "tsfresh==0.19.0",
                      "future==0.18.2",
                      "matplotlib==3.5.1",
                      "pandas-validator==0.5.0"]
)
