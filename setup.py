from setuptools import setup

setup(
    name='PDKitRotationFeatures',
    version='0.0.3',
    description='package wrapper for gait feature pipeline',
    author='Aryton Tediarjo and Larsson Omberg',
    author_email='aryton.tediarjo@sagebase.org',
    packages=['PDKitRotationFeatures'],
    install_requires=["numpy",
                      "pandas",
                      "scipy",
                      "pdkit==1.2",
                      "scikit-learn",
                      "tsfresh",
                      "future",
                      "matplotlib",
                      "pandas_validator"]
)
