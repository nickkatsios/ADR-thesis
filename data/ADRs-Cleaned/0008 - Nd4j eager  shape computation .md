ndj eager shape computation proposed adam gibson discussed paul dub ndjs model import framework often compute shape variable created order resolve properly create graph based graph descriptor another framework tensorflow pytorch often called eager mode proposal focus eager shape computation intended model import assumption could build later fully eager computation order aid building model import easier proposal focused implementing dynamic shape computation model import composed part outputvariables call sdvariable trigger ndjgetexecutionerexec call relevant operation extract shape set appropriate shape based result sdvariable field intentionally include dummy call control flow ops enter shape dont matter beyond knowing number output samediff instance eager mode boolean determine whether functionality invoked eager mode variable required model import case usually model import framework turn eager needed without user needing involved samediff instance separate arrayholder looking ndarrays relevant eager computation proper session instead store computing shape discussion paul originally would full eager mode adam dont fully implemented eager mode model import full eager mode would mean proper session support training support would incremental shape calculation model import consequence advantage allows model import flexibility add base real eager mode later disadvantage add complexity model import addition dynamic shape calculation model import could hard debug want see full would imported graph computation blocking import workflow state attached eager array holder attached samediff instance another flag turning feature onoff