improvement deciders lauren zugai dan schomburg barry chen vijay budhram wil clouser technical story document rfc contains jira link information problem statement firefox account migrated gettext fluent last year several question around including infrastructure package inconsistency general improvement surfaced discussion occurred linked document adr capture major doc mention relevant past list proscons negative consequence new reasonable alternative note cover fluent package fxasettings fxapaymentsserver fxareact fxaauthserver noted rfc fxacontentserver still gettext share fluent infrastructure refactor react driver consistency across package reliability robust complete testing allowing fxareact manage straightforward email outcome consistent ftl path name setup across package enus fxas default locale early team recommended switch fxasettings still contains enusftl file updated enftl historically deploy enus fluent bundle since may support missing fallback text consistency across locale environment fxapaymentsserver setup change fxapaymentsserver commits single file publiclocalesenusmainftl copied repo differs fxasettings fxaauthserver wherein separate ftl file per component concatenate file together copy repo consistency better maintainability set concatenation anyway see fxareact well split fxapaymentsservers ftl file percomponent enftl file require setting something similar fxaauthservers mergeftltest script test make sure reference relative path also rename mainftl become paymentsftl negative consequence keeping string single file doesnt additional build step testing pushing repo mean final output could feel clear since single committed file would reflect exactly whats going fluent configuration file fluent configuration file useful repository support different locale different file complex path involved fxa manages translation separate repository wont benefit well remove fxapaymentsservers config file outcome continue fallback text set better testing strategy theory fluent always insert translated string found bundle including english string considered dropping fallback text favor relying fluent pro dropping fallback text better maintainability guarantee consistency due needing duplicate string one fallback text one ftl file codebase might feel infriendly depend fluent instead prioritizing english speaking user explicitly setting english fallback text con dropping fallback text string extraction timing consideration currently delay fxa land reference latest compiled ftl file including fluentreact doc actually recommend fallback text state future may automatic extraction source copy ran small test see technical story doc showed least rare occasion fluent may fail retrieve string browser cant always load fluent bundle file loading page successfully wherein fallback text displayed would take least two search find string ultimately end component finding corresponding ftl searching solution one primary concern around fallback text maintainability consistency guarantee testing provided ftl exist sourceoftruth bundle fallback text match message tied enftl bundle validate variable referenced message string available message doesnt contain straight quote nice reactbased package create two wrapper one localized one lngetstring enforce fallback text always provided set mergeftltest script test run mock wrapper test whats outlined fxaauthserver create helper function send template easily grab message fluent bundle thing like alt text otherwise require additional complexity due mjml fluentdom set also automatically apply datalnargs test email template enormous single test file email string adjust email test set separate per component better maintainability easier testing outcome concat fxareact ftl file package global branding file component fxareact another package add ftl string package component rather fxareact easily forgotten lead duplication idsmessages across package instead concat file fxareact existing fluent bundle additionally help consistency maintainability across board well create global ftl file license branding shared across package first build bundle considered could create new bundle fxareact similar package however wed ship outputted file package would create another network request importantly wed reconfigure fluent set check translation two different bundle outcome clone fxacontentserverln instead perpackage currently clone repo package via clonelnsh script postinstall step instead every package cloning repo script pull repo central location package skip script update build step per package accordingly know script work tweak doesnt require management engineer new string land subtrees may good would heavily modify still maintain script introducing newtofxa git concept considered git submodule git submodules essentially gitlinks reference commit locally link look different clone see poke around fxacontentserverln within package git track reference commit gitmodules config file pro could ditch clonelnsh script favor native git feature make pushing repo easier feature would often submodule command known submodules useful switching different state comparison neutral well maintain gitmodules configuration file con engineer run git submodule init engineer wont know much submodules one thing read understand visible clone script essentially hidden developer could add git submodule update remote call build postinstall step fetch latest would still commit update fxa repo update gitlink commit sha least one mozilla project bot may tweak build step set git subtree git subtree replica copy git repository creates relationship parent repository fxa pro similar existing setup unlike submodules complexity hidden engineer may able remove copying directory build step package favor gitsubtreessplit gitsubtreemerge con subtree wouldnt add new metadata file like git module would would modify create new version clonelnsh script git subtree add tree alongside check updating subtree requires command git subtree pull since want gitignore output update postinstall may always run additional command first remove subtree add every time extra check see pull add engineer wont know much subtrees one thing read understand link original rfc created adr