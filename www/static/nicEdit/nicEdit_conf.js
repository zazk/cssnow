bkLib.onDomLoaded(function() {
    try {
        new nicEditor({iconsPath : '/static/nicEdit/nicEditorIcons.gif',fullPanel : true}).panelInstance('id_descrip');
    } catch(err) {
    }
});