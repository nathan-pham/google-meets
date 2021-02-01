from selenium.webdriver.chrome.options import Options

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"

normal = [
	"--no-sandbox",
  "--ignore-certificate-errors",
  "--homepage=about:blank",
  "--no-first-run",
  "--disable-infobars",
  "start-maximized",
  "--disable-extensions",
  "--no-sandbox",
  "--disable-dev-shm-usage",
  f'user-agent={user_agent}',
  "disable-infobars",
  "--user-data-dir=chrome-data",
  "--disable-popup-blocking",
  "--ignore-certificate-errors"
  "--incognito"
]


# chrome_options.add_argument("--profile-directory=Default")


# chrome_options.add_argument("--disable-plugins-discovery")

experimental = {
  "prefs": { 
		"profile.default_content_setting_values.media_stream_mic": 1, 
		"profile.default_content_setting_values.media_stream_camera": 1,
		"profile.default_content_setting_values.geolocation": 1, 
		"profile.default_content_setting_values.notifications": 1 
	},
	"excludeSwitches": [ "enable-automation" ],
  "useAutomationExtension": False
}

opt = Options()
for option in normal:
  opt.add_argument(option)
for key in experimental:
  opt.add_experimental_option(key, experimental[key])