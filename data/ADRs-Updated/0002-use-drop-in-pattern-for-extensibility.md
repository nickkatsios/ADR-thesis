# 2. use drop in pattern for extensibility

Date: 2020-12-05

## Status

Accepted

## Context

Facilitate organizing shell customizations into smaller, more readable, more understandable, more maintainable blocks and to provide a clear and common patter for extensibility.

## Decision

Create a $ZDOTDEEDIR directory where extension files can be stored. Add a rooutine to .zprofile or .zshrc which sources all files found in this directory in lexagraphical order by file name.

## Consequences

This will ensure that zprofile/zshrc file remains small, and unlike zsh plugins keeps the custom code local for readily available inspection / modification
