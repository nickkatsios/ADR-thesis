# ADR 002 - Don't decrypt payload from Google Pay

## Context

There are two possible tokenization methods when making a payment request to Google Pay: [PAYMENT_GATEWAY and DIRECT](https://developers.google.com/pay/api/web/guides/tutorial#tokenization).

Features of PAYMENT_GATEWAY tokenization:

- Merchant id identifying GOV.UK Pay with Google Pay needs to be set up
- We simply pass the encrypted response from Google Pay through to the payment gateway as is
- No need of the operational overhead of key management as is already handled between Google Pay and the payment gateway

Features of DIRECT tokenization:

- No need for a Merchant id between GOV.UK Pay and Google Pay
- Need to be PCI DSS compliant (which we already are)
- Need to decrypt the response to get information to send to the payment gateway
- Need the operational overhead of key management as we need to [roll keys once a year and register these with Google Pay](https://developers.google.com/pay/api/web/guides/resources/payment-data-cryptography#key-management)


With either tokenization method, we get a [number of data](https://developers.google.com/pay/api/web/reference/object#response-objects), but the ones relevant to us are:

- Last 4 card digits
- Billing address (which includes name)
- Email address
- Card Network

With DIRECT tokenization we decrypt to get:

- PAN
- expiration month and year

[and other things](https://developers.google.com/pay/api/web/guides/resources/payment-data-cryptography#encrypted-message).


Choosing whether to decrypt the payload from Google Pay or not is informed by the following two deal breakers:

- We need to be able to retrieve the cardholder name, email, and last 4 digits of a card
- We don't want services to have to manage any sort of keys/certificates


## Decision

Unlike the current implementation of Apple Pay, we have chosen to go with not decrypting the payload for the following reasons:

- We get all the information we require (Last 4 card digits, billing address name, email address, card network) in unencrypted form
- Services won't need to manage any keys/certificates. This is because when a payment request is made to Google Pay we specify the payment gateway, e.g. "Worldpay". 
Google Pay will return a response encrypted with the payment gateway's public key. 
This response is decryptable by the payment gateway as they have their private encryption key.
So there is already a key management process between Google Pay and the payment gateway. 
Our initial assumption that Google Pay encrypts with the merchant id's public key was incorrect. 
- No operational process is needed on our part to manage keys/certs.

## Status

Accepted