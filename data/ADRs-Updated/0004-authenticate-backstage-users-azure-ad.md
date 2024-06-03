# 4. Provide frontend authentication for SEPA users (backstage) with Azure Active Directory and AD connect

* Status: proposed
* Deciders: [TBC]
* Date: 2019-09-19

Technical Story: CCP 1205 - Create Customer Account and Login

## Context

Azure Cloud Services and Microsoft Dynamics 365 have been proposed to support the CCP case & contact management, therefore, to maximise vendor reuse 
& interoperability, Azure's identity management system will be used to provide authentication for the frontend application (back stage/SEPA users).

## Decision Drivers
 
SEPA uses Active Directory for it's existing internal account management so providing one unified single sign on login would improve security and usability.

## Considered Options

1. Azure Active Directory
2. Dynamics user accounts

## Decision Outcome

[Option 1] SEPA should look to integrate Azure Active Directory with Dynamics to provide a shared identity 'federation', where backstage (SEPA) users are able to access Dynamics data via the WebAPI & perform CRUD operations using their existing single sign on login.

Dynamics users would therefore match the users within the Active Directory, and SEPA would require a Dynamics license for each SEPA user.

If SEPA's Active Directory is managed on premises, Azure AD connect can be used to auto sync existing Active Directory accounts to the Azure setup.

### Positive Consequences
* Reuse of existing SEPA logins
* Better backstage user experience

### Negative Consequences
* If Azure Active Directory connect is used to sync accounts, this would need to be monitored & managed by SEPA.

## Pros and Cons of the Options 

### 1. Azure Active Directory

Use cloud based Azure Active Directory storage to store accounts.  Provide single sign on to the CCP backstage application using OAuth JWT tokens.

#### Positive
* Best practice in terms of security - Microsoft manages authentication & accounts, SEPA inherits future enhancements/implementation.
* Provides a single sign on experience for SEPA staff - they can reuse their logins.

#### Negative
* If SEPA have a hosted AD setup, AD Connect would need to be used to keep the logins in sync.  Any syncing operation introduces a possible point of failure which would need to be managed.

### 2. Dynamics user accounts
Managing user accounts directly in Dynamics.  This option can only be used if the back stage users are logging into the Dynamics interface directly, it 
cannot be used for external access via the WebAPI.  

#### Positive
* Simple setup, reduces need for multiple linked 'account entities'.

#### Negative
* Does not support WebAPI access, therefore does not support a custom back stage user experience
* SEPA would need to setup new standalone logins for any Dynamics users and these would be managed in isolation.

## Links

* [Manage user account synchronization](https://docs.microsoft.com/en-us/power-platform/admin/manage-user-account-synchronization)
* [What is federation with Azure AD?](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/whatis-fed)
* [Single sign-on to applications in Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/what-is-single-sign-on)
