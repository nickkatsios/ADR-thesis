adr substeps list size calculation substepslist animated showing hiding substeps step animating prof convenient maxheight initially hard coding maxheight property substeps list maximum animate however hardcoding value proved flexible especially substep also holding errormessage could span undeterminate height multiple line responsiveness etc height list determines height progress bar point settled working little work exploration many available make sure precalculate dynamic correct potential maxheight list one way could render list somewhere dom hidden order retrieve height however prof problematic prerender mean complicating dom application code another solution read height list element rendered maintain locally within parent class super elegant overwrite style property rendering chose follow second approach requires code work however creating issue html templating function litelement since change state attribute without informing library latter would mean rerendering via state prop would updated didrender moment would create complains polymer thus decided trick component calculate totalheight since content change rendered force maxheight calculated height component forced rendered havent applied trick already discovered would require click hide button finally close list research led discover html templating function handle value attribute trigger change httpsgithubcompolymerlithtmlblobmastersrccoretsl state code active value totalheightpx forced since closing value code didnt see reason change circumvent issue setting hidden state value allows initial closing consequence elegant hack seems least aggressive browser avoid approach though