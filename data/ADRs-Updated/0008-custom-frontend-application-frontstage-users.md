# 8. Custom frontend application for front stage users

* Status: proposed
* Deciders: 
* Date: 2019-10-03

## Context and Problem Statement

Microsoft Dynamics CRM has been proposed as the system to manage contacts, accounts & permits (cases) for the CCP prototype.  
Users should be able to recognise that the service is provided by SEPA (styling) and the interface should be sufficiently customisable
to support a good user experience.

## Decision Drivers

* Data is stored in the CRM so all interactions must be compatible with the data entities available.
* A user-centered design approach requires the technical solution to support custom journeys and styling as much as possible.

## Considered Options

1. Create a custom web application to interact with Dynamics & Azure APIs.
2. Use Microsoft's Dynamics 365 Web Portals to provide & manage the interface.

## Decision Outcome

[Option 1] A custom web application, combining a modern reactive frontend framework with a backend API gateway to interact with Dynamics and Azure services via restful webs APIs
would provide the best support for optimising the user journey.

Avoiding the use of a hosted web application (MS Portals), by decoupling the frontend, reduces the reliance on a single platform.

### Positive Consequences

* Complete control over the user interface and user journey.
* SEPA can reuse & build upon shared web patterns & components.

### Negative Consequences

* Additional overhead required for maintenance, testing and deployment.

## Pros and Cons of the Options

### 1. Create a custom web application 

A custom web frontend application pushes/pulls data either directly via the service APIs (in the case of Azure Blob Storage & authentication services) or via a server side API gateway (built as part of the application).

#### Positive
* Full control over styling, interactions and journey.
* A modular / component based frontend build can be reused across other web projects.
* Separates display logic from the data layer - all data is managed in the CRM then consumed and displayed using API endpoints.
* Custom build pipelines can be used to manage the deployment & testing directly from the code repository.
* Minimal domain specific knowledge required to configure and maintain frontend code.

#### Negative
* Built from the ground up, requiring more up front development time and resource.
* Managed, updated and deployed by SEPA.

### 2. Use Microsoft's Dynamics 365 Web Portals to provide & manage the interface.

Microsoft Dynamics 365 Web Portals provide an 'out the box' customisable web interface for their Dynamics systems.  The
styling, page elements & functionality can be customised using the open source templating library 'Liquid' which was created by Shopify.

#### Positive
* Web forms and lists can be setup for any custom workflow.
* Login and registration can be integrated with Azure Active Directory & Azure Active Directory B2C
* Multiple website can be setup, potentially allowing SEPA to handle multiple license types.
* All infrastructure and code management is handled within the Dynamics portal.

#### Negative
* Out of the box, CRM forms and portals are targeted for sales, marketing and support so additional work is required to repurpose and restyle whats available.
* Increases vendor lock in - frontend code is stored within the CRM system.
* Without in-depth experience of this solution, it is not initially clear how much Web portals can support a custom journey, and if so, how difficult it would be to build (what level of custom coding would be required?).
* Potentially requires more domain specific knowledge & resources in terms of Dynamics, Portals & Liquid, to customise and maintain this solution.

## Links 
[Deliver web engagement experiences with Dynamics 365 Portals](https://docs.microsoft.com/en-us/dynamics365/portals/administer-manage-portal-dynamics-365)
