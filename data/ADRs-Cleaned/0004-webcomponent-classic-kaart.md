webcomponent voor classic ngkaartfeature caching zonder service worker ngkaart moet webcomponent gebruikt kunnen worden parent injection waarbij component die enclosing tag beheert genjecteerd wordt component van enclosed tag werkt niet angular element onze classic kaart componenten steunen heel hard parent injection kaartclassiccomponent krijgen het geval van legende componenten ook contentchildren annotatie die ook niet werkt angular element wat wel werkt zijn service dus alles wat door ngmodule waarin angular element geregistreerd zijn geprovided wordt wordt gedeeld door verschillende componenten gebruiken angular element onze classickaart tag vormen naar webcomponents consequence moeten voorzien een kaartclassiclocatorservice die dom tree afgaat zoeken naar component van enclosing tag ipv injector dit betekent dat alle classic kaart componenten aangepast moeten worden die service gebruiken een nadeel van deze manier van werken dat moeten zorgen dat enclosing componenten aangemaakt worden voordat enclosed componenten hun parent component nodig hebben dit een bijkomend probleem angular element want het niet dom tree die bepaalt welke volgorde componenten aangemaakt worden maar volgorde waarin componenten geregistreerd zijn bij angular element ook moeten componenten rekening mee houden dat bij gebruik een angular template hun attribuutwaarden native vorm krijgen bij html web component string moeten die dat laatste geval dus converteren van een string naar het verwachte type complexe input zoals bijvoorbeeld functies worden helemaal niet ondersteund wanneer een nood blijkt zijn aan deze attributen zullen geval per geval een oplossing moeten voorzien implementatienotas meeste componenten zijn niet moeilijk vormen kunnen gebruik maken van een nieuwe classicbasecomponent die het werk doet extra werk nodig voor legende componenten daar moet injectie omgedraaid worden ipv dat parent zijn kinderen opvraagt moeten kinderen zichzelf registreren bij hun parent