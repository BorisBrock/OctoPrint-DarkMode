# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class DarkModePlugin(octoprint.plugin.AssetPlugin):

	def get_assets(self):
		return dict(
			css=["css/darkmode.css",
			"css/bootstrap-modal.css",
			"css/overrides.css",
			"css/overrides-icons.css"],
			 js=["js/octoprint-darkmode.js"]
	)

	
	def get_update_information(self):
		return dict(
			darkmode=dict(
				displayName="Dark Mode",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="VanKurt",
				repo="OctoPrint-DarkMode",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/VanKurt/OctoPrint-DarkMode/archive/{target_version}.zip"
		)
	)

__plugin_name__ = "DarkMode"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = __plugin_implementation__ = DarkModePlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}