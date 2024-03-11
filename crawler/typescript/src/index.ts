import { chromium } from 'playwright';
import { DatabaseUtility } from './db/db';
import { Scraper } from './scraper/scraper';
import { getWeekendDate } from './utils/dateUtils'

(async () => {
  const db = new DatabaseUtility();
  const scraper = new Scraper(db);
  await scraper.ensureTableExists();
  const date = getWeekendDate();
  await scraper.scrapeRaces(date);
})().catch(console.error);
