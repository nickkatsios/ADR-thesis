title adding storableflow instead flowevent implementing flow delayaction flow builder area servicessettings tag flow event refactoring action flow builder listening business event want implement flow delayaction flow builder mean action delayed executed set amount time problem action delayed event may contain old data data may updated delay currently dont way restore data delay rule reevaluated data rule could outdated changed rule reloaded well rule exist anymore would detach event system flow system thus removing dependency runtime object within event meaning action must access original event would create class storableflow store data original event scalar value restore original data based stored data php class storableflow contains scalar value based original event store serialized restore object data protected array store contains restored object data like data defined availabledata original event data serialized restored store protected array data public function constructarray store array data thisstore store thisdata data method called storer store representation data public function setstorestring key value thisstorekey value public function getstorestring key return thisstorekey restored data storer set data well thisdata instead getter data original event public function setdatastring key value thisdatakey value public function getdatastring key return thisdatakey storableflow class flow builder php class flowdispatcher public function dispatchevent event currently dispatch flow builder original event execute flow thiscallflowexecutorevent php class flowdispatcher public function dispatchevent event flowfactory createrestore storableflow original event flow thisflowfactorycreateevent storableflow execute flow builder action instead original event thisexecuteflow flow builder action may longer access original event aware interface get storer class restore data aware many storer like orderstorer mailstorer customerstorer main task storer restore data scalar storage storer provides store function order store data order restore object storer provides restore function restore object store data php interface flowstorer example orderstorer php class orderstorer implement flowstorer function check original event instanceof aware interface store representation public function storefloweventaware event array storeddata array event instanceof orderaware storeddataorderid eventgetorderid return storeddata function restore data based representation storeddata public function restorestorableflow flow void flowhasstoreorderid allows provide closure lazy data loading open opportunity lazy loading big data load entity add necessary association entity flowlazyorder load additional data defined availabledata original event arent defined aware interface cant restore data storer cover additional data original event another store additionalstorer store data php class additionalstorer extends flowstorer public function storefloweventaware event array storeddata based thegetavailabledata original event get type additional data additionaldatatypes eventgetavailabledatatoarray foreach additionaldatatypes key eventdata check type data entity entitycollection storeddata store presentation like entity entity well restore data additionalstorerrestore eventdatatype entity entitycollection storeddatakey eventgetid entity entity check type data scalarvaluetype eventdatatype scalarvaluetype storeddatakey value start implement serializable objecttype eventdatatype objecttype storeddatakey valueserialize return storeddata function make sure restore additional data original data covered storer additional data entity entity defined aware interface like order customer covered storer public function restorestorableflow flow void type entity association entity data mostly additional entity data base entity dont add association flowsetdatakey thisload else flowsetdatakey flowgetstorekey association entity data mostly additional entity data base entity dont add association objecttype data enforce value objecttype implement serializable serialize object store storeddata flow builder action work storableflow instead flowevent storableflow restore data original event via storer action get data via getdatakey storableflow instead getavailabledata original event flow action still dependency aware interface php public function handlestorableflow event baseevent eventgetevent baseevent instanceof customeraware customerid baseeventgetcustomerid flow action php public function handlestorableflow event eventhasstorecustomerid customerid eventgetstorecustomerid getavailabledata must responsible access data create new restore storableflow existing stored data provider flowfactory php class flowfactory public function createfloweventaware event storeddata foreach thisstorer storer storer responsible move corresponding data original event storerstoreevent storeddata return thisrestorestoreddata public function restorearray stored array data flow new storableflowstored data foreach thisstorer storer storerrestoreflow return flow executing delayed action wont astorableflow thestoredfrom previously storedstorableflow based thestored restore newstorableflow example delay action php handler delay action put action toqueue stored jsonencodeflowstored connectionexecutestatementinsert swagdelayaction store value stored stored stored php handler execute delay action stored select store fromswagdelayaction flow thisflowfactoryrestorejsondecodestored consequence new class storableflow instead flowevent class flow builder cannot original event aware interface anymore symfony event listener flowevent continue interface store yet filled well remove next major version symfony event listener interface store yet filled flow builder store functionality interface might implemented