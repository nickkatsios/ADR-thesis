user identity author opqdonut macroz jaakkocsc background currently rem userid received oidc server sub claim another claim based configuration userid internal database key user userid embedded application event workflow etc problem current approach sub attribute might opaque usable system sending entitlement system different login method may different format external user identifier different login method might conflicting value claim foocscfi via haka csc sso todo know case like single user might multiple external identifier todo know case like case user identity user identifier multiple thing might want different identifier different purpose referring user inside rem data workflow handler referring user api response workflow handler enriching referring user api request set workflow handler get entitlement user referring user entitlement post call internal user identifier well add internal random user rem internal user key user referred within rem user external stored attribute json blob allow flexibility future identity requirement case change might also make sort migration easier since internal user dont touched login user log rem fetch user token find first attribute oidcuserattributes set token call attributevalue pair attr value find user rem database attr value stored user attribute user found set current session identity internal user user user found create new internal user store attr value attribute set current session identity created internal user user identity resolution somebody userid xyz api call rem search user like user rem internal user xyz user iterate every attribute attr oidcuserattributes order user attr xyz user keep iterating user found multiple user found return http bad request example referring user external rem configured two userid attribute oidcuseridattributes cscid eppn handler logged cscid user logged eppn user database table userid attribute eedddfdfbdccc cscid handlercscfi name hannah handler bccebbefaf eppn userexamplecom name example user api call impersonating handler add user reviewer referring user eppn note xremsuserid must always internal rem user see open question post apiapplicationsrequestreview xremsuserid eedddfdfbdccc applicationid reviewer userexamplecom rem find user command succeeds content application queried json document contains internal userids well external get apiapplications applicationid applicationevents eventtype applicationeventreviewrequested applicationid eventactor eedddfdfbdccc eventactorattributes userid eedddfdfbdccc cscid handlercscfi name hannah handler applicationreviewers userid bccebbefaf eppn userexamplecom name example user changing identity problem user logged identity provider created application however started logging via another identity provider entitlement associated new identity solution copy user attribute new user row old user row remove new user row user log get old identity entitlement associated external related entitlement also changed implementation plan add support multiple userid attribute first add support list oidcuseridattribute value would ordered list attribute check user log value first attribute found get userid backwards compatible current behaviour issue workaround thl instance sub attribute going change identity provider thl instance change however time idp able provide oldsub attribute user log via old method via haka eduuni virtu user logging via new elixir method well elixirid attribute user cause right user pushing entitlement elixir service accomplished setting oidcuseridattributes elixirid oldsub internal everywhere implement login section adr also write necessary database migration see also migration open question issue support external apis implement user identity resolution section adr one api time probably release step issue open question api format switch apis take userids structured userid abc form could specify user explicitly like eppn userexamplecom alternatively could make apis polymorphic specify user userid attr value would backwardscompatible make code complex xremsuserid allow external user xremsuserid user search api api searching resolving user issue migration migrate existing userids new random value keep asis database index good index needed performance looking user based attribute storing data jsonb fine also add new column also lucene implement user searching issue push post etc outbound apis see issue httpsgithubcomcscfiremsissues note discussed whether store show attribute user example handler see identity user old attribute always replaced user come changing idp also may change email attribute could confuse handler decided anything yet since existing behavior also storing old attribute might mean store show user old email name way change authentication method removed