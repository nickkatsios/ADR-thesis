bulk import primary goal current data upload refactoring project includes enabling user upload data bulk producing multiple new data object userside operation mean introducing interface handle following step selecting several data file concurrently import new data object launching would amount several import job bulk import operation monitoring state job restarting necessary viewing result job currently work done user one cell time app cell generated desired data file upload timeconsuming cluttering narrative new design support bulk operation author briehl background app cell cell built jupyter front end extension framework application page load framework allows overriding customization component specifically narrative framework cell jupyter notebook thus narrative cell come three type code markdown raw kbase cell extension operate jupyter code cell easiest think subclassing app cell code cell specialized running narrative apps extension activated creating cell specific metadata component describes cell treated example adding following block code cell metadata tell extension machinery treat kbase app cell kbase type app app cell far complicated extension cell type several component serve different purpose finite state machine fsm thats determine cell state core system render cell based state message bus thats communicate rest application well kernel get job state interpreter manager app spec turn app spec set input form element code translator turn various set input code executed run app reason app cell extension code cell last point essence primary component app cell serve fancy code generator user interaction form element generate code start apps view result thus anything app cell done programmatically advanced user also noted regardless choice made may alter app spec made interpreted rendered bulk import design various input output listed horizontal row existing app spec rendered vertically there notion rowscolumns app spec right visually display various input along grid pattern order effectively match design may one following alter app spec support multiple inline parameter retaining backward compatibility including documentation etc distinct app spec importer include hardcode import apps look feel narrative interface decide update app spec work mean working narrativemethodstore catalog repos well internal documentation alternative considered implement existing app cell codebase implement new cell type dont cell interface outcome bulk import developed new cell type based existing app cell point discussed considered different interface cell decided changing entire paradigm right would heavy burden design product team would push back development effort also clear consensus whether thats desired result discussed implementation impact importer app parameter layout decided something internal narrative repo opposed modifying app spec general final implementation left later discussion consequence team develop new cell type mean building new jupyter notebook extension mostly startup code loadipythonextension function thats common among extension team also spending time extracting component app cell embedded making easily shareable new cell type pro con alternative implement existing app cell code base would entail adding different mode current app cell likely based additional metadata feature reduce spread additional yet similar cell type similar code reuse existing cell control mechanism currently place minimal modification reuse existing wrapping element cell title icon tab etc work done app cell made backward compatible existing functionality breaking work refactor etc complete release possible making intermediate release possibly challenging adding yet another mode app cell increase maintenance burden already complex code base see especially fsm draft complex may turn existing code deep series nested logic implement new cell type create new nbextension serve new cell type extension code cell would mean working fresh codebase without existing constraint intermediate minimally functional change rapidly prototyped released stick dry principle would mean refactoring part current app cell make various component importable message bus response job state management tab menu etc instead integration really might want consider anyway much structure mockup already function similar existing app cell might become duplicated work additional maintenance burden would mean updating component make narrative static narrative interface search dashboard example introspect narrative handle cell based type dont cell interface bulk importer work mocked cell becomes part narrative workflow could change would mean interface rather cell implement bulk import work discussed especially narrative intended work repeatable record analysis discussion generally importing file data object isnt useful trying repeat work especially dont access file also happen file expire server longer available case including one import cell misleading cell cannot run implying analysis narrative performs cannot completely reproduced unimpeded constraint around cell architecture imposed jupyter notebook kbase codebases keeping import job consolidated one place outside cell would reduce narrative length narrative object size removing import cell separate interface would positive impact load time entrypoint interface would something entirely new new work would done make app state management system kernel communication reference jira ticket draft design dataup jupyter notebook front end extension