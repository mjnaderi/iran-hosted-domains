# Iran Hosted Domains

A lot of services and domains are outside of Iran and they are restricted or blocked by iranian censorship infrastructure or tech companies around the world, 
for accessing this service you need to use VPN or proxies with tunneling option, apart from these problems, when we use 
proxies the domestic services are unavailable because our IP is not in Iran; for bypassing these issues we gathered a list of 
Iranian domains and services to help our people bypass this situation.

## VPN Problems

The following issues arise when using VPN for some Iran hosted websites:

- They may force you to have Iran IP to be able to access.
- They may offer 50% off bandwidth while having Iran IP.
- They may limit speed for non-Iran IPs or VPNs are slow.

## Usage

This can differ depending on which tool you use. You can download the domains list from
the [release page][link-release].  
In v2ray clients you can set Domain Resolution Strategy to `IPIfNonMatch` for better routing. 
[more info.](https://www.v2ray.com/en/configuration/routing.html)

### [Qv2ray](https://github.com/Qv2ray/Qv2ray)

In the release section, you'll find the qv2ray_schema file.

1. Download the file.
2. open `preferences` and click on `Advanced Route Settings`.
3. From the bottom of the screen, click on `import schema...`.
4. choose the downloaded file (qv2ray_schema.json).
5. in the opened dialogue box, click on yes.
6. Click on OK.

![image](https://user-images.githubusercontent.com/24422125/115480663-397d3880-a260-11eb-88db-d3d7f8074767.png)

### .dat file

It can be used in all v2fly, v2ray and xray clients.

1. Download `iran.dat` file from [here][link-release].
2. Copy/Import file in your client.  
  for example:
    - v2ray macOS: `/usr/local/share/v2ray`
    ![image](https://user-images.githubusercontent.com/24422125/123522516-f2ce1380-d6d2-11eb-971f-0176f6e5b8ec.png)

3. Add proper rules:
    - `ext:iran.dat:ir`
    - `ext:iran.dat:other`
    - `ext:iran.dat:ads`

4. Reconnect.

### [SagerNet](https://github.com/SagerNet/SagerNet)
1. Download `iran.dat` file from [here][link-release].
2. Import .dat file from `Route -> Three dots -> Manage Route Assets`:  
<p align="center">
  <img alt="sagernet" src="https://user-images.githubusercontent.com/24422125/123522689-1cd40580-d6d4-11eb-90c1-a0341927e283.jpg">
</p>

3.  Add proper rules  `Route -> Create Route`:  
    - Block Ads:
      - domain: `geosite:category-ads-all`
      - outbound: `Block`
    - Block Iran Ads:
      - domain: `ext:iran.dat:ads`
      - outbound: `Block`
    - Bypass Iran .ir Domains:
      - domain: `regexp:.+\.ir$`
      - outbound: `Bypass`
    - Bypass Iran non .ir Domains:
      - domain: `ext:iran.dat:other`
      - outbound: `Bypass`
    - Bypass Iran geoip:
      - ip: `geoip:ir`
      - outbound: `Bypass`
> for screenshots of routing settings [click here](https://imgur.com/a/SEq1Bvg).

4. Reconnect.

### [Shadowrocket](https://apps.apple.com/us/app/shadowrocket/id932747118)

1. Download `shadowrocket.conf` file.
2. Tap `Import From Cloud` in the Shadowrocket app and then import the file.

<p align="center">
  <img alt="shadowrocket" src="https://user-images.githubusercontent.com/24422125/124380820-3678dc80-dcd4-11eb-8f59-96fb619d5710.png">
</p>

3. Finally, tap on the `shadowrocket.conf` and select `Use Config`.

<p align="center">
  <img alt="shadowrocket" src="https://user-images.githubusercontent.com/24422125/124380847-5d371300-dcd4-11eb-8274-aa72d470357f.png">
</p>


## Files

- **iran.dat:** Contains both `ir_domains.txt` and `other_domains.txt`.
- **ir_domains.txt:** Contains all websites that ends with `.ir`.
- **other_domains.txt:** Contains all websites that ends with `.com` or other Top-level domains name.
- **qv2ray_schema.json:** Importable json schema that can be used in [Qv2ray](https://github.com/Qv2ray/Qv2ray).
- **shadowrocket.conf:** Importable conf file that can be used in [Shadowrocket](https://apps.apple.com/us/app/shadowrocket/id932747118).

## Source

- Iran Domains:
  - [ITO GOV](https://g2b.ito.gov.ir/index.php/site/list_ip)
  - [ADSL TCI](https://adsl.tci.ir/panel/sites)
  - [Custom List][link-custom]
- ADs:
  - [adblock-iran](https://github.com/farrokhi/adblock-iran)

If you know of any other source, or you found a website that isn't here, please open
an [issue][link-issues] or add that specific website to [custom_domains.py][link-custom] and make a [PR][link-pr].

## How does it work?

A Python script is executed by Github Action and generates files that are on the release page.

[link-custom]: src/data/custom_domains.py
[link-pr]: ../../pulls
[link-issues]: ../../issues
[link-release]: ../../releases
