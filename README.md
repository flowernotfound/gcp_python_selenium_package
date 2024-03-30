## English Version

# GCP Python Selenium Package

This package allows for the operation of Selenium on Google Cloud Functions. It enables automation of browser operations and file downloads/manipulations in GCP's serverless environment.

## How to Use

1. **Clone the Package**

   ```bash
   git clone https://github.com/flowernotfound/gcp_python_selenium_package.git
   ```

2. **Setup**

   ```bash
   cd gcp_python_selenium_package
   ./setup.sh
   ```

3. **Add Your Script**

   Create your Selenium script in the `automation/` directory and adjust the variables and `main.py` as needed.

4. **Deploy to Google Cloud Functions**

   ```bash
   gcloud functions deploy [function_name] \
       --gen2 \
       --runtime python39 \
       --region [region] \
       --entry-point main \
       --trigger-topic [topic_name] \
       # Add other settings as needed...
   ```

## About utils

The `utils/` directory contains several useful functions:

- **get_credentials**: Retrieves GCP authentication credentials.
- **setup_driver**: Configures the WebDriver for headless operation of Selenium and enables file downloads.
- **upload_file_to_drive**: Uploads files to Google Drive.
- **get_value_from_sheets**: Retrieves values from specified cells in spreadsheets.

## License

This package is released under the [MIT License](LICENSE.txt). Please see LICENSE.txt for more details.

## 日本語版 README.md

# GCP Python Selenium Package

このパッケージは、Google Cloud Functions 上で Selenium を動作させるためのものです。GCP のサーバーレス環境でブラウザ操作、ファイルのダウンロード・操作を自動化できます。

## 使い方

1. **パッケージのクローン**

   ```bash
   git clone https://github.com/flowernotfound/gcp_python_selenium_package.git
   ```

2. **セットアップ**

   ```bash
   cd gcp_python_selenium_package
   ./setup.sh
   ```

3. **スクリプトの追加**

   `automation/` ディレクトリに Selenium のスクリプトを作成し、必要に応じて変数や `main.py` を調整してください。

4. **Google Cloud Functions へのデプロイ**

   ```bash
   gcloud functions deploy [function_name] \
       --gen2 \
       --runtime python39 \
       --region [region] \
       --entry-point main \
       --trigger-topic [topic_name] \
       # その他の設定...
   ```

## utils について

`utils/`ディレクトリには以下の便利な関数が含まれています。

- **get_credentials**: GCP の認証情報を取得します。
- **setup_driver**: Selenium を headless モードで動作させ、ファイルのダウンロードが可能なように WebDriver を設定します。
- **upload_file_to_drive**: ファイルを Google Drive にアップロードします。
- **get_value_from_sheets**: スプレッドシートの指定のセルから値を取得します。

## ライセンス

このパッケージは [MIT ライセンス](LICENSE.txt) の下で公開されています。詳細は LICENSE.txt を参照してください。
