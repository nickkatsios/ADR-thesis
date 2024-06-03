# 3.  ARM templates

Date: 2020-08-18

## Status

Accepted

## Context

Application will be hosted in Azure & validated after each pull request to master/main branch.

## Decision

ARM template will be created to quickly create test environment to execute all unit tests.

## Consequences

Some consumption on Azure subscription will occur & some process to remove everything from subscription will be required.