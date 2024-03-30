#!/bin/bash

CURRENT_DIR=$(pwd)
cd "${CURRENT_DIR}/bin" || exit
echo "Unzipping chromedriver.zip, headless-chromium.zip..."
unzip -o chromedriver.zip
unzip -o headless-chromium.zip

echo "Removing zip files..."
rm chromedriver.zip headless-chromium.zip

if [ -d "__MACOSX" ]; then
    echo "Removing __MACOSX..."
    rm -rf __MACOSX
fi

echo "Finished."
cd "$CURRENT_DIR" || exit
