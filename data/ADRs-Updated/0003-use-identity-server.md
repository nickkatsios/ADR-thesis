# 2.  Use IdentityServer 4

Date: 2020-06-24

## Status

Accepted

## Context

This application need a user authentication and a fine granularity for roles.

## Decision

I decided to choose IdentityServer 4 because it is a mature, use by many people and well documented project.
It implement OpenID connect and support external authentication (Google, Facebook, ...)

## Consequences

- IdentityServer 4 will be setup
- IdentityServer 4 will store roles for users
- API and Front will use theses roles to authorize functionnalities