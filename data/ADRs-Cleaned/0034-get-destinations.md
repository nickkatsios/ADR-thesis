get destination api approved user would like get destination account sdk would nice expose proper interface getalldestinations function similiar getdestination function following api export async function getdestination destinationfetchoptions destinationforservicebindingoptions promisedestination null const destination searchenvvariablesfordestinationoptions await searchregistereddestinationoptions await searchservicebindingfordestinationoptions await getdestinationfromdestinationserviceoptions return destination include lookup step could become quite cumbersome well relatively expensive currently function searching destination work single destination name meaning would either rewrite create new function every single lookup process decided implement function get destination destination service fulfill user story still implement function ondemand omit authtokens returned destination running authentication flow receive token destinatioon service every destination could lead heavy burden destination service type destinationwithouttoken omitdestination authtokens user desire receive authtokens every destination still map returned array additionally neither selectionstrategy isolationstrategy serve purpose destinationoptions scenario selectionstrategy would specify destination supposed fetched decided based provided jwt isolationstrategy decide cache destination tenantuser doesnt make sense destination arent depending specific user therefore omit tenant reasonable strategy therefore tenant isolation strategy omit type alldestinationoptions omitdestinationoptions selectionstrategyisolationstrategy export async function getalldestinationsfromdestinationservice alldestinationoptions promisedestinationwithouttoken null function throw warning one destination incompletecompromised user feature request lookup function searchenvvariablesfordestination etc shall implement ondemand end implementing every lookup function get destination implement parent function deprecate remove preceding function consequence user get access function returning destination destination service appendix potential candidate considered rewrite existing create new lookup function return destination instead specific one would result relatively expensive call requires alot rework however would provide user api consistent getdestination export async function getalldestinations destinationoptions destinationforservicebindingoptions promisedestination null const destination searchenvvariablesforalldestinationsoptionsconcat await searchregisteredalldestinationsoptions await searchservicebindingforalldestinationsoptions await getalldestinationsfromdestinationserviceoptions return destination get destination destination service far common case would require least amount effort wouldnt cover potential corner case export async function getalldestinationsfromdestinationservice destinationoptions promisedestination null similar offer possibility toggle onoff certain lookup would take effort increase code complexity give user interface destinationlookupoptions extends destinationoptions searchenvvariablesfordestinations boolean searchregistereddestinations boolean searchservicebindingfordestinations boolean getdestinationfromdestinationservices boolean export async function getalldestinations destinationlookupoptions destinationforservicebindingoptions promise const destination searchenvvariablesforalldestinationsoptionsconcat await searchregisteredalldestinationsoptions await searchservicebindingforalldestinationsoptions await getalldestinationfromdestinationserviceoptions return destination