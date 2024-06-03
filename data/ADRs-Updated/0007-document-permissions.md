# 7. Provide access to permit case file documents (Azure Blob storage) via Active Directory groups & Shared Access Signature tokens

* Status: proposed
* Deciders: 
* Date: 2019-10-03

## Context and Problem Statement

Azure Blob Storage will be used to store all files associated with permit application.  Both front stage and back stage users need to be able to read and upload documents to a 'case file'.

## Decision Drivers

* Back stage users should be able to see all files relating to a permit
* Front stage users should only be able to view and download files that are relevant to them.
* Sensitive data privacy / security requirements mean access to certain documents should be restricted for both front stage and back stage users.

## Considered Options

1. Use active directory groups to manage all access to Azure Blob Storage containers
2. Use active directory groups to manage access to Azure Blob Storage containers for back stage users, create Shared Access Signature tokens for front stage users to provide temporary access, and also leverage SAS tokens for special sensitive document access

## Decision Outcome

[Option 2] Using a combination of Active Directory groups and SAS tokens provides the greatest flexibility to manage document access. 

### Positive Consequences

* Front stage users are only able to access documents that are relevant to them, this would be managed by the frontend application & the document type attribute stored in the CRM / document metadata.
* Using SAS tokens for sensitive documents also simplifies the private access.

### Negative Consequences

* SAS tokens would potentially need be generated for each file download.

## Pros and Cons of the Options

### 1. Use active directory groups to manage all access to Azure Blob Storage containers

Active Directory groups can be assigned security roles on each container in Azure Blob Storage, therefore inheriting access from the Active Directory login.

#### Positive
* No need to grant any additional access permissions on files.
* Active Directory groups are already proposed for separating user and admin roles for both front and back stage.

#### Negative
* Multiple permit 'containers' would potentially be required to separate front stage files, back stage only files and any sensitive files. 

### 2. Use active directory groups to manage access to Azure Blob Storage containers for back stage users, create Shared Access Signature tokens for front stage users to provide temporary access, and also leverage SAS tokens for special sensitive document access

Access to all non sensitive documents for back stage users is managed via Active Directory groups & roles.  When front stage users try to download any files within the container, the application will generate a temporary SAS token that allows the user to access the file.  A similar process can also be used to grant temporary access to specific 'sensitive' files for back stage users when required.

#### Positive
* When combined with Dynamics / metadata file type look up by the application, this solution provides the most flexibility for file access.
* Maintains private managed access to all files.
* Temporary / managed access to sensitive data is more easily managed.

#### Negative
* Temporary access may require additional management from SEPA.

## Links

* [Authorize access to Azure blobs and queues using Azure Active Directory](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad)
* [Grant limited access to Azure Storage resources using shared access signatures (SAS)](https://docs.microsoft.com/en-us/azure/storage/common/storage-sas-overview)
