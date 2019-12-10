import shutil
import subprocess
from distutils.command.clean import clean
from glob import glob
from os import path, walk, remove

from typing import List

from setuptools import setup, Command
from setuptools.config import read_configuration

import pkgutil


def get_files(directory: str, recursive: bool = False) -> List[str]:
    return [item for item in glob(path.join(directory, '*'), recursive=recursive) if path.isfile(item)]


class ExtendedClean(clean):
    """
    This class extend clean command in order to remove all __pycache__ directories.
    Indeed these directories contains pre-computed file with module path write in
    unix or windows style. Depends of latest os which build the file.
    In multi-OS environment this could lead to strange behavior.
    """

    @staticmethod
    def _find_all_directories(dir_name: str, path_to_scan: str) -> List[str]:
        result = []
        for root, dirs, files in walk(path_to_scan):
            if dir_name in dirs:
                result.append(path.join(root, dir_name))
        return result

    def run(self) -> None:
        clean.run(self)
        c = clean(self.distribution)
        c.finalize_options()
        c.run()
        # sources directories
        for directory in self.distribution.package_dir.values():
            for file_path in self._find_all_directories('__pycache__', directory):
                shutil.rmtree(file_path)
            for file_path in self._find_all_directories(self.distribution.metadata.name+'.egg-info', directory):
                shutil.rmtree(file_path)
        # tests directory
        if path.exists('tests'):
            for file_path in self._find_all_directories('__pycache__', 'tests'):
                shutil.rmtree(file_path)
        if path.exists('.coverage'):
            remove('.coverage')
        if path.exists('htmlcov'):
            shutil.rmtree('htmlcov')
        if path.exists('.eggs'):
            shutil.rmtree('.eggs')
        if path.exists('.pytest_cache'):
            shutil.rmtree('.pytest_cache')


if __name__ == '__main__':
    conf = read_configuration('setup.cfg')
    setup(
        name=conf['metadata']['name'],
        version=conf['metadata']['version'],
        description=conf['metadata']['description'],
        author=conf['metadata']['author'],
        license=conf['metadata']['license'],
        classifiers=conf['metadata']['classifiers'],
        keywords=conf['metadata']['keywords'],
        cmdclass={'clean': ExtendedClean},
        packages=['proba'],
        package_dir={'': 'src'},
        include_package_data=True,
        data_files=[
            (
                'etc/{}/'.format(conf['metadata']['name']),
                get_files('resources/etc/{}'.format(conf['metadata']['name']))
            ),
            (
                'etc/{}/schema/'.format(conf['metadata']['name']),
                get_files('resources/etc/{}'.format(conf['metadata']['name']+'/schema/'))
            )
        ],
        install_requires=[],
        setup_requires=['wheel >= 0.33.4',
                        'setuptools >= 36.2.1'],
        tests_require=[],
        entry_points={
            'console_scripts': [
                'proba = proba.__main__:main'
            ]
            #nom de l'executable
        },
        zip_safe=True
    )
