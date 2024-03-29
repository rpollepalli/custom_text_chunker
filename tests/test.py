import pathlib

import pkg_resources

"""main function"""
if __name__ == "__main__":
    with pathlib.Path('requirements.txt').open() as requirements_txt:
        install_requires = [
            str(requirement)
            for requirement
            in pkg_resources.parse_requirements(requirements_txt)
            ]
print(install_requires)