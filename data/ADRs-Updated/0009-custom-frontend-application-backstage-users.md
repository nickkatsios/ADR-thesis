# 9. Custom frontend application for back stage users

* Status: proposed
* Deciders: 
* Date: 2019-10-03

## Context and Problem Statement

Microsoft Dynamics CRM has been proposed as the system to manage contacts, accounts & permits (cases) for the CCP prototype.  
The interface used by back stage users (SEPA modellers, registry, officers, regulators) to process tasks and actions against permits should be sufficiently customisable to support a good user experience.

## Decision Drivers

* Data is stored in the CRM so all interactions must be compatible with the data entities available.
* A user-centered design approach requires the technical solution to support custom journeys and styling as much as possible.
* A custom frontend application has also been proposed for the front stage users (applicants).

## Considered Options

1. Create a custom web application to interact with Dynamics & Azure APIs.
2. Use Microsoft's Dynamics 365 Web Portals to provide & manage the interface.
3. Use Microsoft's Dynamics existing UI and add custom workflows, apps and UI components to support the permit workflow.

## Decision Outcome

[Option 1] Reusing the application's components and functionality built for the front stage users would provide both a unified best practice user experience, and a decoupled frontend application that minimises the reliance upon and customisations required to the Dynamics CRM. 

### Positive Consequences

* SEPA creates & relies upon a reusable set of back stage components that can be used by other project's requiring a web interface.
* Least reliance / lock in to CRM vendor, both in terms of customisations but also in terms of the domain specific resources required.
* Best support for evolutionary design & architecture - changing the standalone frontend application would be less costly compared to changing the CRM interface.  Facilitates hypothesis driven development.

### Negative Consequences

* The Dynamics UI would retain it's default labelling, which could sit out of the context of 'permitting'.
* Additional resources required to maintain the standalone frontend application.
* A custom backstage needs to be considered in the wider SEPA architectural context.

## Pros and Cons of the Options

### 1. Create a custom web application 

A custom web frontend application pushes/pulls data either directly via the service APIs in the case where the user pushes files to Azure Blob Storage, or via a server side API gateway (built as part of the application) which utilises the Dynamics & Azure blob storage and Active Directory APIs.

#### Positive
* Full control over styling, interactions and journey.
* A modular / component based frontend build can be reused across other web projects.
* Separates display logic from the data layer - all data is managed in the CRM then consumed and displayed using API endpoints.
* Custom build pipelines can be used to manage the deployment & testing directly from the code repository.
* Minimises the customisation of Dynamics, reduces vendor lock in.
* Minimal domain specific knowledge required to configure and maintain frontend code.
* Reuses the front stage components to build the majority of the application, most back stage specific logic is related to workflow.
* Consistent best practice (reuse of gov.uk patterns) user experience for front and back stage users.
* When taking into account the front stage interface, this would seem to require the least amount of up front work.

#### Negative
* Built from the ground up, requiring more up front development time and resource.
* Additional time & effort require to manage, update and deploy as the codebase is managed by SEPA.  
* If Dynamics is not customised / configured to match the SEPA processes, the Dynamics UI would show labels / context that do not match the web interface.

### 2. Use Microsoft's Dynamics 365 Web Portals to provide & manage the interface.

Microsoft Dynamics 365 Web Portals provide an 'out the box' customisable web interface for their Dynamics systems.  The
styling, page elements & functionality can be customised using the open source templating library 'Liquid' which was created by Shopify.

#### Positive
* Web forms and lists can be setup for any custom workflow.
* Login and registration can be integrated with Azure Active Directory & Azure Active Directory B2C
* Multiple website can be setup, potentially allowing SEPA to handle multiple license types.
* All infrastructure and code management is handled within the Dynamics portal.

#### Negative
* Out of the box, CRM forms are targeted for sales, marketing and support so additional work is required to repurpose and restyle whats available.
* Increases vendor lock in - frontend code is stored within the CRM system.
* Without in-depth experience of this solution, it is not initially clear how much Web portals can support a custom journey, and if so, how difficult it would be to build (what level of custom coding would be required?).
* Potentially requires more domain specific knowledge & resources in terms of Dynamics, Portals & Liquid templating language, to customise and maintain this solution.

### 3. Use Microsoft's Dynamics existing UI and add custom workflows, apps and UI components to support the permit workflow.

Microsoft Dynamics 365 would be configured & customised to provide custom workflows and custom UI elements using the Unified Interface.

#### Positive
* Dynamics UI reflects the processes of the CCP permit application.
* Reuse of existing Azure AD logins, no additional auth components required.
* All infrastructure and code management is handled within Dynamics.
* Depending on SEPA's level of Microsoft 365 product integration, the Dynamics UI could support a consistent 'Microsoft' admin experience (and depending on who speak to, that could be considered a positive or a negative).

#### Negative
* Out of the box, CRM forms are targeted for sales, marketing and support so additional work is required to relabel the CRM for a unified context.
* Depending on the level of customisations implemented inside the Dynamics UI, additional staff training would be required to use the existing interface.
* Increases vendor lock in - all any customisations to CRM would likely require substantial work to port to / replication on a new system.
* Without in-depth experience of this solution, it is not initially clear how much the Dynamics UI can support a custom journey, and if so, how difficult it would be to build (what level of custom coding would be required?).

## Links 
* [Deliver web engagement experiences with Dynamics 365 Portals](https://docs.microsoft.com/en-us/dynamics365/portals/administer-manage-portal-dynamics-365)
* [About Unified Interface for model-driven apps in PowerApps](https://docs.microsoft.com/en-us/power-platform/admin/about-unified-interface)
