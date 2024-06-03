# 5. viewflow-for-grant-management-portal

Date: 2020-12-07

## Status

Accepted

## Context

We need a system to manage the lifecycle of a grant application.

## Decision

Viewflow was chosen as a framework to help us achieve this goal while making the development process efficient. 

### Build vs Buy Paper
Various alternatives to Viewflow were considered when making this decision. Those alternatives are details in the 
alpha stage of the project here: https://uktrade.atlassian.net/l/c/zEAEM37j

### Viewflow analysis
Some initial analysis on how viewflow could be used was also done in alpha: https://uktrade.atlassian.net/l/c/Lc77C4mq

## Consequences

Viewflow provides many aspects which make the development process efficient. These include:

  - A frontend UI which requires minimal changes to cater for our basic needs
  - A state machine to manage the lifecycle of tasks associated with each grant application process.
  - Task permissions can be organised as required.
  - AA compliance
