# Use Azure Blob Storage features to support large file uploads via file 'chunks' & containers to represent permit case files

Date: 2019-10-17

## Status

Proposed

## Context

Azure Blob Storage has been proposed as the storage mechanism for CCP case & supporting files, because of the interoperability with other Azure & Microsoft (Dynamics) services.

How the documents are uploaded & stored needs to be considered taking into account the following:

1. How will large file uploads be supported that can be restarted in the case of connection error, or resumed in the case of a user closing their browser?
2. How can the files be grouped & related to the Dynamics case (permit), in isolation within the Azure Blob Storage service?

## Decision

Azure Blob storage supports file uploads via block 'chunks' where a file is split into smaller parts that are uploaded and recommitted into the full file once all 
blocks have uploaded.  This enables the following:
* browser upload limits are avoided as the file is usually split into 4-5 MB chunks
* more efficient uploads as multiple chunks can be uploaded in parallel
* in the case of the failed or interrupted uploads, the number of successfully uploaded blocks for a file can be requested from Azure.  Using this information the application can then resume an upload by sending only the remaining blocks, before committing the entire file.

Azure Blob Storage supports grouping files together into 'containers', essentially a folder structure.  SEPA should create a container for each permit application naming it with the CLAS CAR reference number.
Azure Blob Storage also supports file metadata and this should be used to store additional user information (user id) and the CAR reference.

## Consequences

Azure Blob Storage retains 'uncomittedblocks' (or unfinished file uploads) for a week before they are removed, so there are additional management (and potentially cost) considerations involved.

Uploading via file chunks is part of the HTML5 specification and therefore is supported by modern browsers, however there may be additional work required to 'polyfill' certain browsers which do not offer full support for the File API features. 
