- Age Of Empire 3: Complete Collection (105450)
- Age of Empires 2 HD Edition (221380)
- Age of Mythology: Extended Edition (266840)
- A Hat in Time (253230)
- Banished (242920)
- Batman Arkham Asylum (35140)
- Batman Arkham City (200260)
- Battlefield: Bad Company 2 (24960)
- BioShock 2 Remastered (409720)
- Call of Duty (2620)
- Chronophantasma Extend (388750)
- Civilization 4 (Beyond the Sword) (8800)
- Crysis (17300)
- Cuphead (268910)
- Dark Sould Prepare To Die Edition (211420)
- DMC Devil May Cry (220440)
- Doom 2016 (379720)
- EVE Online (8500)
- Fallout 2 (38410)
- Fallout: A Post Nuclear Role Playing Game (38400)
- Fallout: New Vegas (22380)
- FINAL FANTASY IX (377840)
- Forts (410900)
- Grand Theft Auto V (271590)
- Killer is Dead at Launch (261110)
- Little Nightmares (424840)
- Oddworld: Abe's Oddysee (15700)
- Oddworld: Munch's Oddysee (15740)
- Order of Battle: World War II (312450)
- Plants vs. Zombies: Game of the Year (3590)
- Portal Knights (374040)
- Puyo Puyo Tetris (546050)
- RiME (493200)
- Rise of Nations: Extended Edition (287450)
- Rising Storm/Red Orchestra 2 Multiplayer (35450)
- Serious Sam Double D XXL (111600)
- Sleeping Dogs: Definitive Edition (307690)
- Spacewar (480)
- STAR WARS Jedi Knight II - Jedi Outcast (6030)
- STAR WARS Jedi Knight - Jedi Academy (6020)
- Styx: Master of Shadows (242640)
- SUGURI 2 (390710)
- Tesla Effect (261510)
- The Evil Within (268050)
- Titan Quest Anniversary Edition (475150)
- Tomb Raider I (224960)
- You Need a Budget 4 (227320)

```bash
# generate gamelist
for i in protonfixes/gamefixes/*.py; do head -q -n1 "$i" |\
sed \
-e 's/"""//g' \
-e 's/\s\?Game fix\( for\)\?\s//' \
-e 's/\s\?([0-9]\+)//' \
-e "s/$/ \($(basename "$i" .py)\)/" \
-e 's/^/- /';
done | sort
```