import { chromium } from 'playwright';

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({
    viewport: { width: 1440, height: 900 }
  });
  
  // Navigate to the frontend
  await page.goto('http://localhost:5174/47-starter-django/', { 
    waitUntil: 'networkidle',
    timeout: 30000 
  });
  
  // Wait for the app to fully load
  await page.waitForTimeout(3000);
  
  // Take screenshot
  await page.screenshot({ 
    path: '/Users/mkazi/60 Projects/screenshots/starters/starter-47.png',
    fullPage: true 
  });
  
  console.log('Screenshot saved to /Users/mkazi/60 Projects/screenshots/starters/starter-47.png');
  
  await browser.close();
})();
