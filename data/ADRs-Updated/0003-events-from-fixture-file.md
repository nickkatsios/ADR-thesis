# 3. events-from-fixture-file.md

Date: 2020-12-07

## Status

Accepted

## Context

Trade show events are stored in many places across the TAP team.

  - At the beginning of the year the Glasgow operations team validates the list of events in a spreadsheet stored on sharepoint.
  - Events are uploaded to a hosted service called Aventri so that they are visible on great.gov.
  - Any updates to event details are communicated via email.

As of 2020-12-17 there are still discussions ongoing about how to manage trade show event data centrally within DIT 
and move away from the spreadsheet being the golden source of truth. One idea is to use digital workspace for this. 
However as of right now no decision on this has been made.

In the meantime the our services still need a way of displaying trade show events to our users to select and view.

## Decision

Without a firm decision on where events will ultimately be centrally stored we have decided to use a fixture file
to load events into our backoffice as a temporary solution. 

The fixture file exists at `backoffice/web/trade_events/fixtures/trade_events.json` and is automatically loaded on 
startup.

## Consequences

This allows some initial events to exist in the service while discussions continue around the topic.
