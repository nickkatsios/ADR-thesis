# 2. Use Hexagonal Architecture

Date: 2020-01-18

## Status

Accepted

## Context

The SDARS application consists of 3 independent components that can be communicated in various ways.
To enable different communication ways we need to apply a proper architectural style.

## Decision

Adopt Hexagonal Architecture for project.

## Consequences

It will be easy to communicate application components just by changing communication adapters.
