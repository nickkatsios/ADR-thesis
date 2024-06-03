# 6. Relate applicant and SEPA documents to the permit (CRM case entities)

* Status: proposed
* Deciders: 
* Date: 2019-10-03

## Context and Problem Statement

Document uploads will be stored in Azure Blob storage because of the requirement to store very large files & the fact that Azure Blob storage offers high availability and low costs.

The Azure Blob storage system is a separate cloud service which is not directly linked to Dynamics CRM, therefore we need to consider how the permits, stored using CRM case/incident entities, will be linked to the the files within Azure.

## Decision Drivers

* Files will be displayed to users via a web frontend, therefore the entity used to store the file reference attribute should be accessible and filterable via the WebAPI.
* The existing Dynamics UI should be able to display links to the Azure files for administrators.

## Considered Options

1. Use the existing CRM 'annotation' entity
2. Create a new custom CRM entity 

## Decision Outcome

[Option 1] Use the existing 'annotation' entity in the CRM & set the entity attributes to match Azure blob data.

### Positive Consequences

* Minimises customisation of the CRM data, reuse of existing

### Negative Consequences

* Labelling within the CRM does not match the context of the upload.

## Pros and Cons of the Options

### 1. Use the existing CRM 'annotation' entity

Once a file is uploaded via the application, a WebAPI call is made to create a new 'annotation' entity in Dynamics, the Azure Blob data is stored on the entity using the following (suggested) attributes:
* [tbd] documentbody / filename / subject - Azure Blob storage URI
* notetext - description of the upload time & file metadata
* isdocument - true
* objecttypecode - 'azureBlobStorageFile'

#### Positive
* Minimises customisation of the CRM
* Reuse of existing entity which is used to store uploads on cases.

#### Negative
* Labelling within the CRM UI will not be relevant.

### 2. Create a new custom CRM entity 

Create a new custom 'azureBlobStorage' entity within the CRM, create a new instance via the WebAPI once the file upload is completed.

#### Positive
* The Dynamics UI and WebAPI entity are more closely related to the use case.

#### Negative
* Customisation of the CRM could result in more difficult migration paths and bigger overheads in terms of management.
* Custom workflow & UI work may be required to display the custom entity within Dynamics UI.

## Links 

* [Alternatives of Document storage in Dynamics CRM](https://community.dynamics.com/crm/b/dynamicscrmbestpractices/posts/alternatives-of-document-storage-in-dynamics-crm)
* [Create an entity in Dynamics](https://docs.microsoft.com/en-us/dynamics365/customerengagement/on-premises/customize/create-entities)
