
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from . import Named
class AvatarId(Named):
  DEFAULT = 0
  ORIGIN = 9918
  VIP = 23203, 'VIP'
  STRIKER = 23209
  TERMINATING = 23226
  CORRUPTER = 23442
  THE_LOST_HAND = 23549
  ONI_MASK = 23550
  CUTESY_MAEVE = 23552
  CUTESY_SNEK = 23553
  CUTESY_ZHIN = 23554
  GOODNIGHT = 23555
  SHADOWBLADE = 23564
  FLAMETONGUE = 23661
  SNACK_TIME = 23662
  DEATH_SPEAKER = 23714
  KNIGHTMARE = 23715
  DAY_WALKER = 23716
  HARBINGER = 23717
  SYNTH = 23924
  NOM_NOM = 23925
  CUTESY_YETI = 24079
  CUTESY_LIAN = 24080
  ROWDY_CORSAIR = 24081
  WINTER_WORKOUT = 24088
  SUIT_UP = 24120
  SHIELD_BEARER = 24143
  THE_KING = 24164
  POPPY = 24165
  GREENWOOD_FRIEND = 24166
  WHITE_KNIGHT = 24167
  MASTERPIECE = 24168
  BATTLE_RAGE = 24169
  GROVERLING = 24170
  FORKASEN_WANDERER = 24171
  KITTEN = 24172
  TIGRON_THIEF = 24173
  I_WUV_YOU = 24174, 'I WUV YOU'
  TEPID_FRIENDSHIP = 24175
  VULPIN = 24176
  DUMPSTER_DIVER = 24177
  ABYSSAL_VESSEL = 24178
  THE_RETURNED = 24179
  TWILIGHT_ASSASSIN = 24180
  HAPPY_HUNTRESS = 24181
  THE_BLOSSOM = 24182
  MIRROR_MIRROR = 24183
  PALADINS_DEFENSE_FORCE = 24202
  IMPERIAL_MAGISTRATE = 24203
  FIRE_AND_ICE = 24204, 'Fire and Ice'
  ASSEMBLY_OF_CHAMPIONS = 24241, 'Assembly of Champions'
  QUEEN_OF_HEARTS = 24350, 'Queen of Hearts'
  FUTURES_PROTECTOR = 24354, "Future's Protector"
  SQUIDLY = 24355
  FORLORN_FUTURE = 24356
  DRAGON_QUEEN = 24375
  DIAMOND_BADGE = 24393
  GOLD_BADGE = 24394
  BLUE_WARRIOR = 24482
  HOW_QUAINT = 24505
  CHAMPIONS_ARE_ETERNAL = 24597, 'Champions are Eternal'
  BEST_BOY = 24611
  SUMMER_BLOSSOM = 24612
  VANGUARD = 24669
  BUBBLES = 24678
  BABY_STEPS = 24679
  DRAGON_FORGED = 24680
  DWARVEN_STRENGTH = 24681
  UNRELENTING = 24709
  CHARMING = 24758
  SUNSET = 24759
  LIFESAVER = 24760
  BEACH_VIBES = 24824
  GROOVY_GROVER = 24887
  GROHK_ROCK = 24888
  CELEBRITY_IO = 24889
  POPSTAR_SKYE = 24890
  GREASER_LEX = 24891
  FALLEN_CHAMPION = 24892
  RECKONING = 24897
  RESOLUTE = 24898
  REDBEARD = 24969
  BUBBLY = 24970
  PIRATEER = 24972
  KITSUNE = 24973
  BLU = 25021
  MOLLY_THE_SHARK = 25022, 'Molly the Shark'
  SUAVE_SAGUARO = 25138
  WANTED_MAN = 25139
  BANDITS_FURY = 25140, "Bandit's Fury"
  SMOKED = 25141
  LENNY_THE_PIRATE = 25161, 'Lenny the Pirate'
  GODDESS_OF_DEATH = 25222, 'Goddess of Death'
  SKADRIN_ASH = 25223, "Ska'drin Ash"
  DARK_MONARCH = 25224
  SOUL_BRIAR = 25225
  WUKONG = 25226
  MISCHIEVOUS = 25227
  FOREST_PROTECTOR = 25228
  ICE_BOX = 25229
  SPRING_FLING = 25342, 'Charity Avatar Community Patch'
  ADANAS_THE_BALANCE_MASTER = 25355, 'Adanas the Balance-Master'
  GENTLEMAN_RAUM = 25356
  TYRA_NOVA = 25357, 'Tyra-nova'
  FOUR_LEAF_GROVER = 25421
  TERMINEASTER = 25422
  TEMPLE_GUARDIAN = 25434
  DEVIOUS = 25435
  DIVINE_PRIESTESS = 25437
  THE_RISEN = 25438
  SCALED_MENACE = 25506
  HUNTERS_FURY = 25507, "Hunter's Fury"
  BROOD_GUARD = 25545, "Brood-Guard"
  EYE_OF_SAURUS = 25546, 'Eye of Saurus'
  SURVIVOR = 26291

  def icon(self, c=None, **kw):
    __url__ = f'https://hirez-api-docs.herokuapp.com/paladins/avatar/{int(self)}{kw.pop("http_param", "")}'
    if c:
      if hasattr(c, 'http'):
        return c.http.get(__url__, **kw)
      return c.get(__url__, **kw)
    return __url__

"""
for _ in AvatarId:
  print(f'{_._display_name_.upper().replace(" ", "_")} = {_.value}, \'{_._display_name_}\'')
"""
