# General description
The purpose of the application is to function as a reference database and it should assist identifying and providing documentation of historical business cases as a basis of tendering. The application is a prototype for potential commercial product to be utilized in a organization with thousands of business engagements annually. 

The user of the application may upload commercial documents into the database. The documents may be then browsed and searched based on the provided document classification and full-text search. User may then download the most applicable commercial documents to be used as a benchmark for the new business opportunity.

# User groups

There are two user groups:
- **User**: User (consultant, project manager, bid manager or alike) can upload and download commercial documents. He / she can also search and browse the classification database and related full-text indices
- **Super user**: Super user (administrator or alike can manage the classification database and related full-text indices via graphical user interface
	- NOTE! Super user functions are strictly extensions that may or may not be fulfilled during the lab work period (see. below "Extensions")

# Functionalities

### The base functionalities

**Document upload**
- User can select a document file from from hard drive and upload it to the database (done as of 22.11.2020)
- User can assing a project title to the document (done as of 28.11.2020)
- User can add a customer title to the document (done as of 5.12.2020)
- ~~User may upload UNICODE text documents (done as of 22.11.2020, however not checked yet)~~
	- Above requirement has become redundant after adding the extension feature which parses the text content from PDF files

**Document browsing, searching and download**
- User can search the by the document content matches(Done as of 22.11.2020)
	- Hit highlight(s) is shown to the user (done as of 28.11.2020)
- Search results are rated by the best match (done as of 28.11.2020)
	- Search score is displayed to the user, BM25F scoring algorithm used (done as of 5.12.2020)
- User may download the selected document (searched or browsed) to the selected directory (done as of 28.11.2020)

### The extensions

**Maintenance**
- Super user may login and logout
- Super user may manage other superuser accounts (including his / her own)
- Super user can remove mistakenly document record
	- Document removal removes the database record and full-text search index completely

**Document upload**
- User can give limited amount of classification details pertaining to the document
	- User may browse by classification details
	- User may search by classification or the document contents
- System performs a scan and warns if similar document has been already uploaded
(A very, very naive if-else validation done today)
- System allows user to add (only) .ppt(x) and .pdf documents
	- System parses the text from the documents in to unicode in order to allow for Whoosh full-text search (PDF parse added as of 5.12.2020, note PDF parsing can only deal with UTF-8 encoding at the moment)

**Document browsing and searching**
- User can apply filters on browsing and searching
- User interface allows for a preview of the full-text search result (naive preview with keyword hits added as of 28.11.2020)
- Allow user to define maximum hit number during the search
- Allow user to select search scoring method (radio buttons to select the Whoosh algorithms)


**Usability and GUI**
- Progress animation is shown to user during uploads and downloads (done as of 5.12.2020)
- Allow user to include keyword hit preview