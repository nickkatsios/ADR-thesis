# 2.  Record architecture decisions

Date: 2020-05-16

## Status

Accepted

## Context

To quickly check database connection and created objects as a result of Northwind database reverse engineering.

## Decision

Simple call from handler to DbContext is used without any middle layer.

## Consequences

Project not use best practices in software development like usage of ViewModels. This directs to lack of separation between Domain and application logic.