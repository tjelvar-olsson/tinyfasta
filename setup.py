from setuptools import setup
import tinyfasta

# Importing the "multiprocessing" module is required for the "nose.collector".
# See also: http://bugs.python.org/issue15881#msg170215
try:
    import multiprocessing
except ImportError:
    pass

# Define the test runner.
# See also:
# http://fgimian.github.io/blog/2014/04/27/running-nose-tests-with-plugins-using-the-python-setuptools-test-command/
from setuptools.command.test import test as TestCommand
class NoseTestCommand(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        # Run nose ensuring that argv simulates running nosetests directly.
        import nose
        nose.run_exit(argv=['nosetests'])


readme = open('README.rst').read()

setup(name="tinyfasta",
      packages=["tinyfasta"],
      version=tinyfasta.__version__,
      description="Tiny FASTA package, without dependencies, for processing biological sequence files.",
      long_description=readme,
      author="Tjelvar Olsson",
      author_email="tjelvar.olsson@gmail.com",
      url="https://github.com/tjelvar-olsson/tinyfasta",
      download_url="https://github.com/tjelvar-olsson/tinyfasta/{}".format(tinyfasta.__version__),
      license='MIT',
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
      ],
      keywords=["fasta", "bioinformatics"],
      cmdclass={"test": NoseTestCommand},
      tests_require=["nose", "coverage"],
)
