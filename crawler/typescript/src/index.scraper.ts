import { chromium } from 'playwright';

(async () => {
  const browser = await chromium.launch({
    channel: 'chrome',
    headless: true,
  });
  const page = await browser.newPage();
  await page.goto('https://race.netkeiba.com/top/');
  await page.screenshot({ path: `tmp/screenshot.png` });
  await browser.close();
})();