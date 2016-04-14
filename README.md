# diviner
*noun* | di_vin_er | *a person who uses special powers to predict future events*
![water](images/water)

## Purpose
diviner is a github hosted clinical risk model library whose single purpose is
to corral as many clinical risk models as possible and experiment with the best
possible way to tag and disseminate the inherent algorithms.

## Repository Structure
To help catalog these models, each model will be stored in it's own folder where
the name of the folder is a unique DOI. If the model is not associated with a
publication, it must be linked to a DOI of some sort. We recommend following the
github guidelines for [making your code citable](https://guides.github.com/activities/citable-code/).

## Folder Structure
To try to be as flexible as possible, each folder will have as little structure
as possible. The minimal requirements are that each folder have a README.md file
and contain at least one machine-readable representation of the model. This can
range from SAS macros, to Dockerfile's that help expose the model through
RESTful APIs.
