# 6. split-service-into-two

Date: 2020-12-07

## Status

Accepted

## Context

The TAP service comprises of 2 distinct responsibilities:

  - Provide a public facing grant application form styled using the GOVUK GDS style guide.
  - Provide a private portal to manage grant applications in a formal recorded manner.

The private grant management area will need to be secured behind the DIT VPN while the public facing grant application 
process will not.

Both areas will require an authentication system but they will not necessarily be required to use the same 
authentication system.

These two areas should not share the same user accounts or user types.

A person could feasibly have the need to access both areas for different purposes but this should be done using two 
unconnected user accounts. 

Grant application data will need to be shared between these two areas.

## Decision

We have decided to separate these two systems into services.

These services will be split out in the codebase as separate projects. However, we will leave these within the same git
repository for a few reasons:
  - Having these services share a single git repo will remove any need for versioning between the two services. Thus 
    saving valuable development effort.
  - The development environment will be much easier to spin up locally because all services can be managed within a 
    single docker-compose.yml file
  - We do not foresee that the codebase for these services will become very large.
  
We will name these services `frontend` and `backoffice`.

Due to developer constraints within the team (we are a small team with 1 backend developer) we will use the Django
framework to create both services.

These services will communicate via json REST requests only. They will each have their own database and will not have 
read or write access to the other's database.  

## Consequences

This will require more work on the infrastructure side of the project. However, the DIT ecosystem is already made up of 
many small services running through PAAS so the ground work around tooling is already available for us to utilise, 
mitigating any additional work this decision will create.      

Development and testing will require more effort when building features which require changes to both services. 

The separation of data and users will help to manage the data access requirement that a user only has access to what 
they need and nothing more.
