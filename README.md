# Module Versions

## Purpose
When running versions.py in a Drupal module's root directory it will detect the current version of the module and increment it to the next version. These version are incremented using [Semantic Versioning](https://semver.org/). You ca increment either Major, Minor, or Patch versions. These version numbers will be changed/added to the info.yml file. a new git commit will be created stating the new version, a new git tag will be made and pushed to the origin server.

## Usage
To increment patch version:  
example: version 1.2.4  
    `version.py patch`  
new version will be 1.2.5.  

To increment minor version:   
example: version 1.2.4  
    `version.py minor`  
new version will be 1.3.0.   
 
To increment major version:    
example: version 1.2.4   
    `version.py major`   
new version will be 2.0.0.   


## Contributing
If you would like to contribute to this project please create a merge request.

## Project status
As I am currently developing Drupal modules I constantly am needing to create new realses, this makes it easier so I will keep worjing on it.
