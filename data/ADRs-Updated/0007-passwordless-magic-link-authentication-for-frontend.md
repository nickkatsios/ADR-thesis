# 8. passwordless-magic-link-authentication-for-frontend

Date: 2020-12-08

## Status

Accepted

## Context

We need a authentication system for the frontend service. 

The authentication method must be publicly accessed.  

## Decision

A few authentication options were suggested and discussed:
  - username/password
  - social authentication (facebook, twitter, etc.)
  - passwordless email link authentication (also known as magic link)

It was decided that we would use passwordless email link authentication to authenticate our public users (grant 
applicants). 

The user will enter their email address into a login page served by the frontend service. The service will then
send a authentication link containing a one time use token in the url. The user can then visit this url to start or 
continue their application.

Constraints
  - The token will be limited to one time use.
  - The token will have a datetime expiry assigned to it.
  - On issuing a new token to a user all previous tokens will be invalidated.

## Consequences

Users will not need to remember a password.

Users will be able to save and continue incomplete grant applications.
