# Software architecture

## Layer structure

The application conforms to two-layered architectural design:

![Package diagram](./package_diagram.jpg)

Package _ui_ comprises of the graphical user interface logic. Package _document_ contains the data access objects including storage and search functions for document class. If more class objects are added (such as _user_ class which is considered an extension in application requirements) those are added as separate packages. 

Additionaly, package _config_ contains the application configuration files.


## Graphical user interface



## Software logic


## Storage and upload


### Document and indexing files



## Major features