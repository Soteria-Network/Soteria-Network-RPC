# Soteria Network RPC

Simple Soteria Network RPC library, designed to work with all versions of Soteria.

#### INSTALL:

pip install soteriarpc


## Setting Up soteriad (Linux)

go to your `.soteria` folder, add a `soteria.conf` file if there is not one already, in that file add:

```
rpcuser=username
rpcpassword=password
```

**Make sure you use a secure username and password!**

Then run `./soteriad` in the directory that it is located!

Examples:

```python
from soteriarpc import Soteria

soteria = Soteria('username', 'password')
soteria.getinfo()
soteria.listreceivedbyaddress(0, True)
```

Any other rpc method:

```python
soteria.<METHOD>(<param1>, <param2>, ...)
```

**Note**: If the username and password are incorrect, then a empty string will be returned. 

Please report any bugs by filling out an issue!

## Use it with other cryptos too!!

Just set the port when accessing:

```python
btc = Soteria('username', 'password', port=8332)
```

And if you want to use a different host:

```python
btc = Soteria('username', 'password', host='host.com', port=8333)
```
