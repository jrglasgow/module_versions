# Module versions
## Purpose
For custom Drupal modules and themes it is important to have versions for Composer to easily manage your code. Usually it is sufficient to have a Git (or other VCS) tag for composer to manage, unfortunately when that is the case you cannot easily tell by looking at your Modules ("Extend") page in the website which version you are running as the version number is not in your info.yml file.
This python script will do the following
- Read the module's info.yml file to get the version number
- Increment the patch version (minor and major version updated are also supported).
- Save the file
- update all info.ylm files in a repository (is there are multiple modules in the same repo)
- commit the change in the info.yml file
- tag the repostory with that version
- performa ```git push --tags``` to push all tags to the origin remote
- perform a ```git push origin``` to get all commits in the current branch on the origin remote.

## Installation

- clone the repository
- Change to the repository directory ```cd module_versions```
- ensure pip is installed; e.g. `sudo apt-get install python3-pip`
- [activate the virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#activate-a-virtual-environment) - `source bin/activate`
- install dependencies ```python -m pip install -r requirements.txt```

## Usage
Update the patch version, i.e. from 1.2.12 t 1.2.13 

```version.py patch```

Update the minor version, i.e. from 1.2.13 to 1.3.0

```version.py minor```

Update the major version, i.e. from 1.3.0 to 2.0.0

```update major```


## Contributing
If you would like to contribute to this project please create a merge request.

## Project status
As I am currently developing Drupal modules I constantly am needing to create new realses, this makes it easier so I will keep worjing on it.
