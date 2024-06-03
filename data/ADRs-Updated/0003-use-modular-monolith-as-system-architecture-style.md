# 3. Use modular monolith as system architecture style

Date: 2020-02-05

## Status

Accepted

## Context

We need to adopt system architecture style adjecent to our architectural drivers

## Decision

We will use modular monolith architecture style

## Consequences

Will be fast to start development from scratch (no topology planning)
will be fast to proceed with development (no interfaces flooding)
Fast to deploy from code to running instance
Resilience is not needed (this is a prototype)
Scalability is not needed (single user only)
Development autonomy is not needed (single developer only)