record initial architecture notify integration introduction october govuk email team began project intending expand responsibility emailalertapi application handle creating sending alert enter system changed system intends notify transportation layer send email part considering conducted piece work outline architecture application document present treating digest time putting together unclear exactly product functionality would regarding digest however want considered architecture clarity explains best guess understanding digest work prior appropriate product digest expected continue current behaviour merging multiple subscription single email essential digest return content user subscription digest processed joe processed min steve may get slightly different result something published time subscribed thing produce content two subscription different digest frequency receive notification piece content higher frequency digest take effect point subscription joined weekly digest wednesday sent friday youd get alert content joined send remaining digest email someone change subscription preference specific architecture visualised two diagram domain model represents data model relate sequence diagram represents component communicate achieve specified functionality document concept diagram outline role responsibility contentchange responsibility representing piece content either new changed produce alert shall store information title content description content change note associated update path content store information subscription criterion match link tag supertypes field required auditing request came able determine whether processed worker processedat presence persisted forever may future association entity model subscription criterion information link tag super type considered part alert supertype may represent type alert system subscriber list responsibility type list user subscribe storing information specific list shall store information list name require list name unique dont know differentiate identically named list user yet temporarily maintain relationship corresponding govdelivery list store information subscription criterion match link tag documentsupertypes information source subscriber list originated may future association entity model subscription criterion information link tag super type release requirement list name unique able establish way differentiate list store statistic related list stored even removed logging purpose dependent impact unique constraint determine scenario subscriber list removed subscriber responsibility represent individual user subscribe content store information related subscription user may shall store information email address support email address changing deleteable user may wish remove account break history email sent future authentication purpose may store preference affect user subscription ability disabled problem user account store personalisation information name associated statistic regarding subscriber determine allow term removing subscriber associated data log subscription responsibility store subscriber association subscriber list associated data preference shall store association subscriber store association subscriber list store preference associated particular subscription removed system user unsubscribes subscriber list provides log user subscribed associated content maintaining record allows restore preference subscription resumed may store statistic subscriber activity relating subscription future something paused determine happen either subscriber list subscriber removedarchived subscriptioncontent responsibility represent content change emailed subscription shall association contentchange association subscription nullable association email know whether processed allow multiple subscription associated subscriber associated contentchange emailgeneration responsibility consolidate allow multiple entry contentchange subscription allow content change reprocessed event error support email record removed system auditing process deleteable scenario user change subscription email sent determine archiving strategy persisted forever match persistence strategy email instance email responsibility distinct email system sending sent shall created time email alert api sends email store information recipient subject body notify markdown delivery shall one recipient know anything content led generation exist database non permanent time period associated subscriber logging purpose may archived log somewhere later analysis deliveryattempt responsibility storing information communicate transportation service email shall store information email associated provider notify provider reference look email successpendingfailure provider specific errorswarnings created whenever email attempted sent updated sufficient information known whether email sent deleted email deleted may created success state known delivery attempt successful synchronously future different transport mechanism expand beyond email contentchangecontroller responsibility storing contentchange enquing processing returning success shall create contentchange model enqueue subscriptioncontentworker job determine responsibility worker failing run subscriptioncontentworker responsibility responsible determining subscription receive email prospectively creating subscriptioncontent object accordingly shall given sufficient input lookup contentchange liaise subscriptionmatcher determine subscription match contentchange create subscriptioncontent entity subscription match contentchange trigger emailgenerationworker email run immediately able multiple instance worker processing contentchange concurrently may accept frequency argument match subscription frequency order allow rebuilding email went error subscriptionmatcher responsibility given certain criterion determine subscription object associated shall accept contentchange object input input determine subscription object match existing logic subscriberlistquery determine considering might scale huge number subscription emailgenerationworker responsibility responsible finding subscription object sent given frequency producing email object sent shall find subscriptioncontent entity match frequency processed take one subscriptioncontent entry user create corresponding email entity update subscriptioncontent entry associate email indicate processed liaise emailrenderer convert one subscriptioncontent entity subject body email take input frequency immediate weekly daily able consolidate subscriptioncontent entry refer contentchange able process subscriptioncontent object multiple concurrent process may interface reconsidered allow increased ability build email parallel determine user multiple subscription different frequency class consolidate digesttimer responsibility triggering emailbuilderworker run given frequency shall trigger emailgenerationworker run daily interval trigger emailgenerationworker run weekly interval determine interval mechanism would place handle failing occur emailrenderer responsibility converting one email entry notify markdown formatted text shall take input one subscriptioncontent entity frequency generate subject plain text generate body notify markdown able generate differently formatted email weekly daily email may sufficient information include unsubscribe link email emaildeliveryworker responsibility finding email sent creating deliveryattempts updating email accordingly shall communicate transportation layer notify send email create deliveryattempt object associate email update email deliveryattempt object based outcome request able retry request notify fail retryable temporary network outage able abort trying send email situation retrying wont result success bad request may react transportation layer returning code determine happen email exhausted retries happen email fails due bad request deliverymonitor responsibility determining whether notify able send email tried send shall communicate transportation layer notify determine pending delivery attempt still progress successful failure update email deliveryattempt object based outcome request able abort attempting send email notify return temporary failure email address able removesuspend user account notify return permanent failure corresponding email address able retry sending email notify return notify failure error indicates sending retried determine system rule behaviour follow removingsuspending account receive permanent failure message notify