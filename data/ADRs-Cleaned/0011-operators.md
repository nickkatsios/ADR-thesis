managing operator deciders tumido humairak nnd anishasthana larsks martinpovolny technical story issue problem statement clusterscope application definition introduced adr bit vague case like deploying operator operator lifecycle manager olm defines resource overlap single resource kind different example subscription resource subscribe specific operator either clusterscoped namespacescoped may distinction introduced adr document provides guidance resource kind olm treated usage variant aim support driver definition clusterscope application adr provide enough guidance olm various olm resource way effect whole cluster way limit effect single namespace various olm resource permission restriction behave singleton within namespace operator deployed via olm yet behave operator across namespaces placement manifest also disputed handle metaoperators operate across namespaces deploy operator operate across namespaces considered deploy operatorrelated resource within clusterscope application require namespaced resource deployed within individual application outside clusterscope find balance deploy resource effect cluster level within clusterscope app also namespacescoped one rest deployed individual application outcome chosen find balance desired keep track resource may effect user namespaces operator provisioned manage cluster namespaces proposed defines strict rule given resource rule subject future update needed repository application required consistently enforce operator lifecycle manager compatible operator operator lifecycle manager defines following resource kind cluster service version catalog source subscription install plan operator group set guideline want enforce cluster service version resource meant deployed manually expected provided catalog source there really deploy custom cluster service version resource live within clusterscope application catalog source uncommon catalog source declared manually operator expected provisioned default catalog advised publish desired operator community catalog rather deploying custom catalog source necessary deploy additional catalogsource resource resource must deployed openshiftmarketplace namespace therefore must declared within clusterscope application subscription subscription resource namespacescoped resource effectively responsible operator deployment therefore recognise possible scenario case resource namespaced operator single namespace visibility subscription resource hosted along application manifest application repository application deployed namespace specified subscription operator namespaces visibility operator global effect expect subscription resource hosted clusterscope application deciding namespace olm resource reside global operator done casebycase basis general rule thumb put openshiftoperators however take note may various exception rule clusterlogging openshift metering etc subscription resource manifest expected deployed namespace corresponding operatorgroup located install plan operator expected deploy custom install plan expect every plan provided cluster service version resource belonging given operator operator group operatorgroup resource namespacescoped resource however require resource placed clusterscope application due following reason resource singleton namespace cant multiple instance said resource namespace even name differs deployed generates clusterrole clusterrolebinding aggregation rule specify namespaces visibility operator default project admins createedit right operatorgroups due point clusteradmins manage operator group number possible conflict direct consequence operatorgroup deployment resource treated carefully therefore required placed maintained clusterscope application level centralized operator group management ensures wont deploying namespaced operator already another instance namespace visibility etc according upstream documentation operatorgroup target namespace selection enforce support target namespace specification operator group specification global clusterwide operator visibility namespaces mean spec section manifest blank single namespace operator resource manifest specifies spectargetnamespaces singlemembernamespace namespace deployed via clusterscope application well operatorgroup resource manifest expected deployed namespace corresponding subscription located direct operator deployment operator deployed via olm mean manifest require manual deployment customresourcedefinitions clusterroles etc require kind resource deployed via clusterscope application contrast resource required nonolm operator deployment like deployment route etc treated namespace scoped application manifest required deployment expected located separate application operatefirstapps repository root folder metaoperators special kind operator metaoperator understood operator allowing deployment operator cluster scope intention limit possibility operator able interfere cluster management clusterscope application expect metaoperators provide either limit permission via operator configuration able deploy resource requiring clusteradmin permission limit createedit access permission custom resource create order limit normal project user project admins escalating privilege possible deploy metaoperator way respect one condition expected operator requester raise issue upstream fixed expect operator installed manually via direct operator deployment via olm framework therefore allowing manually control custom resource access permission regular user operator service account clusterrole positive consequence clear guidance individual resource regarding operator may appear confusing without rule allows operator treated like normal application case deployed manually clutter clusterscope applicaton anymore enforces restriction prevent user privilege escalation via metaoperators negative consequence complex set rule clusteradmins follow fully understand pro con deploy operatorrelated resource within clusterscope application good easy implement good make rule clear user want operator live every time bad impossible achieve metaoperators like odh bad hard maintain since especially namespaced operator may owned different team bad amount resource deployed clusterscope application may increase drastically bad doesnt solve metaoperators access custom resource deploy operator cluster scope anyways require namespaced resource deployed within individual application outside clusterscope good easy implement good doesnt require complex rule follow user bad impossible achieve metaoperators like odh bad namespacescoped resource required unique said namespace bad namespacescoped resource grant access operator cluster scope level find balance good weight resource kind separately decide based case good allows keep clusterscope application reasonable size good give enough control individual applicationproject owner want deploy namespaced operator bad requires complex rule full understanding resource system integrator want provision operator link add detail specific usecase adr operator lifecycle manager concept operatorgroup design document operatorgroup target namespace selection