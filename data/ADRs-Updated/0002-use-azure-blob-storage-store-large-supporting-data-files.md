# 2. Use Azure blob storage to store large supporting data files

Date: 2019-09-16

## Status

Proposed

## Context

A cloud storage solution is required to allow operators and SEPA staff to upload the large supporting data files required to process an application.

The storage solution would need to integrate with the case management tool (Microsoft Dynamics 365)

## Decision

MS Dynamics offers close integration with Azure Cloud services, therefore Azure Blob Storage has been selected.

## Consequences

Additional security implications need to be considered and audited to ensure relevant access or restrictions to files per document & license.
