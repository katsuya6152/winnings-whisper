import { chromium } from 'playwright';

import { DatabaseUtility } from './db/db'
import { getWeekendDate } from './utils/dateUtils'

class Scraper {
  private db: DatabaseUtility;

  constructor(db: DatabaseUtility) {
    this.db = db;
  }

  async ensureTableExists() {
    const createTableSql = `
      CREATE TABLE IF NOT EXISTS weekly_races (
          id varchar(45) NOT NULL,
          race_name varchar(255) NOT NULL,
          race_place varchar(255) DEFAULT NULL,
          number_of_entries int DEFAULT NULL,
          race_state varchar(255) DEFAULT NULL,
          date varchar(255) DEFAULT NULL
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    `;
    try {
      await this.db.query(createTableSql);
      console.log('Table is ready.');
    } catch (error) {
      console.error('Error ensuring table exists:', error);
    }
  }

  async scrapeRaces(date: string) {
    const browser = await chromium.launch({ headless: false });
    const page = await browser.newPage();
    await page.goto('https://race.netkeiba.com/top/');
    await page.locator(`//li[@date="${date}"]`).click();

    const races = await page.locator(`//span[@class="RaceList_ItemLong Turf"]`).all();
    for (const race of races) {
      await race.click();
      await this.processRace(page);
      await page.goBack();
    }

    await browser.close();
  }

  private async processRace(page: any) {
    const id = await this.extractId(page);
    const raceName = await this.extractTextContent(page, `//div[@class="RaceName"]`);
    const racePlace = await this.extractTextContent(page, `//ul[contains(@class, "Col")]/li[@class="Active"]`);
    const numberOfEntries = (await page.locator(`//tbody/tr[@class="HorseList"]`).all()).length;
    const raceState = await this.extractTextContent(page, `//div[@class="RaceData01"]`);
    const date = await this.extractTextContent(page, `//dd[@class="Active"]`);

    const weeklyRace = { id, raceName, racePlace, numberOfEntries, raceState, date };
    await this.insertRace(weeklyRace);
  }

  private async extractId(page: any): Promise<string> {
    let id = await page.locator(`//link[@rel="canonical"]`).getAttribute('href');
    return id ? id.slice(-12) : '';
  }

  private async extractTextContent(page: any, selector: string): Promise<string> {
    let content = await page.locator(selector).textContent();
    return content ? content.replace(/\n/g, '') : '';
  }

  private async insertRace(race: any) {
    const sql = "INSERT INTO weekly_races (id, race_name, race_place, number_of_entries, race_state, date) VALUES (:id, :raceName, :racePlace, :numberOfEntries, :raceState, :date)";
    try {
      await this.db.query(sql, race);
      await this.db.query("select * from weekly_races")
      console.log('Race inserted:', race);
    } catch (error) {
      console.error('Error inserting race:', error);
    }
  }
}

(async () => {
  const db = new DatabaseUtility();
  const scraper = new Scraper(db);
  await scraper.ensureTableExists();
  const date = getWeekendDate();
  await scraper.scrapeRaces(date);
})().catch(console.error);
