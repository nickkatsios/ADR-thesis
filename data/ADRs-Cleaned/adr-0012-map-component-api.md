map component adr current leaflet map implementation intentionally made thin wrapper weve developed enough code around quantify leaflet raster foundry well shortcoming current approach initial approach try control leaflet map exclusively thorugh binding callback property weve found creates lot complexity component controller due way data must flow component ideally component oneway data binding possible call bound function order change data parent current way thing set requires important state centralized parent controller modified twoway binding child component adding layer controlled child attribute necessitated creating separate binding type interaction resulted bloated leaflet map component current case scene browser attribute footprintctrlhoveredscenedatafootprint bypassfitboundstrue proposedboundsctrlbounds gridctrllastgridresult onviewchangectrlonviewchangenewbounds zoom requirement display single polygon map fit map view bound display grid polygon callback view change scene detail project scene detail attribute footprintctrlscenefootprint statictrue requirement display single polygon map disable map interaction ability fit map geojson project editor attribute footprintctrlhoveredscenedatafootprint bypassfitboundstrue layersctrllayers highlightctrlhighlight onmapclickctrlonmapclickevent allowdrawingctrlallowdrawing drawnpolygonsctrldrawnpolygons onviewchangectrlonviewchangenewbounds zoom requirement display single polygon map fine grain control layer highlight map click event map view event drawing proposed solution consolidate toggle attribute leaflet component fittolayerid expects layer defined replaces bypassfitbounds static javascript thismapoptions fittolayerid footprint static false thismapaddgeojsonscenefootprint footprint create map service data interaction geojson internal map geojson map layer efficient rerendering change uuid scene uuid general identifier highlight footprint domain specific calculated grid cell identifier leaflet component initialized destroyed register service subviews interact map service dont complex data binding interact map abstract require way define geojson layer modify without rerendering layer way define editable basemap layer reorder parameterize fly way listen map event act callback responsible evalasync necessary efficient way addmanage grid utility function related map interaction mapwrapper class one time function relevant controller global map state stored wrapper geojson object tracking user defined preference api possible initial concept place doesnt make sense create api mapwrapper expose map object leaflet service api mapwrapper api property type description map lmap wrapped leaflet map mapid string wrapped leaflet map callbackcounter int internal counter preventing callback clash callback esmap internal map store callback integer callbackid eventdescriptor wrappedcallback method return description constructorlmap leafletmap string mapid constructor mapwrapper onstring eventdescriptor function callback integer callbackid register map event listener offinteger callbackid unregister map event listener addgeojsonstring object geojson add geojson object layer map identified update deletion geojson object may optionally contain property define style tooltip action getgeojsonstring lgeojson get geojson layer updategeojsonstring object geojson update geojson object layer deletegeojsonstring delete geojson object layer setlayerllayerllayergroup layer string add layer layergroup identified layer wrapped layergroup getlayerstring llayergroup get map layer group deletelayerstring delete map layer mapservice api property type description map esmapstring mapwrapper map mapids mapwrappers mappromises esmapstring promisemapwrapper internal map mapids promise must resolved mapwrappers method return description constructor constructor mapservice registermaplmap map string register map mapservice called rfleafletmap component selfregister deregistermapstring deregister map map service automatically delete remaining user created listener getmapstring promisemapwrapper get promise resolve mapwrapper map service skeleton detailed documentation javascript class mapwrapper constructorleafletmap mapid thismap leafletmap thismapid mapid counter global map dont combine list listener across map thiscallbackcounter thiscallbacks new map event function listener identified number event listener registered controller let listener maponclick event map removed scope destructor thislistenersforeachlistener thismapofflistener params event string string identifier event map fire callback function callback signature event map note mechanism preventing multiple listener event triggering event onevent callback wrap callback track listener internally let wrappedcallback callbacke thismap let callbackid thiscallbackcounter thiscallbackcounter thiscallbackcounter thiscallbackssetcallbackcounter event wrappedcallback create listener map event thismaponevent wrappedcallback return callbackid params callbackid int callback deregister map offcallbackid check valid parameter delete event listener thiscallbackshascallbackid let offpair thiscallbacksgetcallbackid thismapoffoffpair offpair thiscallbacksdeletecallbackid else throw exception geojson layer api geojson layer worst leaflet api function heavy lifting displaying geojson data map simple api customization per component styling stored property geojson property parameter render function function signature property object object map style key value applied svg pretty direct analogue leaflet style property add geojson layer internally create map user assigned leaflet internal layer would allow update large set geojson object selectively params string unique identifier geojson must order edit geojson thats map geojson object geojson feature associate function support editingdeleting set geojson feature together set simplicity sake object identified single removed added back want optimize update component update tracked separately addgeojsonid geojson update geojson layer params string unique identifier geojson layer geojson object geojson feature replace updategeojsonid geojson delete geojson layer params string unique identifier geojson layer deletegeojsonid add layer layergroup map identified param llayer llayergroup layer layer add param string refer layer setlayerlayer get layer return llayergroup getlayerid delete layer map deletelayerid class mapservice constructor thismaps new map thismappromises new map leaflet component selfregister method registermapmap let mapwrapper new mapwrappermap thismapssetid mapwrapper promise resolve thismappromiseshasid thismappromisesgetidforeachpromise promiseresolvemapwrapper thismappromisesdeleteid deregistermapid unregister listener map delete reference map thismapsdeleteid promise resolve failure getmapid let deferred qdefer map registered get map thismaps thismapshasid deferredresolvethismapsgetid otherwise wait return promise get resolved map registered else let mappromise deferredpromise thismappromiseshasid let promise thismappromisesgetid promisespushmappromise thismappromisessetid promise else thismappromisessetid mappromise return mappromise leaflet component attribute javascript class rfleafletcomponent mapid example interface scene footprint preview component html rfleafletmap mapidscenepreview optionsctrlpreviewoptions rfleafletmap javascript class scenepreviewcomponent constructormapservice thispreviewoptions static true fittolayerid footprint mapservicegetmapscenepreviewthenmap thisscenepreviewmap map thisscenepreviewmapaddgeojsonfootprint thisgetscenefootprint example interface browse component html rfleafletmap mapidbrowse optionsctrlbrowseoptions rfleafletmap javascript class browsecomponent constructormapservice thisbrowseoptions mapservicegetmapbrowsethenmap thisbrowsemap map thisbrowsemapmapfitboundsthisparamsbbox thismaplisteners thisbrowsemaponmoveend thisonviewchangebindthis event call back two argument event event map object onviewchangeevent map let newbounds mapgetbounds let zoom mapgetzoom ondestroy thismaplistenersforeachlistener thisbrowsemapofflistener consequence tradeoff limiting angular attribute map interaction happen map service rather angular attribute pro limiting map interaction service map wrapper call avoid much complexity arose trying control map entirely binding leaflet doesnt fit perfectly angular paradigm controlling thing exclusively binding shouldnt try force interaction con mean manage interaction map affect data angular manually creates additional complexity term angular lifecycle self registering map component leaflet component register map service exposed map wrapper pro creates central location map utility function multiple place easy way put multiple map page control place store map specific state containing controller con careful store state would easy keep adding convenience function map wrapper make sure function involves map state placing wrapper simple utility function probably put map service instead keep wrapper getting bloated