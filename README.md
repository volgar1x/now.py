# now.py

Example :

```sh
$ # get current timestamp
$ now.py
1568898565
$ # get timestamp in one year
$ now.py + 365 days
1600434781
$ # copy to clipboard timestamp in one year
$ now.py + 365 days | pbcopy
````

### TODO

- [ ] deb packaging
- [ ] rpm packaging
- [ ] error handling
- [ ] date formatting
- [ ] more resolution (using [dateutil.relativedelta.relativedelta](https://dateutil.readthedocs.io/en/stable/relativedelta.html))
- [ ] more num literals (for example `0xa`, `0b1101`, `0777`, `one`)
- [ ] more operators
- [ ] operator aliases (`plus 1 year` to be equivalent to `+ 1 year`)
- [ ] resolution aliases (`+ 1 yr` to be equivalent to `+ 1 year`)
