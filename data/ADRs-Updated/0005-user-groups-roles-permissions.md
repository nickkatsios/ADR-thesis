# 5. Manage user roles and permissions using Active Directory Groups

* Status: proposed
* Deciders:
* Date: 2019-10-03

## Context and Problem Statement

The application needs to control access to permits & their supporting documents based on user roles.

## Decision Drivers 

* Applicants and operators will be grouped by 'account' in the CRM, however SEPA should be able to differentiate between an organisation's users & it's lead contacts  (administrators).
* SEPA staff will potentially require different access levels depending on the permit application; sensitive data requirements means certain documents should only be accessible to users with specific privileges.

## Considered Options

1. All user roles are managed through Active Directory groups
2. SEPA staff permissions are managed according to the Active Directory group they are assigned to.  Operator / applicant permissions are managed according to the account/contact relationship in Dynamics.

## Decision Outcome

[Option 1] SEPA staff should be assigned to Active Directory groups based on their roles, the following are suggested but need to be reviewed based on a more thorough investigation of roles. 

### Positive Consequences

* This option maintains a basic user hierarchy that would be available outside of the Dynamics system that would potentially be useful if the accounts are used in other applications

### Negative Consequences

* Potentially more overhead in terms of group management & to an extent duplication in terms of the CRM account to contact grouping.

## Pros and Cons of the Options

### 1. All user roles are managed through Active Directory groups.

Groups are used for both Active Directory back stage users and Active Directory B2C front stage users.  Application permissions for each user are then inferred from the group.

Suggested group setup for back stage users: 

* SEPA Marine Pen application - administrators
* SEPA Marine Pen application - users

This setup would allow for additional license type grouping and segmentation in the future.

Front-stage users (applicants and operators) should also be organised into group structures within the Azure Active Directory B2C, 

* [Operator name] - administrators
* [Operator name] - users

This will provide a level of organisation hierachy and administration.

#### Positive
* Provides flexibility to assign additional permissions and actions to multiple operator administrators.
* Provides greater organisation in Active Directory B2C (when viewed in isolation)
* Potential to reuse account setup for other action not related to the CRM.

#### Negative
* This would create an additional relationship between operator roles that is already possible in the CRM (primary/lead contact on the account entity).

### 2. SEPA staff permissions are managed according to the Active Directory group they are assigned to.  Operator / applicant permissions are managed according to the account/contact relationship in Dynamics.

SEPA staff roles & permissions to be inferred from the Active Directory groups they are assigned to.  Front stage users (who authenticate using Active Directory B2C) would be grouped together & assigned app permissions based on how their their user account links to their CRM contact entity.   CRM contacts will be linked to their organisation's account entity (providing the group structure) and administrators would be assigned using the 'primary contact' field on the account entity.

#### Positive
* No duplication of contact to account grouping, CRM is the single source of contact relationships & an organisation's lead contact.

#### Negative
* Seen in isolation, the front stage Active Directory B2C would have no identifiable structure or links without querying the CRM data.

## Links <!-- optional -->

* [Microsoft Graph API for user & group management](https://docs.microsoft.com/en-gb/previous-versions/azure/ad/graph/api/users-operations)
