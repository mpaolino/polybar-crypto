# polybar-crypto
A *polybar script* that displays the price of various **crypto-currencies**.
Disclaimer: This is a fork and a dirty hack to make this work again using [CoinMarketCap API, get your free key here](https://coinmarketcap.com/api/).

There are [other, simpler solutions](https://github.com/polybar/polybar-scripts/tree/master/polybar-scripts/ticker-crypto).

I'm not really interested in maintaining this, just sharing.


![screen](https://user-images.githubusercontent.com/24377188/31326832-34dd06de-ad27-11e7-908f-9e7d72398eb7.jpg)



# Setup
```
git clone https://github.com/mpaolino/polybar-crypto.git &&
    cd polybar-crypto &&
    cp ./{crypto-config,crypto.py} ~/.config/polybar
```

Then in `~/.config/polybar/config`:

```
[bar/top]

...

modules-right = crypto

...

[module/crypto]
type = custom/script
interval = 300
exec = /home/<user>/.config/polybar/crypto.py

```

## Dependencies
The [cryptocoins](https://github.com/allienworks/cryptocoins) *icon font* is used in the screenshots, though you are free to use any other font.

If using the **cryptocoins** icon font, ensure that the following line is present in your `~/.config/polybar/config`:

```
[bar/top]

...

font-0 = cryptocoins:style=Regular;0
```

# Example Configuration

`~/.config/polybar/crypto-config`
```
[general]
base_currency = NZD
display = percentage
api_key = PUT_YOUR_COINMARKETCAP_API_KEY_HERE

[bitcoin]
icon = 

[ethereum]
icon = 

[litecoin]
icon = 

[ardor]
icon = 

[NEO]
icon = 
```

## Display Modes

`display = price`

![screen](https://user-images.githubusercontent.com/24377188/31331319-4ef14406-ad3e-11e7-9242-12440ef96774.jpg)

`display = percentage`

![screen](https://user-images.githubusercontent.com/24377188/31331342-65e40428-ad3e-11e7-88e0-3b87921805c7.jpg)

`display = both`

![screen](https://user-images.githubusercontent.com/24377188/31331368-80faac76-ad3e-11e7-9977-e86b1eebe401.jpg)
