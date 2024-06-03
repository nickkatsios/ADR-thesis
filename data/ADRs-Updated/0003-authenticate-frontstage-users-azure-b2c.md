# 3. Provide frontend authentication for public users with Azure Active Directory B2C using existing 'user flows'

* Status: proposed
* Deciders: [TBC]
* Date: 2019-09-19

Technical Story: CCP 1205 - Create Customer Account and Login

## Context

Azure Cloud Services and Microsoft Dynamics 365 have been proposed to support the CCP case & contact management, therefore, to maximise vendor reuse 
& interoperability, Azure's identity management system will be used to provide authentication for the frontend application.

Actve Directory B2C (business to consumer) provides existing 'user flows' and allows for creation of custom policies that configure & customise the authentication process.  Which option is most suitable needs to be considered taking into account security & support for the custom UX.

## Decision Drivers

* Identity management must allow for permission based access to MS Dynamics 365 & file storage solutions.
* The level of customisation available for the sign up & sign in process should support the user journey being prototyped as much as possible. 

## Considered Options

1. Custom resource policy setup to allow 'resource owner password credentials' (ROPC) flow. This allows us to handle all sign up and sign within the CCP application.
2. Use an existing 'Sign up and sign in' policy & styled interfaced - redirects user to MS server to login
3. Use an existing 'Sign up and sign in' policy where the login page is hosted on a custom domain pointed to the Azure tenant (e.g. https://login.sepa.org.uk)

## Decision Outcome

[Option 2] Using Azure B2C with an existing 'Sign up and sign in' policy leverages the best out of the box authentication.  Users register and login using an Azure hosted service, users are redirected back to the application where a valid OAuth JWToken identifies who is currently logged in.

A custom domains would be best option, but this seems to be unavailable at the time of writing.

### Positive Consequences

* Leverages best practice for auth now and in the future.

### Negative Consequences

* Additional policy customisations would be required to fully customise the flow of the registration and login process (see links).
* Standalone HTML/CSS files will be need to be managed and uploaded to / updated in the Azure Directory  

## Pros and Cons of the Options

### 1. Custom resource policy

Custom resource policies can be setup to allow a 'resource own password credentials' flow, whereby the login is handled entirely 
within the application without redirecting to Microsoft URLs & the username/password is forwarded to Azure AD B2C. 

[Configure the resource owner password credentials flow in Azure Active Directory B2C using a custom policy](https://docs.microsoft.com/en-us/azure/active-directory-b2c/ropc-custom)

[Resource Owner Password Credentials grant flow in Azure AD](https://joonasw.net/view/ropc-grant-flow-in-azure-ad)

[Why the Resource Owner Password Credentials Grant Type is not Authentication nor Suitable for Modern Applications](https://www.scottbrady91.com/OAuth/Why-the-Resource-Owner-Password-Credentials-Grant-Type-is-not-Authentication-nor-Suitable-for-Modern-Applications)

#### Positive
* Consistent user journey is maintained - user see's no change in the URL
* Can support custom journey designed in the prototype
* No additional coding/styling required.

#### Negative
* This login does not work if the user:
    * Has MFA
    * Is a federated account
* Complex policies required to support login, password reset 
* Potentially less secure
* This flow is based on 'existing trust relationship' with the client, "take special care when enabling this grant type and only allow it when other flows are not viable"

### 2. 'Sign up and sign in' on b2clogin.com

Sign up & login are initialised within the application but the user is redirected to a separate Azure domain where authentication happens.
Once authenticated, the user is redirected back to the application with the relevant authentication information stored in their browser as an OAuth token.

#### Positive
* 'Out the box' policies maintained by Microsoft
* Security updates inherited from Microsoft
* Authentication is potentially available across multiple Azure tenants (i.e. applications)

#### Negative
* User is taken to a separate URL (negatively impacting trust?)
* Separate code would need to be applied to the Microsoft page to maintain consistent branding.
* Browser autofill wouldn't pick up any SEPA.org.uk domain logins  

### 3. 'Sign up and sign in' on custom domain

Similar journey to option 2 however the Azure domain can be customised so that a SEPA sub-domain (e.g. login.sepa.org.uk) can be pointed to the Azure tenant. This would create a more consistent user journey. 

[How can we improve Azure AD - customer-owned domains](https://feedback.azure.com/forums/169401-azure-active-directory/suggestions/15334317-customer-owned-domains)

#### Positive
* Consistent user journey is maintained - ui can be styled, user doesn't see any change in URL
* The sub-domain could be a central login point for all SEPA services requiring authentication.
* User's browser is able to apply user's stored SEPA login details whereas using a MS url this wouldn't be possible.  

#### Negative
* This option doesn't seem to be available to all users yet. 
* Separate code would need to be applied to the Microsoft page to maintain consistent branding.

## Links
* [An Introduction to the OAuth Device Flow](https://www.identityserver.com/articles/an-introduction-to-the-oauth-device-flow/)
* [Azure Active Directory B2C preview: Customize the Azure AD B2C user interface (UI)](https://github.com/uglide/azure-content/blob/master/articles/active-directory-b2c/active-directory-b2c-reference-ui-customization.md)
* [How to pass email suggestion to Azure AD B2C SignUp page](https://stackoverflow.com/questions/56501247/how-to-pass-email-suggestion-to-azure-ad-b2c-signup-page)
* [Example custom login flow with verification email](https://github.com/Azure-Samples/active-directory-b2c-advanced-policies/tree/master/wingtipgamesb2c)
