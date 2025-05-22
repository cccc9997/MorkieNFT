
# Morkie NFT

**Auto Mint Morkie NFT**  
A Python script for automating the minting process of Morkie NFTs.

## Overview

MorkieNFT is a simple automation tool designed to streamline the minting of Morkie NFTs. This script interacts with the Morkie NFT minting website, allowing users to mint NFTs automatically without manual browser interaction.

## Features

- Automates the NFT minting process on the Morkie platform
- Built with Python for easy customization and integration
- Open source under the MIT license

## Requirements

- Python 3.7+
- [Pyppeteer](https://github.com/pyppeteer/pyppeteer) or another browser automation library
- A compatible Ethereum wallet (e.g., MetaMask) set up in your browser
- (Optional) A funded wallet on the supported blockchain network

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/cccc9997/MorkieNFT.git
   cd MorkieNFT
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(If `requirements.txt` is not present, install pyppeteer manually: `pip install pyppeteer`)*

## Usage

1. **Configure your wallet:**
   - Ensure your wallet (e.g., MetaMask) is installed, unlocked, and connected to the correct network.

2. **Run the script:**
   ```bash
   python morkie.py
   ```

3. **Follow on-screen instructions:**
   - The script will open a browser window, navigate to the Morkie NFT minting page, and attempt to mint an NFT automatically.

## Notes

- Make sure your wallet is ready for interaction; some steps may require manual confirmation (e.g., signing transactions).
- Use this tool responsibly and in accordance with the Morkie platform’s terms of service.

## License

This project is licensed under the [MIT License](LICENSE).
