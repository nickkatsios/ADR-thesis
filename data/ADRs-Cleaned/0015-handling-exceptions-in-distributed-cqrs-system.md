adr handling exception distributed cqrs system proposed proposed updated author damir murat damirmuratgit gmailcom reviewer none developer consider dealing local runtime exception jvm quite convenient easy consequence exception often mean alternative execution flow one typical example reporting structural business validation violation local jvm environment expected execution flow exception usually created full stack trace included however exception represent normal condition creating full stack trace wasteful term performance resource full stack trace problem additionally emphasized distributed jvm environment stack trace creation wasteful take much bandwidth transfer side finally distributed jvm environment cannot safely assume custom exception class present classpath jvms therefore assume exception created serverside deserialized client remedy situation small number stackless exception class shared jvms included communication belong boundary layer part api distributed communication read boundary layer take look near end domain library section organizing module package article communicating various custom exception violation error code violation code defines severity contains several additional property describing violation detail architectural system klokwrkproject distributed error reporting stackless exception communicating custom error code jvms distributed axon environment distributed axon environment dispatching side let call client sends command query axon server handling side let call server handling side detects broken business invariant raise exception report detail dispatching side axon framework already contains base infrastructure reporting distributed error via socalled exception detail exception detail dtolike class shared communicating party including necessary data describing error condition detail business exception handling case exception detail dto domainexception class descendant stackless exception carry violationinfo property violationinfo contains severity violationcode property violationcode contains code codemessage english also resolvablemessagekey resolvablemessageparameters support error code resolving resource bundle internationalization purpose worth noting domainexception dispatching side client exception unwrapping handling side centralized exception handling dispatching side hidden infrastructural code developer perspective work commandexception queryexception extended domainexception nice addition business invariant handled way handling dispatching side without depending class axon framework usage example handling side take look bookingofferaggregate bookingoffersummaryqueryhandlerservice class example dispatching side found bookingofferfactoryservice class unexpected exception handling handling business exception interested stack trace since business exception form alternate execution flow isnt much benefit logging stacktrace contrary want log stack trace unexpected exception nullpointerexception occurs remote handler however communication constraint still hold still error code communicating exception correlate exception handling dispatching side must exception identifier put log message side logic handling unexpected exception handling side seen commandhandlerexceptioninterceptor queryhandlerexceptioninterceptor class consequence positive consistent optimal handling remote business exception consistent optimal handling remote unexpected exception identical handling local remote business exception developer correlation remote unexpected exception neutral bit unusual way constructing exception negative considered reference organizing module package httpsgithubcomcrozltdklokwrkprojectblobmastersupportdocumentationarticlemodulesandpackagesmodulesandpackagesmd steven van beelen live coding session axon practice start time httpswwwyoutubecomwatchvucmxyejbzfts steven van beelen live coding session axon practice sample code httpsgithubcomsmcvbgamerental axon reference guide exception handling httpsdocsaxoniqioreferenceguideaxonframeworkmessagingconceptsexceptionhandling exceptional performance lil exception httpsshipilevnetblogexceptionalperformance