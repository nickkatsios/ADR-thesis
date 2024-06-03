# 2. deployments

Date: 2020-12-07

## Status

Accepted

## Context

We need a way of deploying our services to our various hosted environments (dev, staging, prod, etc.). We would
prefer these deployments to be automated with minimal to zero human interaction.

## Decision

The DIT infrastructure already has a lot of tooling and infrastructure around deployments so we will utilise this. We 
will use Jenkins to automatically deploy from dedicated git branches - these will be:
  
  - development
  - staging
  - uat

We will have 5 Jenkins jobs in total - these will be:

  - trade-access-program-backoffice
  - trade-access-program-frontend
  - trade-access-program-polling-dev
  - trade-access-program-polling-staging
  - trade-access-program-polling-uat
  
The role of the "polling" jobs are to watch a related git branch for any commit changes. Once a change is detected then
it will trigger the `trade-access-program-backoffice` and `trade-access-program-frontend` jobs with a set of 
environment parameters triggering the deployment to one of our three environments.

This allows us to simply merge or push to one of the three dedicated git branches above and a full automated deployment
will occur for that environment. 
