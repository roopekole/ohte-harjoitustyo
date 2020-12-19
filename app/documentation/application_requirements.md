# General description
The purpose of the application is to function as a reference database and it should assist identifying and providing documentation of historical business cases as a basis of tendering. The application is a prototype for potential commercially utilized product to be uesd in a organization with thousands of business engagements annually. This prototype app explores mainly with the full-text indexing and the related search functions.

The user of the application may upload commercial documents into the database. The documents may be then browsed and searched based on the provided document metadata and full-text search. User may then download the most applicable commercial documents to be used as a benchmark for the new business opportunity.

# User groups

There are two user groups:
- **User**: User (consultant, project manager, bid manager or alike) can upload and download commercial documents. He / she can also search and browse the metadata database and related full-text indices
- **Super user**: Super user (administrator or alike can manage the metadata database and related full-text indices via graphical user interface
	- NOTE! Super user functions are strictly extensions that may or may not be fulfilled during the lab work period (see. below "Extensions")

# Functionalities

### The base functionalities

**Document upload**
- User can select a document file from from hard drive and upload it to the database
	- Document file is parsed and the content is indexed, the file itself is stored
- User can assing a project title to the document
- User can add a customer title to the document
- User may upload only allowed file types (currently .pdf) 
	- Application restricts wrong data types for the document files.

**Document browsing, searching and download**
- User can search the uploaded documents for the document content matches
	- Hit highlight(s) is shown to the user
- Search results are rated by the best match
	- Search score is displayed to the user, BM25F scoring algorithm used
- User may download the selected document (searched or browsed) to the selected directory

**Usability and GUI**
- Progress animation is shown to user during uploads and downloads

### The extensions

**Maintenance**
- Super user may login and logout
- Super user may manage other superuser accounts (including his / her own)
- Super user can remove mistakenly document record
	- Document removal removes the database record and full-text search index completely

**Document upload**
- User can give larger amount of classification details (i.e. metadata) pertaining to the document
	- User may browse by classification details
	- User may search by classification or the document contents
- System performs a scan and warns if similar document has been already uploaded
- System allows user to add also other relevant business document file types (such as .ppt(x), .doc(x))

**Document browsing and searching**
- User can apply filters on browsing and searching
- User interface allows for a preview of the full-text search result (naive preview with keyword hits contained as a base functionality)
- Allow user to define maximum hit number during the search
- Allow user to select search scoring method (radio buttons to select the Whoosh algorithms)


**Usability and GUI**
- Allow user to include keyword hit preview