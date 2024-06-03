# 4. templates-over-js-framework.md

Date: 2020-12-07

## Status

Accepted

## Context

We need to decide how we want to develop and maintain our service UI. In fact we require 3 different user interfaces 
for the TAP project:
  
  - A grant application UI for external companies and individuals to apply for a grant.
  - A grant management UI for internal TAP team members to help them organise the approval/rejection process.
  - An admin interface to manage the inner workings of the TAP service. 

As of right now the development team consists of 1 developer with experience in backend development. Therefore we will
take the simpler solutions when making decisions about UI development.

## Decision

### Grant application

The service will be available to the public via a gov.uk domain, therefore we are required to use 
[GDS](https://design-system.service.gov.uk/) styling.

Because of our development team constraints we will use standard html template views served from Django.   

### Grant management

The grant management portal will only be available to internal TAP team members and approved grant administrators 
(TCPs, ITAs). In the [grant management portal ADR](0005-viewflow-for-grant-management-portal.md) we decided to use
[Viewflow](http://viewflow.io/) to create a grant management portal. Viewflow has a 
[frontend library](http://docs.viewflow.io/viewflow_frontend.html) we can utilise to provide a frontend grant management
portal with minimal development work required from us.

Because of our development team constraints we will use this viewflow frontend library. 

### Admin

We will use the built in Django admin panel for administration of our service. 

## Consequences

As mentioned in the context above our choices of frontend UI are to try and maximise development efficiency and 
simplicity. Therefore we should be able to iterate very quickly with our frontend build. This of course brings the 
restriction of flexibility. The UIs we build will be restricted by the libraries, patterns and html components that 
they use.
    