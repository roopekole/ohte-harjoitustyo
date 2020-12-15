# Software architecture

## Layer structure

The application conforms to two-layered architectural design:

![Package diagram](./package_diagram.jpg)

Package _ui_ comprises of the graphical user interface logic. Package _document_ contains the data access objects including storage and search functions for document class. If more class objects are added (such as _user_ class which is considered an extension in application requirements) those are added as separate packages. 

Additionaly, package _config_ contains the application configuration files.


## Software logic

The logical data structure of the software is comprised of the [Document](https://github.com/roopekole/ohte-harjoitustyo/blob/master/app/src/document/document.py) class. The Document class is intertwined with the [document functions](https://github.com/roopekole/ohte-harjoitustyo/blob/master/app/src/document/document_functions.py) module which contains the storage, indexing, querying, uploading and downloading functions for document object.

The application could be easily extended for instance with the user class (see layer structure) to allow maintenance via GUI. The user class is considered an extension to the lab project scope.

The application could also be extended to link customers and projects, which are now free text entries, as object entities to the document. However, this type of data structural logic is considered uncharacteristic for the scope and hence not implemented.


## Graphical user interface

Graphical user interface contains four different views with sub-view classes:
 * Start view - view where user lands when initiating the application
 * Search view - view which allows for full text index search of the document contents
 * Browse view - view which allows for browsing the stored documents
 * Upload view - view which allows for uploading the documents

Each view has been implemented as it's own class within the ui-module. Search and Upload view contain sub-classes which are displayed based on user's actions.

User interface has been completely isolated from the software logic and it utilizes only the essential methods in the document functions module (along with utility functions in utilities module).


## Storage, upload and download

Storage, upload and download are main features of the application. Application stores a physical document file and its metadata along with the indexed content (see Document and indexing) uploaded by the user. Any other user is later allowed to download that file on his/her harddrive.

The storage related server processes are initiated by user request. The metadata of the document is stored first to the SQLite database, subsequently the file is stored with the db id to the physical file storage, and the file contents are parsed and indexed to Whoosh index storage files.


### Document and indexing files



## Major features