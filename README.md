# LEAGUE CENSUS 

[LEAGUECENSUS.COM](http://www.leaguecensus.com) 

## Description:

LEAGUE CENSUS is a **Django Web Application** for retrieval of summoner, champion, item and server status information by pulling data from [Riot Games API](https://developer.riotgames.com/api/methods). The application is a work in progress and is built from code I had originally written in PHP and JavaScript many years ago and am now converting to Django. It is constantly being improved and updated. Any data is stored in **MongoDB** and comes directly from the FileSystem flat json files provided by Riot Games Data Dragon or by calls directly to Riot Games API (or cache). Caching of data is handled by both **Redis** and **Cloudflare**.

This application also makes use of Cassiopeia Library, written by **Meraki Analytics**. You can find their Github page [here](https://github.com/meraki-analytics/cassiopeia)


[LEAGUECENSUS.COM](https://leaguecensus.com)


## Technical Specifications
* Django
* Python
* MongoDB
* Redis
* Nginx
* Gunicorn
* Digital Ocean (2x vCPU/4GB RAM)
* Cloudflare (DNS/Firewall/Caching/SSL)


Desktop:
[Image of Champion List](https://imgur.com/a/fosMyqa)

[Image of Champion](https://imgur.com/a/GSiPPEq)

Mobile:
[Image of Champion List](https://imgur.com/a/96X6gdX)

[Image of Champion](https://imgur.com/a/Cyn1T6b)


## Version:
**Current Leauge Patch: 10.2.1** 

LEAGUE CENSUS is updated the day after every **major patch** released for League of Legends.

The application is currently in v1.0.0.2


## Creators & Authors:
**Mykel Agathos**

E-mail: mykel.thos[at]gmail[dot]com


## Copyright and Licensing:
**License**

LEAGUE CENSUS is released under the [GNU General Public License](https://github.com/MThos/lolcensus/blob/master/LICENSE.md).

**Copyright**

Copyright © 2021 - LEAGUECENSUS.COM


## Legal Mumbo Jumbo:
**Riot Games Use Of Intellectual Property**

LEAGUE CENSUS isn’t endorsed by Riot Games and doesn’t reflect the views or opinions of Riot Games or anyone officially involved in producing or managing League of Legends. League of Legends and Riot Games are trademarks or registered trademarks of Riot Games, Inc. League of Legends © Riot Games, Inc.
