const URL = "https://st-theme-2.streamlit.app"
const TITLE = "streamlitApp"  // HTML title attribute of the desired iframe.
const TEXT = "Make the CSS adjustment"

// Set timeouts for page load and element finding.
await $webDriver.manage().setTimeouts({
  pageLoad: 30000,  // 30 seconds for page load timeout.
  implicit: 5000,  // 5 seconds for element finding timeout.
});

console.log("Starting the synthetic script.")

console.log("Navigating to:", URL)
await $webDriver.get(URL)

console.log("Finding the iframe with the title:", TITLE)
var iframe = await $webDriver.findElement(
  $selenium.By.xpath("//iframe[@title='" + TITLE + "']")
)

console.log("Switching to the iframe.")
await $webDriver.switchTo().frame(iframe)

console.log("Checking for the presence of an element with the text:", TEXT)
await $webDriver.findElement($selenium.By.xpath("//*[text()='" + TEXT + "']"))

console.log("Script completed successfully.")
