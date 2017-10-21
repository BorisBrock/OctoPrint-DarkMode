$(function() {
    function DarkModeThemePluginViewModel(parameters) {
        var self = this;

        $("body").eq(0).addClass("OctoPrintTheme-DarkMode")
        $("#settings_dialog").eq(0).addClass("DarkMode_Settings")

        }	
		OCTOPRINT_VIEWMODELS.push([
        DarkModeThemePluginViewModel,
		[]
		
    ]);
});