The purpose of the application is to function as a reference database and it should assist identifying and providing documentation of historical business cases as a basis of tendering. The application is a prototype for potential commercial product to be utilized in a organization with thousands of business engagements annually. 

The user of the application may upload commercial documents into the database. The documents may be then browsed and searched based on the provided document classification and full-text search. User may then download the most applicable commercial documents to be used as a benchmark for the new business opportunity.

There are two user groups:
- *User*: User (consultant, project manager, bid manager or alike) can 

The base functionalities

*Document upload
- User can select a document file from from harddrive and upload it to the database
- User can give limited amount of classification details pertaining to the document
- User may upload UNICODE text documents

* Document browsing, searching and download
- User may browse by classification details
- User may search by classification or the document contents
- Search results are rated by the best match
- User may download the selected document

The extensions

* Maintenance
- Super user may login and logout
- Super user may manage other superuser accounts (including his / her own)
- Super user can remove mistakenly document record
	- Document removal removes the database record and full-text search index completely

* Document upload
- System performs a scan and warns if similar document has been already uploaded
- System allows user to add (only) .ppt(x) and .pdf documents
	- System parses the text from the documents in to unicode in order to allow for Swoosh full-text search

* Document browsing
- User can apply filters on browsing and searching
- User interface allows for a preview of the full-text search result
