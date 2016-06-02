# dori
DOI tagged repository of Clinical Risk Models
![water](images/dori_tail.jpeg)

## Table of Contents
* [Purpose](#purpose)
* [Contribute](#contribute)

## [Purpose](*purpose)
dori is a github hosted clinical risk model library whose single purpose is
to corral as many clinical risk models as possible and experiment with the best
possible way to tag and disseminate the algorithms. The intention is that other
applications can use DORI as a data source to help disseminate research.

## [Contribute](*contribute)
To help catalog these models, each model will be...
  1. Stored in it's own folder where the name of the folder is a unique DOI. If the model is not associated with a publication, it must be linke to a DOI of some sort. We recommend following the github guidelines for [making your code citable](https://guides.github.com/activities/citable-code/).
  2. Within each DOI labeled folder, please use the following conventions:
    - README.md file to explain the model to humans (optional)
    - config.json file that captures all of a models metadata (in accordance with TRIPOD) (required)
    - model/algorithm in machine readable format referenced in the config.json file
    - example script to read in the machine readable file and produce a few predictions 

## Folder Structure
Trying to be as flexible as possible, each folder will have as little structure
as possible. The minimal requirements are that each folder have a README.md file
and contain at least one machine-readable representation of the model. This can
range from SAS macros, to R object stores, to python machine learning pipelines.

## Disclaimer
**USE AT YOUR OWN RISK**. This repository is provided as an academic exercise
in the best possible way to store and disseminate risk algorithms. It is possible
that some algorithms are not implemented 100% accurately. Therefore, please use
at your own risk.
