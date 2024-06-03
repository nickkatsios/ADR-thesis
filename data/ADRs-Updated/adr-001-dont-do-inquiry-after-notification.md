# ADR 001 - Don't do inquiry after notifications

## Context

We're working towards private beta for Pay and working towards implementing
handling Worldpay refund notifications.

A decision was made previously to make an 'inquiry' API call to worldpay after
receiving a notification from them. The main motivations for doing this were:

- security - in the case that there is a forged notification from worldpay, we
  can be more confident in getting the accurate information by calling out to
  worldpay
- robustness if a notification is missed for any reason, then doing an inquiry
  will allow us to 'catch up' to the new status.

Regarding refunds, we have determined that Worldpay API does not support
inquiry about specific refunds, only about an order. Here is a sample response
to an inquiry after a refund has occured:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE paymentService PUBLIC "-//WorldPay//DTD WorldPay PaymentService v1//EN" "http://dtd.worldpay.com/paymentService_v1.dtd">
<paymentService version="1.4" merchantCode="MERCHANTCODE">
   <reply>
      <orderStatus orderCode="01105e9b-f0e6-446c-a093-a2ef48f5fd39">
         <payment>
            <paymentMethod>VISA-SSL</paymentMethod>
            <paymentMethodDetail>
               <card type="creditcard" />
            </paymentMethodDetail>
            <amount value="500" currencyCode="GBP" exponent="2" debitCreditIndicator="credit" />
            <lastEvent>REFUNDED</lastEvent>
            <refundReference>refund-1-01105e9b-f0e6-446c-a093-a2ef48f5fd39</refundReference>
            <reference>refund-1-01105e9b-f0e6-446c-a093-a2ef48f5fd39</reference>
            <AuthorisationId id="666" />
            <CVCResultCode description="NOT SENT TO ACQUIRER" />
            <AVSResultCode description="NOT SENT TO ACQUIRER" />
            <cardHolderName><![CDATA[Mr. Payment]]></cardHolderName>
            <issuerCountryCode>N/A</issuerCountryCode>
            <balance accountType="SETTLED_BIBIT_COMMISSION">
               <amount value="15" currencyCode="GBP" exponent="2" debitCreditIndicator="credit" />
            </balance>
            <balance accountType="SETTLED_BIBIT_NET">
               <amount value="484" currencyCode="GBP" exponent="2" debitCreditIndicator="credit" />
            </balance>
            <riskScore value="1" />
         </payment>
         <date dayOfMonth="24" month="08" year="2016" hour="9" minute="53" second="0" />
      </orderStatus>
   </reply>
</paymentService>
```

the inquiry command only returns information about the *last* event on an
order (`<lastEvent>REFUNDED</lastEvent>`). So in the case of an order with two
partial refunds, there's a race condition where an inquiry could return
information about a different refund.

Conducting an inquiry after a notification adds significant complexity to the
codebase. In particular it opens up the possqibility of a lot of edge cases
where, for example, an enquiry might indicate a different status than a
notification. This could in theory be legitimate if two status changes occured
in quick succession but only the first notification has been delivered. Or it
could indicate a bug or issue.

It's hard to know how to sensibly handle these edge cases, and we don't really
have evidence that they will happen in practice.

There's a further issue in that the current implementation performs inquiries
in the same thread that handles the notification HTTP request. This means that
the notification doesn't get an HTTP response until the inquiry roundtrip to
Worldpay has also completed. This could be a potential source of bugs.

Finally, Worldpay themselves advise in the [Order Modification and Inquiries Guide](http://support.worldpay.com/support/kb/gg/pdf/omoi.pdf):

> Although order inquiries can be a useful tool, we recommend that you use
order notifications to find out about changes to your transactions. If
you’re set up for notifications, we do all the work - notifications are
sent to you automatically when the status of a transaction changes.

## Decision

We will not do `inquiry` calls after notifications at all, neither for order
notifications, nor refund notifications.

## Status

Accepted.

## Consequences

We agreed that the possible benefits of performing inquiries do not justify
the significant added complexity.

Removing them will simplify the codebase and tests.

We should be vigilant for unexpected status changes which might indicate
missed notifications. These should be detected by the [charge status transition state machine](https://github.com/alphagov/pay-connector/blob/master/src/main/java/uk/gov/pay/connector/model/domain/StateTransitions.java). Currently that raises an unhandled exception which will trigger 500 errors. We probably will want to change this so that the errors are logged, but we return a 200 status code.

Regarding other payment gateways, smartpay doesn't support order inquiry so
this is not relevant. When integrating with other gateways we should
reconsider the most appropriate approach to use on a case-by-case basis.

