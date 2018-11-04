- Age Of Empire 3: Complete Collection
- Age of Empires 2 HD Edition
- Age of Mythology: Extended Edition
- A Hat in Time
- Banished
- Battlefield: Bad Company 2
- BioShock 2 Remastered
- Call of Duty (2003)
- Chronophantasma Extend
- Civilization 4 (Beyond the Sword)
- Crysis
- Doom 2016
- EVE Online
- FINAL FANTASY IX
- Forts
- Game fix for Fallout 2
- Game fix for Fallout: A Post Nuclear Role Playing Game
- Grand Theft Auto V
- Killer is Dead at Launch
- Little Nightmares
- Oddworld: Abe's Oddysee
- Oddworld: Munch's Oddysee
- Order of Battle: World War II
- Puyo Puyo Tetris
- RiME
- Rise of Nations: Extended Edition
- Rising Storm/Red Orchestra 2 Multiplayer
- Spacewar
- STAR WARS Jedi Knight II - Jedi Outcast
- STAR WARS Jedi Knight - Jedi Academy
- Styx: Master of Shadows
- SUGURI 2
- Tesla Effect
- The Evil Within(268050)
- Titan Quest Anniversary Edition(475150)
- Tomb Raider I
- You Need a Budget 4

```bash
# generate gamelist
head -q -n1 protonfixes/gamefixes/*.py |\
sed \
-e 's/"""//g' \
-e 's/\sGa.*or\s//' \
-e 's/^/- /' |\
sort
```