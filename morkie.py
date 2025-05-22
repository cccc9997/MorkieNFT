import asyncio
from pyppeteer import launch

async def mint_0g_panda():
    browser = await launch(headless=False, args=['--start-maximized'])
    page = await browser.newPage()
    await page.goto('https://morkie.xyz/og')

    # Example: Click wallet connect button (selector depends on site)
    await page.waitForSelector('button.wallet-connect')
    await page.click('button.wallet-connect')

    # Here, automate MetaMask popup interaction if possible (complex)
    # Or manually unlock wallet before running script

    # Wait for mint button and click it
    await page.waitForSelector('button.mint-button')
    await page.click('button.mint-button')

    # Wait for transaction confirmation or success message
    await page.waitForSelector('.mint-success', timeout=60000)

    print("Minting completed")

    await browser.close()

asyncio.get_event_loop().run_until_complete(mint_0g_panda())
