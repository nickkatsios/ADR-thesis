# ADR 3: Sending notifications

* Jeremy Wells

## Status

**proposal** | ~~accepted~~ | ~~depreciated~~ | ~~superceded~~

## Context

### Definitions

* **Command message**: This is a message on a stream that has been generated by 
a user action.
* **Command service**: This is a service that listens to command messages.
* **Data message**: This is a message on a stream that has been generated by 
another service asking to persist data.

The application needs to send notifications to end users about certain events. 
For example, send the volunteer an email to say that their application has 
been accepted.

However, there are rules around the sending of notifications. With the above
 example, the volunteer should receive the accepted application when the 
 following is true:

* Engagement isAccepted = true
* Opp confirmationsOn = true

Further, there are notifications with time based restrictions. For example, it
 may be desirable with the above email to wait for an amount of time before 
 sending the notification so that an event coordinator can move an engagement 
 around without causing a flood of emails.

The above rules mean that if an engagement is accepted, but the confirmations 
are not turned on, and then the confirmations get turned on, then the 
notifications for existing accepted engagements get sent. Any engagements 
that are accepted from that point in time are also sent.

## Options

1. Create the emails in the command services. For the above example, this would require code in the engagements service and the opps service. The engagements 
code would check isAccepted && confirmationsOn. The opps service would 
check confirmationsOn and then loop over all engagements.

    In order to implement the timing rules the service would add a sendAt to the email record. The email service itself would need to do something with this.
    
@startuml
actor User
participant engagements
control emails
control data

User -> engagements: isAccepted = true
engagements -> engagements: confirmationsOn?
alt true
    engagements -> emails: Send accepted
end
engagements -> data: Update
@enduml

@startuml
actor User
participant opps
control emails
control data

User -> opps: confirmationsOn = true
loop isAccepted engagements
    opps -> emails: Send accepted
end
opps -> data: Update
@enduml
    
**Pros**
* Natural way to write it

**Cons**
* Services have too many responsibilities
* Duplication
* Complexity - loop over opp engagements
* Hard to prevent duplicate emails

2. Create a separate service that listens on data topics (engagements, opps) 
and when it sees an update to isAccepted or confirmationsOn, performs the above
 rules and sends to the emails topic.
 
(for brevity user omitted): 
 
@startuml
participant engagements
control data
participant "engagements accepted"
control emails

engagements -> data: Update isAccepted = true
data -> "engagements accepted"
"engagements accepted" -> "engagements accepted": confirmationsOn?
"engagements accepted" -> emails: Send accepted
@enduml

@startuml
participant opps
control data
participant "engagements accepted"
control emails

opps -> data: Update confirmationsOn = true
data -> "engagements accepted"
loop accepted engagements
    "engagements accepted" -> emails: Send accepted
end
@enduml

**Pros**
* Services have single responsibility
* Testing is easier

**Cons**
* Complexity - loop over opp engagements
* Hard to prevent duplicate emails

3. Introduce a notification model to the services in option 2. Thus instead of
emitting email specific messages, the services emit normal data messages. In 
the given example, when an engagement is accepted an accepted notification is 
created.

    The accepted notification model / service will deal with the logic. As 
    engagements are accepted the notifications will be collected. When the opp
    confirmationsOn flag is set the existing notifications will be sent.
    
    The implementation of a notifications service would need to run on a 
    schedule or loop.
    
@startuml
participant engagements
participant "engagements accepted" as accepted
control data
database database

engagements -> data: Update isAccepted = true
data -> database: Update engagement
data -> accepted
accepted -> data: create notification
data -> database: create notification
@enduml

@startuml
participant notifications
database database
control emails

[--> notifications: scheduler
notifications -> database: load
database -> notifications
loop notifications
    notifications -> notifications: condition check
    alt true
        notifications -> emails: Send email
        notifications -> database: Remove notification
    end
end
@enduml
    
**Pros**
* No duplication
* Services have single responsibility
* Notification logic is separated
* Notifications are tracked
* Notifications are generic - will support more than email

**Cons**
* More code
* Notification logic is separated
* Notification model or service requires logic

## Decision

Option 3 is my preference

## Consequences
