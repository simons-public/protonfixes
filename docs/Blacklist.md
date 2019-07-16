# Blacklisting games

Gamefixes can be blacklisted from using the included gamefix by creating a local gamefix with a `main` that does nothing.

``` shell
echo 'main = lambda: None' > ~/.config/protonfixes/localfixes/GAMEID.py
```

For example, to bypass the included gamefix for *A Hat in Time*:

``` shell
echo 'main = lambda: None' > ~/.config/protonfixes/localfixes/253230.py
```