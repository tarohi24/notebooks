Packages
=====

References
- [Post by Jonas recommends](https://medium.com/better-programming/understanding-best-practice-python-tooling-by-comparing-popular-project-templates-6eba49229106)

## Package manager

Pipenv

### Poetry
Poetry is a young project to manage dependencies of a Python package.
Dependencies are listed in pyproject.yaml, whose format is specified in [PEP518](https://www.python.org/dev/peps/pep-0518/).

### Dependabot
Dependabot automatically detects out-of-date packages and opens pull-requests.


## Templates
- https://github.com/jacebrowning/template-python (Jonas recommends)
- https://github.com/sourcery-ai/python-best-practices-cookiecutter
- https://github.com/MartinHeinz/python-project-blueprint
  - `setup.py` is brilliant
- cookiecutter
- 
 

## Development

### Test modules
The vast majority of Python templates rely on **pytest**.  It's so familiar with tox.
coverage.py is a tool to measure code coverage.

### Lint
- flake8
- Pylint is a little slow, but good at linting.
- [wemake-python-styleguide](https://github.com/wemake-services/wemake-python-styleguide)
- Black is a code formatter.


### Documentation
- Sphinx is the most major documentation tool.
- MKDocs is the second.
