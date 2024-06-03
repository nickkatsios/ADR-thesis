# 2.  Use Modular Monolith System Architecture

Date: 2020-06-17

## Status

Accepted

## Context

This application will have severals functionnalities on severals domains. They must be independent to increase maintainability.

## Possible solutions

1. Microservices: domains are developed in differents application who communicates together.
2. Modular monolith: each independent domain run in the same application but the architecture containerize them.

## Decision

I decided to choose the modular monolith for some reasons:
- The time to develop is shorter than microservices
- It can evolve to microservices in the future
- The [Modular monolith DDD](https://github.com/kgrzybek/modular-monolith-with-ddd) project is a great inspiration for this approach

## Consequences

- All modules must run in one single process as single application (Monolith)
- All modules should have maximum autonomy (Modular)
- DDD Bounded Contexts will be used to divide monolith into modules
- DDD tactical patterns will be used to implement most of modules