# Metacritic Scrapy Project

This project is configured to be hosted on [Scrapy Cloud](https://www.zyte.com/scrapy-cloud/).  
It uses [Zyte Smart Proxy Manager](https://scrapinghub.com/?rfsn=4170080.0597ad) as proxy service.  
The dataset can be found [here](https://www.kaggle.com/datasets/patkle/metacritic-scores-for-games-movies-tv-and-music).  
A Jupyter Notebook with some EDA on that data can be found [here](https://www.kaggle.com/patkle/metacritic-scores-exploration).  

## Spiders

The following spiders exist in this project:
- movies
- games
- tv
- music

The spiders can be ran using
```zsh
python3 -m scrapy crawl movies -a pages=5 -O movies.csv
```
where you need to replace `movies` with the desired spider name.

### Arguments

With `-a` you can specify arguments for the spiders.  

|argument   |type  |description   | 
|---|---|---|
|pages   |int   |number of pages to scrape   |

## Setting up locally
  
When setting up this project locally you must create a **.env** file with the following data:  

|setting   |description   |  
|---|---|
|ZYTE_SMARTPROXY_APIKEY   |your smart proxy manager api key   |
  
## Deploy to Scrapy Cloud
There's a shortcut in the Makefile, just running `make deploy` will deploy the project to Scrapy Cloud (given that you provided the project ID in `scrapinghub.yml`).Don't forget to add the following settings in your cloud project's settings:
|setting   |description   | 
|---|---|
|ZYTE_SMARTPROXY_APIKEY   |your smart proxy manager api key   |
  
## Also, 
you could [buy me a coffe](https://www.buymeacoffee.com/kleinp) if you wanted to. I'd really appreciate that.  
